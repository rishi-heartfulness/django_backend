import pytest
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from faker import Faker
from .models import CustomUser, Product  

fake = Faker()

base_url = "http://127.0.0.1:8000/api-method/products/"


@pytest.fixture(scope="session")
def group_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        product_type = ContentType.objects.get_for_model(Product)

        admin_group, _ = Group.objects.get_or_create(name="Admin")
        customer_group, _ = Group.objects.get_or_create(name="Customer")
        supplier_group, _ = Group.objects.get_or_create(name="Supplier")

        admin_permissions = Permission.objects.filter(
            content_type=product_type,
            codename__in=["add_product", "change_product", "delete_product", "view_product"]
        )
        admin_group.permissions.set(admin_permissions)

        view_permission = Permission.objects.get(content_type=product_type, codename="view_product")
        customer_group.permissions.set([view_permission])

        supplier_permissions = Permission.objects.filter(
            content_type=product_type,
            codename__in=["view_product", "change_product"]
        )
        supplier_group.permissions.set(supplier_permissions)


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def product(db):
    product = Product.objects.create(
        name="Test Product",
        price=100,
        stock=50,
        category="Electronics",
        description="A test product for the supplier test"
    )
    return product


@pytest.fixture
def admin_user(db):
    user = CustomUser.objects.create_user(username="admin_user", password="admin123")
    group = Group.objects.get(name="Admin")
    user.groups.add(group)
    refresh = RefreshToken.for_user(user)
    token = str(refresh.access_token)
    return user, token



@pytest.fixture
def customer_user(db):
    user = CustomUser.objects.create_user(username="customer_user", password="cust123")
    group = Group.objects.get(name="Customer")
    user.groups.add(group)
    refresh = RefreshToken.for_user(user)
    token = str(refresh.access_token)
    return user, token


@pytest.fixture
def supplier_user(db):
    user = CustomUser.objects.create_user(username="supplier_user", password="supp123")
    group = Group.objects.get(name="Supplier")
    user.groups.add(group)
    refresh = RefreshToken.for_user(user)
    token = str(refresh.access_token)
    return user, token

# ------------------ TEST CASES ------------------
@pytest.mark.django_db
def test_register_user(client):
    url = reverse("register")
    data = {
        "email": fake.email(),
        "username": fake.user_name(),
        "password": fake.password(),
        "address": fake.address(),
        "phone": fake.msisdn()[:10] 
    }
    response = client.post(url, data, format="json")
    print("Status code:", response.status_code)
    print("Response data:", response.data) 
    assert response.status_code == status.HTTP_201_CREATED
    assert "message" in response.data


@pytest.mark.django_db
def test_login_success(client):
    email = fake.email()
    password = fake.password()
    user = CustomUser.objects.create_user(email=email,username= "rishi",password=password)
    url = reverse("login")  
    data = {
        "email": email,
        "password": password
    }
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data


@pytest.mark.django_db
def test_login_failure(client):
    email = fake.email()
    password = fake.password()
    
    url = reverse("login")  
    data = {
        "email": email,
        "password": password
    }
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


# # ------------------ ADMIN TESTS ------------------

@pytest.mark.django_db
def test_admin_can_crud_products(client, group_setup, admin_user, product):
    user, token = admin_user
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    # List
    response = client.get(base_url)
    assert response.status_code == status.HTTP_200_OK

    # Retrieve
    response = client.get(f"{base_url}{product.id}/")
    assert response.status_code == status.HTTP_200_OK

    # Create
    test_data_creation = {
        "name": "New Product",
        "price": 200,
        "stock": 5,
        "category": "Books",
        "description": "A new product"
    }
    response = client.post(base_url, test_data_creation)
    assert response.status_code == status.HTTP_201_CREATED

    # Update
    test_data_updation = {
        "name": "Updated Product",
        "price": 250,
        "stock": 7,
        "category": "Updated",
        "description": "Updated desc"
    }
    response = client.put(f"{base_url}{product.id}/", test_data_updation)
    assert response.status_code == status.HTTP_200_OK

    # Delete
    response = client.delete(f"{base_url}{product.id}/")
    assert response.status_code == status.HTTP_204_NO_CONTENT


# ------------------ CUSTOMER TESTS ------------------

@pytest.mark.django_db
def test_customer_can_only_view(client, group_setup, customer_user, product):
    demo_user = []
    for user in range(3):
     
        user, token = customer_user
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

        # List
        response = client.get(base_url)
        assert response.status_code == status.HTTP_200_OK

        # Retrieve
        response = client.get(f"{base_url}{product.id}/")
        assert response.status_code == status.HTTP_200_OK

    # Create
    test_data_creation = {
        "name": "Unauthorized Create",
        "price": 100,
        "stock": 5,
        "category": "Misc",
        "description": "Should fail"
    }
    
    response = client.post(base_url, test_data_creation)
    assert response.status_code == status.HTTP_403_FORBIDDEN

    # Update
    test_data_updation = {
        "name": "Hack Update",
        "price": 0,
        "stock": 0,
        "category": "None",
        "description": "Hack"
    }
    response = client.put(f"{base_url}{product.id}/", test_data_updation)
    assert response.status_code == status.HTTP_403_FORBIDDEN

    # Delete
    response = client.delete(f"{base_url}{product.id}/")
    assert response.status_code == status.HTTP_403_FORBIDDEN


# ------------------ SUPPLIER TESTS ------------------

@pytest.mark.django_db
def test_supplier_can_view_and_update(client, group_setup, supplier_user, product):
    user, token = supplier_user
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    # List
    response = client.get(base_url)
    assert response.status_code == status.HTTP_200_OK

    # Retrieve
    response = client.get(f"{base_url}{product.id}/")
    assert response.status_code == status.HTTP_200_OK

    # Create
    test_data_creation = {
        "name": "Not Allowed",
        "price": 999,
        "stock": 1,
        "category": "Illegal",
        "description": "Denied"
    }
    
    response = client.post(base_url, test_data_creation)
    assert response.status_code == status.HTTP_403_FORBIDDEN

    # Update
    test_data_updation = {
        "name": "Supplier Updated",
        "price": 180,
        "stock": 15,
        "category": "SupplierCat",
        "description": "Updated by supplier"
    }
    response = client.put(f"{base_url}{product.id}/",test_data_updation)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == "Supplier Updated"

    # Delete
    response = client.delete(f"{base_url}{product.id}/")
    assert response.status_code == status.HTTP_403_FORBIDDEN
