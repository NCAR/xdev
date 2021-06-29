import pathlib 

root = pathlib.Path("./posts")

paths = ['object-oriented-programming', 'templating-isnt-just-for-web-developers', 'writing-multiple-netcdf-files-in-parallel-with-xarray-and-dask', 'pandas-tutorial', 'python-tutorial-seminar-series-spring-2021', 'cartopy-tutorial', 'python-tutorial-faq', 'numpy-tutorial', 'your-first-package-python-tutorial-faq', 'numpy-faq', 'intake-esm-2020316', 'time', 'python-tutorial-faq-part-3', 'tutorial-seminar-series', 'python-tutorial-faq-part-2', 'we-are-xdev', 'matplotlib-faq', 'jupyter-notebooks-faq', 'matplotlib-tutorial', 'git-and-github-tutorial', 'xarray-tutorial']


for path in paths:
    content = f"""<!DOCTYPE html>
<meta charset="utf-8">
<title>Redirecting to https://ncar.github.io/esds/</title>
<meta http-equiv="refresh" content="0; URL=https://ncar.github.io/esds/{path}/">
<link rel="canonical" href="https://ncar.github.io/esds/{path}/">
    """

    p = root / path 
    p.mkdir(parents=True, exist_ok=True)
    file = p / "index.html"
    file.open('w').write(content)

