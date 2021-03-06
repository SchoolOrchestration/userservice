"""userservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers
from django.contrib import admin
from api import api
from django.urls import (
    re_path,
    path,
)

router = routers.DefaultRouter()

# router.register('organization', api.OrganizationViewset)

schema_view = get_swagger_view(title='Demo Swagger API', url="/users/")

urlpatterns = [
    re_path(r'^docs/', schema_view),
    path('admin/', admin.site.urls),
    re_path(r'^health/', api.health, name='health'),
    re_path(r'^login/', api.get_user_info, name='login'),
    re_path(r'^oauth/test', api.test_user_middleware, name='oauth-test'),
]

urlpatterns += router.urls
