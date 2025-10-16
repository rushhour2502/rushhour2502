from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from . import views

class ProfileView(View):
    def get(self, request):
        user = request.user  # Get the currently logged-in user
        return render(request, 'profile.html', {'user': user})

    def post(self, request):
        # Handle form submissions (e.g., update profile)
        pass

print("ProfileView class defined successfully.")

# simple function view
def hello_view(request):
    return HttpResponse("Hello, Django!")


urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('hello/', views.hello_view, name='hello'),
]