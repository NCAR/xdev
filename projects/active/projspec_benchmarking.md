# Project: BENCHMARKING

Comprehensive Pangeo benchmarking on HPC systems

## Campaigns:

- WORKFLOWS

## Overview

There is a routine request from many people, usually at high levels in organizations,
for benchmarking numbers and studies showing the scalability and performance of the
Pangeo stack.  To address this need, the
[pangeo-data/benchmarking](https://github.com/pangeo-data/benchmarking) repository was
created.  An initial system was created for benchmarking *computation-only* operations,
with the complications of I/O removed from the benchmarks.  The results of this work
was presented at the [2019 Supercomputing Conference](https://sc19.supercomputing.org/)
as part of the [Third Workshop on Interactive High-Performance Computing](https://sites.google.com/view/interactive-hpc/home).

The next phase of benchmarking involves full, *realistic* workflows as part of the
benchmark suite, including I/O operations.  A great many more metrics must be measured
during each benchmark operation, and a thorough analysis of these metrics must be conducted
to determine which metrics are clear indicators of performance and scalability.

The end result of this study should be a paper for publication in an appropriate venue.

## Repositories

- https://github.com/pangeo-data/benchmarking
- https://github.com/pangeo-data/storage-benchmarks (reference only)
- https://github.com/rabernat/zarr_hdf_benchmarks (reference only)

## Skills & Knowledge

- Knowledge of the basic Pangeo stack (xarray, dask)
- Knowledge of batch-mode Dask jobs (i.e., for setting up and running the benchmarks)
- Knowledge of underlying I/O formats, such as Zarr and NetCDF

## Deliverables

- An pip-installable (and possibly conda-installable) benchmarking *utility* with set
  version numbers, based on existing benchmarking code
- Design and implement a versioning scheme for benchmark *environments*, for example
  based on snapshots on given dates.
- Implement basic I/O operations in the benchmarking *utility*
- Design and implement a tagging mechanism to pin benchmark operations to benchmark
  *environment* versions (e.g., some operations may only work with certain versions
  of the environment), or possibly implement a version *exclusion* mechanism instead
- Refactor benchmark operations to be linked together into benchmark *workflows*
- Identify benchmark metrics to be stored for each operation/workflow run (e.g.,
  utility version, environment version, timestamp, graph size, chunk size,
  workflow/operation, etc.)
- Define the suite of benchmark parameters for runs on all systems
- Generate benchmark metrics on Cheyenne, Casper, HAL, etc.
- Sumarize results in a paper

## Milestones & Timeline

| Milestone                        | Deadline     | Done    |
|:---------------------------------|:------------:|:-------:|
| Installable benchmarking utility | ?            | &#9744; |
| Benchmarking environments        | ?            | &#9744; |
| Basic I/O operations             | ?            | &#9744; |
| Operation-environment versioning | ?            | &#9744; |
| Workflow benchmarks              | ?            | &#9744; |
| Benchmark metrics                | ?            | &#9744; |
| Benchmark run suite definition   | ?            | &#9744; |
| HPC benchmarking                 | ?            | &#9744; |
| Paper                            | ?            | &#9744; |
