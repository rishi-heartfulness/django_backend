# from django.urls import path,include
# from . import views

# urlpatterns = [
#     path("register/",views.register,name="register"),
#     path("login/",views.login,name="login"),
#     path("create_product/",views.create_product,name="create_product"),
#     path("get_all_products/",views.get_all_products,name="get_all_products"),
#     path("get_products_by_id/",views.get_products_by_id,name="get_products_by_id"),
#     path("update_product/",views.update_product,name="update_product"),
#     path("delete_product/",views.delete_product,name="delete_product") 
# ]





# urlpatterns = [
#     path('register/', views.register,name="register"),
#     path('login/', views.login,name="login"),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

#     path('get_all_products/', views.get_all_products,name="get_all_products"),
#     path('get_product_by_id/<int:product_id>/', views.get_product_by_id,name="get_product_by_id"),
#     path('create_product/', views.create_product,name="create_product"),
#     path('update_product/<int:product_id>/', views.update_product,name="update_product"),
#     path('delete_product/<int:product_id>/', views.delete_product,name="delete_product"),
# ]

    # path('get_all_products/', views.ProductListView.as_view(), name="get_all_products"),
    # path('create_product/', views.ProductCreateView.as_view(), name="create_product"),
    # path('get_product_by_id/<int:product_id>/', views.ProductDetailView.as_view(), name="get_product_by_id"),
    # path('update_product/<int:product_id>/', views.ProductDetailView.as_view(), name="update_product"),
    # path('delete_product/<int:product_id>/', views.ProductDetailView.as_view(), name="delete_product"),



from django.urls import path
# from . import views
from . import views
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import  TokenObtainPairView,TokenRefreshView

router = DefaultRouter()
router.register(r'products',views.ProductViewSet, basename='product')




urlpatterns = [
    path('register/',views.RegisterView.as_view(), name='register'),  
    path('login/', views.LoginView.as_view(), name='login'),            
    path('orders/', views.OrdersView.as_view(), name='orders'),        
    path('orders-summary/<int:customer_id>/', views.OrderSummaryView.as_view(), name='orders_summary_view'), 
]


urlpatterns += router.urls




# urlpatterns = [
#     path('register/', views.RegisterView.as_view(), name="register"),
#     path('login/', views.LoginView.as_view(), name="login"),
#     path('api/token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),

#     path('products/', views.ProductCRUDView.as_view(), name='product-list-create'),
#     path('products/<int:id>/', views.ProductCRUDView.as_view(), name='product-detail'),
# ]