from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path("supersecret/", admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Real Estate Admin"
admin.site.site_title = "Real Estate Admin Portal"
admin.site.index_title = "Welcome to Real Estate Admin Portal"
# urlpatterns += [
#     path("api/v1/users/", include("apps.users.urls")),
#     path("api/v1/real-estate/", include("apps.real_estate.urls")),
#     path("api/v1/locations/", include("apps.locations.urls")),
#     path("api/v1/transactions/", include("apps.transactions.urls")),
#     path("api/v1/notifications/", include("apps.notifications.urls")),
# ]
