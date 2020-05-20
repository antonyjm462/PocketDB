from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls import include, url
from rest_framework import routers
from Database import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    re_path(r'^api/data/(?P<pk>[0-9]+)$', # Url to get update or delete Data
        views.Database_Get_Update_Delete_Api.as_view(),
        name='Database_Get_Update_Delete_Api'
    ),
    path('api/data/', # urls list all and create new one
        views.Database_Get_Post_Api.as_view(),
        name='Database_Get_Post_Api'
    )

]