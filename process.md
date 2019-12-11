# Xdev Processes

In this document, I will try to detail the processes that we, as a team,
should always follow.  I encourage others to add "rules" and suggestions
for process to this document as described below.

## Communication Process

Other than in-person communications, we use 3 platforms for our team
communications.  Preference should be given to GitHub, then Zulip, and
lastly email.

### Use GitHub for all communication, when possible.

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

### Control your GitHub notifications.

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

### Use Zulip for all other electronic communication.

The idea here is that our communication with each other should be recorded
somewhere.  Zulip allows us to record our _quick_ chat-like communications,
too.  Zulip is good for communication that is short and needs a rapid
turn-around.  For longer discussions and less urgent communication, use
GitHub.  Try to avoid too many private messages, preferring to communicate
in the open, but private messages (and email) are good for some things.

### Use Email sparingly.

Email is useful for some forms of communication.  For example, email is
the only form of communication with someone who is not on GitHub (or is
not a developer, and therefore does not and cannot be expected to follow
GitHub) or does not have an account on our Zulip server.  For some forms
of communication with the team, such as notifications of being out of the
office or similar, email is fine for this (and it is easy since it simply
involves CCing the xdev@ucar.edu mail alias).

### Be nice!!!

This is a no-brainer.  We are all busy, and we all have stresses in our
life that come from outside of our work lives, _in addition_ to the
stresses that come from work itself.  Always be cognizant of this fact,
and be kind and compassionate to each other and to others that we work
with.  Kindness makes everyone's job easier.

## Work Process

As open source developers, all of our work should be done in an _open space_.
This means GitHub and associated Git repositories.  There are many ways of
working with Git and with GitHub, and I will try to describe the ways that
we encourage as part of Xdev.

### Use Forks+Branches instead of just Branches.

Whenever development happens, we strongly encourage you to do everything
in a _fork_, instead of directly pushing changes into the main repository.
We still encourage the use of _descriptive branch names_ in your fork,
describing the feature/fix that is being implemented, so that GitHub
history graphs can be more descriptive than just "master was merged into
master".  Even if you have rights to directly push into a repository,
we recommend doing everything in forks and pull requests.

### Follow Git best practices.

Whenever possible, we also recommend using standard Git best practices,
such as descriptive commit messages, many small commits (rather than one
big commit), 
   