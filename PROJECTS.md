# Current Projects - 2020

## Theme

Improving ESM Diagnostics

## Projects
Multiple for different diagnostic packages.  Clearly-defined by objectives and deliverables.  Design documents with requirements.

## Categories (and repositories)
* Platform Integration & Deployment
   * conda
   * jupyter hub/lab
   * labextensions
* Core Infrastructure
   * xarray
   * numpy
   * dask (distributed, MPI, jobqueue, etc.)
   * pandas
* Cataloging & Workflows
   * intake-esm
* Domain-Specific Functionality
   * esmlab
   * pop-tools (mom-tools)
* Education & Outreach (& supporting the NCL transition to Python)
   * notebook-gallery
   * ncar-python-tutorial

## Generic Process
1. Talk to scientist to determine workflow and desired end result
2. Determine what the platform needs to be (jupyter?)
3. Read data (intake-esm)
4. Compute diagnostics (New domain-specific functionality, or updated core infrastructure)
5. Shape final product (E&O)

## Existing Needs
* esmlab:
   * Define an API, but where the implementation lives is undetermined
   * Mission statement
* intake-esm:
   * Define behavior of multivariable datafile
   * Have CESM workflow generate a catalog file for every run
* notebook collaboration tools
   * Investigate Jovian
   * Investigate nbgallery
* ncar-python-tutorial
   * Self-driven tutorial curriculum