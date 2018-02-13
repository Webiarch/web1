from django.shortcuts import render, redirect
from django.views import View
from .models import Customer

def CustomerDelete(request, user_id):
    Customer.objects.get(id=user_id).delete()
    return redirect("../../customer")

def CustomerEdit(reuest,user_id):

    edit_data = Customer.objects.get(pk=user_id)
    return render(reuest, 'Customer.html', locals())


class CustomerList(View):

    template = 'Customer.html'

    def get(self, request):
        data = Customer.objects.all()
        return render(request, self.template, locals())

    def post(self, request):
        if request.method == 'POST':
            if 'txtSubmit' in request.POST:
                Customer_name = request.POST.get("txtName", None)
                Price = request.POST.get("txtPrice", None)
                Amount= request.POST.get("txtAmount", None)
                insert_record = Customer(Customer_name=Customer_name, Price=Price, Amount=Amount)
                insert_record.save()
                return redirect("../customer")

            elif 'txtUpdate' in request.POST:
                id_ = request.POST.get("txtid", None)
                edit_customer = Customer.objects.get(pk=id_)
                edit_customer.Customer_name = request.POST.get("txtName", None)
                edit_customer.Amount = request.POST.get("txtAmount", None)
                edit_customer.Price = request.POST.get("txtPrice", None)
                edit_customer.save()
                return redirect("../customer")







