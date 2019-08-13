# Overview:

It's a static site, with dynamic site features. I'm pretty stoked on it; the thing's yoked.

## Layers:

There's a preprocessing layer that allows me to run scripts to populate things. This is cool. It's defined in `config.yaml`.

Sidebar and etc is also defined there.

I also allow for `subparts` to generate things. This is sweet, because I can auto-populate stuff and make more pages. For example, I have a python package called `book_networks`, that generates all the html, svgs, and etc for webweb representations of books. This package then hooks into the site. It'll automatically get called when I build.

# standard pages:

Add files in /pages/
- name them:
    - YYYY-MM-DD-title-separated-by-hypens
    - fields:
        - title:
        - description:
        - date: YYYY-MM-DD
        - kind: 
            - one of:
                - Thoughts
                - Projects
                - Playlists
        - tags: [comma, separated]
            - if it is loaded from a file, add in 'independent: 1', as well as a full_path and a url_path

# Updating the site
just run `./update.sh`
