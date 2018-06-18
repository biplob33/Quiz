from tastypie.resources import ModelResource
from models import qusetion

class Qusetion_resourse(ModelResource):
    class Meta:
        query_set = qusetion.objects.all()
        #resource_name = 'question'
        