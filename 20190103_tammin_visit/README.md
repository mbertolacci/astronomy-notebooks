# 20190103_tammin_visit

Here I generate an observing sheet for my January 2019 visit to Tammin, [ASWA](https://aswa-inc.org.au)'s observatory site in rural Western Australia. I went for the evenings of the 3rd and the 4th.

To run all the code in this directory you will need these Python packages: `astropy`, `astroplan`, and `pandas` (and, of course, Jupyter notebook).

[Observing sheet.ipynb](https://github.com/mbertolacci/astronomy-notebooks/blob/master/20190103_tammin_visit/Observing%20sheet.ipynb) makes an observing sheet for a list of targets generated using [DSO Browser](https://dso-browser.com) and stored in [targets.csv](https://github.com/mbertolacci/astronomy-notebooks/blob/master/20190103_tammin_visit/targets.csv).

The resulting observing sheet is in [targets.html](https://github.com/mbertolacci/astronomy-notebooks/blob/master/20190103_tammin_visit/targets.html).

This project constitutes my first experiment with [astropy](http://docs.astropy.org/en/stable/index.html) and [astroplan](https://astroplan.readthedocs.io/en/latest/index.html), two Python packages for astronomy. These are sophisticated libraries designed for use by professional astronomers. But since most of the calculations are the same for amateur astronomy, I figured they would be useful for my own humble pastime. So far I have been very pleased: it is easy to manipulate coordinates, perform calculations such as rise/set times, and so on.
