from jinja2 import Environment, PackageLoader, select_autoescape
import pandas


def datetimeformat(value, format='%Y-%m-%d %H:%M'):
    if pandas.isna(value):
        return ''
    return value.strftime(format)


env = Environment(
    loader=PackageLoader('astromateur', 'templates'),
    autoescape=select_autoescape(['html'])
)
env.filters['datetimeformat'] = datetimeformat

template = env.get_template('template.html')
