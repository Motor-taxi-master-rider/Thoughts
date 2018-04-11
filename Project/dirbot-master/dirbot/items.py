from scrapy.item import Field, Item


class Website(Item):

    name = Field()
    description = Field()
    url = Field()
