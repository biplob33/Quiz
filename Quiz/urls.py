"""Quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from Quiz_app.views import root,login_my_user,logout_my_user,auth_my_user,update,question,question_eval,marks_eval,start,invalid,time,question_body,question_or
#from Quiz_app.api import Qusetion_resourse
#from tastypie.api import Api

#question_resourse = Api(api_name = 'Bips')
#question_resourse.register(Qusetion_resourse())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^questions/$',question_body),
    url(r'^questions/(\d{1,2})/$',question_or),
    url(r'^$',root),
    url(r'^logout/$',logout_my_user),
    url(r'^auth/$',auth_my_user),
    url(r'^login/$',login_my_user),
    url(r'^invalid/$',invalid),
    url(r'^update/$',update),
    url(r'^question/(\d{1,2})/$',question),
    url(r'^next/$',question_eval),
    url(r'^submit/$',marks_eval),
    url(r'^start/$',start),
    url(r'^update_time/$',time),
    #url(r'^api/',include(question_resourse.urls))
]