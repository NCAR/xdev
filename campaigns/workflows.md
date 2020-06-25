# The Workflows Campaign

Improving Scientific Data Analysis Workflows

## Overview

In a very general sense, scientific data analysis workflows usually have a
particular process structure to them:

1. **Search & Discovery**: Locate the *starting point* for your analysis
2. **Ingestion**: Open and read this data or code into a useful format
3. **Analysis**: Perform some computations on the data
4. **Check-point**: Save computed artifact as a new dataset
5. **Publication**: Produce images and/or papers from the computed artifacts

Implied by this process is the existence of a **Platform** for the user upon
which each step in the above process is conducted.  *It is not necessary that
the same platform be used for each step.*  In fact, multiple platforms *could*
be used in a single step.  For example, during the *Search & Discovery* phase,
the scientist might use a combination of web searching to find the larger
dataset or collection, and then move to a Jupyter Notebook to make queries of
the larger dataset to produce subsets).  It is not critical that a *single
platform* be emphasized or prioritized, but making it easier and more
productive for the scientist is critical.  That could mean reducing the number
of platforms the scientist must use, but it could also mean making multiple
platforms inter-operate better.

It is extremely important to understand that this process, as described above,
is just conceptual.  No scientist simply moves through this process *in order*
nor in a *single pass*.  That is, scientists that perform actual analysis many
times jump forward and back in the process.  For example, a scientist may jump
forward from the *Ingestion* phase to the *Check-point* phase before doing any
actual *Analysis*.  Or, a scientist may jump back to the *Search & Discovery*
phase to find another dataset to compare with one they originally started
analyzing.  A scientist might also *iterate* on their analysis, effectively
making this process *cyclic*.  For example, a scientist might *publish* their
Notebook with the expectation that their Notebook can be found during the
*Search & Discovery* phase.

## Vision

The Xdev Vision Statements ([SCOPE](../SCOPE.md#xdev-vision-statements)) are easy
to state in brief, but harder to state in detail.  I will try to describe what I
see as the vision of the future of scientific workflows, based on the Pangeo
ecosystem.

### 1. Search & Discovery

The *Search & Discovery* phase in scientific workflows describes a user
looking for an entry point for their analysis.  This includes searching for
and discovering a particular dataset or datasets, but it also includes searching
for and discovering a particular *existing* workflow that a user either
(1) modifies to create a new workflow or (2) extends by adding to the workflow.
Thus, users need to be able to search for *both* data that they can ingest into
their Notebooks *and other* Notebooks that they can modify or extend.
I will refer to these three kinds of workflow entry points as *Data Access*,
*Workflow Modification*, and *Workflow Extension*.

Regardless of the kind of entry point to a new workflow, the user should be able
to start a new workflow *either* from within JupyterLab *or* from an external
website or service.  For example, a *Data Access* entry point could be a "Data Search"
tab in JupyterLab, provided by a JupyterLab extension that connects to a
data search service like NCAR's [DASH](https://www2.cisl.ucar.edu/dash).  Or,
you could imagine a *Data Access* entry point coming directly from the DASH
website, itself, such as a button on a selected dataset's information page that
directs the user to a JupyterHub or Binder next to the selected dataset.  Similarly,
a *Workflow Modification* or *Extension* entry point could be a "Workflow Search"
tab in JupyterLab, again provided by a JupyterLab extension that connects to a
Notebook sharing service (i.e., similar to
[nbgallery](https://github.com/nbgallery/nbgallery)).
Alternatively, *Workflow Modification* or *Extension* entry point could be from
an external website that allows the user to search for and select existing (shared)
workflows (i.e., Notebooks).

Ideally, the *Data Access* entry point would automatically provide to the user
a semantically queriable (i.e., searchable using language the user knows, rather
than new terminology created by the developer) object that can let the user more
deeply inspect and subselect the parts of the dataset desired.  That is, the
*Data Access* entry point should yield to the user a queriable
*Intake catalog object*.  Ideally, this object should be autoconstructed for the
user in the user's Notebook (e.g., by inserting a cell with minimal code that
"loads" the Intake catalog object).  That is, the user selects a dataset to
analyze, and by clicking an "Analyze" button next to the dataset search return,
a new cell is added to the user's active Notebook with code that returns or
constructs an Intake catalog object.

Ideally, the *Workflow Modification* entry point would launch the selected
Notebook running in the user's personal space.  This requires that the Notebook
kernel be copied into or constructed in (or similar) the user's space.  Ideally,
this process will take just a few seconds from "clicking" on the selected
Notebook and the Notebook loading with a working kernel in a user's JuptyerLab
session (excluding possible authentication if this entry point starts on an
external website).

The *Workflow Extension* entry point should provide the user with an "API"
that the user can access from a new Notebook in their JupyterLab session.  This
would require that certain data objects constructed in the selected Notebook be
"exposed for import" into another Notebook.  To avoid unnecessarily running a
time-consuming Notebook, "exposed" elements of the Notebook should be cached
somewhere so they can be easily and quickly retrieved.  Ideally, this would
consist of the user simply needing to do something similar to:

```python
from shared_notebook_service.some_notebook import computed_object
```

In any of these entry points, if the entry point is from an external website,
then the entry point should take them to a JupyterHub, which may require
authentication and spawning selections, and then launch a new Notebook with
the desired return objects.

#### Possible Projects

- A JupyterLab extension that connects to the DASH respository and can "inject"
  `intake` code into your running/active Notebook (or launch a new Notebook) by
  appending a new cell.
- A Notebook sharing service that can provide a Notebook and the kernel needed
  to run the notebook.  This could be
  [nbgallery](https://github.com/nbgallery/nbgallery), or it could be something
  completely different.
- A JupyterLab extension that connects to a Notebook sharing service.
- A Binder-like capability that maintains a persistent user space so that the
  user can modify an existing Notebook and return to that Notebook later...and
  possibly share *it* via the same service.
- A service that informs the user of all of their scattered persistent Binder
  projects and can take them "back" to their persistent Binder with a single
  click.
- A caching service for selected objects in a shared Notebook, allowing users to
  share *parts* of their Notebook in a way that can be directly used in other
  Notebooks.  For example, a user could decide to share their Notebook via the
  above service, at which point the user is prompted to fill out a form that
  provides a basic description of the Notebook *and* asks the user to (optionally)
  select objects in the Notebook they would like to share as part of the Notebook's
  "public API".
- ...Ideally, all of the above projects could be implemented and integrated with
  each other.

### 2. Ingestion

The *Ingestion* phase describes the step in a scientific workflow when the
user loads the data they want into an analysis-ready format, such as an Xarray
Dataset.  This phase should abstract away concepts that the user should not need
to know about the data itself, such as the format of the data and where the data
is located.  Ideally, the user should only need to understand the semantics
describing the scientific aspects of the data that actually impact their analysis.
Data format or location should not be completely *hidden* from the user, but they
should not need to know anything about that to perform analysis.

Ideally, a user would simply "select a dataset"
(see [Search & Discovery](#1-search--discovery))
and be provided with a queriable object, such as an Intake catalog object.  The
user should be able to search and subselect this object using terminology that is
understood by the *users of the data*, not the developers of the software.
Ideally, the queriable catalog object should provide the user with the
information they need to understand what the data *is*, rather than needing the
user to look up information on an external website.  Ideally, once the queriable
object has been queried (possibly multiple times) to subselet the data desired
for the user's analysis, it should be trivial to return the subselected dataset
in an analysis-ready data format, such as an Xarray Dataset.

Much of this is already provided by `intake` and its plugins, but a critical
aspect of this step is making it easy for data *providers* or *managers* (i.e.,
the people who make the data available for others to analyze) to create catalogs
with the proper semantic translations.  If this step (catalog generation) is
difficult, then catalogs will not be created *at all*, making all the effort of
[Phase 1](#1-search--discovery) pointless.  Ideally, catalogs should be generated
automatically when data is generated, or they should be easily generated
semi-automatically with a simple command-line utility.

#### Possible Projects

- Automatic catalog generation for model data (i.e., catalog generated automatically
  with model run)
- A "master catalog" service, that provides a "master" catalog for all datasets
  stored at the same location.  (It makes no sense to aggregate catalogs for datasets
  stored at scattered locations unless the download cost is extremely low.)  This
  would make it possible for a master "config file" be created for `intake` so that
  an individual catalog need never actually be loaded (i.e., the master catalog is
  loaded automatically).  This could also make it possible to search and discover
  datasets directly from within the Notebook, which might eliminate the need for a
  JupyterLab extension or external website service for search and discovery.
- Automatic catalog generation for dataset (choose your dataset here)

### 3. Analysis

Data analysis is the process of turning computational data into knowledge.  This
is done primarily by computing one or many *reductions* of the original data and
visualizing these reductions.  Sometimes the visualizations are tabular (i.e.,
just numbers in a table), and sometimes the visualizations are graphical (i.e.,
generating plots).  Reductions can be *slices* of the original dataset, or they
can be wholely new computed artifacts.  Reductions are almost always computed
because the original data usually has more then 2 or 3 dimensions.  Three-dimensional
rendering of data is certainly possible on 2D screens, but this is only possible
if the platform allows dynamic interaction with the visualization.  If the
third dimension is time, then the data can be visualized with a movie, but the
practicality of that depends on how long the movie would be to watch the entire
time history.  Normally, a subset of the data is selected, even for 3D rendering
or animation.

Xarray provides an excellent interface for slicing, subsetting, and quickly
visualizing 1D or 2D data.  It also provides an excellent interface for basic
operations on the data to compute new data artifacts (e.g., climatologies,
anomalies, etc.).  Some artifacts, however, are complicated to produce, and
may require an Xarray-aware package to provide the new operation.  We refer
to such abstractions as *Operators*.  At NCAR, new Operators should be placed
in the GeoCAT package.

Visualization can also be complex, and canned visualization routines for specific
kinds of plots should be placed in the GeoCAT-viz package.

With the success of Xarray and visualization packages like Matplotlib and
Cartopy, much of what is needed for analysis already exists, but there are
analysis operations that are routinely done that are needlessly complex.  These
operations should be functionalized and packaged.

#### Possible Projects

- Encoding a complete coverage of the CF conventions is too great of a task
  for a single project, but adding functionality to
  [CF-Xarray](https://github.com/xarray-contrib/cf-xarray) would make things
  much easier for users.
- Better calendar capabilities would be much appreciated.  Traditional
  timestamps used in Pandas and Xarray are fine but they don't necessarily
  work with non-standard calendars.  Any time a *time difference* must be
  computed (i.e., a duration), knowledge of the calendar is critical.  The
  Pandas and Xarray and Numpy calendar is assumed to be the proleptic
  Gregorian calendar.  Being able to properly compute durations in other
  calendars as well as convert between calendars would be very helpful.
- Regridding datasets so that they can be directly compared on the same
  grid would be very helpful.  I have always believed that a representation
  of a gridded data object (i.e., grid + data + coordinates) should be
  abstracted away so that the user need not know anything about the grid.
  I call that a *field*.

### 4. Check-point

The term *check-pointing* here refers to saving a computed artifact from
the *Analysis* phase for later access.  Check-pointing is typically done
specifically for long and/or expensive computations that you do not wish
to reproduce unless the computation producing the artifact needs to
change.  The easiest way to check-point is to simply apply an operation
such as `to_netcdf` or `to_zarr` on an Xarray Dataset.  However, unless
other operations in the same workflow are aware of the check-point data,
re-running the workflow will simply recompute the artifact and re-save
it to disk.

From a user's point of view, ideally, check-pointing should be automatic.
That is, if a an object is computed in the notebook, it is cached on a
persistent storage platform so that it can be retrieved from disk instead
of recomputed.  This requires knowing the *history* of the artifact data
and knowing if any element in the artifact's history has been modified
(e.g., a modification to a function computing an intermediate product).
If any element in the artifact's history has changed, then it must be
re-computed "when accessed."

To limit the amount of data stored on disk, it makes sense to only
cache selected thing in the Notebook.  These items might correspond to
the "public API" that a user designates for a notebook in the
*Workflow Extension* model of [Search & Discovery](#1-search--discovery).

#### Possible Projects

- An automatic caching mechanism for the data objects in the "public API"
  of a Notebook.  Could be similar to Xpersist, but could also be more
  generic.  This is the same as the project suggesting in
  [Section 1](#1-search--discovery).

### 5. Publication

#### Possible Projects

### Platform

#### Possible Projects

-----------

#### Current State & Limitations

- Deployments of the **Platform** for multiple users consist of a JupyterHub
  that authenticates and spawns single-user JupyterLab instances.
- The JupyterHub can provide system-wide kernel environments or user-specific
  custom kernels (via the `nb_conda_kernel`+`ipykernel` JupyterLab extensions)
  for use in a user's Notebook.
- Notebooks are saved in the user's personal storage space, or wherever they
  can access from their *home* directories (or the directory JupyterLab is
  launched from)
- On NCAR's HPC system, JupyterLab sessions are spawned on HPC compute nodes.
- Notebooks with their kernel/environment can be shared via Binder, which
  requires a BinderHub service running "near" the JupyterHub service
- Local data (or data available from the JupyterLab session) cannot easily
  be "discovered"
- User-created Notebooks cannot easily be discovered
- Sharing Binders (i.e., "Binderized" Notebooks) entails containerization

#### Future State & Problems to Solve

- One NCAR's HPC, can JupyterLab sessions be placed on the login nodes?
- Can feedback from the system can be fed to the JupyterLab session running
  (e.g., system is going down, you have exceeded resource limitations, etc.)?
- What's the best way of publishing and sharing Notebooks?
- What's the best way of sharing environments/kernels *with* the Notebooks?
- How can we make published Notebooks easily *discoverable*?
- How can we easily re-use Notebook content (code or generated data) in other Notebooks?

------------

### Search & Discovery (S&E)

Some minimal S&E is provided by Intake and Intake-ESM.  General search and
discovery is *not* provided by Intake, which would include making it easy for
a scientist ignorant of an Intake catalog's to semantically search and discover
relevant datasets, on what system they can be analyzed, and where to locate
their Intake catalogs.  In general, Intake and Intake-ESM provide *semantic
subsetting* of the datasets or collections.

NCAR's [Digital Asset Services Hub (DASH)](https://www2.cisl.ucar.edu/dash),
could provide easy S&E for NCAR assets.  One thought then might be for each
"analyzable" DASH asset to also indicate the path/link to an associated
Intake catalog file.  Then, the DASH asset can be easily discovered via
DASH's online S&E interface, it is is just a simple "cut and paste" of the
Intake catalog link into a Jupyter Notebook session to then get the
queriable Intake collection.

Another, more complicated, option is to integrate NCAR's DASH S&E into
Jupyter Notebooks via something like a DASH Labextension.  Then the S&E
step that occurs via DASH could then be made "push-button" with no
cut-and-paste step between the user's DASH session and their Jupyter-based
analysis.

Efforts to automatically include Intake catalogs with model output (i.e.,
automatic generation of Intake catalogs from CESM runs) should also be
considered a part of the S&E phase.

### Ingestion

The main aspect of ingestion on the Pangeo platform is handled by Intake
and Xarray, via the very simple `to_xarray` method of Intake-Xarray's
data sources.  However, ingestion implies related issues in the ingestion
operation, such as those pertaining to data formats, metadata and data
standardization and specifications that make it easier to ingest.

Also, since Intake is the interface between the Search & Discovery phase
and the Ingestion Phase, it is questionable whether cataloging issues (such
as dataset metadata and standards and specifications) should fall within
the S&E phase or the Ingestion phase.  For practical purposes, I would
suggest that all work related to "how Intake works" be considered as part
of the Ingestion phase, and all work related to "generating Intake
catalogs" as part of the S&E phase (i.e., discoverable data).

### Analysis

A great deal of analysis is provided through the Xarray API.  However,
it is clear to many that the Xarray API has limitations for certain
domain-specific needs, and so thin layers *on top* of Xarray should be
considered to improve the UX.  This includes overlap with the NCL-to-Python
effort, as well as additional diagnostic efforts.

Since a critical aim of the Pangeo project is to provide *scalable*
solutions, Dask is also a critical element of the Analysis phase.  Making
Dask work more efficiently and effectively on NCAR platforms is a critical
aspect of what we need to do.  Hence, Dask-Jobqueue, Dask-Labextension,
Dask-MPI, and core Dask elements should be considered target projects.

### Check-Pointing

Especially in the case of published analysis results, it may become
increasingly desirable to save the results of the Analysis phase for
later reference.  In fact, the *only* reason to save more data to disk
when data storage costs are as expensive as they are is to reference
the data in publications.  Simply saving data to disk for convenience
is no longer something we can afford.  Hence, check-pointing not only
includes the technology to save data to file (e.g., `xarray.Dataset.to_zarr`
or `xarray.Dataset.to_netcdf`), but it also includes metadata that allows
the check-point data to be referenced.

Additionally, once data is referenceable, it can be discovered and ingested
for additional analysis.  Hence, whatever check-pointing technology is
considered should integrate will with the S&E, ingestion, and analysis
tools already discussed.  For example, check-pointed data could be
cataloged for later ingestion with Intake, and therefore function like
a caching mechanism for complex analysis.

### Publication

The most significant part of publication is visualization of data
analyses, which includes making existing visualization utilities in the
Pangeo ecosystem (e.g., matplotlib, cartopy, hvplot, etc.) work with
all of NCAR's datasets.  That means functionality to deal with structured
*and unstructured* (e.g., MPAS) grids, model-generated and observations.

Additionally, though, the Publication phase includes sharing and
distribution of Jupyter notebooks and the results from Jupyter notebooks.

## Objectives

- Improve ingestion of NCAR assets by leveraging Intake-ESM catalogs
- Itemize and implement necessary missing domain-specific tooling on
  top of Xarray
- Make all forms of Dask usage efficient on NCAR platforms
- Make check-pointed analysis data referenceable with Intake catalogs
- Make sharing and distributing scientific analyses easy and automatic
- Make visualization of Xarray data from any grid simple and accurate
- Improve the interoperability of components of the Pangeo platform on
  NCAR systems, including making batch-mode operation easy and reliable.

## Example Projects

- Automatic generation of Intake catalogs from CESM runs
- ESMLab improvements and features
- Xpersist, or similar, prototype
- Dask-MPI integration with Dask-Labextension
- Investigate nbgallery for notebook sharing at NCAR
- "Smart" plotting of MPAS data directly from Xarray
- Investigate Papermill for batch-mode application of Jupyter notebooks
