from django.urls import path
from .views import *

urlpatterns = [
    path('invoice_list/', InvoiceList.as_view(), name="invoice_list"),
    path('invoice_create/', InvoiceCreate.as_view(), name="invoice_create"),
    path('invoice_detail/<int:id>/', InvoiceDetail.as_view(), name="invoice_detail"),
    path('invoice_update/<int:id>/', InvoiceUpdate.as_view(), name="invoice_update"),
    path('invoice_delete/<int:id>/', InvoiceDelete.as_view(), name="invoice_delete"),


    path('customer_list/', CustomerList.as_view(), name="customer_list"),
    path('customer_create/', CustomerCreate.as_view(), name="customer_create"),
    path('customer_update/<int:id>/', CustomerUpdate.as_view(), name="customer_update"),
    path('customer_delete/<int:id>/', CustomerDelete.as_view(), name="customer_delete"),

    path('payment_list/', PaymentList.as_view(), name="payment_list"),
    path('payment_create/', PaymentCreate.as_view(), name="payment_create"),
    path('payment_update/<int:id>/', PaymentUpdate.as_view(), name="payment_update"),
    path('payment_delete/<int:id>/', PaymentDelete.as_view(), name="payment_delete"),

]