
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('receitas.urls')),
    path('autenticacao/', include('autenticacao.urls')),
    path('cadastro_receitas/', include('receitas.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

