from msilib.schema import AdminExecuteSequence
from django.urls import path
from django.urls import path, include
from . import views
from .views import submit_form

urlpatterns = [
   # path('admin/', AdminExecuteSequence.site.urls),

#    path('members/', views.members, name='members'),
    path('api/submit-form/', views.submit_form, name='submit-form')
]