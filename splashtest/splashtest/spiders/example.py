# -*- coding: utf-8 -*-
import cStringIO as StringIO
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"

    def start_requests(self):
        yield scrapy.Request(self.urls, callback=self.parse_urlfile,
                             meta={"use_splash": False})

    def parse_urlfile(self, response):
        limit = int(getattr(self, 'limit', '0'))
        for cnt, line in enumerate(StringIO.StringIO(response.body).readlines(), start=1):
            yield scrapy.Request(line.strip(), meta={"use_splash": True})
            if limit and cnt >= limit:
                break

    def parse(self, response):
        self.log("response.url:         %r" % response.url)
        self.log("response.request.url: %r" % response.request.url)
        splashed = response.meta.get("splashed_url")
        if splashed:
            self.log("Splashed request:     %r" % splashed)
