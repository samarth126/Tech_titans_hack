from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .import views


urlpatterns = [
    path('', views.home, name="home"),
    path('categories/', views.categories, name="categories"),
    path('allproducts/', views.allproducts, name="allproducts"),
    path('search/', views.search, name='search'),
    path('cloth_classifier/', views.cloth_classifier, name='cloth_classifier/'),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  