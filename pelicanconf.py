#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'imeixi'
TITLENAME = "IMEIXI's BLOG"
SITENAME = 'THE GROWTH PATH OF DATA SCIENTISTS'
SITEURL = '//imeixi.github.io/blog'
RELATIVE_URLS = False

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


##---------------------------------add notebook plugins-----------------------##
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-ipynb.markup','neighbors.neighbors'] #pelican-ipynb 为添加的submodule文件夹名
IGNORE_FILES = [".ipynb_checkpoints"] # 如果有ipynb_checkpoints文件添加这一行以忽略

##---------------------------------add theme----------------------------------##
# THEME = "themes/blue-penguin"
THEME = "themes/pelican-striped-html5up"
STATIC_PATHS = ['images']
# PLUGINS = ['neighbors']

