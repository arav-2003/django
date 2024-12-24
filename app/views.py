from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import UserDetailForm
from .models import UserDetail

# Create your views here.

def say(request):
    return render(request,'welcome.html')

def user_details(request):
    if request.method == 'POST':
        form = UserDetailForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('user_details')  # Redirect to the same page to refresh the list
    else:
        form = UserDetailForm()

    # Fetch all the user details from the database
    user_details = UserDetail.objects.all()

    # Handle remove button action
    if 'remove' in request.POST:
        user_id = request.POST.get('user_id')
        if user_id:
            UserDetail.objects.filter(id=user_id).delete()  # Delete the user details with the given ID
            return redirect('user_details')  # Refresh the page after deletion

    return render(request, 'user_details.html', {'form': form, 'user_details': user_details})