from django.conf.urls import include, url
from django.contrib import admin
from nick01 import url as nickurl
from nick01 import views
urlpatterns = [
    url(r'^nick01/', include(nickurl)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^one/',views.one)
    ]

