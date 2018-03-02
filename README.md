# Pre-Release CHIPSEC

******************************************************************
 
*PRE-RELEASE NOTICE*

This private repository contains pre-release CHIPSEC functionality

Please do not distribute contents of this repository publicly

******************************************************************

# Building and Using Pre-Release CHIPSEC

* Download/clone CHIPSEC framework from https://github.com/chipsec/chipsec to \<CHIPSEC_PATH\>

* Merge contents of chipsec-prerelease repository into downloaded CHIPSEC located in \<CHIPSEC_PATH\>. This is a simple directory merge. chipsec-prerelease repository has the same directory structure as public CHIPSEC framework. All files from chipsec-prerelease should be moved to corresponding sub-directories in \<CHIPSEC_PATH\>

* Follow CHIPSEC install instructions in [chipsec-manual.pdf](https://github.com/chipsec/chipsec/blob/master/chipsec-manual.pdf) to install and run CHIPSEC in your environment

******************************************************************

### Using CHIPSEC through DAL/ITP2

- Modify `chipsec/helper/helpers.py` and add the line `from chipsec.helper.dal import *`
- Load `itpii` module, then run from command line as usual. Operations will go through DAL to target platform.
  **NOTE:** all actions which do not specify a thread explicitly use Core 0 Thread 0, this cannot be reconfigured currently.
  **WARNING:** using chipsec over DAL at a command prompt is excruciatingly slow, as the DAL stack must be initialized and torn down for every command. Importing chipsec in a DAL CLI session will give much better performance. 
- Alternatively, launch the DAL CLI and enter `import chipsec_util` or `import chipsec_main` to load desired chipsec functions.
  See `chipsec_util.py` for examples of how to use the chipsec utilities from inside the Python CLI.
