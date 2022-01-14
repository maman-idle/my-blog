from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('spilled_bits.urls')),
    path('tinymce/', include('tinymce.urls')),
]

handler404 = "spilled_bits.views.PageNotFound"
