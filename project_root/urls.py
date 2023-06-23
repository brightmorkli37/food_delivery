from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from accounts.serializers import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include(('djoser.urls'))),
    path('auth/', include(('djoser.urls.jwt'))),
    path('auth/jwt/create/', TokenObtainPairView.as_view()),

    # path('users/', include('accounts.urls', 'accounts')),
]

urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )