from flask import Flask, render_template, redirect, request, url_for
from flask_flatpages import FlatPages
from flask_frozen import Freezer

import argparse
import datetime
import markdown
import math
import os
import yaml
from pathlib import Path

import subparts.networks as networks_generator


STATIC_DIR = Path.cwd().joinpath('static')
TEMPLATES_DIR = Path.cwd().joinpath('templates')
PAGES_DIR = Path.cwd().joinpath('pages')


################################################################################
# ARGUMENTPARSING
################################################################################
def get_args():
    """Defines an argument parser for this script and returns the flags this
    package is called with
    """

    parser = argparse.ArgumentParser(description='my site')

    parser.add_argument(
        '-b', '--build',
        help='build flatpages',
        default=False,
        action='store_true')

    parser.add_argument(
        '-d',
        '--debug',
        help="print debug messages",
        default=False,
        action="store_true")

    parser.add_argument(
        '-s',
        '--rebuild_subparts',
        help="rebuild the subparts",
        default=False,
        action="store_true")

    return parser.parse_args()


args = get_args()

if args.debug:
    FREEZER_DESTINATION = 'build_test'

FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = '.md'
FREEZER_DESTINATION_IGNORE = ['.git*']
PER_PAGE = 5

app = Flask(__name__)
app.config.from_object(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.url_map.strict_slashes = False
pages = FlatPages(app)
freezer = Freezer(app)


config = yaml.load("".join(Path.cwd().joinpath('config.yaml').read_text()))


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


def path_is_of_type(path, type_sequence):
    """given a path and a type_sequence, determines if the path is in the type
    examples:
    1. general type (match):
        - in:
            - path: '/type_1/type_2/file.html'
            - type_sequence: ['type_1']
        - out:
            - True
    2. specific type (match):
        - in:
            - path: '/type_1/type_2/file.html'
            - type_sequence: ['type_1', 'type_2']
        - out:
            - True
    3. mismatch:
        - in:
            - path: '/type_1/type_2/file.html'
            - type_sequence: ['type_1', 'type_3']
        - out:
            - False
    """
    if path.startswith('/'):
        path = path[1:]

    if not type_sequence:
        return True

    expected_type = type_sequence[0]
    actual_type, remainder = path.split('/', 1)

    if actual_type == expected_type:
        return path_is_of_type(remainder, type_sequence[1:])
    else:
        return False


def remove_types_from_path(path, type_sequence):
    """removes the portions of a path in a type sequence"""
    if path.startswith('/'):
        path = path[1:]

    if not type_sequence:
        return path

    current_type = type_sequence[0]

    return remove_types_from_path(path.replace(current_type, '', 1), type_sequence[1:])


def get_path_type(path):
    if path.startswith('/'):
        path = path[1:]

    if '/' in path:
        return path.split('/', 1)[0]
    else:
        return None

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

    recent = sorted(dated, reverse=True, key=lambda p: p.meta['date'])
    this_page = recent[(page - 1) * PER_PAGE:][:PER_PAGE]

    return render_template('index.html', pages=this_page, pagination=pagination)

################################################################################
# 'Simple' Routes
################################################################################
@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)

    if page.meta.get('independent'):
        kind = page.meta.get('kind', '')
        page_url = page.meta.get('url_path', '')

        redirect(url_for(kind + '/' + page_url + '.html'))
    elif page.meta.get('raw'):
        return render_template('raw.html', page=page)

    return render_template('page.html', page=page)

################################################################################
# networks
################################################################################
@app.route('/networks.html')
def networks():
    network_pages = [p for p in pages if path_is_of_type(p.path, ['networks'])]

    network_page_types = set()
    for network_page in network_pages:
        network_page_subpath = remove_types_from_path(network_page.path, ['networks'])
        network_page_type = get_path_type(network_page_subpath)

        if network_page_type:
            network_page_types.add(network_page_type)

    network_page_types = sorted(list(network_page_types))
    network_page_urls = [f'/networks/{_type}.html' for _type in network_page_types]

    return render_template(
        'link_list.html',
        title='network types',
        item_names=network_page_types,
        item_urls=network_page_urls,
    )


@app.route('/networks/books.html', defaults={'page': 1})
@app.route('/networks/books/<int:page>.html')
def networks_of_books(page):
    type_sequence = ['networks', 'books']
    book_pages = [p for p in pages if path_is_of_type(p.path, type_sequence)]

    print(book_pages)

    book_pages.append(book_pages[0])

    return paged_response(
        page=page,
        pages=book_pages,
        template='booklist.html',
        sort_by='author_lastname',
        # kwargs_to_send={
        #     'kind': kind,
        #     'subkinds': list(
        #         set(
        #             [p.meta.get('subkind') for p in in_kind if p.meta.get('subkind')]
        #         )
        #     ),
        # }
    )


################################################################################
# Kinds
################################################################################
@app.route('/kind/<string:kind>.html', defaults={'page': 1})
@app.route('/kind/<string:kind>/<int:page>.html')
def kind(kind, page):
    in_kind = list(filter(lambda p: kind in p.meta.get('kind', ''), pages))

    return paged_response(
        page=page,
        pages=in_kind,
        template='kind.html',
        kwargs_to_send={
            'kind': kind,
            'subkinds': list(
                set(
                    [p.meta.get('subkind') for p in in_kind if p.meta.get('subkind')]
                )
            ),
        }
    )


@app.route('/kind/<string:kind>/sub/<string:subkind_slug>.html', defaults={'page': 1})
@app.route('/kind/<string:kind>/sub/<string:subkind_slug>/<int:page>.html')
def sub_kind(kind, subkind_slug, page):
    subkind = sluggify_subkind(subkind_slug, to_slug=False)
    return paged_response(
        page=page,
        template='subkind.html',
        pages=list(
            filter(
                lambda p: kind in p.meta.get('kind', ''),
                filter(lambda p: subkind == p.meta.get('subkind', ''), pages)
            )
        ),
        kwargs_to_send={
            'kind': kind,
            'subkind': subkind,
            'subkind_slug': subkind_slug,
        }
    )


@app.route('/tagged/<string:tag>.html', defaults={'page': 1})
@app.route('/tagged/<string:tag>/<int:page>.html')
def tag(tag, page):
    return paged_response(
        page=page,
        template='tag.html',
        pages=list(filter(lambda p: tag in p.meta.get('tags', []), pages)),
        kwargs_to_send={
            'tag': tag,
        }
    )


@app.route('/year/<int:year>.html', defaults={'page': 1})
@app.route('/year/<int:year>/<int:page>.html')
def year(year, page):
    dated_pages = [p for p in pages if p.meta.get('date')]
    year_pages = [p for p in dated_pages if p.meta['date'].year == year]
    return paged_response(
        page=page,
        template='year.html',
        pages=year_pages,
        kwargs_to_send={
            'year': year,
        }
    )


def paged_response(page, template, kwargs_to_send={}, pages=[], sort_by='date'):
    pagination = Pagination(page, PER_PAGE, len(pages))
    if page > pagination.pages:
        return render_template('404.html')

    recent = sorted(pages, reverse=True, key=lambda p: p.meta.get(sort_by))
    kwargs_to_send['pages'] = recent[(page - 1) * PER_PAGE:][:PER_PAGE]
    kwargs_to_send['pagination'] = pagination

    return render_template(template, **kwargs_to_send)


@app.route('/kind/<string:kind>/<string:name>.html')
def independent_page(kind, name):
    matching_pages = []
    for p in pages:
        if kind not in p.meta.get('kind', []):
            continue

        if p.meta.get('url_path', '') != name:
            continue

        matching_pages.append(p)

    if matching_pages:
        page = matching_pages.pop()

        content_path = os.path.join(
            config['directories']['prepages'],
            kind,
            page.meta.get('file_path', '')
        )

        if os.path.isfile(content_path):
            with open(os.path.join(content_path), 'r') as f:
                text = markdown.markdown(f.read())

            if text:
                return render_template('independent_page.html', page=page, text=text)

    return render_template('404.html')


################################################################################
# Dynamic Routes
################################################################################
@app.route('/tags.html')
def tags():
    all_tags = [p.meta.get('tags', []) for p in pages if p.meta.get('tags', [])]
    flattened = sorted(set([item for sublist in all_tags for item in sublist]))
    return render_template(
        'link_list.html',
        title='tags',
        item_names=flattened,
        item_urls=[url_for('tag', tag=tag) for tag in flattened],
    )


@app.route('/years.html')
def years():
    all_years = [p.meta['date'].year for p in pages if p.meta.get('date')]
    flattened = sorted(set(all_years), reverse=True)
    return render_template(
        'link_list.html',
        title='years',
        item_names=flattened,
        item_urls=[url_for('year', year=year) for year in flattened],
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
def formatdate(value, format='%Y/%m/%d'):
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
app.jinja_env.filters['zip'] = zip


def subpart_to_module_map():
    return {
        'networks': networks_generator,
    }


def rebuild_subparts(config):
    for subpart in config['subparts']:
        module = subpart_to_module_map()[subpart]
        module.regenerate(
            pages_directory=PAGES_DIR,
            static_directory=STATIC_DIR,
            templates_directory=TEMPLATES_DIR,
            reset=False,
        )


################################################################################
# Run
################################################################################
if __name__ == '__main__':
    if args.rebuild_subparts:
        rebuild_subparts(config)

    if args.build:
        freezer.freeze()
    else:
        app.run(port=8000, debug=args.debug)
