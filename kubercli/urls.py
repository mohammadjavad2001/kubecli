from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
#from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='K8s API')

urlpatterns = [
    path("doc/", schema_view),

    path('admin/', admin.site.urls),
    path('cli/', include('cli.urls'))
] 