from django.contrib import admin
from django.urls import path
from userform_app import views
from userform_app.views import user_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user-form/', views.user_form, name='user_form'),
]
