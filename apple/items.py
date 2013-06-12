# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class AppItem(Item):
    # define the fields for your item here like:
    app_name = Field()
    category = Field()
    appstore_link = Field()
    img_src = Field()
