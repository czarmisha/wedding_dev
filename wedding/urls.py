"""wedding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = 'wedding'
urlpatterns = i18n_patterns(
    path('', views.home, name='home'),
    path('promo/', views.promo, name='promo'),
    path('catalog/', views.catalog, name='catalog'),
    path('account/', include('account.urls', namespace='account')),
    path('services/', include('services.urls', namespace='services')),
    path('tender/', include('tender.urls', namespace='tender')),
    path('budget/', include('budget.urls', namespace='budget')),
    path('guest-list/', include('guest_list.urls', namespace='guest_list')),
    path('plan/', include('plan.urls', namespace='plan')),
    path('favorite/', include('favorite.urls', namespace='favorite')),
    path('admin/', admin.site.urls),
    path('search/', include('search.urls', namespace='search')),
    path('__debug__/', include('debug_toolbar.urls')),
    # path('ratings/', include('star_ratings.urls', namespace='ratings')),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "wedding.views.page_not_found_view"