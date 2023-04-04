from django.urls import path, re_path

from api.views import hello, product_list, product_det, category_list
urlpatterns =[
    path('hello/', hello),
    path('products/', product_list),
    path('products/<int:id>/', product_det),

    path('categories', category_list)
]