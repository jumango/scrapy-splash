# -*- coding: utf-8 -*-

# Scrapy settings for splashmw project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'splashtest'

SPIDER_MODULES = ['splashtest.spiders']
NEWSPIDER_MODULE = 'splashtest.spiders'

DOWNLOADER_MIDDLEWARES = {
    'splashtest.middleware.splash.SplashMiddleware': 725,
}

SPLASH_ENABLED = True
SPLASH_ENDPOINT = 'http://localhost:8050/render.html'
SPLASH_WAIT = 2
SPLASH_IMAGES = False
#SPLASH_URL_PASS = (r'example\.com',)
#SPLASH_URL_BLOCK = (r'badexample\.com',)

CONCURRENT_REQUESTS_PER_DOMAIN = 5
CONCURRENT_REQUESTS = 5
RETRY_ENABLED = False
