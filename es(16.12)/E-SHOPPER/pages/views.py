from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from product.models import Product
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


def index(request):
    product = Product.objects.order_by("-list_date").filter(is_published=True)
    # product = Product.objects.all()
    paginator = Paginator(product, 12)
    page = request.GET.get("page")
    product_per_page = paginator.get_page(page)
    context = {
        "products": product_per_page
    }
    return render(request, 'pages/index.html', context)


def contact(request):
    return render(request, 'pages/contact.html')


def login(request):
    return render(request, 'pages/login.html')


def page_not_found(request):
    return render(request, 'pages/page_not_found.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'User logged in')
            messages.error(request, 'error test')
            messages.warning(request, 'warning test')

            return redirect('dashboard')
        else:
            messages.error(request, 'Incorrect login or password')
            return redirect('login')

    return render(request, 'pages/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "Logged out")
    return redirect('index')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        passwordConfirm = request.POST['passwordConfirm']

        user_condition = not User.objects.filter(username=username).exists()
        password_condition = password == passwordConfirm
        email_condition = not User.objects.filter(email=email).exists()

        if user_condition and password_condition and email_condition:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )
            user.save()
            messages.success(request, 'User registered')
            return redirect('login')
        else:
            if not user_condition:
                messages.error(request, "User with login '" +
                               username + "' exists")
            if not password_condition:
                messages.error(request, "Passwords do not match")
            if not email_condition:
                messages.error(request, "User with email '"+email+"' exists")
            return redirect("register")

    return render(request, 'pages/register.html')


def dashboard(request):
    return render(request, "pages/dashboard.html")


def cart(request):
    if request.method == 'POST':
        
        product_title =   request.POST['title']
        product_price =   request.POST['price']
        # product_sale =   request.POST['sale']
        send_mail(
            'New Order',
            'There has been an inquiry for ' + product_title +
            '. ', "Price " + product_price +
            'testsendpython2@gmail.com',
            ["andrijmaticak@gmail.com", 'andrijmaticak@gmail.com'],
            fail_silently=False
        )

        messages.success(
            request, 'Your request has been submitted, a realtor will get back to you soon')
        
        return render(request, 'pages/dashboard.html')
    else:
        return render(request, 'pages/cart.html')
