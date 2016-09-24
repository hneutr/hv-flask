import sys
from math import ceil
from flask import Flask, render_template, redirect, request, url_for
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
PER_PAGE = 5
FREEZER_DESTINATION_IGNORE = ['.git*']

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

###############################################################################

class Pagination(object):
    def __init__(self, page, per_page, total_count):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages

###############################################################################

@app.route('/', defaults={'page':1})
@app.route('/page/<int:page>.html')
def index(page):
    dated = [p for p in pages if 'date' in p.meta]

    pagination = Pagination(page, PER_PAGE, len(dated))
    if page > pagination.pages:
        return render_template('404.html')

    recent = sorted(dated, reverse=True, key=lambda p: p.meta['date'])
    this_page = recent[(page - 1) * PER_PAGE:][:PER_PAGE]

    return render_template('index.html', pages=this_page, pagination=pagination)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route('/kind/<string:kind>.html', defaults={'page':1})
@app.route('/kind/<string:kind>/page/<int:page>.html')
def kind(kind, page):
    in_kind = [p for p in pages if kind in p.meta.get('kind', [])]

    pagination = Pagination(page, PER_PAGE, len(in_kind))
    if page > pagination.pages:
        return render_template('404.html')

    recent = sorted(in_kind, reverse=True, key=lambda p: p.meta['date'])
    this_page = recent[(page - 1) * PER_PAGE:][:PER_PAGE]

    return render_template('kind.html', pages=this_page, kind=kind, pagination=pagination)

@app.route('/tag/<string:tag>.html', defaults={'page':1})
@app.route('/tag/<string:tag>/page/<int:page>.html')
def tag(tag, page):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]

    pagination = Pagination(page, PER_PAGE, len(tagged))
    if page > pagination.pages:
        return render_template('404.html')

    recent = sorted(tagged, reverse=True, key=lambda p: p.meta['date'])
    this_page = recent[(page - 1) * PER_PAGE:][:PER_PAGE]

    return render_template('tag.html', pages=this_page, tag=tag, pagination=pagination)

@app.route('/year/<int:year>.html', defaults={'page':1})
@app.route('/year/<int:year>/page/<int:page>.html')
def year(year, page):
    in_year = [p for p in pages if year == p.meta['date'].year]

    pagination = Pagination(page, PER_PAGE, len(in_year))
    if page > pagination.pages:
        return render_template('404.html')

    recent = sorted(in_year, reverse=True, key=lambda p: p.meta['date'])
    this_page = recent[(page - 1) * PER_PAGE:][:PER_PAGE]

    return render_template('year.html', pages=this_page, year=year, pagination=pagination)

###############################################################################

@app.route('/tags.html')
def tags():
    all_tags = [p.meta.get('tags', []) for p in pages if p.meta.get('tags', [])]
    flattened = sorted(set([item for sublist in all_tags for item in sublist]))
    return render_template('tags.html', tags=flattened)

@app.route('/years.html')
def years():
    all_years = [p.meta['date'].year for p in pages if p.meta['date']]
    flattened = sorted(set(all_years), reverse=True)
    return render_template('years.html', years=flattened)

@app.route('/me.html')
def me():
    return render_template('about.html')

@app.route('/resume.html')
def resume():
    return render_template('resume.html')

@app.route('/semanticweb.html')
def semanticweb():
    return render_template('semantic_web.html')

@app.route('/404.html')
def notfound():
    return render_template('404.html')

###############################################################################
@app.template_filter()
def formatdate(value, format='%Y/%m/%d'):
    """convert a datetime to a different format."""
    return value.strftime(format)

@app.template_filter()
def excerpt(content):
    return content.split('</p>', 1)[0] + '</p>'

def short(content):
    return True if len(content) < 500 else False

def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)

app.jinja_env.filters['formatdate'] = formatdate
app.jinja_env.filters['excerpt'] = excerpt

app.jinja_env.globals['short'] = short
app.jinja_env.globals['url_for_other_page'] = url_for_other_page

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
            freezer.freeze()
    else:
        app.run(port=8000)
