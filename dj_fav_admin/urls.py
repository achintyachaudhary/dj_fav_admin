from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    # favicon for admin-admin panel
    path('favicon.ico', RedirectView.as_view(url='/static/images/package.png')),
    path('favorite.svg', RedirectView.as_view(url='/static/images/favorite.svg')),

]
