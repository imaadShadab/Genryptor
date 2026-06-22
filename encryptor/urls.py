from django.urls import path
from . import views

urlpatterns = [
    # path('', views.PasswordListView.as_view(), name = 'pass-list'),
    path('', views.pass_list, name = 'pass-list'),
    path('generator/', views.home, name = 'home'),
    path('encryptor/', views.encryptor, name = 'encryptor'),
    path('decryptor/', views.decryptor, name = 'decryptor'),
    path('decryptor/<int:pk>', views.decryptor, name = 'decryptor-id'),
]

