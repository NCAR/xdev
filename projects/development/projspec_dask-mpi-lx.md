# Project: Dask-MPI-LX

Dask-MPI Labextension

## Campaigns:

- WORKFLOWS

## Overview

Addressing [Dask-MPI Issue #44](https://github.com/dask/dask-mpi/issues/44), there is a use case
where the user launches their Jupyter Lab environment *with all of their necessary resources at
once*.  That is, during the Jupyter Lab launching/spawning process, the user requests resources
to run not only the Jupyter Lab process, but also the Dask cluster, as well.  This would be the
case if a user specified many CPUs or processing from the Spawner Options page of the NCAR
JupyterHub.  In such a situation, Dask-Jobqueue will spawn *more* jobs when you launch your
Dask cluster, and therefore will leave most of the resources you have already acquired stagnant.
On the other hand, Dask-MPI can take advantage of these resources by launching your Dask cluster
with MPI.

Currently, Dask-MPI provides a CLI (`dask-mpi`) and a batch-mode interface (`dask_mpi.initialize`).
The batch-mode interface can effectively do what is needed in the example use case from the previous
paragraph, *but it does require testing to prove this fact*.  However, in order for the Dask
Labextension (i.e., the Dask tab on the left in Jupyter Lab) to work with Dask-MPI, there needs
to be a Dask `Cluster` interface in Dask-MPI.  Currently, this does not exist, though I have
discussed it in [Dask-MPI Issue #9](https://github.com/dask/dask-mpi/issues/9).

## Repositories

- https://github.com/dask/dask-mpi
- https://github.com/dask/dask-labextension

## Skills & Knowledge

- Knowledge of Dask-MPI
- Knowledge of Dask-Labextension

## Deliverables

- Better and more thorough testing (i.e., testing refactor, use `mpirical`)
- Test for `dask_mpi.initialize` in multi-process JupyterHub-spawned environment
- Implement `dask_mpi.MPICluster` interface and test with Dask-Labextension, according
  to discussion in [#9](https://github.com/dask/dask-mpi/issues/9)
- Should close Dask-MPI Issues [#9](https://github.com/dask/dask-mpi/issues/9) and
  [#44](https://github.com/dask/dask-mpi/issues/44)
- On project completion, write up thoughts on how NCAR's JuptyerHub can use Dask-Labextension
  better.

## Milestones & Timeline

| Milestone                                      | Deadline     | Done    |
|:-----------------------------------------------|:------------:|:-------:|
| JupyterHub Dask-MPI demonstration              | {2020-01-10} | &#9744; |
| `dask_mpi.MPICluster` JupyterHub demonstration | {2020-02-10} | &#9744; |
| NCAR Dask-Labextension write-up                | {2020-03-10} | &#9744; |
