from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from cheeseFactory.models import *
import json
from datetime import datetime

_UNDEFINED_ID = -1
_UNDEFINED_STR = ''

def cheeseDeserialized(listCheeses):
    for i, cheese in enumerate(listCheeses):
        listCheeses[i] = {
            'Артикул': cheese.vendor_code,
            'Название': cheese.name,
            'Описание': cheese.description,
            'Цена за 1 кг': cheese.price,
            'Осталось в продаже (кг)': cheese.left,
        }
    return listCheeses

@csrf_exempt
@require_GET
def listCheese(request):
    list_cheese = list(Cheese.objects.all())
    return JsonResponse({'Список сыров': cheeseDeserialized(list_cheese)})
    # return JsonResponse({'info': 'Soon there will be a list of cheeses available for order'})


@csrf_exempt
@require_GET
def cheese(request):
    if (_id := request.GET.get("vendor_code", _UNDEFINED_ID)) == _UNDEFINED_ID:
        list_cheese = list(Cheese.objects.all())
    else:
        list_cheese = list(Cheese.objects.filter(vendor_code=_id))
    
    return JsonResponse({'Сыры': cheeseDeserialized(list_cheese)})
    # return JsonResponse({'info': f'Soon there will be information about cheese with article {request.GET.get("id", -1)}'})


def orderDeserialized(listOrders):
    for i, order in enumerate(listOrders):
        cheeses_in_order = List_cheese.objects.filter(order=order.id)
        listOrders[i] = {
            'Номер заказа': order.id,
            'Дата заказа': order.data_order,
            'Пользователь': f'{order.user.name} {order.user.secondName}',
            'Список заказа': [f'{cheese.cheese.name} ..... {cheese.quantity} кг' for cheese in cheeses_in_order],
            'Итого': order.total,
        }
    return listOrders


@csrf_exempt
@require_GET
def orderHistory(request):
    list_orders = list(Order.objects.all())
    return JsonResponse({'Заказы': orderDeserialized(list_orders)})
    return JsonResponse({'info': 'Your order history will be here soon'})


@csrf_exempt
@require_GET
def order(request):
    if (_id := request.GET.get("id", _UNDEFINED_ID)) == _UNDEFINED_ID:
        list_orders = list(Order.objects.all())
    else:
        list_orders = list(Order.objects.filter(id=_id))
    
    return JsonResponse({'Заказы': orderDeserialized(list_orders)})
    return JsonResponse({'info': 'You will soon be able to place your order here'})


@csrf_exempt
@require_GET
def profile(request):
    user = None
    if (_id := request.GET.get("id", _UNDEFINED_ID)) != _UNDEFINED_ID:
        try:
            user = User.objects.get(id=_id)
        except User.DoesNotExist:
            user = None
    if user:
        responce = {'Имя': user.name, 'Фамилия': user.secondName, 'Телефон': user.phone}    
        return JsonResponse(responce)
    return JsonResponse({'info': 'This is your future profile'})


@csrf_exempt
@require_GET
def welcomeToFactory(request):
    return JsonResponse({'info': 'Hello! This is a cheese factory website where you can buy delicious cheese!'})



@csrf_exempt
@require_POST
def createCheese(request):
    post_data = json.loads(request.body.decode("utf-8"))
    cheese = Cheese()
    cheese.name = post_data.get('name')
    cheese.price = post_data.get('price')
    cheese.left = post_data.get('left')
    cheese.description = post_data.get('description')
    cheese.save()

    return JsonResponse({'info': 'ok'})


@csrf_exempt
@require_POST
def createOrder(request):
    post_data = json.loads(request.body.decode("utf-8"))

    order = Order.objects.create(user=User.objects.get(id=post_data.get('user_id')), data_order=datetime.today())
    total = 0
    for item in post_data.get('list_cheeses'):
        list_cheeses = List_cheese(order=order, cheese=Cheese.objects.get(vendor_code=item['vendor_code']), quantity=item['quantity'])
        total += Cheese.objects.filter(vendor_code=item['vendor_code']).values_list('price', flat=True)[0] * item['quantity']
        list_cheeses.save()
        Cheese.objects.filter(vendor_code=item['vendor_code']).update(left=Cheese.objects.filter(vendor_code=item['vendor_code']).values_list('left', flat=True)[0] -  item['quantity'])

    Order.objects.filter(id=order.id).update(total=total)
    return JsonResponse({'info': 'ok'})


@csrf_exempt
@require_GET
def searchCheese(request):
    if (search_str := request.GET.get("q", _UNDEFINED_STR)) != _UNDEFINED_STR:
        list_cheese = list(Cheese.objects.filter(Q(name__icontains=search_str) | Q(description__icontains=search_str)))
        return JsonResponse({'Сыры': cheeseDeserialized(list_cheese)})
    else:
        return JsonResponse({'info': 'Ничего не найдено'})