from product.views import *
from django.urls import path


urlpatterns = [
    # path("", main_page),
    path("", ListProduct.as_view()),
    # path("catalog/", catalog),
]















