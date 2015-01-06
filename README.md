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
* `SPLASH_ENDPOINT`: the endpoint for your splash server. Default is 'http://localhost:8050/render.html'
* `SPLASH_TIMEOUT`: render timeout in seconds (see http://splash.readthedocs.org/en/latest/api.html#render-html)
* `SPLASH_WAIT`: wait time in seconds (see http://splash.readthedocs.org/en/latest/api.html#render-html)
* `SPLASH_IMAGES`: `True` or `False` (default is `True`)
* `SPLASH_URL_PASS`: tuple of regular expressions matching URLs to send to Splash (default is `None`, i.e. no request goes through splash)
* `SPLASH_URL_BLOCK`:  tuple of regular expressions matching URLs NOT to send to Splash (default is `None`, i.e. do not filter out anything)

How to use it
-------------

To tell scrapy to send some requests to Splash using this middleware,
you have the following options:

* set a `use_splash` key to `True` in your `Request` `meta`: e.g. `yield Request(url, meta={"use_splash": True})`
* use `SPLASH_URL_PASS` and `SPLASH_URL_BLOCK`, for example
`SPLASH_URL_PASS = (r'.',)` would match all URLs, and send everything
through Splash


Example spider
--------------

You can test the example spider like this:

* start your splash server

```shell
cd src/splash
python -msplash.server
```

Let's assume splash is listening at http://localhost:8050/render.html,
otherwise change `settings.py` `SPLASH_ENDPOINT`.

* The spider expects a `urls` parameter that is a URL of a file
containing URLs to fetch.

```shell
~/src/scrapy-splash$ cd splashtest/
~/src/scrapy-splash/splashtest$ scrapy crawl example -a urls=https://gist.githubusercontent.com/redapple/93c97ce85dbceddcb063/raw/6250c37003d77b0ac006d95e7d15e3a71e701bea/urls.txt

```
