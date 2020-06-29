# Experimental Development Team

This repository is for the internal developments of the NCAR Experimental Development Team (Xdev).
This repository contains information about the team, links to team products (such as the `xdev-bot`
and the `xdev-status-dashboard`) and the team blog hosted on GitHub Pages.

## Team Scope & Strategy

The scope of work performed by the Xdev Team is described in the [PURPOSE](PURPOSE.md) document.
That document also links to documents in the [campaigns](campaigns) directory.  If you want to
know about the mission, vision and strategic plans for the Xdev Team, start with the
[Xdev PURPOSE](PURPOSE.md).

## Project Status Dashboard

Dashboard: https://ncar.github.io/xdev/pages/status/

The main configuration of the dashboard is done via the [dashboard.yml](status-dashboard/dashboard.yml) file, which can contain several sections with a list of packages, and a list of services for each section.

**Note:**

To update the dashboard with a new package or a new service, one needs to run the `make_status` script (after updating `status-dashboard/dashboard.yml`) from the root directory:

```bash
python ./status-dashboard/make_status.py
```

## Xdev Blog

The Xdev blog site is deployed using GitHub Pages from this repository. It uses [Nikola](https://getnikola.com)
to generate static web pages, the content of which are contained in files in the `site` directory of this
repository. To write a new blog post, you should follow this procedure:

1. Make sure you have Nikola installed on your machine (`pip install nikola[extras]`) in a
   separate conda environment (e.g., I call my conda environment `xdev` to match the repo.).
2. Fork this repository into your own space and check out your fork.
3. Use Nikola (from within your fork) to create a new blog post file in the format of your
   choosing (`FORMAT` can be `rest`, `markdown`, or `ipynb`):

   ```bash
   nikola new_post -f FORMAT -a "Your Name"
   ```

   and follow the prompt from Nikola to give your blog post a title (and hit enter).

4. Note important metadata fields within the blog post file:

   - `title`: A string that can have spaces (will be the text at the top of the blog
     post HTML page).
   - `slug`: This is a string that _cannot_ have spaces. It will become the name of the
     blog post file (with extension matching the FORMAT chosen in Step 3). Nikola will
     automatically generate this for you to match the `title` string, with spaces replaced
     by hyphens and other punctuation removed.
   - `date`: This is the displayed date and time of the blog post. On the main page, the
     posts will be ordered in reverse chronological order of this date-time.
   - `tags`: Comma-separated strings (can have spaces) that topically categorize the post
   - `description`: A very short description of the blog post. This is displayed in the
     card when the link to the post is generated from a tweet (i.e., a Twitter announcement).
   - `author`: This should be your name (i.e., the author of the blog post).

   Other metadata fields are less critical.

5. Edit the file that was created in `site/posts/your-title.FMT` where `FMT` is either `rst`,
   `md`, or `ipynb`. (Obviously, if you are creating a blog post from a Jupyter Notebook
   file, you will probably want to exit your `ipynb` file with Jupyter Notebook or Lab.)
6. To view how your blog post will look when published, you can run a local web server with
   the following commands:

   ```bash
   nikola build && nikola serve
   ```

7. When your blog post is finished, make sure your changes are committed to your fork and
   then create a Pull Request.
8. Tests that build the new web pages from your blog post will be run on CircleCI, and if
   these tests pass, then you need 2 reviews of your PR before it can be merged (so we read
   each others blog posts).
9. Once the PR is merged, the new site will be generated on GitHub Pages automatically by a
   CircleCI job. And, in a little while, the new website will be visible to the public.

## Xdev Bot & Bot Testing Respositories

Bot: https://github.com/NCAR/xdev-bot

Testing: https://github.com/NCAR/xdev-bot-testing
