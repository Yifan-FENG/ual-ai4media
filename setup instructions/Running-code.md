Now we are going to run a Jupyter notebook. This where we will run most of our Python scripts.

First we need to get the code for this unit onto our local machines.

### GitHub App

All the code for this unit lives in something called a “repository”. The largest
commercial version of this is [GitHub](https://github.com)

We have our own version at (https://git.arts.ac.uk). The easiest way to get code, and weekly updates, is to use the Github App.

Get the App
- https://desktop.github.com/
- Download the app
- Install the app
- Click “Sign into enterprise server" (git.arts.ac.uk)
- Use UAL username and password
- Browser opens -> Authorise -> Same username and password

Clone the Repo
- Go to repo (https://git.arts.ac.uk/lmccallum/STEM-4-Creatives-22-23)
- Click Clone or download
- Open in App
- Choose an install location on your computer (by default this is a Github folder_

Get updates (in App)
- Click Fetch origin
- Click Pull origin

### Running Jupyter Notebook

#### From Terminal/Console
1. ``conda activate stem`` (or a different name if your environment isn't called __stem__
2. Type `jupyter notebook`
3. Use the file explorer that opens in the browser to locate the downloaded Github repo

What has happened here is we have launched the notebook program from the terminal, and we have then opened a web browser and navigated to localhost:8888.  

It's important to understand this split, the program is running in the terminal, and we have a view on it through the browser. This client – server set up means that if we close the browser, the notebook doesn’t close. It also means we can run notebooks on servers in the cloud, and then interact with them through the browsers on our local machines.  

### Troubleshooting Python

- Which install of Python are you using? `which python` (unix) `where python` (windows)
- Which version of Python are you using? `python —-version`
- Which install of pip are you using? `which pip` (unix) `where pip` (windows)
- Which version of package is installed using pip? `pip show [package name]`
- Which install of Anaconda are you using? `which conda` (unix) `where conda` (windows)
- Which version of package is installed using Anaconda? `conda list [package name]`
