def map_number(coordinate):
    ra_h = coordinate.ra.hms[0]
    chart_group = int(ra_h / 3)
    return('{} to {}'.format(
        10 * chart_group + 1,
        10 * (chart_group + 1)
    ))
