from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(('django.contrib.auth.urls', 'auth'), namespace='accounts')),
    path('', include('main_app.urls')),
    path('appointment/', include('appointment.urls')),
]
urlpatterns += static(settings.STATIC_URL , document_root=settings.STATICFILES_DIRS) 
urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT) 