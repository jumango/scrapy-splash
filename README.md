scrapy-splash
=============

Scrapy - Splash integration for javascript support

Enable the middleware
---------------------

See http://doc.scrapy.org/en/latest/topics/downloader-middleware.html

```python
DOWNLOADER_MIDDLEWARES = {
    'splashtest.middleware.splash.SplashMiddleware': 725,
}
```

Order `725` is just before `HttpProxyMiddleware` (750) in default scrapy settings.

Available settings
------------------

* `SPLASH_ENABLED` = `True` or `False`
* `SPLASH_URL`: the endpoint for your splash server. Default is 'http://localhost:8050/render.html'
* `SPLASH_WAIT`: wait time in seconds (see http://splash.readthedocs.org/en/latest/api.html#render-html)
* `SPLASH_IMAGES`: `True` or `False` (default is `True`)
* `SPLASH_URL_PASS`: tuple of regular expressions matching URLs to send to Splash (default is `(,)`, i.e. every request goes through splash)
* `SPLASH_URL_BLOCK`:  tuple of regular expressions matching URLs NOT to send to Splash (default is `(,)`, i.e. do not filter out anything)
