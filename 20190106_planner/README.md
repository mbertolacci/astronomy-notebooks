# 20190106_planner

Here I plan visits to Tammin, [ASWA's](https://aswa-inc.org.au) observatory site in rural Western Australia.

To run all the code in this directory you will need these Python packages: `astropy`, `astroplan`, `pandas` and `sqlalchemy` (and, of course, Jupyter notebook).

[Tammin visit ranges.ipynb](Tammin visit ranges.ipynb) finds Friday and Saturday evenings with relatively little moonlight at Tammin. This is done by comparing a hypothetical observation session from the start of astronomical twilight to 2am the next morning, and calculating how much of that session has the moon above the horizon. Obviously, these times end up being weekends close to the New Moon. The code calculates the session parameters for all days, not just weekends, so it could easily be adapted to other purposes if you are lucky enough to be able to observe during the week.

This project constitutes my first experiments with [astropy](http://docs.astropy.org/en/stable/index.html) and [astroplan](https://astroplan.readthedocs.io/en/latest/index.html), two Python packages for astronomy. These are sophisticated libraries designed for use by professional astronomers. But since most of the calculations are the same for amateur astronomy, I figured they would be useful for my own humble pastime. So far I have been very pleased: it is easy to manipulate coordinates, perform calculations such as rise/set times, and so on.
