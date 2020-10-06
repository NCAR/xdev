# Project: Development-Driven JupyterHub Deployment

- [Project: Development-Driven JupyterHub Deployment](#project-development-driven-jupyterhub-deployment)
  - [Campaigns](#campaigns)
  - [Overview](#overview)
  - [Repositories](#repositories)
  - [Skills & Knowledge](#skills--knowledge)
  - [Deliverables](#deliverables)
  - [Milestones & Timeline](#milestones--timeline)

## Campaigns

- WORKFLOWS: Platform

## Overview

The goal of this project is to develop and maintain a development-driven Jupyterhub to allow us to test, and develop services such as `dask-gateway`, `nbviewer`, `binder` for HPC.

## Repositories

- https://github.com/NCAR/jupyterhub-deploy
- https://github.com/andersy005/jupyterhub-sshspawner
- https://github.com/andersy005/jupyterhub-sshauthenticator

## Skills & Knowledge

- Knowledge of JupyterHub
- Knowledge of Docker
- Knowlegde of Kubernetes
- Knowledge of [HashiCorp's vault](https://www.hashicorp.com/products/vault)

## Deliverables

- A multi-container Slurm cluster using docker-compose.
- A dask-gateway enabled JupyterHub running on Rancher Lab’s minimal Kubernetes [(k3s) distribution](https://github.com/rancher/k3d/).
- SSH Authenticator Plugin (that uses [HashiCorp's vault](https://www.hashicorp.com/products/vault) for SSH key management and rotation) for JupyterHub.


## Milestones & Timeline

| Milestone                                      | Deadline     | Done    |
|:-----------------------------------------------|:------------:|:-------:|
| Multi-container Slurm cluster   | 10-30-2020 | &#9744; |
| SSH Authenticator   | 11-30-2020 | &#9744; |
| A running JupyterHub with core features   | 12-30-2020 | &#9744; |
| Enable dask-gateway as a JupyterHub service   | 01-30-2021 | &#9744; |
