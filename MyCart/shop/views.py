import razorpay
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4 + ceil((n/4)-n//4)
        allProds.append([prod,range(1,nSlides), nSlides])
    params={'allProds':allProds}
    return render(request,'shop/index.html',params)
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    thank=False
    if request.method=='POST':

        name=request.POST.get('name','')
        email = request.POST.get('email', '')
        phone = request.POST.get('number', '')
        query = request.POST.get('query', '')
        contact=Contact(name=name,email=email, phone=phone, query=query)
        thank=True
        contact.save()
    return render(request, 'shop/contact.html',{'thank':thank})
def tracker(request):
    if(request.method=="POST"):
        orderId=request.POST.get('orderId','')
        email=request.POST.get('email','')
        try:
            order=Orders.objects.filter(order_id=orderId,email=email)
            if(len(order)>0):
                update=OrderUpdate.objects.filter(order_id=orderId)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response=json.dumps([updates,order[0].items_json],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'shop/tracker.html')

def productView(request,myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/productview.html',{'product': product[0]})

def search(request):
    return render(request, 'shop/search.html')

def checkout(request):
    if request.method=='POST':
        itemsJson=request.POST.get('itemsJson','')
        name=request.POST.get('name','')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address1', '')+" "+request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip', '')
        amount=request.POST.get('amount','')

        order=Orders(items_json=itemsJson,amount=amount,name=name,email=email, phone=phone, address=address, city=city, state=state, zip_code=zip_code)

        order.save()
        update=OrderUpdate(order_id=order.order_id,update_desc="Your Order has been placed")
        update.save()
        thank=True
        id = order.order_id;
        order_amount = order.amount

        client=razorpay.Client(auth=('rzp_test_KKeqcQjexEYfMv','tS1XP8FRqRzF2zdoFvok7Bx6'))
        payment=client.order.create({'amount':order_amount, 'currency':'INR', 'payment_capture': '1'})

        return render(request, 'shop/razorpay.html',)
    return render(request, 'shop/checkout.html')

@csrf_exempt
def handlerequest(request):
   pass
