from django.http import JsonResponse
from django.shortcuts import render

import json

# Create your views here.
def orders(request):
    with open('assets/orders.json') as orders:
        allOrders = json.load(orders)

    if request.method == 'POST':
        data = json.loads(request.body.decode())
        orderId = list(data.keys())[0]

        allOrders[orderId] = data[orderId]

        with open('assets/orders.json', 'w') as orders:
            json.dump(allOrders, orders, indent=4)
        
        return JsonResponse({
            'orderPlaced': True
        })
    
    return JsonResponse(allOrders)

def getCart(request, email):
    with open('assets/users.json') as users:
        userCred = json.load(users)
    
        for user in userCred:
            if user['email'].lower() == email:
                return JsonResponse({
                    'cartData': user['cartData']
                })

    return JsonResponse({
        'cartData': []
    })

def pushCart(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        with open('assets/users.json') as users:
            userCred = json.load(users)

            search = -1
            for user in userCred:
                print(user)
                search += 1
                if user['email'].lower() == data['email'].lower():
                    break
            else:
                return JsonResponse({})
            
            userCred[search]['cartData'] = data['cartData']

        with open('assets/users.json', 'w') as users:
            json.dump(userCred, users, indent=4)
    
    return JsonResponse({})


def authLogin(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        with open('assets/users.json') as users:
            userCred = json.load(users)

            for user in userCred:
                if user['email'].lower() == data['email'].lower():

                    return JsonResponse({
                        'loginStatus': True
                    })

    return JsonResponse({
        "loginStatus": False
    })

def signUp(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        with open('assets/users.json') as users:
            userCred = json.load(users)

            for user in userCred:
                if user['email'].lower() == data['email'].lower():

                    return JsonResponse({
                        'signUpStatus': False
                    })
            
        userCred.append({
            'name': data['name'],
            'email': data['email'],
            'phno': data['phno'],
            'password': data['password'],
            'cartData': []
        })

        with open('assets/users.json', 'w') as users:
            json.dump(userCred, users, indent=4)

    
    return JsonResponse({
        "signUpStatus": True
    })


