from django.contrib import admin
from django.urls import path, include
from django.conf import settings            # for the image in a dev mode
from django.conf.urls.static import static  # for the image in a dev mode

# Records master urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('quote/', include('quote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'REcords Admin'       # default: "Django Administration"
admin.site.index_title = 'REcords Admin List'  # default: "Site administration"
admin.site.site_title = 'REcords Title'        # default: "Django site admin"


    