# 20190106_planner

Here I plan visits to Tammin, [ASWA](https://aswa-inc.org.au)'s observatory site in rural Western Australia.

To run all the code in this directory you will need these Python packages: `astropy`, `astroplan`, `pandas` and `sqlalchemy` (and, of course, Jupyter notebook).

[Tammin visit ranges.ipynb](https://github.com/mbertolacci/astronomy-notebooks/blob/master/20190106_planner/Tammin%20visit%20ranges.ipynb) finds Friday and Saturday evenings with relatively little moonlight at Tammin. This is done by comparing a hypothetical observation session from the start of astronomical twilight to 2am the next morning, and calculating how much of that session has the moon above the horizon. Obviously, these times end up being weekends close to the New Moon. The code calculates the session parameters for all days, not just weekends, so it could easily be adapted to other purposes if you are lucky enough to be able to observe during the week.
