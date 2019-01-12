# astronomy-notebooks

This is a place I store IPython notebooks for amateur astronomy.

At present I am using Python 3.6 via [Anaconda](https://www.anaconda.com/download) to run these. I haven't tried Python 3.7, though general experience suggests it would work fine.

The folders with dated names (e.g. [20180106_planner](https://github.com/mbertolacci/astronomy-notebooks/tree/master/20190106_planner)) correspond to mini 'projects' where I try a thing or two. Inside each are a README and one or more IPython notebooks attempting what the project is about.

## How to use these

GitHub should allow you to view the results of each notebook just by clicking through the repository.

If you want to download the notebooks and run them locally / modify them for your own purpose, you need to somehow get a Python environment with Jupyter installed, and install the dependencies.

The easiest way to do this is to download the [Anaconda distribution](https://www.anaconda.com/download) of Python 3. Then, in your Anaconda environment, install the packages

- `jupyter`
- `astropy`
- `astroplan`
- `pandas`

Then download the notebook you want to run, launch Jupyter via Anaconda, and use the file browser to navigate to the `ipynb` file you just downloaded. With any luck this should open and you should be able to run the code yourself.

More resources on Anaconda and Jupyter that might be helpful:

- DataCamp's tutorial on [Jupyter notebooks](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook)
- The Anaconda [user guide](https://docs.anaconda.com/anaconda/user-guide/)
