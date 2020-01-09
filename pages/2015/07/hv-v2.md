title: hunter (verb) - Version 2
date: 2015-07-23
kind: projects
tags: [computing]
description: Finally, a place all my own!

After a long period of inactivity - which, I'm sure, had everyone on edge - I finally got back around to my working on my website. Rather than write more content (the hard part) I rewrote the site from scratch (the easier part).

The original site was built using [Jekyll](http://jekyllrb.com/), a static website generator, and [Hyde](http://hyde.getpoole.com/), an open source theme for Jekyll. Fortunately, I claim zero responsibility for that terrible pun.

I had a couple problems with Jekyll: it would only paginate things with a date, and only when they were in a specific directory; tag support was spotty; and it was written in Ruby, a language I didn't care to learn for this project.

Despite those qualms, my biggest issue with the first version was that I never really got comfortable enough with the code I hadn't written to make the site _mine_ - the whole point of the project in the first place. 

---

I had a couple goals for the rewrite: site-wide pagination; support for tags; ease of extensibility for one-offs and unique pages; to keep the site on [GitHub Pages](https://pages.github.com/) (because I didn't want to pay for hosting); and to write everything, from server to styling, myself.

I love Python, so I decided to use [Flask](http://flask.pocoo.org/) for the server and a combination of [Flask-FlatPages](https://pythonhosted.org/Flask-FlatPages/) and [Frozen-Flask](http://pythonhosted.org/Frozen-Flask/) to turn that server into a static set of pages GitHub could host. 

I'm pretty happy with how it turned out.

---

You can find all the code for the project [here](https://github.com/hunter-/hv-flask).
