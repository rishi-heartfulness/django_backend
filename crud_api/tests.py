# from rest_framework.test import APITestCase
# from rest_framework import status
# from django.urls import reverse
# from faker import Faker
# from .models import CustomUser,Product,Transaction,TransactionItem
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import Permission


# User = get_user_model()

# fake = Faker()

# class RegisterUserTestCase(APITestCase):
#     def test_register_user(self):
#         url = reverse("register")

#         data = {
#             "email": fake.unique.email(),
#             "username": fake.unique.user_name(),
#             "password": "Test@12345",
#             "address": fake.address(),
#             "phone": fake.msisdn()[:10] 
#         }

#         response = self.client.post(url, data, format="json")

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertIn("message", response.data)





# class LoginViewTest(APITestCase):
#     def setUp(self):
#         self.user = CustomUser.objects.create_user(username="rishi", password="qwerty123")
#         self.login_url = "http://127.0.0.1:8000/api-method/login/" 

#     def test_login_success(self):
#         response = self.client.post(self.login_url, {"username": "rishi", "password": "qwerty123"})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn("access", response.data)

#     def test_login_failure(self):
#         response = self.client.post(self.login_url, {"username": "var@gmail.com", "password": "qwerty123"})
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)




# # for admin 

# class ProductViewSetTestAdmin(APITestCase):
#     def setUp(self):
#         customUser = get_user_model()
#         self.user = CustomUser.objects.create_user(
#             username="rishi", password="testpass123"
#         )
#         refresh = RefreshToken.for_user(self.user)
#         self.access_token = str(refresh.access_token)
#         self.auth_headers = {"HTTP_AUTHORIZATION": f"Bearer {self.access_token}"}

#         self.product = Product.objects.create(
#             name="Test Product",
#             price=100,
#             category="Electronics",
#             description="Sample product for testing",
#             stock=10
#         )

#         permissions = Permission.objects.filter(
#             codename__in=["add_product", "change_product", "delete_product", "view_product"]
#         )
#         self.user.user_permissions.set(permissions)
#         self.user.save() 
#         self.base_url = 'http://127.0.0.1:8000/api-method/products/'
#         self.detail_url = f'{self.base_url}{self.product.id}/'

#     def test_list_products(self):
#         response = self.client.get(self.base_url, **self.auth_headers)
#         print(response,"from list ")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_retrieve_product(self):
#         response = self.client.get(self.detail_url, **self.auth_headers)
#         print(response,"from single prod ")

#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_create_product(self):
#         data = {
#             "name": "New Product",
#             "price": 150,
#             "stock": 5,
#             "category": "Stationery",
#             "description": "Test description"
#         }
#         response = self.client.post(self.base_url, data, **self.auth_headers)
#         print(response,"from create prod ")

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_update_product(self):
#         data = {
#             "name": "Updated Product",
#             "price": 120,
#             "stock": 8,
#             "category": "Updated Category",
#             "description": "Updated description"
#         }
#         response = self.client.put(self.detail_url, data, **self.auth_headers)
#         print(response,"from update prod ")

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["name"], "Updated Product")

#     def test_delete_product(self):
#         response = self.client.delete(self.detail_url, **self.auth_headers)
#         print(response,"from delete prod ")

#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)





# # for customer 

# class ProductViewSetTestCustomer(APITestCase):
#     def setUp(self):
#         customUser = get_user_model()
#         self.user = CustomUser.objects.create_user(username=fake.user_name(), password=fake.password())
#         refresh = RefreshToken.for_user(self.user)
#         self.access_token = str(refresh.access_token)
#         self.auth_headers = {"HTTP_AUTHORIZATION": f"Bearer {self.access_token}"}
#         self.product = Product.objects.create(
#             name="Test Product",
#             price=100,
#             category="Electronics",
#             description="Sample product for testing",
#             stock=10
#         )
#         permissions = Permission.objects.filter(codename__in=["view_product"])
#         self.user.user_permissions.set(permissions)
#         self.user.save()
#         self.base_url = 'http://127.0.0.1:8000/api-method/products/'
#         self.detail_url = f'{self.base_url}{self.product.id}/'

#     def test_list_products(self):
#         response = self.client.get(self.base_url, **self.auth_headers)
#         print(response,"from list prod ")

#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_retrieve_product(self):
#         response = self.client.get(self.detail_url, **self.auth_headers)
#         print(response,"from get 1 prod ")

#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_create_product(self):
#         data = {
#             "name": "New Product",
#             "price": 150,
#             "stock": 5,
#             "category": "Stationery",
#             "description": "Test description"
#         }
#         response = self.client.post(self.base_url, data, **self.auth_headers)
#         print(response,"from create prod ")

#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

#     def test_update_product(self):
#         data = {
#             "name": "Updated Product",
#             "price": 120,
#             "stock": 8,
#             "category": "Updated Category",
#             "description": "Updated description"
#         }
#         response = self.client.put(self.detail_url, data, **self.auth_headers)
#         print(response,"from update prod ")

#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

#     def test_delete_product(self):
#         response = self.client.delete(self.detail_url, **self.auth_headers)
#         print(response,"from delete prod ")
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)







# # for supplier 

# class ProductViewSetTestSupplier(APITestCase):
#     def setUp(self):
#         customUser = get_user_model()
#         self.user = CustomUser.objects.create_user(username=fake.user_name(), password=fake.password())
#         refresh = RefreshToken.for_user(self.user)
#         self.access_token = str(refresh.access_token)
#         self.auth_headers = {"HTTP_AUTHORIZATION": f"Bearer {self.access_token}"}
#         self.product = Product.objects.create(
#             name="Test Product",
#             price=100,
#             category="Electronics",
#             description="Sample product for testing",
#             stock=10
#         )
#         permissions = Permission.objects.filter(
#             codename__in=["view_product","change_product"]
#         )
#         self.user.user_permissions.set(permissions)
#         self.user.save()
#         self.base_url = 'http://127.0.0.1:8000/api-method/products/'
#         self.detail_url = f'{self.base_url}{self.product.id}/'

#     def test_list_products(self):
#         response = self.client.get(self.base_url, **self.auth_headers)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_retrieve_product(self):
#         response = self.client.get(self.detail_url, **self.auth_headers)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_create_product(self):
#         data = {
#             "name": "New Product",
#             "price": 150,
#             "stock": 5,
#             "category": "Stationery",
#             "description": "Test description"
#         }
#         response = self.client.post(self.base_url, data, **self.auth_headers)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

#     def test_update_product(self):
#         data = {
#             "name": "Updated Product",
#             "price": 120,
#             "stock": 8,
#             "category": "Updated Category",
#             "description": "Updated description"
#         }
#         response = self.client.put(self.detail_url, data, **self.auth_headers)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["name"], "Updated Product")

#     def test_delete_product(self):
#         response = self.client.delete(self.detail_url, **self.auth_headers)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)






 

















