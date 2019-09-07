from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template import RequestContext
from django.views.generic import ( 
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView,
)
from django.contrib import messages
from django.urls import reverse

from .models import Quote, Comment
from .forms import CommentForm, QuoteForm


# Account views.

def quote_list_view(request):
    queryset = Quote.objects.all()
    queryset_order_created = queryset.order_by("-created_quote")

    paginator = Paginator(queryset_order_created, 6) 
    page = request.GET.get('page')
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages) 

    context = {
        "object_list": paginated_queryset,
    }

    return render(request, 'quote/quote_list.html', context)


@login_required
def account_list_view(request):
    queryset = Quote.objects.order_by("-created_quote")
    queryset_user = queryset.filter(author=request.user)
   
    paginator = Paginator(queryset_user, 6) 
    page = request.GET.get('page')
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages) 

    context = {
        "object_list": paginated_queryset,
    }
    return render(request, 'quote/account_quote_list.html', context)


@login_required
def quote_detail_view(request, id):
    quote = get_object_or_404(Quote, id=id)
    comments = quote.comments.all() # == quote.comment_set.all()
    
    comment_form = CommentForm(request.POST or None)
    if request.method == "POST":
        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment_form.instance.quote = quote
            comment_form.save()
            return redirect(reverse("quote-detail", kwargs={
                'id': quote.id
            }))
    
    else:
        comment_form = CommentForm()
    
    context = { 
        "quote": quote,
        "comments": comments,
        "comment_form": comment_form,
    }
    return render(request, 'quote/quote_detail.html', context)


def search(request):
    queryset = Quote.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(quote__icontains=query) |
            Q(author_quote__icontains=query)
        ).distinct()

    paginator = Paginator(queryset, 6) 
    page = request.GET.get('page')
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages) 

    context = {
        "object_list": paginated_queryset,
    }

    return render(request, 'quote/search_results.html', context)

@login_required    
def quote_create_view(request):
    form = QuoteForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            quote = form.cleaned_data.get("quote")
            author_quote = form.cleaned_data.get("author_quote")
            messages.success(request, f"The quote \"{ quote }\" by \"{ author_quote }\" has been created")
            return redirect(reverse("quote-detail", kwargs={
                'id': form.instance.id
            }))

    context = {
        "form": form
    }

    return render(request, "quote/quote_form.html", context)


@login_required
def edit_comment(request, id_quote, id_comment):
    quote = get_object_or_404(Quote, id=id_quote)
    comment = get_object_or_404(Comment, id=id_comment)
    comment_form_update = CommentForm(request.POST or None, instance=comment)
    if request.method == "POST":
        if comment_form_update.is_valid():
            comment_form_update.instance.user = request.user
            comment_form_update.instance.quote = quote
            comment_form_update.save()
            messages.success(request, f"The comment has been updated")
            return redirect("quote-detail", id_quote)

    context = { "comment_form_update": comment_form_update }

    return render(request, 'comment/edit_comment.html', context)

@login_required
def delete_comment(request, id_quote, id_comment):
    quote = get_object_or_404(Quote, id=id_quote)
    comment = get_object_or_404(Comment, id=id_comment)
    comment.delete()
    messages.success(request, f"The comment has been deleted")
    
    return redirect("quote-detail", id_quote)


@login_required
def quote_update_view(request, id):
    quote = get_object_or_404(Quote, id=id)
    form = QuoteForm(request.POST or None, instance=quote)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, f"The quote \"{ quote.quote }\" by \"{ quote.author_quote }\" has been updated")
            return redirect(reverse('quote-detail', kwargs={
                'id': form.instance.id
            }))
    context = {
        'form': form,
    }
    return render(request, 'quote/quote_update.html', context)

@login_required
def quote_delete_view(request, id):
    quote = get_object_or_404(Quote, id=id)
    if request.method == "POST":
        quote.delete()
        messages.success(request, f"The quote \"{ quote.quote }\" by \"{ quote.author_quote }\" has been deleted")
        return redirect('quotes-home')

    context = {
        "object": quote,
    }

    return render(request, 'quote/quote_confirm_delete.html', context)