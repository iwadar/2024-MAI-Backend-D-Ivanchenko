from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])

def listCheese(request):
    return JsonResponse({'info': 'Soon there will be a list of cheeses available for purchase'})

def purchaseHistory(request):
    return JsonResponse({'info': 'Your purchase history will be here soon'})

def order(request):
    return JsonResponse({'info': 'You will soon be able to place your order here'})

def profile(request):
    return JsonResponse({'info': 'This is your future profile'})

def welcomeToFactory(request):
    return JsonResponse({'info': 'Hello! This is a cheese factory website where you can buy delicious cheese!'})