# Design After the End of the World

This is work-in-progress for a speculative design project. [Visit a site wireframe here](https://johnjung.github.io/design_after_the_end_of_the_world/). 

## Project Plan

### Step 1: Choose a direction

While brainstorming we sketched out two general ideas:

#### Option 1: "Medieval Times"

This is set in a dystopian future about 100 years from now. Society has entered a neo-medieval period. Peoples interests include homesteading, farming, and defending themselves against marauders.

The system of higher education has collapsed, but the desire to continue doing science remains. For a fee, apprentice scientists learn their craft from a master. Much of this science is of dubious value: for example, a fermentation-powered replication machine promises to create the comforts of the 21st century, but requires users to mash materials in a large vat with their feet, like wine-making.

Individual videos explore these dubious scientific efforts, and the website itself exists to promote an organization that offers an alternative to current scientific education. 

#### Option 2: "X-Files"

This is set in a dystopian version of the United States, about ten years from now. Economic and political pressures on newspapers have continued to erode people's trust in the news. Consipracy theories abound and spread quickly on the internet.

This website contains short videos that offer a form of investigative reporting, although paranoid and without the traditional ethics of journalism. Stories involve spying on neighbors, digging through trash, and piecing together complicated stories about a mysterious company and the environmental damage it does.

The website itself is a type of news outlet, and individual videos explore aspects of this evolving conspiracy theory.

#### Option 3: continue brainstorming

If neither option feels right, its ok to brainstorm some more.

### Step 2: Branding, web design and copywriting

1. Choose a name for the fictional organization and website. [Check to be sure an appropriate domain name is available.](https://www.domain.com)
2. Design a wordmark for the organization.
3. Design site templates- feel free to modify elements of the wireframe.
4. Write copy for the site itself: e.g., pages about the organization.

### Step 3: Web development

Update templates. Point domain name to GitHub Pages.

### Step 4: Produce content

Brainstorm ideas and produce individual videos. 

## Technical Notes

The site wireframe uses [Frozen-Flask](https://pythonhosted.org/Frozen-Flask/) to
generate a static site from a Flask app. The static site is currently hosted on
GitHub using [GitHub Pages](https://pages.github.com/).

To hack on a local copy of the site, clone it from GitHub and install dependencies using pip:

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
