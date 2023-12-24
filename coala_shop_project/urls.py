from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from coala_shop_app.views import home, add_buy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('auth/', include('coala_shop_app.urls.auth')),
    path('add-buy/<int:product_id>/', add_buy, name='add_buy')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
