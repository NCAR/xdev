# Project: NBInvest

Notebook Gallery Investigation

## Campaigns:

- WORKFLOWS
- EOCB

## Overview

With the goal of producing a notebook gallery that scientists can learn from via examples demonstrating Pangeo tools, we want to consolodate all of the many fragmented notebook galleries within the Pangeo community and add our contributions from the NCAR/notebook-gallery. 
    There are 2 targeted modalities for sharing notebooks: Static views
of the notebooks (ex: Sphinx-nbexamples) and Binder. Both are useful for scientists as educational tools. The first being a strong method for reference material, the second being more hands on (ideal for tutorials, self-guided learning, etc). Ideally, we would like both static views and Binder for every notebook where possible.

To do this we have to answer a number of questions: 

1. Can we run nbconvert on Dask NBs? Notebooks that require Dask parallelism cannot currently be run from ReadTheDocs or Github Pages, making them impossible to build as part of a Sphinx website.
2. Can we bring all examples into 1 gallery (from disparate repos)? Currently all of our notebooks are scattered across many different repositories, each repository for a different purpose. Many of these repositories are binderized with their own environments.
3. Does nbconvert NEED to run NBs (or display saved rendered output)? This could solve the need for multiple environments, and it can also solve the requirement that the notebooks run when building the Sphinx site on ReadTheDocs or GitHub Pages. However, this may not be ideal; perhaps someone changes a cell without rerunning the output, then the notebook displayed is no longer accurate.
4. Can we have multiple environments? This is an alternative choice to point 3. 
5. Can we run our own BinderHub on Cheyenne/Casper (for NCAR specific workflows)? This is somewhat out of our control, but it could demonstrate the use of the Pangeo stack on NCAR systems. This would require an authentication step on the BinderHub. An alternative to this would be to move NCAR data to the cloud from Glade, but then we may no longer be demonstrating use ON NCAR systems.
6. What is the mission statement of the existing Pangeo gallery? We need to talk to Ryan Abernathy and the authors of the notebooks in many of the other galleries. 


## Repositories

- NCAR/notebook-gallery
- pangeo-data/pangeo "Use Cases"
- pangeo-data/pangeo={*}-examples
- pangeo-data/pangeo-example-notebooks

## Skills & Knowledge

- Jupyter Notebooks
- Python
- Xarray
- Dask
- Intake-ESM
- Cartopy and plotting tools
- Nikola (or similar blogging tool)
- Sphinx-nbexamples
- ReadTheDocs
- GitHub Pages actions
- An understanding of Atmospheric and Oceanic Science questions/calculations

## Deliverables

- A fleshed out project plan for contributing our notebooks to a consolodated notebook gallery.

## Milestones & Timeline

| Milestone     | Deadline     |
|---------------|--------------|
| Answer for Q6 | 2020-02-14 |
| Answer for Q1 | 2020-02-21 |
| Answer for Q2 | 2020-02-28 |
| Answer for Q3 | 2020-02-28 |
| Answer for Q4 | 2020-03-06 |
| Answer for Q5 | 2020-03-13 |
| New Project Spec | 2020-03-20 |
