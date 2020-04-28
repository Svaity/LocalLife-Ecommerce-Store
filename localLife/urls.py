"""localLife URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import include, path
from pages.views import home_view, contact_view, about_view
from products.views import search
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('s/', search, name='search'),
    path('products/', include('products.urls')),
    path('', include('store.urls')),
    path('', include('user.urls')),
    # path('order/', include('user.urls', namespace='accounts')),
    # path('order/'),
    path('contact/', contact_view),
    path('about/', about_view),


    path('', include('shopping_cart.urls', namespace='shopping_cart')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
