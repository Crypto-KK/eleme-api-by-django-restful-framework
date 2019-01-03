from django.urls import path
from front import views
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('detail/<pk>', views.DetailView.as_view(), name='detail')
]