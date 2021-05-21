from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.shortcuts import redirect, HttpResponse
from .tasks import create_random_user_accounts
        

def index(request):
    create_random_user_accounts.delay(100000)
    return HttpResponse('created 20 users successfully.')
