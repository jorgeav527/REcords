from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import AccountRegister, AccountUpdateForm, ProfileUpdateForm
from .models import Profile
from quote.models import Quote

# Account views.

def home_account_view(request):
    query = Quote.objects.all()
    query_most_recent = query.order_by("-updated_quote")[:3]

    context = {
        "object_list": query_most_recent,
    }

    return render(request, 'info/home.html', context)


def about_account_view(request):
    query = Quote.objects.all()
    query_most_recent = query.order_by("?")[:3]

    context = {
        "object_list": query_most_recent,
    }

    return render(request, 'info/about.html', context)


def contact_account_view(request):
    return render(request, 'info/contact.html')


def register(request):
    if request.method == "POST":
        form = AccountRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for { username }")
            return redirect('login')
    else:
        form = AccountRegister()
    context = { "form": form }
    return render(request, 'account/register.html', context)


@login_required
def profile(request):
    queryset_quote = Quote.objects.all()
    queryset_users = Profile.objects.all()
    if request.method == "POST":
        account_form = AccountUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if account_form.is_valid() and profile_form.is_valid():
            account_form.save()
            profile_form.save()
            messages.success(request, f"Account has been updated")
            return redirect('account-profile')

    else:
        account_form = AccountUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        

    context = {
        "object_list": queryset_users,
        "queryset_quote": queryset_quote,
        "account_form": account_form,
        "profile_form": profile_form,
    }

    return render(request, 'account/profile.html', context)


def delete_user(request, username):
    if request.method == "POST":
        u = User.objects.get(username=username)
        u.delete()
        messages.success(request, f"Account has been deleted")
        return redirect('account-home')
        
    return render(request, 'account/account_confirm_delete.html') 
