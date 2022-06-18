from django.shortcuts import render

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import View, CreateView, DeleteView, UpdateView
from .models import *



class InvoiceList(ListView):
    model = Invoice
    paginate_by = 2
    context_object_name = 'invoices'

    def get(self, request, *args, **kwargs):
        keyword = request.GET.get('keyword')
        if keyword:
            products = Invoice.objects.filter(inv_no__contains=keyword)
            return render(request, "invoice/invoice_list.html", {'invoices': products})
        return super(InvoiceList, self).get(request, *args, **kwargs)


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['soldProducts'] = SoldProduct.objects.all()


        context['payments'] = Payment.objects.all()
        product_list = Invoice.objects.all()
        paginator = Paginator(product_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            file_products = paginator.page(page)
        except PageNotAnInteger:
            file_products = paginator.page(1)
        except EmptyPage:
            file_products = paginator.page(paginator.num_pages)
        context['invoices'] = file_products
        return context

    template_name = 'invoice/invoice_list.html'




class InvoiceDetail(DetailView):
    pk_url_kwarg = 'id'
    model = Invoice
    context_object_name = 'invoice'
    template_name = 'invoice/invoice_detail.html'




class InvoiceCreate(CreateView):
    model = Invoice
    fields = '__all__'
    context_object_name = 'invoice'
    template_name = 'invoice/invoice_update.html'
    success_url = reverse_lazy('invoice_list')


class InvoiceUpdate(UpdateView):
    pk_url_kwarg = 'id'
    model = Invoice
    fields = '__all__'
    context_object_name = 'invoice'
    template_name = 'invoice/invoice_update.html'
    success_url = reverse_lazy('invoice_list')


class InvoiceDelete(DeleteView):
    pk_url_kwarg = 'id'
    model = Invoice
    context_object_name = 'invoice'
    template_name = 'invoice/invoice_update.html'
    success_url = reverse_lazy('invoice_list')













class CustomerList(ListView):
    model = Customer
    paginate_by = 10
    context_object_name = 'customers'


    def get(self, request, *args, **kwargs):
        keyword = request.GET.get('keyword')
        if keyword:
            products = Customer.objects.filter(name__contains=keyword)
            return render(request, "customer/customer_list.html", {'customers': products})
        return super(CustomerList, self).get(request, *args, **kwargs)


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['soldProducts'] = SoldProduct.objects.all()


        context['payments'] = Payment.objects.all()
        product_list = Customer.objects.all()
        paginator = Paginator(product_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            file_products = paginator.page(page)
        except PageNotAnInteger:
            file_products = paginator.page(1)
        except EmptyPage:
            file_products = paginator.page(paginator.num_pages)
        context['customers'] = file_products
        return context

    template_name = 'customer/customer_list.html'




class CustomerDetail(DetailView):
    pk_url_kwarg = 'id'
    model = Customer
    context_object_name = 'customer'
    template_name = 'customer/customer_detail.html'




class CustomerCreate(CreateView):
    model = Customer
    fields = '__all__'
    context_object_name = 'customer'
    template_name = 'customer/customer_update.html'
    success_url = reverse_lazy('customer_list')


class CustomerUpdate(UpdateView):
    model = Customer
    pk_url_kwarg = 'id'
    fields = '__all__'
    context_object_name = 'customer'
    template_name = 'customer/customer_update.html'
    success_url = reverse_lazy('customer_list')


class CustomerDelete(DeleteView):
    pk_url_kwarg = 'id'
    model = Customer
    context_object_name = 'customer'
    template_name = 'customer/customer_delete.html'
    success_url = reverse_lazy('customer_list')
















class PaymentList(ListView):
    model = Payment
    paginate_by = 10
    context_object_name = 'payments'


    def get(self, request, *args, **kwargs):
        keyword = request.GET.get('keyword')
        if keyword:
            products = Payment.objects.filter(customer__name__contains=keyword)
            return render(request, "payment/payment_list.html", {'payments': products})
        return super(PaymentList, self).get(request, *args, **kwargs)


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['soldProducts'] = SoldProduct.objects.all()

        context['payments'] = Payment.objects.all()
        product_list = Payment.objects.all()
        paginator = Paginator(product_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            file_products = paginator.page(page)
        except PageNotAnInteger:
            file_products = paginator.page(1)
        except EmptyPage:
            file_products = paginator.page(paginator.num_pages)
        context['payments'] = file_products
        return context

    template_name = 'payment/payment_list.html'




class PaymentDetail(DetailView):
    pk_url_kwarg = 'id'
    model = Payment
    context_object_name = 'payment'
    template_name = 'payment/payment_list.html'




class PaymentCreate(CreateView):
    model = Payment
    fields = '__all__'
    context_object_name = 'payment'
    template_name = 'payment/payment_update.html'
    success_url = reverse_lazy('payment_list')


class PaymentUpdate(UpdateView):
    pk_url_kwarg = 'id'
    model = Payment
    fields = '__all__'
    context_object_name = 'payment'
    template_name = 'payment/payment_update.html'
    success_url = reverse_lazy('payment_list')


class PaymentDelete(DeleteView):
    model = Payment
    pk_url_kwarg = 'id'
    context_object_name = 'payment'
    template_name = 'payment/payment_delete.html'
    success_url = reverse_lazy('payment_list')












