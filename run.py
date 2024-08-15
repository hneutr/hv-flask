import argparse
import datetime
import markdown
import math
import yaml
from pathlib import Path

from flask import Flask, render_template, redirect, request, url_for
from flask_flatpages import FlatPages
from flask_frozen import Freezer

import constants


URLS = [
    "www.hne.golf",
    "hne.golf",
]

FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = '.md'
FREEZER_DESTINATION = ".build"
FREEZER_DESTINATION_IGNORE = ['.git*']
PER_PAGE = 50

app = Flask(__name__)
app.config.from_object(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.url_map.strict_slashes = False
pages = FlatPages(app)
freezer = Freezer(app)

config = yaml.load(
    constants.CONFIG_PATH.read_text(),
    Loader=yaml.FullLoader
)


################################################################################
# Pagination
################################################################################
class Pagination(object):
    def __init__(self, page, per_page, total_count):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

    @property
    def pages(self):
        return int(math.ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages


################################################################################
# Index
################################################################################
@app.route('/', defaults={'page': 1})
@app.route('/<int:page>.html')
def index(page):
    dated = [p for p in pages if 'date' in p.meta]

    pagination = Pagination(page, PER_PAGE, len(dated))
    if page > pagination.pages:
        return render_template('404.html')

    recent = sorted(dated, key=lambda p: p.meta['date'], reverse=True)
    this_page = recent[(page - 1) * PER_PAGE:][:PER_PAGE]

    print(url_for("static", filename=f"pdfs/thesis-defense.pdf"))
    return render_template('index.html', pages=this_page, pagination=pagination)

################################################################################
# 'Simple' Routes
################################################################################
@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)

    return render_template('page.html', page=page)


@app.route('/kind/<string:kind>.html', defaults={'page': 1})
@app.route('/kind/<string:kind>/<int:page>.html')
def kind(kind, page):
    return paged_response(
        page=page,
        pages=[p for p in pages if kind in p.meta.get('kind', '')],
        template='kind.html',
        kwargs_to_send={
            'kind': kind,
        }
    )


@app.route('/year/<int:year>.html', defaults={'page': 1})
@app.route('/year/<int:year>/<int:page>.html')
def year(year, page):
    return paged_response(
        page=page,
        template='year.html',
        pages=[p for p in pages if p.meta.get('date') and p.meta['date'].year == year],
        kwargs_to_send={
            'year': year,
        }
    )


def paged_response(page, template, kwargs_to_send={}, pages=[]):
    pagination = Pagination(page, PER_PAGE, len(pages))
    if page > pagination.pages:
        return render_template('404.html')

    recent = sorted(pages, reverse=True, key=lambda p: p.meta['date'])
    kwargs_to_send['pages'] = recent[(page - 1) * PER_PAGE:][:PER_PAGE]
    kwargs_to_send['pagination'] = pagination

    return render_template(template, **kwargs_to_send)


################################################################################
# Dynamic Routes
################################################################################
@app.route('/years.html')
def years():
    return render_template(
        'years.html',
        years=sorted({p.meta['date'].year for p in pages if p.meta.get('date')}, reverse=True),
    )

################################################################################
# Static Routes
################################################################################
@app.route('/me.html')
def me():
    return render_template('about.html')


@app.route('/cv.html')
def cv():
    return render_template('cv.html')


@app.route('/404.html')
def notfound():
    return render_template('404.html')

################################################################################
# Filters/Miscellaneous
################################################################################
@app.template_filter()
def formatdate(value, format='%Y%m%d'):
    """convert a datetime to a different format."""
    return value.strftime(format)


@app.template_filter()
def sluggify_subkind(subkind, to_slug=True):
    if to_slug:
        return subkind.replace(' ', '_')
    else:
        return subkind.replace('_', ' ')


def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)


app.jinja_env.filters['formatdate'] = formatdate
app.jinja_env.filters['lower'] = lambda x: x.lower()

app.jinja_env.globals['url_for_other_page'] = url_for_other_page
app.jinja_env.globals['kinds'] = config['kinds']
app.jinja_env.globals['metas'] = config['metas']
app.jinja_env.globals['now'] = datetime.datetime.utcnow


################################################################################
# CNAME
################################################################################
def write_cname():
    cname_path = Path(__file__).parent.joinpath('.build', 'CNAME')

    if cname_path.exists():
        cname_path.unlink()
    
    cname_path.touch()
    cname_path.write_text("\n".join(URLS))

################################################################################
# Run
################################################################################
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='hne.golf website')

    parser.add_argument(
        '-b', '--build',
        help='build flatpages',
        default=False,
        action='store_true')

    args = parser.parse_args()

    if args.build:
        freezer.freeze()
        write_cname()
    else:
        app.run(port=8000, debug=True)
