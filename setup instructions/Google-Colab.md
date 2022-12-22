# What is colab? Why colab?

Google colab is a free (unless you pay for faster access) online tool that allows you to run Python notebooks (very similar to Jupyter) in the browser, which use GPUs hosted by Google. 
  
You don't need to install anything to use it. You can connect it to your Google drive to allow it to read and write files.

We strongly encourage you to have a working local setup using Anaconda/miniconda/miniforge as this will give you more flexibility as well as useful practice working with these tools on your own machine. However, colab can be a very useful resource if you don't have a GPU on your machine, if you have installation/conflict woes on your machine, or if you just want to run one of the many good existing notebooks shared online. 

## To use Colab to work on lab activities:

### To open a notebook in Colab:
 * Make sure you've first downloaded a copy of your desired notebook (e.g., by cloning/pulling from a git repository; see git instructions on main moodle page).
  
 * Then visit https://colab.research.google.com/ and select "upload" (you can only use the "git" option for the public github.com repositories, not for UAL git.arts.ac.uk repositories)

* Follow the instructions in the notebook. Occasionally you will have to do things a bit differently, and there will often (not always) be instructions in the notebook telling you what to do.
  
### To work with files in Colab
* If you need to work with files (e.g., datasets) outside the notebook, you will need to upload them to server thats running the code as well (or connect your google drive).

*  You will need to use the "folder" icon on the far left to add a new file. 
  
* Once you've clicked this icon, click the icon that looks like a rectangle with a little up-arrow in it; this will allow you to upload files from your machine to colab. Keep in mind that you may need to edit the path for these files in Python so it reflects where they land in your colab file structure (e.g., you may need to change something like "data/file1.csv" to just "file1.csv" if it lives in your top-level colab directory rather than in a subfolder named data.)
  
* You will need to re-upload your data any time you start a new colab session (e.g., because you close your browser or your session timesout.)
              
Alternatively, you can connect your google drive to colab so that it reads from and writes to your files there.
