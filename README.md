# Experimental Development Team

This repository is for the internal developments of the NCAR IOWA Experimental Development Team (xdev).
This repository contains information about the team, links to team products (such as the `xdev-bot` and
the `xdev-status-dashboard`) and the team blog.

## Project Status Dashboard

Dashboard: https://ncar.github.io/xdev-status-dashboard/

## XDev Blog

The XDev blog site is deployed using GitHub Pages from this repository.  It uses (Nikola)[https://getnikola.com]
to generate static web pages, the content of which are contained in files in the `site` directory of this
repository.  To write a new blog post, you should follow this procedure:

0. Make sure you have Nikola installed on your machine (`pip install nikola[extras]`)
1. Fork this repository into your own space and check out your fork
2. Use Nikola (from within your fork) to create a new blog post file in the format of your choosing 
   (`FORMAT` can be `rest`, `markdown`, or `ipynb`):
   
   ```bash
   nikola new_post -f FORMAT -a "Your Name"
   ```
   and follow the prompt from Nikola to give your blog post a title (and hit enter).
4. Edit the file that was created in `site/posts/your-title.FMT` where `FMT` is either `rst`, `md`, or `ipynb`.  (Obviously, if you are creating a blog post from a Jupyter Notebook file, you will probably want to exit your `ipynb` file with Jupyter Notebook.)
5. When your blog post is finished, make sure your changes are committed to your fork and then create a Pull Request.
6. Tests that build the new web pages from your blog post will be run on CircleCI, and if these tests pass, then you need 2 reviews of your PR before it can be merged (so we read each others blog posts).

## XDev Bot & Bot Testing Respositories

Bot: https://github.com/NCAR/xdev-bot

Testing: https://github.com/NCAR/xdev-bot-testing
