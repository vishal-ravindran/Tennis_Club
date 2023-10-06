from django.urls import path

from. import views

urlpatterns=[
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('', views.main, name='home'),
    path('testing/', views.testing, name='testing'),
    path('form/', views.show_form, name='form'),
    path('add_member/', views.add_member, name='add_member'),
    path('delete_member/<int:id>/', views.delete_member, name='delete_member'),
    path('edit_member/<int:id>/', views.edit_member, name='edit_member'),
    # path('delete_confirmation/<int:id>/', views.delete_confirmation, name='delete_confirmation'),
]