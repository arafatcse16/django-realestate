from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path("supersecret/", admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    # path("api/v1/profile/", include("apps.profiles.urls")),
    # path("api/v1/ratings/", include("apps.ratings.urls")),
    # path("api/v1/enquiries/", include("apps.enquiries.urls")),
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
