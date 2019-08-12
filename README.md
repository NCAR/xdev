# Experimental Development Team

This repository is for the internal developments of the NCAR IOWA Experimental Development Team (xdev).
This repository contains information about the team, links to team products (such as the `xdev-bot` and
the `xdev-status-dashboard`) and the team blog.

## Project Status Dashboard

Dashboard: https://ncar.github.io/xdev/pages/status/

The main configuration of the dashboard is done via the [dashboard.yml](status-dashboard/dashboard.yml) file, which can contain several sections with a list of packages, and a list of services for each section.

To update the dashboard with a new package or a new service, one needs to run the `make_status` script from the root directory:

```bash
python ./site/status-dashboard/make_status.py
```

## XDev Blog

The XDev blog site is deployed using GitHub Pages from this repository.  It uses (Nikola)[https://getnikola.com]
to generate static web pages, the content of which are contained in files in the `site` directory of this
repository.  To write a new blog post, you should follow this procedure:

1. Make sure you have Nikola installed on your machine (`pip install nikola[extras]`)
2. Fork this repository into your own space and check out your fork
3. Use Nikola (from within your fork) to create a new blog post file in the format of your choosing 
   (`FORMAT` can be `rest`, `markdown`, or `ipynb`):
   
   ```bash
   nikola new_post -f FORMAT -a "Your Name"
   ```
   and follow the prompt from Nikola to give your blog post a title (and hit enter).
4. Edit the file that was created in `site/posts/your-title.FMT` where `FMT` is either `rst`, `md`, or `ipynb`.  (Obviously, if you are creating a blog post from a Jupyter Notebook file, you will probably want to exit your `ipynb` file with Jupyter Notebook.)
5. When your blog post is finished, make sure your changes are committed to your fork and then create a Pull Request.
6. Tests that build the new web pages from your blog post will be run on CircleCI, and if these tests pass, then you need 2 reviews of your PR before it can be merged (so we read each others blog posts).
7. Once the PR is merged, the new site will be generated on GitHub Pages automatically by a CircleCI job.  And, in a little while, the new website will be visible to the public.

## XDev Bot & Bot Testing Respositories

Bot: https://github.com/NCAR/xdev-bot

Testing: https://github.com/NCAR/xdev-bot-testing
