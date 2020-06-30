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

The [Xdev Vision Statements](../PURPOSE.md#xdev-vision-statements) are easy
to state in brief, but harder to state in detail.  I will try to describe what I
see as the vision of the future of scientific workflows, based on the Pangeo
ecosystem.

### Search & Discovery

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

### Ingestion

The *Ingestion* phase describes the step in a scientific workflow when the
user loads the data they want into an analysis-ready format, such as an Xarray
Dataset.  This phase should abstract away concepts that the user should not need
to know about the data itself, such as the format of the data and where the data
is located.  Ideally, the user should only need to understand the semantics
describing the scientific aspects of the data that actually impact their analysis.
Data format or location should not be completely *hidden* from the user, but they
should not need to know anything about that to perform analysis.

Ideally, a user would simply "select a dataset"
(see [Search & Discovery](#search--discovery))
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
[Phase 1](#search--discovery) pointless.  Ideally, catalogs should be generated
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

### Analysis

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
  *NOTE:* The `cftime` package might be able to properly compute temporal
  durations properly, but it is uncertain if it can convert calendars.
  One simple way to convert calendars is to have a *baseline* calendar
  (e.g., Julian) and to conert calendars by going *through* the baseline
  calendar.  Thus, every calendar needs to know how to convert its datetimes
  to and from the baseline calendar.
- Regridding datasets so that they can be directly compared on the same
  grid would be very helpful.  I have always believed that a representation
  of a gridded data object (i.e., grid + data + coordinates) should be
  abstracted away so that the user need not know anything about the grid.
  I call that a *field*.
- Make it easier to plot data on unstructured grids with Python, such as MPAS
  data.  May need utilities to deal with cyclic coordinates with unstructured
  data.

### Check-point

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
*Workflow Extension* model of [Search & Discovery](#search--discovery).

#### Possible Projects

- An automatic caching mechanism for the data objects in the "public API"
  of a Notebook.  A good candedate for the base functionality (or possibly
  the entire solution) might be [provenance](https://github.com/bmabey/provenance).
  *NOTE:* This is the same as the project suggestion in [Section 1](#search--discovery).

### Publication

The publication phase of a workflow is when the final workflow is
*published* for other users to use.  This is the same as the process
suggested in the [Search & Discovery](#search--discovery) section,
above.  This phase involves submitting the Notebook to a "repository"
so that other users can "download" the Notebook for modification or
import elements of the Notebook's "public API" into their own Notebook.

Ideally, published Notebooks will be tested for regression as new
versions of the software stack change, so that owners of the Notebook
know that their Notebook will no-longer work with updated versions of
the Notebook environment.

Ideally, published Notebooks will be versioned and tied to a specific
environment/kernel with pinned versions of the software used in the
Notebook.  Ideally, the version of the Notebook and the version of the
environment can be updated independently of each other.

Ideally, published Notebooks will be published with metadata that
contains (at a minimum) a description of what the Notebook does, a
list of "public API" elements, the author's name and contact information
(email), the version of the Notebook, the date and timestamp of the
last change to the Notebook.  Ideally, this metadata will also contain
information about who has "downloaded" the Notebook for modification,
who has used which "public API" elements of the Notebook, how many
times has the Notebook been "downloaded" and how many times has each
"public API" element been accessed.

#### Possible Projects

- A Continuous Integration service to test Notebooks on HPC (and/or in
  the cloud) that informs owners of the Notebook of failures with
  given versions of the software in the Notebook kernel
- A Notebook publication repository (e.g., a Gallery) that is searchable,
  as proposed above, with versioning of the Notebook file and its
  kernel.

### Platform

The *Platform* is the suite of software products and deployments that
make scalable scientific workflows, as described above, possible.  The
platform currently exists as a combination of JupyterHub, JupyterLab,
Binder, Xarray, Dask, Intake, and peripheral packages in the Pangeo
stack.

Ideally, all of these utilities will work exactly the same way on
any platform, cloud or HPC.  Ideally, the user should *not* need to
understand how to set up the environment.  Ideally, the user should
be able to get as quickly to scientific analysis as possible, with as
many features or concerns about the platform being abstracted away as
possible.

#### Possible Projects

- Binder on HPC, or something that looks and works like Binder on HPC.
  Unlike the cloud version of Binder, the HPC version could require
  authentication.
- Dask clusters that span different cloud and HPC environments.  This
  would allow users to analyze datasets located at different locations
  from the same Notebook.  And if only reductions were directly
  compared, it would facilitate the computation of the reductions on the
  "server side" (i.e., next to the data) and then transport only the
  reduced dataset.
- Experimental Dask-Gateway deployment on Cheyenne+Casper
- Environments and Notebooks, if the data itself is portable, be "portable"
  as much as possible.  That is, if the data accessed by the Notebook
  can be downloaded easily, the Environment and the Notebook should easily
  be sharable with other users on a different deployment of the platform.
- Users of the NCAR JupyterHub should be able to run on the login nodes and
  not be charged.  It should be treated no differently than having multiple
  SSH sessions open on a login node.
- Users who SSH into Cheyenne or Casper should have access to the same Notebook
  kernels they have access to through the NCAR JupyterHub.
- Make Dask-MPI connect with the Dask-Labextension (i.e., create an MPICluster
  object)
