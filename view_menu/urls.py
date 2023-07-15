# # from django.urls import path
# # from . import views
# # from django.conf import settings
# # from django.conf.urls.static import static
# from .views import page_not_found, permission_denied, breakfast
# # from django.views.generic import TemplateView



# # app_name = 'view_menu'

# # urlpatterns = [
# #     path('menu/', views.menu, name="menu"),   
# #     path('breakfast/', views.breakfast, name="breakfast"),
# #     path('lunch/', views.lunch, name="lunch"),
# #     path('dinner/', views.dinner, name="dinner"),
# #     path('side/', views.side, name="side"),
# #     #path('create-menu/', views.create_menu, name='create_menu'),
# #    # path('delete-menu/', views.create_menu, name='delete_menu'),
# #     path('view_menu/edit/<int:pk>/', views.EditMenuView.as_view(), name='edit_menu'),
# #     path('view_menu/manage_menu/', views.manage_menu, name='manage_menu'),
# #     path('view_menu/delete/<int:pk>/', views.DeleteMenuView.as_view(), name='delete_menu'),
# #     path('view_menu/create-menu/includes/403/', TemplateView.as_view(template_name='includes/403.html'), name='403'),
    
# #     path('page_not_found/', page_not_found, name='page_not_found')
    
# # ]
# # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# # from django.urls import path
# # from . import views

# # app_name = 'view_menu'

# # urlpatterns = [
# #     # Other URL patterns...

# #     # Edit Menu
# #     path('menu/edit/<int:pk>/', views.EditMenuView.as_view(), name='edit_menu'),

# #     # Delete Menu
# #     path('menu/delete/<int:pk>/', views.DeleteMenuView.as_view(), name='delete_menu'),
# # ]



# from django.urls import path
# #from . import views
# from django.conf import settings
# from django.conf.urls.static import static
# from django.views.generic import TemplateView
# from django.shortcuts import render
# #from .models import View_Menu
#  #from django.urls import path
# from . import views
# # from django.conf import settings
# # from django.conf.urls.static import static
# from django.urls import path
# #from view_menu import view
# #from view_menu.views import edit_menu




# app_name = 'view_menu'

# urlpatterns = [
#     path('menu/', views.menu, name="menu"),   
#     path('breakfast/', views.breakfast, name="breakfast"),
#     path('lunch/', views.lunch, name="lunch"),
#     path('dinner/', views.dinner, name="dinner"),
#     path('side/', views.side, name="side"),
#     path('create-menu/', views.create_menu, name='create_menu'),

#     path('menu/delete/<int:menuitem_id>/', views.delete_menu_item, name='delete_menu_item'),
#     path('menu/edit/<int:menuitem_id>/', views.edit_menu_item, name='edit_menu_item'),

#     #path('edit_menu/<menuitem_id>/', views.EditMenuView.as_view(), name='edit_menu'),
#     path('manage_menu/', views.manage_menu, name='manage_menu'),
#    # path('delete/<int:pk>/', views.DeleteMenuView.as_view(), name='delete_menu'),
#     path('create-menu/includes/403/', TemplateView.as_view(template_name='includes/403.html'), name='403'),
#     #path('update/<menuitem_id>/', views.update_menu, name='update_menu'),
#    # path('edit/<int:menuitem_id>/', views.edit_menu, name='edit_menu'),
#     path('page_not_found/', views.page_not_found, name='page_not_found')
# ]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


