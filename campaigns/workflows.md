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
looking for a starting point for their analysis.  This includes searching for,
and discovering, a particular dataset or datasets, but it also includes searching
for, and discovering, a particular *existing* workflow that a user either
(1) modifies to create a new workflow or (2) extends to add to the workflow.
Thus, users need to be able to search for both data that they can ingest into
their Notebooks *and other* Notebooks that they can modify or extend.

When searching for *data*, it makes sense for the entry point for the workflow
be *either* from within JupyterLab (e.g., a "Data Search" tab provided by a
JupyterLab extension that hooks into a service like DASH) *or* from an external
website (e.g., [the DASH repository](https://www2.cisl.ucar.edu/dash)).  Ideally,
datasets selected from a search from *within* JupyterLab would provide data to the
user in a form that is *ready for analysis* (e.g., an Xarray Dataset).  Ideally,
datasets selected from an external website would automatically take the user to a
JupyterLab session with the data "pre-loaded" in an analysis-ready format (e.g.,
an Xarray Dataset).

When searching for *workflows* to modify or extend, like the *data* searches,
it makes sense for the entry point for the *new* workflow be *either* from within
JupyterLab or from an external website.  Ideally, workflows selected for modification
would load the selected Notebook into JupyterLab in a *usable state* (i.e., with
the kernel required to run the Notebook).  Ideally, workflows selected for
extension should make available a "public API" of elements from the *original*
workflow that can be used in the *new* workflow, without the user needing to
manually *run* the original workflow Notebook.  In either case, the result is
a running JupyterLab session with the new Notebook loaded.

#### Possible Projects

- A JupyterLab extension that provides a service connected to the DASH respository
  that can "inject" `intake` code into your running Notebook (or launch a new
  Notebook) by appending a new cell.
- A JupyterLab extension that connects to a service where Notebooks can be "added"
  or "retrieved" from a shared "repository."
  - A further expansion of this service that can "import" elements from the selected
    Notebook without the need to run the selected Notebook (see [Check-point](#4-check-point))
- A searchable website of "shared" Notebooks that launches selected Notebooks in
  a JupyterLab session, copying the Notebook into the user's personal space.  ...This
  would be like a Notebook Gallery with Binder links from each Notebook, if each
  Binder session could persist.
  - Make elements inside each Notebook in the Gallery "importable" into other Notebooks.

### 2. Ingestion

The *Ingestion* phase describes the step in a scientific workflow when the
user loads the data they want into an analysis-ready format.  This phase should
abstract away concepts that the user should not need to know about the data itself,
such as the format of the data and where the data is located.  Ideally, the user
should only need to understand the semantics describing the aspects of the data
that actually impact their analysis.  Data format or location should not be
completely *hidden* from the user, but they should not need to know anything
about that to perform analysis.

Ideally, a user would simply "select a dataset" (see [Search & Discovery](#1-search--discovery))
and be provided with a queriable object, such as an "intermediate" catalog object
or an Xarray Dataset.  The user should be able to search and slice this object
using terminology that is understood by the *users of the data*, not the developers
of the software.

#### Possible Projects

### 3. Analysis

#### Possible Projects

### 4. Check-point

#### Possible Projects

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
