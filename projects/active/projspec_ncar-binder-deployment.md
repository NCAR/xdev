# Project: NCAR Pangeo Infrastructure Deployment on AWS

- [Project: NCAR Pangeo Infrastructure Deployment on AWS](#project-ncar-pangeo-infrastructure-deployment-on-aws)
  - [Campaigns](#campaigns)
  - [Overview](#overview)
  - [Repositories](#repositories)
  - [Skills & Knowledge](#skills--knowledge)
  - [Deliverables](#deliverables)
  - [Milestones & Timeline](#milestones--timeline)

## Campaigns

- WORKFLOWS: Publication

## Overview

The primary goal of this project is to gain expertise in deploying and maintaining Pangeo infrastructure in a cloud computing setting, specifically on Amazon Web Services (AWS). As part of this project, we will deploy an NCAR Pangeo+Binder Hub on AWS using GitHub Actions and HashiCorp Terraform.
A secondary goal of this project is to provide a platform for developing and testing new technologies in the Pangeo software ecosystem that can be deployed on NCAR systems or with other Pangeo cloud deployments.
The success of this project will be determined by a working Pangeo deployment on AWS that we can use, internally, for testing, prototyping, and experimentation.

**NOTE:** Cost of running this service will be closely monitored.  Success of this project can only be achieved if the costs are both *well understood* and *affordable*.

## Repositories

- https://github.com/NCAR/ncar-pangeo-binder-terraform-deploy
- https://github.com/pangeo-data/terraform-deploy
- https://github.com/pangeo-data/pangeo-binder/tree/staging/k8s-aws
- https://medium.com/pangeo/terraform-jupyterhub-aws-34f2b725f4fd

## Skills & Knowledge

- Knowledge of [BinderHub](https://github.com/jupyterhub/binderhub): allows users to interact with code and environment from a Git Repo within a JupyterHub instance.
- Knowledge of [JupyterHub](https://github.com/jupyterhub/jupyterhub): provides authentication, and spawns single user Jupyter Notebook servers.
- Knowledge of [Kubernetes](https://kubernetes.io/): Kubernetes is an orchestration tool allowing users to run and manage container based workloads.
- Knowledge of [Dask-Gateway](https://gateway.dask.org/): Dask Gateway provides a secure, multi-tenant server for managing Dask clusters.
- Knowledge of [Terraform](https://www.terraform.io/docs/index.html): Terraform is an open source tool that allows a user to define their infrastructure as code using a simple, declarative language and to deploy and manage that infrastructure across a variety of public cloud providers (e.g., Google Cloud Platform, Amazon Web Services, Microsoft Azure, Digital Ocean) using a few commands.
- Knowledge of [GitHub Actions](https://github.com/features/actions): GitHub Actions provide continuous integration and continuous delivery features through GitHub.
- Knowledge of [AWS](https://aws.amazon.com/)

## Deliverables

- A GitHub repository with Terraform Github actions enabled for continuous deployment.
- An analysis of usage metrics and cost
- Summarize lessons learned in a blog post

## Milestones & Timeline

| Milestone                                      | Deadline     | Done    |
|:-----------------------------------------------|:------------:|:-------:|
| BinderHub first deployment    | {2020-07-18} | &#9744; |
| Enable Dask-Gateway                    | {2020-08-18} | &#9744; |
| Testing and Benchmarking            | {2020-10-18} | &#9744; |
| An analysis of usage metrics / cost collection                    | {2020-11-18} | &#9744; |
| Write-up                    | {2020-12-18} | &#9744; |
