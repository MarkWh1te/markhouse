#!/usr/bin/env python # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

SITENAME = "Mark White's Blog"
SITETITLE = "Mark White"

AUTHOR = 'mark'

SITESUBTITLE = 'Software Engineer'
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR

BROWSER_COLOR = '#333333'

# SITEURL = '127.0.0.1:8000'
# SITEURL = 'markwh1te.github.io'
SITEURL = ''


PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# images related
# SITELOGO = SITEURL + '/images/profile.peg'
# FAVICON = SITEURL + '/images/favicon.ico'
SITELOGO = 'http://7xq2dq.com1.z0.glb.clouddn.com/minlake.jpg'
FAVICON = 'http://7xq2dq.com1.z0.glb.clouddn.com/minlake.jpg'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Social widget
SOCIAL =(
    # ('linkedin', 'https://br.linkedin.com/in/alexandrevicenzi/en'),
    ('github', 'https://github.com/markwh1te'),
    ('twitter', 'https://twitter.com/wh1temark'),
    ('envelope-o', 'mailto:iamwh1temark@gmail.com')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "Flex"

# license related
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}
COPYRIGHT_YEAR = 2017


# plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ["render_math"]

# menu related
# MAIN_MENU = True
MAIN_MENU = False

# MENUITEMS = (
#     ('Archives', '/archives.html'),
#     ('Categories', '/categories.html'),
#              # ('Tags', '/tags.html'),
# )

# Blogroll
LINKS = (
    ('home', 'http://markwh1te.github.io'),
    ('archives', 'http://markwh1te.github.io/archives.html'),
    ('categories', 'http://markwh1te.github.io/categories.html'),
    # ('contact', 'pages/contact.html'),
    # ('You can modify those links in your config file', '#'),
)
