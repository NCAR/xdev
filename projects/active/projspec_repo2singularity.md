# Project: Repo2singularity

Repo2singularity

## Campaigns:

- WORKFLOWS: Publication

## Overview

[BinderHub](https://github.com/jupyterhub/binderhub) allows users to interact with code and environment from a Git Repo within a JupyterHub instance. To achieve this, binderhub ties together

- [JupyterHub](https://github.com/jupyterhub/jupyterhub): Provides authentication, and spawns single user Jupyter Notebook servers.
- [Repo2Docker](https://github.com/jupyter/repo2docker): Generates a Docker image from the Git Repo.
  
Currently, BinderHub as a Python package can not run on traditional HPC systems. As [Joe Hamman](https://github.com/jhamman) pointed out in the [BinderHub for HPC](https://discourse.jupyter.org/t/binderhub-for-hpc/143/4) post on discourse, some of the reasons why it's difficult to run BinderHub on HPC include:

- HPC systems are rarely container friendly (BinderHub requires both Kubernetes and Docker).
- Often, compute nodes do not have access to the outside network.
- Managing a server attached to an HPC is not going to be popular from sys admins (though this opinion is changing in the HPC world)
- Provisioning resources requires waiting in a job queue.

Despite these challenges, there's hope that we can re-purpose some key pieces of BinderHub, and be able to get *BinderHub-like functionality on HPC*. [Yuvi Panda](https://github.com/yuvipanda) suggested breaking BinderHub down into two components:

1. Dynamic image building from a git repository. One way to accomplish this on an HPC system is to swap Docker with some HPC compatible container/image builder. For example [Singularity](https://github.com/hpcng/singularity), [Shifter](https://github.com/NERSC/shifter), or [Charliecloud](https://github.com/hpc/charliecloud).
2. Launching an interactive web application from inside the image. This involves some work on JupyterHub's side.  

This project is going to address the first point (1): **Dynamic image building from a git repository**. Since singularity containers are currently supported on Cheyenne (`module load singularity/3.3.0`), this project will implement **repo2singularity**, a sister project of repo2docker that will allow users to turn git repos into singularity images that can be run on Cheyenne, Casper or other HPC systems that support singularity containers.

## Repositories

- https://github.com/jupyter/repo2docker
- https://github.com/andersy005/repo2singularity

## Skills & Knowledge

- Knowledge of Docker (Required)
- Knowledge of [singularity](https://github.com/hpcng/singularity) (Required)
- Knowlegde of [repo2docker](https://github.com/jupyter/repo2docker) (Optional)

## Deliverables

1. Implement `repo2singularity`, a command line tool that will

   - build singularity images from a git/GitHub repo.
   - push built images to a singularity image registry such as https://cloud.sylabs.io/library

   Example:

   - Build and push image via `repo2singularity`:

     ```bash
     repo2singularity --push --image-name binder-examples-continuous-build https://github.com/binder-examples/continuous-build
     ```

   - Pull built image via `singularity`:

     ```bash
     singularity pull library://andersy005/test/binder-examples-continuous-build:latest
     ```

2. Write up thoughts on `repo2singularity` usage at NCAR upon project completion.

## Milestones & Timeline


| Milestone                                      | Deadline     | Done    |
|:-----------------------------------------------|:------------:|:-------:|
| `repo2singularity` prototype implementation    | {2020-05-18} | &#9744; |
| `repo2singularity` demonstration               | {2020-05-27} | &#9744; |
| `repo2singularity` write-up                    | {2020-06-15} | &#9744; |
