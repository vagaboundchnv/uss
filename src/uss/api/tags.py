from uss.api.baseresource import USSResource, USSObject
from tastypie import fields
from tastypie.authorization import Authorization
import json

class TagResource(USSResource):
    """
    It will be used for getting contacts of given parents
    And updating the contact details
    """
    id = fields.IntegerField(attribute="id", null=True)
    name = fields.CharField(attribute="name", null=True)
    count = fields.IntegerField(attribute="count", null=True)

    class Meta:
        resource_name = 'tags'
        object_class = USSObject
        authorization = Authorization()

    def get_object_list(self, request):
        tags = json.loads(open('src/uss/fixtures/tags.json').read())
        return map(USSObject, tags)

    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle.request)
