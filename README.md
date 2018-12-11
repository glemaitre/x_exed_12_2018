Introduction to data science
============================

Instructors
-----------

- [Guillaume Lemaitre](https://glemaitre.github.io/)  [@glemaitre](https://github.com/glemaitre) - Inria, Université Paris-Saclay

---

Obtaining the Tutorial Material
--------------------------------

If you have a GitHub account, it is probably most convenient if you clone or
fork the GitHub repository. You can clone the repository by running:

```bash
git clone https://github.com/glemaitre/x_exed_12_2018.git
```

If you are not familiar with git or don't have an
GitHub account, you can download the repository as a .zip file by heading over
to the GitHub repository (https://github.com/glemaitre/x_exed_12_2018) in
your browser and click the green “Download” button in the upper right.

Please note that we may add and improve the material until shortly before the
tutorial session, and we recommend you to update your copy of the materials one
day before the tutorials. If you have an GitHub account and cloned the
repository via GitHub, you can sync your existing local repository with:

```bash
git pull origin master
```

If you don’t have a GitHub account, you may have to re-download the .zip
archive from GitHub.


Installation Notes
------------------

This tutorial will require recent installations of

- [NumPy](http://www.numpy.org)
- [SciPy](http://www.scipy.org)
- [matplotlib](http://matplotlib.org)
- [seaborn](https://seaborn.pydata.org/)
- [pandas](http://pandas.pydata.org)
- [pillow](https://python-pillow.org)
- [scikit-learn](http://scikit-learn.org/stable/)
- [IPython](http://ipython.readthedocs.org/en/stable/)
- [Jupyter Notebook](http://jupyter.org)

For users who do not yet have the required packages installed, a relatively
painless way to install all the requirements is to use a Python distribution
such as [Anaconda](https://www.anaconda.com/download/ "Anaconda"), which includes
the most relevant Python packages for science, math, engineering, and
data analysis; Anaconda can be downloaded and installed for free
including commercial use and redistribution.
The code examples in this tutorial should be compatible to Python 2.7,
Python 3.4-3.7.

We provided an `environment.yml` file allowing to specifically install
the required packages into a specific `conda` environment. You can
create this environment by entering the following command:

``` bash
conda env create -f environment.yml
```

Once the packages installed, you can activate the environment:

``` bash
conda activate datascience
```

You will be able to use Jupyter Lab or Notebook by executing either:

``` bash
jupyter notebook
```

or 

``` bash
jupyter lab
```
