<!--
.. title: Templating isn't just for Web Developers!
.. slug: templating-isnt-just-for-web-developers
.. date: 2020-05-08 10:42:05 UTC-06:00
.. tags: templating,jinja2
.. category: 
.. link: 
.. description: A short tutorial on templating with Jinja2 for those with no frontend development experience
.. type: text
.. author: Kevin Paul
-->

Recently, I found myself rambling on in an unprepared attempt to
explain templating to a colleague of mine who had no prior experience
with frontend design.  It didn't take me long to realize that my
explanation was convoluted and confusing.  Attribute that to being
unprepared, or sleep deprived (i.e., child *still* not sleeping through
the night!), or just a bad teacher.  Regardless, I decided to point
them to a tutorial online that *certainly must exist*, but after a
brief Google search (which you should read as, "I didn't find anything
in the first page of search results!"), all I could find were tutorials
for frontend developers.  And if you aren't an HTML expert, or already
have experience with Flask or Django, teaching templating in those
contexts can actually be more confusing than illuminating.

So, as I always do when I find myself struggling with something that
I think should be easy, I ask my wife for advise.  I tried to explain
the concept of templating to my wife, who is not a software developer
*at all*.  My wife looked at me with this look that said, "What's not
to get?"  Then she said, "You mean filling out a form letter
automatically..."

Yes.  Exactly.  And while my palm was hitting my forehead, it occurred
to me that I should write a templating tutorial for those who really
don't have any prior experience with frontend development and who
might even be scared when they read "less-than-h-t-m-l-greater-than".
Today, we'll learn Jinja2 templating through an example Use Case where
we want to generate a form letter for a number of different addressees.

## Jinja2

I'll be using Jinja2 for this tutorial.  It's extremely popular and
widespread in the Python developer community, and it has very good
documentation... except for the fact that all of their documentation
is almost entirely geared toward frontend designers.

You can install Jinja2 with `pip` or `conda` as follows:

```bash
$ pip install Jinja2
```

or

```bash
$ conda install jinja2
```

That's it.  You should now be set up with an environment that
has (at least) python3 and jinja2 installed in it.

## The Letter

Here is the scenario that we will envision as motivation for
learning templating:

Imagine that you are the attorney for an oil tycoon with $4.5M
held in the Bank of [Freedonia](https://en.wikipedia.org/wiki/Duck_Soup_(1933_film)).
With tensions mounting between Freedonia and neighboring Sylvania,
and war looming on the horizon, your client has authorized you to
move these assets to another bank outside of Freedonia.  Clearly,
your only course of action is to email as many people for whom
you can find addresses to ask them if they would be willing to
hold the assets in their account for the duration of the conflict.
Obviously, you will need to pay them for their kind services, and
the oil tycoon has agreed to authorize you to gift 20% of the assets
to whomever holds them, as payment for their kindness.  You have
obtained your list of addressees from a kind person working for
the humanitarian "WikiLeaks" Foundation, and now you must craft
an email to send to all of these addressees.

So, there is your entirely believable, totally serious, and extremely
common scenario motivating your need to learn templating.

