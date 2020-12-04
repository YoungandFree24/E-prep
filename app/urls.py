from django.urls import path
from . import views

# index is always the root route
urlpatterns = [
	path('', views.index),
    path('register',views.register),
    # rule of thumb, when sending form or post data to a route in server ,you must redirect
    path('dashboard', views.dashboard),
    path('login', views.login),
    path('logout', views.logout),
    path('delete_quote/<int:quote_id>', views.delete_quote),
    path('create_quote',views.create_quote),
    path('edit_user', views.edit_user),
    path('update_user',views.update_user),
    path('show_user/<int:user_id>',views.show_user),
    
]