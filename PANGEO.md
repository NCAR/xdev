# Xdev as a member of Pangeo

One of the Xdev Team's responsibilities is to act as a member
of the Pangeo Community "stationed at NCAR."  In general, anything
happening in the Pangeo Community is "fair game" for Xdev work,
but it is common that Xdev concerns itself with more NCAR-focused
aspects of the Pangeo effort.  Regardless of what we actually
work on and contribute to, being a member of Pangeo means a number
of things.

## Learn the Stack

The first aspect of being a member of Pangeo is learning the
"Pangeo Stack."  There is no single approved "stack" of software
for *all* of Pangeo.  The Pangeo Community has members from many
different areas of the geosciences, and each "subcommunity" has
different needs.  Hence, the complete stack tends to change from
context to context.  However, there is a *core* set of tools that
the Pangeo Community endorses, and they are:

- [Conda](https://conda.io)
- [Xarray](https://xarray.pydata.org/) (or [Iris](https://scitools.org.uk/iris))
- [Dask](https://dask.org) (and Dask-Distributed)
- [Intake](https://intake.readthedocs.io/) (and its plugins)
- [Jupyter](https://jupyter.org/) (including JupyterLab/Hub and Binder)

The Pangeo Community also endorses a number of different storage
formats for different environments, with [Zarr](https://zarr.readthedocs.io/)
being strongly recommended for cloud deployments and NetCDF being
recommended for HPC deployments.

More information about the "Stack" can be found on the Pangeo
website: [http://pangeo.io](http://pangeo.io).

The community endorsed tutorial for these tools can be found here:
[https://github.com/pangeo-data/pangeo-tutorial](https://github.com/pangeo-data/pangeo-tutorial).

## Stay Connected

The second aspect of being a member of Pangeo is knowing how to
stay connected with other members of the Pangeo Community.  Pangeo
communicates in a number of different spaces, which means it can
be challenging to fully understand where to go for which kind of
communication and to follow what is happening in the Pangeo Community
space.  I will try to enumerate the different communication spaces
that the Pangeo Community uses and how they use each space:

1. **GitHub:**  Most of the Pangeo Community contribute to Pangeo
   as developers.  Hence, most of their communication happens in
   GitHub, which is why we (Xdev) try to do the same.  Like Xdev,
   Pangeo contributes to *many* different repositories, though,
   many of which exist outside the `pangeo-data` GitHub organization.
   (In fact, you will find that almost *all* software in the Pangeo
   stack is in a different GitHub organization.)  The `pangeo-data`
   GitHub organization is primarily used for the website, the gallery,
   deployments, benchmarking, tutorials, etc.  The `pangeo-data/pangeo`
   repository is *special*, though.  This repository is used for
   "community-wide" discussions pertaining to software, deployments,
   development plans, etc.  These all happen in the GitHub Issues on
   this repository.  It was the first, and is still one of the
   primary, channels used for communication across the community.

2. **Weekly Meetings:**  The Pangeo Community holds weekly *general*
   meetings over Zoom, and the different "Technical Working Groups"
   in Pangeo hold bi-weekly meetings, too.  The schedule for these
   meetings can be found on the [Pangeo Meeting Calendar](https://pangeo.io/meeting-notes.html#meeting-calendar).
   You can add this calendar to your Google Calendar so you don't miss
   anything important.

   These meetings are usually informal and *open to anyone*.  I recommend
   that if you want to stay connected to the Pangeo community, you should
   *at least* watch the [meeting notes](https://docs.google.com/document/d/e/2PACX-1vRerhoxG-wOvh-wQTj7F8HPYve75l8pAtL-tgtzY_3YLqVUsaMSEgE4K70HgMt5S91FMwSu8EIizewy/pub)
   regularly and/or attend the general weekly meetings with some frequency
   (e.g., every other week).

3. **Gitter:**  The Pangeo community has general discussions in their
   Gitter channel: [https://gitter.im/pangeo-data/Lobby](https://gitter.im/pangeo-data/Lobby).
   Since this is primarily for rapid communication, these discussions can
   be varied.  They can be long conversations between people who are sprinting
   on something technical, or they can just be "How do I...?" or
   "I'm having a problem with..." discussions.

4. **Discourse:**  For longer, less-technical discussions (and sometimes for
   technical discussions, too), the Pangeo Community has started using Discourse.
   You can find their Discourse space here:  [https://discourse.pangeo.io/](https://discourse.pangeo.io/).
   I would go to Discourse when you have something that you don't necessarily
   need discussed *solely* by developers, this is where it should take place.

## Be Involved

The last aspect of being a member of the Pangeo Community is actually contributing.
This is a pet peeve of mine, so I want to emphasize this, but at the same time I'll
try not to harp on...

Being a *member* of the community means actually chipping in.  This is the *only*
way for Open Source Software to survive.  It's not enough to just *observe* what is
happening in the community and to *use* the software stack; members of the community
need to actually chip in to help solve problems and contribute code to help achieve
community goals.

The truth is that *this is hard!*  It is very easy for our jobs to take so much of
our time that we do not feel that we have time to do any development on things that
"don't have anything to do with NCAR."  But that's not the right way of seeing things.
All of the OS software that we use was developed by volunteers, and their effort
made it possible (or easier) for us to do what we do.  It's fair for us to spend
some of our time contributing back to those OS communities.  Hence, keep some room
in your calendar to give back.  It doesn't have to be extremely large, but even a
small contribution can make a difference.
