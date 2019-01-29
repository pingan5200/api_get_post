from django.urls import path
from . import views

app_name = 'index'
urlpatterns = [
    path('<int:pk>', views.product_get),
    # path('', views.product_post)
    path('', views.product_class.as_view())
]
