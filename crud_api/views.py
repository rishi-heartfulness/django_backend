# from django.shortcuts import render
# from .models import *
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json

# @csrf_exempt
# def register(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)

#             email = data.get("email")
#             password = data.get("password")

#             if not email or not password:
#                 return JsonResponse({"error": "All fields are required"}, status=400)

#             if users.objects.filter(email=email).exists():
#                 return JsonResponse({"error": "User already exists"}, status=409)

#             users.objects.create(email=email, password=password, role=role)
#             return JsonResponse({"message": "User registered successfully"}, status=201)

#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)
#     else:
#         return JsonResponse({"error": "Invalid request method"}, status=405)


# @csrf_exempt
# def login(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)           # return access token 
#             email = data.get("email")
#             password = data.get("password")

#             # Check if a user with the provided email and password exists
#             if users.objects.filter(email=email, password=password).exists():
#                 return JsonResponse({"message": "Login successful"}, status=200)
#             else:
#                 return JsonResponse({"error": "Invalid email or password"}, status=401)

#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)
#     else:
#         return JsonResponse({"error": "Invalid request method"}, status=405)




# @csrf_exempt
# def create_product(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             product = products.objects.create(
#                 name=data["name"],
#                 price=data["price"],
#                 category=data["category"],
#                 description=data["description"],
#                 stock=data["stock"]
#             )
#             product_dict = {
#                 "id": product.id,
#                 "name": product.name,
#                 "price": product.price,
#                 "category": product.category,
#                 "description": product.description,
#                 "stock": product.stock,
#             }
#             return JsonResponse({"Product added successfully": product_dict}, status=201)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)
#     else:
#         return JsonResponse({"error": "Invalid request method"}, status=405)





# def get_all_products(request):
#     if request.method == "GET":
#         try:
#             product_list = []
#             retrived_product_list= products.objects.all()
#             for product_data in retrived_product_list:
#                 product_dict = {
#                     "id": product_data.id,
#                     "name": product_data.name,
#                     "price": product_data.price,
#                     "category": product_data.category,
#                     "description": product_data.description,
#                     "stock": product_data.stock,
#                 }

#                 product_list.append(product_dict)
#             return JsonResponse({f"retrived {len(product_list)} Products successfully": product_list}, status=200)
        
#         except products.DoesNotExist:
#             return JsonResponse({"error": "Product not found"}, status=404)

#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)
#     else:
#         return JsonResponse({"error": "Invalid request method"}, status=405)




# def get_products_by_id(request):
#     if request.method == "GET":
#         try:
#             data = json.loads(request.body)
#             product_id = data.get("product_id")
#             retrieved_product= products.objects.get(id = product_id)

#             product_dict = {
#                 "id": retrieved_product.id,
#                 "name": retrieved_product.name,
#                 "price": retrieved_product.price,
#                 "category": retrieved_product.category,
#                 "description": retrieved_product.description,
#                 "stock": retrieved_product.stock,
#             }
#             return JsonResponse({"retrived Product successfully": product_dict}, status=200)

#         except products.DoesNotExist:
#             return JsonResponse({"error": "Product not found"}, status=404)

#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)
#     else:
#         return JsonResponse({"error": "Invalid request method"}, status=405)




# @csrf_exempt
# def update_product(request):
#     if request.method == "PUT":
#         try:
#             data = json.loads(request.body)
#             product_id = data.get("id")
#             retrieved_product = products.objects.get(id=product_id)
#             # Update fields if provided
#             if "name" in data:
#                 retrieved_product.name = data["name"]
#             if "price" in data:
#                 retrieved_product.price = data["price"]
#             if "description" in data:
#                 retrieved_product.description = data["description"]
#             if "stock" in data:
#                 retrieved_product.stock = data["stock"]
#             retrieved_product.save()
#             return JsonResponse({"message": "Product updated successfully"}, status=200)
#         except products.DoesNotExist:
#             return JsonResponse({"error": "Product not found"}, status=404)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)
#     else:
#         return JsonResponse({"error": "Invalid request method"}, status=405)






# @csrf_exempt
# def delete_product(request):
#     if request.method == "DELETE":
#         try:
#             data = json.loads(request.body)
#             product_id = data.get("product_id")

#             retrieved_product = products.objects.get(id=product_id)
#             retrieved_product.delete()

#             return JsonResponse({"message": "Product deleted successfully"}, status=200)

#         except products.DoesNotExist:
#             return JsonResponse({"error": "Product not found"}, status=404)

#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)
#     else:
#         return JsonResponse({"error": "Invalid request method"}, status=405)









# _______________________________set 2__________________________________________________



# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.hashers import make_password, check_password
# from .models import *
# from django.contrib.auth.models import User
# from .serializers import ProductSerializer



# @api_view(['POST'])
# @permission_classes([AllowAny])
# def register(request):
#     try:
#         email = request.data.get("email")
#         username = request.data.get("username")
#         password = request.data.get("password")

#         if not email or not password:
#             return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

#         # if User.objects.get(email=email).exists():
#         #     return Response({"error": "User already exists"}, status=status.HTTP_409_CONFLICT)

#         hashed_password = make_password(password)
#         new_user =  User.objects.create_user(email=email, password=hashed_password,username=username)
#         new_user.save() 
#         return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

#     except Exception as e:
#         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




# @api_view(['POST'])
# @permission_classes([AllowAny])
# def login(request):
#     try:
#         email = request.data.get("email")
#         password = request.data.get("password")

#         if not email or not password:
#             return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

#         # user_retrieved = User.objects.get(email=email)
#         users = User.objects.filter(email=email)
#         user_retrieved = users.first()  
#         if email != user_retrieved.email or  check_password(password, user_retrieved.password):
#             return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)


#         refresh = RefreshToken.for_user(user_retrieved)
#         return Response({
#             "message": "Login successful",
#             "access": str(refresh.access_token),
#             "refresh": str(refresh)
#         }, status=status.HTTP_200_OK)

#     except Exception as e:
#         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_product(request):
#     try:
#     #     data = request.data
#     #     product = products.objects.create(
#     #         name=data.get("name"),
#     #         price=data.get("price"),
#     #         category=data.get("category"),
#     #         description=data.get("description"),
#     #         stock=data.get("stock")
#     #     )

#     #     product_dict = {
#     #         "id": product.id,
#     #         "name": product.name,
#     #         "price": product.price,
#     #         "category": product.category,
#     #         "description": product.description,
#     #         "stock": product.stock,
#     #     }
#     #     return Response({"Product added successfully": product_dict}, status=status.HTTP_201_CREATED)
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"Product added successfully": serializer.data}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     except Exception as e:
#         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_all_products(request):
#     try:
#         # product_list = []
#         # for p in products.objects.all():
#         #     product_list.append({
#         #         "id": p.id,
#         #         "name": p.name,
#         #         "price": p.price,
#         #         "category": p.category,
#         #         "description": p.description,
#         #         "stock": p.stock,
#         #     })
#         # return Response({"products": product_list}, status=status.HTTP_200_OK)
#         all_products = products.objects.all()
#         serializer = ProductSerializer(all_products, many=True)
#         return Response({"products": serializer.data}, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_product_by_id(request, product_id):
#     # try:
#     #     product = products.objects.get(id=product_id)
#     #     product_dict = {
#     #         "id": product.id,
#     #         "name": product.name,
#     #         "price": product.price,
#     #         "category": product.category,
#     #         "description": product.description,
#     #         "stock": product.stock,
#     #     }
#     #     return Response({"product": product_dict}, status=status.HTTP_200_OK)
#     # except products.DoesNotExist:
#     #     return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    
#     try:
#         product = products.objects.get(id=product_id)
#     except products.DoesNotExist:
#         return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

#     serializer = ProductSerializer(product)
#     return Response({"product": serializer.data}, status=status.HTTP_200_OK)
#     # except Exception as e:
#     #     return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def update_product(request, product_id):
#     # try:
#     #     product = products.objects.get(id=product_id)
#     #     data = request.data

#     #     product.name = data.get("name", product.name)
#     #     product.price = data.get("price", product.price)
#     #     product.category = data.get("category", product.category)
#     #     product.description = data.get("description", product.description)
#     #     product.stock = data.get("stock", product.stock)
#     #     product.save()

#     #     return Response({"message": "Product updated successfully"}, status=status.HTTP_200_OK)
#     # except products.DoesNotExist:
#     #     return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
#     try:
#         product = products.objects.get(id=product_id)
#     except products.DoesNotExist:
#         return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

#     serializer = ProductSerializer(product, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "Product updated successfully", "product": serializer.data}, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     # except Exception as e:
#     #     return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# @api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
# def delete_product(request, product_id):
#     try:
#         product = products.objects.get(id=product_id)
#         product.delete()
#         return Response({"message": "Product deleted successfully"}, status=status.HTTP_200_OK)
#     except products.DoesNotExist:
#         return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
















# _______________________________set 3__________________________________________________

# api view 

# class ProductCreateView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request):
#         try:
#             serializer = ProductSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({"Product added successfully": serializer.data}, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class ProductListView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):
#         try:
#             all_products = Products.objects.all()
#             serializer = ProductSerializer(all_products, many=True)
#             return Response({"products": serializer.data}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class ProductDetailView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, product_id):
#         try:
#             product = products.objects.get(id=product_id)
#             serializer = ProductSerializer(product)
#             return Response({"product": serializer.data}, status=status.HTTP_200_OK)
#         except products.DoesNotExist:
#             return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     def put(self, request, product_id):
#         try:
#             product = products.objects.get(id=product_id)
#             serializer = ProductSerializer(product, data=request.data, partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({"message": "Product updated successfully", "product": serializer.data}, status=status.HTTP_200_OK)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except products.DoesNotExist:
#             return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     def delete(self, request, product_id):
#         try:
#             product = products.objects.get(id=product_id)
#             product.delete()
#             return Response({"message": "Product deleted successfully"}, status=status.HTTP_200_OK)
#         except products.DoesNotExist:
#             return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)







# class ProductCRUDView(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [permissions.IsAuthenticated]  
#     lookup_field = 'id'

#     def get(self, request, id=None, *args, **kwargs):
#         if id:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def put(self, request, id=None, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, id=None, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)                                                                                                     














from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password
# from django.contrib.auth.models import User
from .models import Products,CustomUser ,Transaction,PaymentMode
from .serializers import ProductSerializer
from rest_framework import generics, mixins, permissions,viewsets






class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            email = request.data.get("email")
            username = request.data.get("username")
            password = request.data.get("password")
            address = request.data.get("address")
            phone = request.data.get("phone")

            # if not email or not password:
            #     return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

            if CustomUser.objects.filter(email=email).exists():
                return Response({"error": "User already exists"}, status=status.HTTP_409_CONFLICT)

            new_user = CustomUser.objects.create_user(email=email, password=password, username=username,address=address,phone=phone)
            new_user.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            email = request.data.get("email")
            password = request.data.get("password")

            if not email or not password:
                return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

            user_retrieved = CustomUser.objects.filter(email=email).first()
            if  user_retrieved and user_retrieved.check_password(password):

                refresh = RefreshToken.for_user(user_retrieved)
                return Response({
                    "message": "Login successful",
                    "access": str(refresh.access_token),
                    "refresh": str(refresh)
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ProductViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated,permissions.DjangoModelPermissions]
    lookup_field = 'id'







# class OrdersView(APIView):
#     permission_classes = [permissions.AllowAny]

#     def post(self, request):
#         try:
#             customer_id = request.data.get("customer_id")
#             orders = request.data.get("orders", [])
#             payment_mode = request.data.get("payment_mode", "").lower()

#             if not customer_id or not orders or not payment_mode:
#                 return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

#             if payment_mode not in ["upi", "cod", "card"]:
#                 return Response({"error": "Payment mode must be 'upi', 'cod', or 'card'."}, status=status.HTTP_400_BAD_REQUEST)

#             # Fetch all products once
#             products_queryset = Products.objects.all()
#             products_dict = {product.id: product for product in products_queryset}  # Map by id for fast lookup

#             total_bill = 0
#             total_products_ordered = len(orders)

#             for item in orders:
#                 requested_product_id = item.get("product_id")
#                 requested_quantity = item.get("quantity")

#                 if requested_product_id not in products_dict:
#                     return Response({"error": f"Product ID {requested_product_id} not found."}, status=status.HTTP_404_NOT_FOUND)

#                 product = products_dict[requested_product_id]

#                 if requested_quantity > product.stock:
#                     return Response({"error": f"Not enough stock for product {product.name} (Available: {product.stock})"}, status=status.HTTP_400_BAD_REQUEST)

#                 # Update the stock in memory
#                 product.stock -= requested_quantity

#                 # Add to the bill
#                 total_bill += product.price * requested_quantity

#             # Save the updated stock to database
#             for product in products_dict.values():
#                 product.save()

#             # Create transaction record
#             transaction = Transaction.objects.create(
#                 customer_id=customer_id,
#                 total_products=total_products_ordered,
#                 total_price=total_bill,
#                 transaction_mode=payment_mode
#             )

#             return Response({
#                 "transaction_id": transaction.id,
#                 "message": "Purchase successful",
#                 "total_price": total_bill
#             }, status=status.HTTP_201_CREATED)

#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




# request body
# {
#     "customer_id" : 2,
#     "payment_mode" : "upi",
#     "orders" : [{"product_id":1,
# 	            "quantity":10},

#           {"product_id":2,
# 	        "quantity":10}

#     ]
# }







class OrdersView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            customer_id = request.data.get("customer_id")
            orders = request.data.get("orders", [])
            payment_mode = request.data.get("payment_mode", "").lower()

            if not customer_id or not orders or not payment_mode:
                return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

            if payment_mode not in PaymentMode.values:
                return Response({
                    "error": f"Invalid payment mode. Must be one of: {list(PaymentMode.values)}"
                }, status=status.HTTP_400_BAD_REQUEST)

            # Fetch products once
            product_ids = [item.get("product_id") for item in orders]
            products_queryset = Products.objects.filter(id__in=product_ids)
            products_dict = {product.id: product for product in products_queryset}

            total_bill = 0
            total_products_ordered = 0
            transaction_items = []

            for item in orders:
                product_id = item.get("product_id")
                quantity = item.get("quantity")

                if not product_id or not quantity:
                    return Response({"error": "Each order must include 'product_id' and 'quantity'."}, status=status.HTTP_400_BAD_REQUEST)

                product = products_dict.get(product_id)
                if not product:
                    return Response({"error": f"Product ID {product_id} not found."}, status=status.HTTP_404_NOT_FOUND)

                if quantity > product.stock:
                    return Response({
                        "error": f"Not enough stock for {product.name} (Available: {product.stock})"
                    }, status=status.HTTP_400_BAD_REQUEST)

                # Reduce stock
                product.stock -= quantity
                total_bill += product.price * quantity
                total_products_ordered += 1

                # Prepare item entry
                transaction_items.append((product, quantity))

            # Save stock
            for product in products_dict.values():
                product.save()

            # Save transaction
            transaction = Transaction.objects.create(
                customer_id=customer_id,
                total_products=total_products_ordered,
                total_price=total_bill,
                transaction_mode=payment_mode
            )

            # Save related products in intermediate model
            for product, quantity in transaction_items:
                TransactionItem.objects.create(
                    transaction=transaction,
                    product=product,
                    quantity=quantity
                )

            return Response({
                "transaction_id": transaction.id,
                "message": "Purchase successful",
                "total_price": total_bill
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)









class OrderSummaryView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, customer_id):
        transaction_queryset = Transaction.objects.filter(customer_id=customer_id)
        order_summary = []
        total_spent = 0
        total_orders = len(transaction_queryset)

        for order in transaction_queryset:
            items = TransactionItem.objects.filter(transaction=order)
            product_list = []

            for item in items:
                product = item.product
                product_list.append({
                    "product_id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "quantity": item.quantity,
                    "subtotal": product.price * item.quantity
                })

            order_details = {
                "transaction_id": order.id,
                "total_price": order.total_price,
                "payment_mode": order.transaction_mode,
                "total_products": order.total_products,
                "products": product_list
            }

            order_summary.append(order_details)
            total_spent += order.total_price

        return Response({
            "order_summary": order_summary,
            "total_orders": total_orders,
            "total_spent": total_spent
        })







# class OrderSummaryView(APIView):
#     permission_classes = [permissions.AllowAny]

#     def get(self,request,customer_id):
#         transaction_queryset = Transaction.objects.filter(customer_id=customer_id)            
#         order_summary = []
#         total_spent = 0
#         total_orders = len(transaction_queryset)

#         for order in transaction_queryset:
#             order_details = {
#                 "transaction_id": order.id,
#                 "total_price": order.total_price,
#                 "payment_mode": order.transaction_mode,
#                 "total_products": order.total_products,
#             }
#             order_summary.append(order_details)
#             total_spent += order.total_price

#         return Response({
#             "order_summary": order_summary,
#             "total_orders": total_orders,
#             "total_spent": total_spent
#         })



