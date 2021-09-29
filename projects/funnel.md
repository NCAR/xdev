# Xdev Project: Funnel

[<img style="float: right;" src="https://hackmd.io/F4m79FUGQiuP_8X1haXR0Q/badge" />](https://hackmd.io/F4m79FUGQiuP_8X1haXR0Q)

[Project Trello Board](https://trello.com/b/FfQmlXoh/xdev-project-funnel)

Repositories:
- [xdev](https://github.com/NCAR/xdev) (for this document)
- [intake-esm](https://github.com/intake/intake-esm)
- [xcollection](https://github.com/NCAR/xcollection)

## Rolling Project Meeting Notes

### 25 August 2021

#### Review

- No changes since last week, so we'll skip.

#### Retrospective

- Team Practices
  - See the [2i2c Team Practices docs](https://team-compass.2i2c.org/en/latest/practices/index.html) and [Max and Anderson's "How we Get Stuff Done"](https://hackmd.io/yA_SvspYTxeiidtEV9uyIQ)
  - What are the goals for our Team Practices?
    - "Give team members insight into what one another is working on (not to “report up”)"
    - "Look for opportunities to work together and/or support one another’s work efficiently"
    - "Provide some social accountability to get stuff done"
  - Can we automate practices as much as possible?
    - e.g., auto-generated weekly GitHub issues (see [here](https://team-compass.2i2c.org/en/latest/practices/index.html#weekly-team-syncs))
    - The link between Trello and GitHub is tenuous, so not sure how to use both or how to get started
    - Not necessary to automate anything
  - Can we asynchronously work as a team as much as possible?
    - e.g., do people feel comfortable having a "sync day"
  - What do we need?
    - Dedicated pair programming time
  - How do we work as a team?
    - Pair Programming
      - Gather Town during weekly Team Time
      - And hackathons
      - VSCode plugin for pair programming (see [Max's blog post](https://ncar.github.io/esds/posts/2021/paired_programming_vs/))
    - Creating cards on the board for Issue assignment
      - Scope out weekly work (tasks) in 30-minute weekly meetings
      - Other tasks are added to board as the week progresses (by anyone)
    - Reviews - Tying GitHub to Trello
      - Manually attach GitHub issues and PRs to Trello cards
      - Code reviews then happen in GitHub
      - Card reviews happen during the asynch "sync day"
    - How to use the Trello board effectively
      - **Use it as a way of seeing what other people are working on** (and where you can work on next via the Backlog column)
      - Use labels
      - Use email notifications from the Trello board (when you are @mentioned on the board)
    - **Feel comfortable enough to ask questions (trust!) and need to be willing to drop what we are doing to help each other out**
    - How do we ask questions (urgent or otherwise?)
      - Zulip is for urgent questions
      - Trello is for non-urgent questions
    - "Asynchronous catch-up day"
      - Replace most of weekly meeting with a day of asynchronous catchup
      - Remind everyone to update the Trello board (everything you are working on)
      - Let everyone label their cards with what they want to hack on during the Team Time
      - Keep the board clean / clean up the board (consolidate duplicate cards, etc.)


#### Planning

- What are the next steps?
  - Finish main User Story
  - Work as a team to extract "To Do" items from the user story
  - [GatherTown Link](https://gather.town/app/NF3AQ5keuLywswp2/xdev-projects)
- How can we do this asynchronously (or at least outside of the weekly meetings)?

### 18 August 2021

#### Review

- https://trello.com/c/jiNo33GP/15-add-map-method-to-map-functions-to-all-datasets-in-collection
- https://trello.com/c/M0shh0bN/17-add-chooseallvar-method-to-collection and https://trello.com/c/18pfLL45/18-add-chooseanyvar-method-to-collection
  - Choosing multiple variables requires all variables have to be in a dataset to "choose" that dataset
- https://trello.com/c/n5Dw0mAt/12-create-collection-as-a-subclass-of-mutablemapping
  - xcollection is not a dictionary-like object designed to contain xarray.Datasets (like Dataset is designed to contain DataArrays)
- https://trello.com/c/xNK9Wxuu/11-add-collectioninit-to-initialize-from-dictionary-of-xarraydatasets
- https://trello.com/c/DUoWxd3b/10-create-a-xarray-collection-repository

#### Retrospective

- What is working?
  - Some people are charging forward on development!  That's great, and thanks for the wonderful contributions!
- What isn't working?
  - Some people aren't contributing at all, and I think that's because they are lost and don't know where to start.  I think we need to spend some time focusing on define the common vision for everyone.
  - User Stories got a little too implementation-focused without 

#### Planning

##### New User Stories

- User Story 1: *The Main Feature*
  - The Story:
    - "I want a means of accessing and returning data with processing steps applied that is easily parameterizable and extensible so that it is capable of returning an arbitrary number of datasets"
      - "Accessing and returning data" --> `intake`
      - "Processing steps" or *operators* --> functions that act on datasets (see below)
      - "datasets" --> in the sense of an xarray.Dataset (the cohesive unit that a bunch of data can be grouped into)
      - "collection" is a hand-full of datasets
      - "catalog" is the mapping from files/data assets *on disk* to datasets
      - "parameterizable" --> invoke funnel "elements" (i.e., the functions/processing steps) on a subset of the data that is returned from a "query" on a *catalog*?
      - "A query on a catalog returns another catalog (which is a subset of the original catalog)"
      - "A catalog can be converted to a collection"
      - "extensible" --> funnel doesn't *own* the operators (processing steps) but provides the framework for adding custom-built operators; want functions that don't just work with funnel!
      - "capable of returning an arbitrary number of datasets" --> returns a collection
    - "Thinking of processing steps that impede the interactive aspects of this" - *caching*
      - Want to track provenance
      - If the user invokes the same workflow twice, the system can retrieve the appropriate cached data instead of recomputing
  - Example Code
    ```python
    cat = intake.open_catalog(catfile)
    subcat = cat.search(query)
    assert type(subcat) is type(cat)
    
    col = subcat.to_collection()
    assert isinstance(col, Collection)
    
    col2 = col.apply(f, *params, **kwargs) # assume f has the "correct" signature
    
    # EVERYTHING BELOW IS UP FOR DISCUSSION!
    cat.append(col2.to_catalog(newkey))
    assert cat[newkey].to_collection() == col2
    ```
    
    - Do caching at the function/operator level
  
  - Required Tasks