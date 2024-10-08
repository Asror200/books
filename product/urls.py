from django.urls import path

from product.views import product, category, group

urlpatterns = [
    # Category
    path('', category.CategoriesDetailListApiView.as_view(), name='categories-detail-list'),
    path('category/<slug:slug>/', category.CategoryDetailApiView.as_view(), name='category-detail'),
    path('add-category/', category.CategoryAddView.as_view(), name='add-category'),

    # Group
    path('category/<slug:category_slug>/<slug:slug>/', group.GroupDetailListApiView.as_view(),
         name='group-detail'),
    path('add-group/', group.GroupAddView.as_view(), name='add-group'),

    # Product
    path('products/', product.ProductsListApiView.as_view(), name='products-list'),
    path('product/view/<slug:slug>/', product.ProductDetailApiView.as_view(), name='product-detail'),
    path('add-product/', product.ProductAddView.as_view(), name='add-product'),
    path('product-attribute-key/', product.AttributeKeyListApiView.as_view(), name='product-attribute-key'),
    path('product-attribute-value/', product.AttributeValueListApiView.as_view(), name='product-attribute-value'),
    path('product-attribute-key-value/', product.AttributeKeyValueListApiView.as_view(),
         name='product-attribute-key-value'),
]
