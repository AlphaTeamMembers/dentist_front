import requests as req
from django.contrib import messages
from django.db.models import Count

from django.urls import reverse

from app.forms import SendAppointmentForm, SignUpForm, ContactForms, CommentForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Blog, About, Comment, Contact
from django.views import View




class Home_view(View):
    def get(self, request):
        forms = SendAppointmentForm()
        return render(request, 'index.html', {'forms': forms})

    def post(self, request):
        token = "6396978493:AAHuEJdpjRA446MD15dUNp3V_fgqe8O8AaU"
        chat_id = "1091980088"
        method = 'sendMessage'
        url_req = f"https://api.telegram.org/bot{token}/{method}"
        forms = SendAppointmentForm(request.POST)
        if request.method == "POST":
            forms = SendAppointmentForm(request.POST)
            if forms.is_valid():
                a_user = forms.save()
                message = f"""
👨‍🦰Fullname: {a_user.fullname}
📧Email: {a_user.email}
📞 Aloqa: {a_user.phone}
🕔Vaqti: {a_user.time}
✍️Xabar: {a_user.message}
                """
                req.post(url=url_req, data={'chat_id': chat_id, 'text': message})
                return redirect('home')
        return render(request, 'index.html', {'forms': forms})


def about_view(request):
    posts = About.objects.filter(is_published=True)
    context = {
        'posts': posts
    }
    return render(request, 'about.html', context)


class services_view(View):
    def get(self, request):
        forms = SendAppointmentForm()
        return render(request, 'services.html', {'forms': forms})

    def post(self, request):
        token = "6396978493:AAHuEJdpjRA446MD15dUNp3V_fgqe8O8AaU"
        chat_id = "1091980088"
        method = 'sendMessage'
        url_req = f"https://api.telegram.org/bot{token}/{method}"
        forms = SendAppointmentForm(request.POST)
        if request.method == "POST":
            forms = SendAppointmentForm(request.POST)
            if forms.is_valid():
                a_user = forms.save()
                message = f"""
👨‍🦰Fullname: {a_user.fullname}
📧Email: {a_user.email}
📞 Aloqa: {a_user.phone}
🕔Vaqti: {a_user.time}
✍️Xabar: {a_user.message}
                """
                req.post(url=url_req, data={'chat_id': chat_id, 'text': message})
                return redirect('home')
        return render(request, 'services.html', {'forms': forms})


def pricing_view(request):
    return render(request, 'pricing.html')


def blog_view(request):
    posts = Blog.objects.filter(is_published=True)
    post = Blog.objects.get(id=1)
    reviews = post.comment_set.all()
    count = post.comment_set.all().count()
    context = {
        'posts': posts,
        'count':count
    }
    return render(request, 'blog.html', context)


class blog_single_view(View):
    def get(self, request, pk):
        post = Blog.objects.get(pk=pk)
        reviews = post.comment_set.all()
        count = post.comment_set.all().count()
        forms = CommentForm()
        return render(request, 'blog-single.html', {'post': post, 'forms': forms,'comments':reviews,'count':count})

    def post(self, request, pk):
        post = Blog.objects.get(pk=pk)
        user = request.user.profile
        forms = CommentForm(data=request.POST)
        if forms.is_valid():
            blog_id = forms.save(commit=False)
            blog_id.user = user
            blog_id.blog = post
            forms.save()
            messages.success(request, 'You have successfully create comment')
            return redirect(reverse("blog_detail", kwargs={"pk": post.pk}))
        return render(request, 'blog-single.html', {'forms': forms, 'post': post})


class contact_view(View):
    def get(self, request):
        forms = ContactForms()
        return render(request, 'contact.html', {'forms': forms})

    def post(self, request):
        forms = ContactForms(data=request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
        return render(request, 'contact.html', {'forms': forms})


class Signup_view(View):
    def get(self, request):
        forms = SignUpForm()
        return render(request, 'signup.html', {'forms': forms})

    def post(self, request):
        forms = SignUpForm()
        if request.method == 'POST':
            forms = SignUpForm(data=request.POST)
            if forms.is_valid():
                forms.save()
                return redirect('login')
        return render(request, 'signup.html', {'forms': forms})


class signin_view(View):
    def get(self, request):

        return render(request, "signin.html")

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(username,password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'You have successfully logged in')
                return redirect('home')
                # Redirect to a success page.
            elif request.user.is_authenticated():
                return render(request, 'signin.html', {'error': 'This user is authenticated .'})
            else:
                return render(request, 'signin.html', {'error': 'This user is not active.'})
        else:
            return render(request, 'signin.html', {'error': 'Invalid username or password.'})

        # return render(request, "signin.html")

def user_profile(request):
    profile = request.user.profile
    return render(request,'profile.html',{'profile':profile})
