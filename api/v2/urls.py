from django.urls import path
from api import views
from api.v2 import views as views_v2

urlpatterns = [
    path('items/', views.EntryList.as_view(), name=views.EntryList.name),
    path('item-detail/<int:pk>', views.EntryDetail.as_view(), name=views.EntryDetail.name),
    path('', views_v2.ApiRootVersion2.as_view(), name=views_v2.ApiRootVersion2.name)
]