from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from coala_shop_app.views import home, add_buy, product_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('auth/', include('coala_shop_app.urls.auth')),
    path('add-buy/<int:product_id>/', add_buy, name='add_buy'),
    path('product/<int:product_id>/', product_details, name='show_product')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
