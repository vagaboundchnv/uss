from uss.api.baseresource import USSModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from uss.scrapper import scrapper
from uss.models import UrlDesc
from tastypie.http import HttpBadRequest
from tastypie.exceptions import ImmediateHttpResponse

class UrlResource(USSModelResource):
    """
    It will be used for getting contacts of given parents
    And updating the contact details
    """
    scrap_data = fields.DictField(attribute="scrap_data", null=True)

    class Meta:
        resource_name = 'urls'
        queryset = UrlDesc.objects.all()
        authorization = Authorization()


    def get_object_list(self, request):
        user_id = request.user.id
        if not user_id:
            raise ImmediateHttpResponse(HttpBadRequest("Please login first"))
        
        this_user_urls = super(UrlResource, self).get_object_list(request).filter(user_id=user_id)
        return this_user_urls
    
    def alter_list_data_to_serialize(self, request, data):
        user_id = request.user.id
        if not user_id:
            raise ImmediateHttpResponse(HttpBadRequest("Please login first"))
        
        objects = data['objects'] 
        for obj in objects:
            obj.data["scrap_data"] = scrapper(obj.data["link"]) 
        return data