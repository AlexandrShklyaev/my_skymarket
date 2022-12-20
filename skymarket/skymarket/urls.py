from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# TODO здесь необходимо подклюючит нужные нам urls к проекту

urlpatterns = [
    path("api/admin/", admin.site.urls),

    path("api/redoc-tasks/", include("redoc.urls")),
    path("api/schema/", SpectacularAPIView.as_view(),name='schema'),
    path("api/swagger-tasks/",SpectacularSwaggerView.as_view(url_name='schema'),),

    path("api/api/", include("ads.urls")),
    # path("api/api/users/", include("users.urls")),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)