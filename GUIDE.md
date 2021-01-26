# Xdev Team Guide

In this document, I will try to detail the processes that we, as a team,
should always follow.  I encourage others to add guidance and suggestions
for our process to this document as described below.

## 1. Communication Processes

Other than in-person communications, we use 3 platforms for our _internal
team_ communications.  These communication platforms are GitHub, Zulip, and
email.  Preference should be given to GitHub, then Zulip, and
lastly email.  More details on all of our Communication options can
be found in the [COMMPLAN](COMMPLAN.md).

Please keep in mind that _other_ developer communities might use other
platforms for communication.  It is important that you follow and use those
platforms when doing work _as a member_ of that community.  For example,
both [Dask](https://gitter.im/dask/dev) and [Xarray](https://gitter.im/pydata/xarray)
use Gitter for developer communications, in addition to GitHub.  This can
get unwieldy, but I recommend _focusing_ on one project at a time and
limiting your communication (and notifications,
[see below](#1-2-control-your-notifications)) to those that are most relevant
to your project.

### 1.1 Use GitHub for all communication, when possible.

The idea here is that there should be one best method for communication
with the team.  This method should be _open_ for all to read, so that
others can not only see our final work products, but so that others can
know how we got to those products, too.  This includes the following:

- Indicate what you are working on (or going to work on in the future)
  by creating GitHub Issues that are cross-referenced in Pull Requests.
- When discussing work being done or details of technical work,
  communicate with other team members through comments on their
  GitHub Issues.
- When you need to get someone's attention on GitHub, you should
  @-mention them explicitly.  (This also implies that everyone should
  set their [GitHub notification preferences](https://help.github.com/en/github/receiving-notifications-about-activity-on-github/choosing-the-delivery-method-for-your-notifications)
  to notify you in a way that will not be lost or missed.)

### 1.2 Control your GitHub notifications.

For GitHub to be effective for communication, you need to make sure
_both_ that you are receiving  notifications from GitHub _and_ that
you do not receive so many notifications that you miss the important
ones.  Hence, we _strongly_ recommend that you limit your GitHub
notifications to those that _are important only_.  To do this, you
must understand the 2 ways you can get notifications in GitHub:

- **_Watching_:** GitHub allows you to "watch" a _repository_.  GitHub
  notifies you of any new Issues or Pull Requests and any comments made
  on those Issues and Pull Requests.  ...So, watching an actively
  developed repository can lead to a _lot_ of notifications.

- **_Subscribing_:** Individual Issues and Pull Requests can be
  "subscribed" to.  And, even if you aren't watching the repository,
  once you subscribe to an Issue or Pull Request, you will get
  notifications every time a comment is made on them.  If you make
  a comment to any Issue or Pull Request (whether you own the repo
  or not, or whether you are watching the repo or not), you will
  automatically be subscribed to that Issue or PR.

Go to your [GitHub notification preferences](https://help.github.com/en/github/receiving-notifications-about-activity-on-github/choosing-the-delivery-method-for-your-notifications)
page to change _how_ GitHub notifies you if any of the above events
happen.  Choose methods for notification that you will not miss. For
example, if you get a ton of email on a daily basis already, having
GitHub send you emails may not be a good idea.

To prevent from being swamped with notifications, we recommend that
you limit your _Watched_ repositories to those that you are _actively_
_working on only_.  Once you finish work on one collection of repositories
and move to another project (with a different collection of repositories),
you can changed the repositories that you are watching.

### 1.3 Use Zulip for all other electronic communication.

The idea here is that our communication with each other should be recorded
somewhere.  Zulip allows us to record our _quick_ chat-like communications,
too.  Zulip is good for communication that is short and needs a rapid
turn-around.  For longer discussions and less urgent communication, use
GitHub.  Try to avoid too many private messages, preferring to communicate
in the open, but private messages (and email) are good for some things.

### 1.4 Use Email sparingly.

Email is useful for some forms of communication.  For example, email is
the only form of communication with someone who is not on GitHub (or is
not a developer, and therefore does not and cannot be expected to follow
GitHub) or does not have an account on our Zulip server.  For some forms
of communication with the team, such as notifications of being out of the
office or similar, email is fine for this (and it is easy since it simply
involves CCing the xdev@ucar.edu mail alias).

### 1.5 Be nice!!!

This is a no-brainer.  We are all busy, and we all have stresses in our
life that come from outside of our work lives, _in addition_ to the
stresses that come from work itself.  Always be cognizant of this fact,
and be kind and compassionate to each other and to others that we work
with.  Kindness makes everyone's job easier.

## 2. Development Processes

As open source developers, all of our work should be done in an _open space_.
This means GitHub and associated Git repositories.  There are many ways of
working with Git and with GitHub, and I will try to describe the ways that
we encourage as part of Xdev.

### 2.1 Use Forks+Branches instead of just Branches.

Whenever development happens, we strongly encourage you to do everything
in a _fork_, instead of directly pushing changes into the main repository.
We still encourage the use of _descriptive branch names_ in your fork,
describing the feature/fix that is being implemented, so that GitHub
history graphs can be more descriptive than just "main was merged into
main".  Even if you have rights to directly push into a repository,
we recommend doing everything through forks and pull requests.

Also, keep in might that the Git best practice of "commit early and
commit often" also, in a way, applies to forks+branches.  Try to keep each
fork+branch limited to changes that implement _only one feature_; Do not
implement multiple features in one fork+branch.  This can seem like an
inconvenient rule, but it helps others when they look at the history
later.

### 2.2 Follow Git best practices.

Whenever possible, we also recommend using standard Git best practices,
such as:

- _Do_ write descriptive commit messages,
- _Do_ commit early and commit often,
- _Don't_ change the published history of a repository.

There are other git best practices that many other teams suggest (and
sometimes demand), but, for now, we will not demand them.  These include
the ["squash and merge"](https://blog.pairworking.com/why-you-should-care-about-squash-and-merge-in-git-675856bf66b0)
rule and the ["no merge commits"](https://shinglyu.com/web/2018/03/25/merge-pull-requests-without-merge-commits.html)
rule.  If there is demand from the team that we _do_ implement these
rules, then we can discuss them and how best to implement them.

We also recommend the use of [Git pre-commit hooks](https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/)
for formatting code whenever you make new changes.

### 2.3 Clearly define (and use) project Conda environments.

Whenever working on a project, whether it be software development or
testing or helping scientists translate code into Python or developing
educational material and documentation, it is important to do your work
within a virtual environment that safely provides all of the software
dependencies you need for your work.  We recommend using Miniconda to
create and manage these environments.

It can be useful to _share_ these environments with other collaborators
at times.  If all you need is an environment for testing a specific
package, we usually keep a Conda YAML environment file in the CI
directory for the package of interest ([see below](#2-4-use-ci-for-as-much-as-possible)).
However, if you are doing a project that requires multiple packages that
are not dependencies of each other, then I advise learning how to easily
take a "snapshot" of your environment via `conda`:

```bash
conda env export > environment.yml
```

and then to create this environment from the YAML file:

```bash
conda env create -f environment.yml
```

Normally, it is not considered good practice to include YAML environment files
in a project repository (unless used for testing on CI,
[see below](#use-ci-for-as-much-as-possible.)), so we recommend sharing these
environment files with collaborators upon request.

### 2.4 Use CI for as much as possible.

Many of our projects use CircleCI for continuous integration (e.g., PR
testing) and continuous deployment (e.g., the Xdev blog website).  I
highly recommend doing the same in _all_ of our project repos.  If CI
has not been enabled in an Xdev repository that you are working within,
then take the time to enable it.  I recommend using CI for _all_ of these
tasks, when appropriate:

- **Testing:** When we write code (almost always in Python), we recommend
  using PyTest (`conda install pytest`) for testing.  Typically, there are two
  recommended organizational patterns used for tests:
  - place a `tests` directory _parallel_ to the package directory (e.g., the
    `tests` directory and the `package` directory in the root of your repository),
    with the contents of the `tests` directory mirroring the directory structure
    within the `package` directory, or
  - place a `tests` directory inside each `package` directory and subdirectory
    (i.e., sub-package).
  We do not prescribe one approach over another, only that it remain consistent.

- **Linting:** We recommend enforcing code formatting standards.  For these
  purposes, we recommend the combined use of `flake8` and `black`.  The `black`
  tool is an _opinionated_ Python code formatter.  Namely, it will change your
  source code to match a set of formatting rules, and you have some control over
  the rules you wish to enforce.  The `flake8` tool checks to make sure your
  Python source code complies with the PEP8 standard.  Typically, you run
  `black` and then `flake8` to make sure your reformatted code is PEP8
  compliant.

  There are many other tools to help lint your source code, such as `isort`
  (sorting your import statements) and `blacken-docs` (formats Python code
  snippets that show up in your documentation) and others.  I believe that these
  tools are optional, and I would consider `flake8` and `black` to be more of a
  requirement (or much stronger recommendation).

  For CI, you only want to check that the code that is being submitted via a
  PR is formatted correctly.  It is difficult (but not impossible) to allow your
  CI service to actually _format_ the submitted code for you, so for simplicity,
  we usually just check to make sure that the code is formatted correctly and
  fail the CI check if it is not.  Hence, we typically only run `flake8` in
  our CI tests.

  However, it is _strongly_ advised that you run both `black` and then `flake8`
  on your code whenever you make git commits.  Fortunately, there is a way to
  automate this through the use of [Git pre-commit hooks](https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/).
  This feature will run these tools _every time you commit_, instead of only
  running them via CI.

- **Documentation Building:** As always, whenever you write code you should
  write documentation for it.  We recommend the use of [Sphinx](http://www.sphinx-doc.org/en/master/usage/quickstart.html)
  for documentation.  Sphinx can also automatically generate API documentation
  based on Python docstrings within your source code.  So, every time you add
  new code to your repository, you should update the API docs.  Using CI, you can
  test that your documentation actually builds (without failure).

  [Readthedocs](https://readthedocs.org/) is a CI service that can be set up
  to build your documentation and _host_ it for you on their servers.  It is
  quite easy to set up and use, and so we recommend it for the actual
  publication of your documentation.

  _A note about advertisements on Readthedocs_: Readthedocs.org provides their
  documentation hosting service to _open source projects_ for free, but it pays
  for the running of the service through commercial/enterprise-level services
  (that commercial customers pay for) and advertisements that are displayed on
  the freely hosted documentation websites.  Some people think that it is
  unethical to have advertisements for free and open source scientific
  software websites (and particularly for NCAR, tax-funded work).  If this is a
  concern you need to avoid, then I recommend hosting your documentation via
  [GitHub Pages](https://pages.github.com/) which can let you host content,
  such as documentation, directly from your GitHub repository.  To make this
  work, however, we recommend that you create a CI job (e.g., via CircleCI)
  to build _and commit_ your updated documentation for display on your GitHub
  pages site ([see here](https://circleci.com/blog/deploying-documentation-to-github-pages-with-continuous-integration/)).

CI services are the critical lynchpin of open source community software development,
so they should be used whenever possible.

I recommend setting your CI up to run _tests_ (including _linting_ tests)
whenever a Pull Request is _created_ (and when edits/changes are made to an
existing PR).  You can either use GitHub to block commits directly into the
main branch (i.e., force all commits to go through PRs), or you can also
run CI on changes made directly to your main branch.  I recommend setting
up your CI to _build (and publish) documentation_ only when a PR is _merged_
(i.e., only after it has been tested and approved).

## 3. General Work Practices

In general, most of what we do can be categorized as _Communication_ and/or
_Development_.  However, there are a lot of aspects of what we do that fall
outside of, or peripheral to, these practices.  As a team, this is the area
of guidance that I believe we need to develop more.

### 3.1 Periodically check your mirrors.

Like driving a car, you need to periodically check your "mirrors" to see what
is going on around you.  For us, that means checking your GitHub notifications
periodically, checking your email, checking Zulip, _etc._.  However, you shouldn't
go down the rabit hole whenever a new notification comes in.  Instead, you
should assess whether the notification _does_ or _does not_ require a response.
If the notification _does_ require a response, you must determine if that
response can be delayed or must be immediate.  In general, I recommend short
responses _immediately_ and longer responses (e.g., significant code modification)
later, _after you are done with your current task_.  In fact, if a notification
requires significant work, I would recommend an immediate _short_ response
indicating that a _longer_ response will be coming.  I recommend this
approach because it allows you to stay focused as much as possible.

### 3.2 Be transparent.

With everything that we do, we should strive to do it _in the open_.  That means
not only holding communications in public forums (e.g., GitHub Issues and PRs),
but also working in _public_ repositories.  There is no real reason why anything
that _we_ do should be private.

The [Xdev Project Board](https://github.com/NCAR/xdev/projects/1) was created
to make all of our work transparent.  To this end, it does a good job of putting
everything we are doing (and hope to do in the future) in one place.  However,
the Project Board (currently) does a bad job of helping to identify what needs
to be done next (i.e., prioritization), and it can actually be distracting from
the work that you are actually working on now.

The Xdev Project Board was not designed to be a replacement for GitHub
notifications.  GitHub notifications should be seen as the _primary_ mechanism
for keeping you up-to-date on the development work we are doing.

### 3.3 Assign yourself to GitHub Issues

You can assign yourself to any GitHub Issue that you think would be nice to work
on in the future.  Then, you can search the Xdev Project Board with the
`assignee:githubid` tag to _focus in_ on your own planned work.  I recommend this
approach because it also communicates to the rest of the team what you plan to
work on.  _Note: You can assign yourself to an Issue even if someone else has
assigned themself.  There can be more than one assignee!_

### 3.4 Measure twice, cut once.

The best way of helping yourself stay focused and avoiding distraction
(currently) is with good planning.  With only the Xdev Project Board, or just
responding to GitHub notifications, it is very easy to get distracted from
you current task at hand.  It is also extremely difficult to know what to
do next.

To aid with this, you should plan your work over weeks _ahead of time_.  This
planning should be done with the relevant members of the Xdev Team, so that
the plan is well thought out and reviewed.  Currently, we do not have an
explicit mechanism to do this, so it must be done with _ad hoc_ interactions.
However, I am open to better ways of planning and possibly encoding our plans
in our organizational tools (such as the Xdev Project Board).
