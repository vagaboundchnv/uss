from uss.api.baseresource import USSResource, USSObject
from tastypie import fields
from tastypie.authorization import Authorization
import json
from uss.scrapper import scrapper

class UrlResource(USSResource):
    """
    It will be used for getting contacts of given parents
    And updating the contact details
    """
    id = fields.IntegerField(attribute="id", null=True)
    link = fields.CharField(attribute="link", null=True)
    my_descriptions = fields.CharField(attribute="my_descriptions", null=True)
    comments = fields.CharField(attribute="comments", null=True)
    tags = fields.ListField(attribute="tags", null=True)
    scrap_data = fields.DictField(attribute="scrap_data", null=True)

    class Meta:
        resource_name = 'urls'
        object_class = USSObject
        authorization = Authorization()

    def get_object_list(self, request):
        urls = json.loads(open('src/uss/fixtures/urls.json').read())
        for url in urls:
            url["scrap_data"] = scrapper(url)
        return map(USSObject, urls)

    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle.request)
