# -*- coding: utf-8 -*-

# Scrapy settings for PyntedScrapers project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

AWS_REGION_NAME = 'eu-west-3'

BOT_NAME = 'PyntedScrapers'

FEED_EXPORT_ENCODING = 'utf-8'

FEED_FORMAT = 'jsonlines'

FEED_URI = 's3://toffaascrapingbucket/%(name)s/%(thread)s/%(time)s.json'

LOG_LEVEL = 'INFO'

NEWSPIDER_MODULE = 'PyntedScrapers.spiders'

ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}

IMAGES_STORE = 's3://toffaascrapingbucket/images'

IMAGES_URLS_FIELD = 'image_urls'

ROBOTSTXT_OBEY = True

SPIDER_MODULES = ['PyntedScrapers.spiders']
