# Xdev Communication Plan

In addition to the Best Practices described in the [GUIDE](GUIDE.md),
there are a number of different communication platforms and options
available.  In this document, we primarily detail which communication
channels we use, why we use them, and what we use them for.

## TL;DR: Summary

The table below attempts to summarize the content described in much
greater detail in the rest of this document.  The table describes *with
whom* each communication channel is ideally suited and *for what kind*
of communication it is best suited.

| Channel | With Whom? | What Kind? |
|---------|------------|------------|
| GitHub  | Developers | Bug Reports, Feature Requests, Code Reviews, Design Discussions |
| Zulip `Xdev` stream | The Xdev Team | Questions, General Comments, Soliciting Feedback, Jokes, *etc.* |
| Zulip public streams | NCAR Python Users | Announcements, Questions/Answers, Development Problems, Soliciting Feedback, *etc.* |
| Xdev Blog | General Public | Announcements, Technical Examples, Howtos, *etc.* |
| Twitter (`@NCARXdev`) | General Public | Announcements of Blog Posts |
| Email (`xdev@ucar.edu`) | General Public | Incoming questions from outside entities |
| Google Calendar | Anyone who can be added to a Calendar Event | Event coordination and timing |


## Communication Channels

### GitHub

#### Why should we use it?

GitHub is the perfect communication platform for communicating
directly with software developers about *specific software issues*.
Therefore, GitHub is also useful for other people to communicate
with *us* about specific issues in *our* software.  Hence, GitHub
is a two-way platform, for us to reach out to others and for others
to reach out to us.  For this reason, it is important to follow
the guidance in the [GUIDE](GUIDE.md) for how best to use GitHub.

#### What should we use it for?

Use GitHub to report bugs, provide reported bug fixes, request new
features, or discuss software design issues, including providing code
reviews, comments on other issues, etc.

#### What should we *not* use it for?

If a software package has a large enough user base, they may have
a different forum for asking general use questions, like "How do I
do...?"  For example, Dask has two Gitter channels, one for general
Dask users and one for Dask developers.  Xarray also has a Gitter
channel.  Both Dask and Xarray also have many questions answered
on stackoverflow.com.  In these cases, it is best to use the best
forum for your question or comment.  Sometimes it is not clear which
forum is best, but do your best to find the best forum.

### Zulip

#### Why should we use it?

Zulip is an excellent quick messaging forum, making it possible to
share both short and long communications that *persist* over time
(and are findable via search later).  Zulip uses markdown to display
messages in an easy-to-read form, with language-specific syntax
highlighting, which makes it perfect for instant messaging about
software issues, general software use questions, or other technical
discussions.

Zulip has multiple *streams* which are designed to topically target
certain messages.  You can create *topics* within each of these
streams, much like subject headings in email.

#### What should we use it for?

Use Zulip for NCAR-wide communication.  Note that Zulip is accessible
by *invitation only*, which means it really only includes NCAR staff
and close collaborators.

Use Zulip to post and answer public questions about our services
(e.g., the NCAR JupyterHub) or software (e.g., "How do I do X with Y?").
Some people on Zulip may feel uncomfortable asking questions on other
messaging/chat platforms that other software communities use, such as
Gitter or StackOverflow, and they may feel more comfortable asking
their questions on Zulip first.  Some of their questions may relate
more to the environment that we provide for them to *use* the software,
which is another reason why they may ask their questions on Zulip first.
In general, Zulip is the first line of question/answer for staff here
at NCAR on Python topics.

Public streams (i.e., those labeled with a `#` symbol) can be "joined"
by *anyone* on Zulip.  Hence, they should be used to ask, or answer,
questions, or make comments of public interest, related to the public
stream subject.  For example, the `dask` stream should be used for any
Dask-specific issues or questions. The `jupyter` stream should be used
for any Jupyter (Lab or Hub) issues or questions.  The `python-dev` and
`python-questions` public streams are *catch-all* streams for any
Python-related discussion that doesn't fall into the more specific
public streams (e.g., `jupyter`, `dask`).  NCAR-wide *announcements*
should be made to the `announce` public stream.  In general, the name
of the public stream defines the *subject* of its discussions.

Private streams (i.e., those labeled with a lock symbol) should be used
for *internal* communications between people who have been invited to
the private stream.  For example, the `Xdev` private stream is meant
for internal communication within the Xdev Team.  In general, the
name of the private stream defines the *group of people* included in
the discussions.

Zulip is also excellent for instant messaging *in general*, so if you
are going to be watching Zulip to help out other Python users here at
NCAR, then it makes sense to use it for direct communication amongst
Xdev Team members, too.

#### What should we *not* use it for?

Don't use Zulip for communication that is meant for the
*entire user community* (e.g., all of Pangeo), and not just NCAR staff.
In those cases, I recommend using the Pangeo communication channels, as
described in the [PANGEO Guide](PANGEO.md).

### The Xdev Blog

#### Why should we use it?

[Our blog](https://ncar.github.io/xdev) is an excellent way for us to
communicate complex ideas, or to make announcements, to the *broader*
community (i.e., beyond NCAR) in an easy-to-access form.  Blogs persist
and are designed to be referenceable at a later date, which makes them
excellent for sharing our individual (or Team) accomplishments in a
way that can be cited.  By hosting our *own* blog, which is connected
to Google Analytics, we can gather metrics and visit statistics on
our blog posts, which can provide us useful information about who is
making use of our posts.  Career-wise, blog posts are strongly
encouraged in the software engineering community!

#### What should we use it for?

Use our blog as a way of publicizing new software package, new software
versions, solutions to hard problems, or any general accomplishment.
Use our blog to make *general public announcements* about things like
tutorials or new services.  Use our blog to publicize Xdev Team work and
achievements.

#### What should we *not* use it for?

Don't use the blog for rants or making complaints about anything.  The
blog should only be used for *constructive* communication.

### Twitter ([@NCARXdev](https://twitter.com/NCARXDev))

#### Why we should use it?

Twitter is a commonly used platform by many people in the Tech Industry,
especially software engineers and scientists.  For example, a very large
fraction of the Pangeo community regularly tweet.  Hence, Twitter makes
an excellent platform for getting the attention of the general public
(or the fraction of the general public interested in NCAR's Python
work).

#### What should we use it for?

[The Xdev Twitter account](https://twitter.com/NCARXDev) should be for
making *announcements* to the general public, such as making an
announcement of a new blog post. In general, Twitter *could* be used
for any announcement, but because of the limitations of the platform
(i.e., limiting the length of the tweet) it is best to tie the tweet
to *another* communication platform, such as a blog post.

#### What should we *not* use it for?

[The Xdev Twitter account](https://twitter.com/NCARXDev) should *not* be
used for personal use.  Currently, only Kevin has the "keys" to the
Twitter account.  If you want to make a broad announcement, contact Kevin
via Zulip.

### Email

#### Why should we use it?

The Xdev email address (`xdev@ucar.edu`) should be used only sparingly by
any of us on the Xdev Team.  As a general rule, having the Xdev email address
is useful for communication from *outside* of NCAR (or just *outside* of
our Team) with the entire team.  It is also useful for creating Google
Calendar meetings, as it allows the entire team to be invited to a meeting
(and nobody is forgotten).

#### What should we use it for?

The Xdev email address should be used for sharing with outside entities or
individuals as a means of reaching out to the entire team.  For example,
we might want to share this email address with participants of our tutorials,
or with users of our websites.  It should be used as the main point of
contact with us for people who are *external to NCAR*.

It is also incredibly handy to use the Xdev email address for inviting
the entire team to Google Calendar events (see below), or for announcing
Google Calendar event cancelations, etc.

#### What should we *not* use it for?

Avoid using the Xdev email address for internal communication.  Use Zulip
or GitHub for collaboration within the team.

### Google Calendar

#### Why should we use it?

Google Calendar is really the best way of coordinating times for meetings and
any timed activities that we engage in as a team.  Together with the Xdev
email address, it is the best way of reaching out to the entire team to see
if they are available to meet at a specific time, on a specific day.

#### What should we use it for?

Use Google Calendar for scheduling all meetings.  Note that it can be difficult
to find time for all people on the team to meet.  To accommodate this potential
need, we have 2 standing "slots" on the UCAR Google Calendar called "Team Time".
These slots are for *ad hoc* meetings with the entire team.  Having these
regular meetings on the calendar, even if they are not used every week, lets
everyone on the team know to try their best to keep those times free.  Then we
have the best chance of everyone being available for any *ad hoc* meetings we
might need to have.

#### What should we *not* use it for?

As usual, don't use Google Calendar for personal things.  Otherwise, use
Google Calendar for what it was intended: to schedule meetings and events.  It
is hard to use Google Calendar for something it was not intended.

### Other Channels

There are many other communication channels for other (albeit similar)
communities, even ones that we might consider ourselves members.  The
most notable case is Pangeo Community, which has its own communication
channels, as described in the [Pangeo Guide](PANGEO.md).  If directly
interacting with an external community, such as Pangeo, use the communication
channels *used by that community.*  Note that this could me, regretfully,
re-posting or double-posting announcements or questions in multiple
channels because of different community expectations.
