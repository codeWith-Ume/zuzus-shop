from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from .models import Order,Contact


# Create your views here.
def index(request):
    context = {
        "variable":"this is sent"
    }
    return render(request,'index.html',context)
    # return HttpResponse("This is my homepage")

def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is my aboutpage")

def services(request):
    return render(request,'services.html')
    # return HttpResponse("THis is my servicepage")

def contact(request):
    return render(request,'contact.html')
    # return HttpResponse("this is my contact page")

def shop(request):
    return render(request,'shop.html')

products = {
    1: {"name": "Classic Teddy Bear", "price": 499},
    2: {"name": "Lovely Bunny", "price": 349},
    3: {"name": "Cute Panda", "price": 599},
    4: {"name": "Baby Elephant", "price": 449},
    5: {"name": "Playful Monkey", "price": 399},
    6: {"name": "Fluffy Kitty", "price": 299},
    7: {"name": "Little Puppy", "price": 399},
    8: {"name": "Little Lion", "price": 549},
    9: {"name": "Yellow Duck", "price": 249},
    10: {"name": "Magic Unicorn", "price": 699},
    11: {"name": "Happy Frog", "price": 329},
    12: {"name": "Sleepy Koala", "price": 499},
}


def buy_now(request, product_id):
    product = products.get(product_id)

    if product is None:
        from django.http import Http404
        raise Http404("Product not found")

    if request.method == "POST":
        name = request.POST.get("customer_name", "").strip()
        phone = request.POST.get("phone", "").strip()
        address = request.POST.get("address", "").strip()

        try:
            quantity = int(request.POST.get("quantity", 1))
        except (ValueError, TypeError):
            quantity = 0

        if (
            not name
            or not phone
            or not address
            or not phone.isdigit()
            or not 1 <= len(phone) <= 15
            or not 1 <= quantity <= 100
        ):
            return render(request, "buy_now.html", {
                "product": product,
                "product_id": product_id,
                "error": "Please enter valid details and a quantity between 1 and 100."
            })

        Order.objects.create(
            product_name=product["name"],
            price=product["price"],
            customer_name=name,
            phone=phone,
            address=address,
            quantity=quantity,
        )

        return redirect("order_success")

    return render(request, "buy_now.html", {
        "product": product,
        "product_id": product_id,
    })


def order_success(request):
    return render(request, "order_success.html")


def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message")
        )
        return redirect("contact")

    return render(request, "contact.html")
