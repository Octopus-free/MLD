from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import include, url  # For django versions before 2.0
from django.urls import include, path  # For django versions from 2.0 and up

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dbcreate.urls', namespace='dbcreate')),
    path('ManagingUsers/', include('ManagingUsers.urls', namespace='ManagingUsers'))

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns