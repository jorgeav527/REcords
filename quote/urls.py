from django.urls import path

from . import views

# Quote urls 

urlpatterns = [
    path('quotes/', views.quote_list_view, name='quotes-home'),    
    path('quotes/my-quotes/', views.account_list_view , name='account-quotes-home'),    
    # Search
    path('quotes/search/', views.search , name='search'),    
    # quote > comments
    path('quote/<int:id>/', views.quote_detail_view, name='quote-detail'),
    path('quote/<int:id_quote>/comment/<int:id_comment>/edit/', views.edit_comment, name='edit-comment'),
    path('quote/<int:id_quote>/comment/<int:id_comment>/delete/', views.delete_comment, name='delete-comment'),
    # crud quote
    path('quote/create/', views.quote_create_view, name='quote-create'),    
    path('quote/<int:id>/update/', views.quote_update_view, name='quote-update'),    
    path('quote/<int:id>/delete/', views.quote_delete_view, name='quote-delete'),    
]