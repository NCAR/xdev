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
explanation was convoluted and confusing, not that I stopped talking,
mind you.  Attribute that to being unprepared, or sleep deprived (i.e.,
child *still* not sleeping through the night!), or just a bad teacher.
Regardless, I decided to point them to a tutorial online that
*certainly must exist*, but after a brief Google search (which you
should read as, "I didn't find anything in the first page of search
results!"), all I could find were tutorials for frontend developers.
And if you aren't an HTML expert, or already have experience with
Flask or Django, teaching templating in those contexts can actually
be more confusing than illuminating.

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
Today, we'll learn Jinja2 templating through an example use case where
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

## The Use Case

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
to whomever holds them, as payment for their kindness.  You just
need some personal information from them and some bank routine
information.  That's all.  You have obtained your list of addressees
from a kind person working for the humanitarian WikiLeaks "Foundation,"
and now you must craft an email to send to all of these addressees.

So, there is your entirely believable, totally serious, and extremely
common scenario motivating your need to learn templating.

## The Letter

Fortunately, you already have a "template" for a formal *written* business
letter sitting around on your hard drive.  It looks like this:

```text
[Your Address]

[Date]

[Recipient Name]
[Recipient Title]
[Recipient Company]
[Recipient Address]

[Greeting] [Recipient Name]:

[Letter Body]

[Closing],

[Your Name]
[Your Title]
```

Each element in this "template" that is enclosed in `[]`-brackets is
just a placeholder for some other text.  Some of that text is short,
like names, titles, or greeting or closing text.  Some of that text
will me multi-line input, such as the letter's body and the addresses.
In Python, all you would want to do is something like string
substitution, for example replacing `[Your Name]` with `Jane Smith`.

This is exactly what "templating" is all about.  It is, essentially,
just string substitution...but with a touch more sophistication.

## The Jinja2 Template

So, to start out, we are going to convert this text template into a
Jinja2 template.  To do so, the easiest first step would be to just
replace every `[]`-bracketted item with a Jinja2 *expressions*,
which are repressented with `{{}}`-brackets:

```text
{{ your_address }}

{{ date }}

{{ recipient_name }}
{{ recipient_title }}
{{ recipient_company }}
{{ recipient_address }}

{{ greeting }}  {{ recipient_name }}:

{{ letter_body }}

{{ closing }},

{{ your_name }}
{{ your_title }}
```

Also, notice that I have converted the text labels inside the
`[]`-brackets into valid Python variable names.  Let's assume
that this new *template file* is called `letter.j2` (where
the `.j2` means it is a Jinja2 template).

We can now "write" this letter using Python variables from a
Python script.  First, let's start writing a Python script that
can "render" this Jinja2 template:

```python
#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader('./')
)

template = env.get_template('letter.j2')

data = {}

print(template.render(**data))
```

