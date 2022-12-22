# Setting up a conda environment 

## Create the environment
We are going to create a new conda environment (a specific collection of packages) for this unit (recommended if you are doing other Python/ML work on the same machine, or if you're on a shared machine)

You can use the terminal/console and type 

``conda create --name aim python=3.9`` 

This will create a Python 3.9 environment named "stem" (you can choose some other memorable name if you'd like)

Once you've created an environment, install jupyter and pandas in this environment using the terminal console:

``conda activate aim``

``conda install -c conda-forge -y pandas jupyter``

You will know you have been successful because the environment name will appear at the front of the terminal line in brackets 

For example

``(aim) tbroad STEM-4-Creatives-22-23``

If you do create an environment for this unit, just make sure you're always using that environment when you work on lab/project activities!


