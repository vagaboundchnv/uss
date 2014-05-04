from uss.api.baseresource import USSModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from uss.models import Tag
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.http import HttpBadRequest

class TagResource(USSModelResource):
    """
    It will be used for getting contacts of given parents
    And updating the contact details
    """
    count = fields.IntegerField(attribute="count", null=True)

    class Meta:
        resource_name = 'tags'
        queryset = Tag.objects.all()
        authorization = Authorization()

    def get_object_list(self, request):
        user_id = request.user.id
        if not user_id:
            raise ImmediateHttpResponse(HttpBadRequest("Please login first"))
        
        this_user_tags = super(TagResource, self).get_object_list(request).filter(user_id=user_id)
        return this_user_tags
    
    def alter_list_data_to_serialize(self, request, data):
        user_id = request.user.id
        if not user_id:
            raise ImmediateHttpResponse(HttpBadRequest("Please login first"))
        
        tags = Tag.objects.raw("""SELECT tag.id, count(*) as 
                                count from uss_tag as tag JOIN 
                                uss_urldesc_tags as urldesc_tags on 
                                tag.id =urldesc_tags.tag_id where 
                                tag.user_id=%s group by tag.id""", [user_id])
        tag_map = {}
        for tag in tags:
            tag_map[tag.id] = tag.count
        print tag_map
        objects = data['objects'] 
        for obj in objects:
            obj.data["count"] = tag_map.get(obj.data["id"], 0) 
        return data    