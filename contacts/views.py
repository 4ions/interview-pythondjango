from django.shortcuts import render, redirect
from contacts.forms import UsersForm, AddCompanyForm
from contacts.models import Users, Enterprise
from django.views.generic import ListView

# Create your views here.
def index(request):
    return redirect("/emp/")

def emp(request):
    if request.method == "POST":
        form = UsersForm(request.POST)
        print(form)
        if (form.is_valid()):
            try:
                form.save()
                return redirect('/view')
            except:
                pass
    else:
        form = UsersForm()
    return render(request, 'index.html', {'form':form})

def view(request):
    users = Users.objects.all()
    return render(request,"users_list.html",{'users':users})

def delete(request, id):
    users = Users.objects.get(id=id)
    users.delete()
    return redirect("/view")

def edit(request, id):
    users = Users.objects.get(id=id)
    return render(request,'edit.html',{'users':users})

def update(request, id):
    users = Users.objects.get(id=id)
    users.name = request.POST.get('name')
    users.lastname = request.POST.get('lastname')
    users.email = request.POST.get('email')
    users.save()
    print(request.POST.get('name'))
    print(users.email)
    return redirect("/view")


def add_sale(request):
    print(id)
    if request.method == "POST":
        form = AddCompanyForm(request.POST)
        print(form)
        if (form.is_valid()):
            try:
                form.save()
                return redirect('/view')
            except:
                pass
    else:
        form = AddCompanyForm()
    return render(request, 'add_sale.html', {'form':form})

def viewsales(request):
    enters = Enterprise.objects.all()
    return render(request,"sales_list.html",{'enters':enters})

def delete_sale(request, id):
    enter = Enterprise.objects.get(id=id)
    enter.delete()
    return redirect("/totalsales")

