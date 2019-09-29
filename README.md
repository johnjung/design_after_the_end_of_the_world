# Design After the End of the World

## To Do

Coming soon...

## Updating this code

The site uses [Frozen-Flask](https://pythonhosted.org/Frozen-Flask/) to
generate a static site from a Flask app. The static site is currently hosted on
GitHub using [GitHub Pages](https://pages.github.com/).

To hack on a local copy of the site, clone it from GitHub:

```console
$ mkdir dateotw
$ cd dateotw
$ python3 -m venv env
$ source env/bin/activate
$ git clone https://github.com/johnjung/design_after_the_end_of_the_world.git
$ cd design_after_the_end_of_the_world
$ pip install -r requirements.txt
```

Run it locally using the Flask development server:

```console
$ python dateotw.py
```

Make changes using your favorite editor. After committing your changes to
master, update the static site on GitHub Pages:

```console
$ python freeze.py
$ git subtree push --prefix build origin gh-pages
```

[Visit the site here](https://johnjung.github.io/design_after_the_end_of_the_world/). 
