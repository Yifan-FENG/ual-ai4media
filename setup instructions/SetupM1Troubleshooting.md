# M1 Users: Troubleshooting if you encounter errors with Tensorflow

If you get an error when doing your imports (e.g., in Week 4.1 notebooks), there may be incompatibilities between the tensorflow package and your current environment.

You can try the following options:

* Option 1: Create a new environment.
   *  Follow Louis' steps at https://git.arts.ac.uk/lmccallum/nlp-22-23/blob/main/Setup-Conda-Enviroment.md and give your new environment a new name, like nlp2
   * Activate this environment
   * Start at the top of this notebook with the M1-specific conda commands, and see if it works this time.
* Option 2: Create a new environment with Python 3.8 instead of 3.9 (it's worth a try)
   * Follow [Louis' instructions to create a new environment](https://git.arts.ac.uk/lmccallum/nlp-22-23/blob/main/Setup-Conda-Enviroment.md) **except use python=3.8 instead of python=3.9**, and **giving your new environment a new name, like nlp2**

* Option 3: If the above fail, you may want to use miniforge instead of anaconda and start installation from scratch.
   * First, uninstall anaconda using [these instructions](https://docs.anaconda.com/anaconda/install/uninstall/)
   * Then download miniforge from [here](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh)
   * Then, navigate to this downloaded file in your Terminal and type the following commands:
      * `xcode-select --install`
      *  `chmod +x Miniforge3-MacOSX-arm64.sh`
      *  `./Miniforge3-MacOSX-arm64.sh`
      *  `conda config --set auto_activate_base false`
   * Then follow [these instructions](https://caffeinedev.medium.com/how-to-install-tensorflow-on-m1-mac-8e9b91d93706) **starting from Step 3**.
   * Finally, recreate your nlp conda environment using [Louis' instructions](https://git.arts.ac.uk/lmccallum/nlp-22-23/blob/main/Setup-Conda-Enviroment.md)