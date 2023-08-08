from django.urls import path
from . import views
# from .views import RegisterView,GetTokenView
urlpatterns = [
    
    path('create pod /', views.creat_pod),
    path('getlistpod/', views.list_pods),
    path('create_deployment/', views.creat_deployment),
    path('getlistnode/', views.list_node),
    path('getlistnamespace/', views.list_namespace),
    path('deletenode/', views.delete_node),
    #path('getlistdeployment/', views.list_deployments),
    path('getlistservice/', views.list_service),
    path('deletepod/', views.delete_pod),
    path('createnode/', views.create_ndoe),
    path('getlistnamespace/', views.list_namespace),

    



]