from django.http import JsonResponse
from django.shortcuts import render

import requests

import json

# Create your views here.
def getMenu(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        data = json.loads(data['menu'])
        
        with open('assets/menu.json', 'w') as menuFile:
            json.dump(data, menuFile, indent=4)
        
        return JsonResponse({})
    
    with open('assets/menu.json') as menuFile:
        menu = json.load(menuFile)

    return JsonResponse(menu, safe=False)

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
                search += 1
                if user['email'].lower() == data['email'].lower():
                    break
            else:
                return JsonResponse({})
            
            userCred[search]['cartData'] = data['cartData']

        with open('assets/users.json', 'w') as users:
            json.dump(userCred, users, indent=4)
    
    return JsonResponse({})

def getInvoice(request, email):
    with open('assets/users.json') as users:
        userCred = json.load(users)
    
        for user in userCred:
            if user['email'].lower() == email:
                return JsonResponse({
                    'totAmount': user['totAmount'],
                    'totItems': user['totItems']
                })

    return JsonResponse({
        'error': []
    })

def pushInvoice(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        with open('assets/users.json') as users:
            userCred = json.load(users)

            search = -1
            for user in userCred:
                search += 1
                if user['email'].lower() == data['email'].lower():
                    break
            else:
                return JsonResponse({})
            
            userCred[search]['totItems'] = data['totItems']
            userCred[search]['totAmount'] = data['totAmount']

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


def getAccessToken_instagram(request):
    if request.method == "POST":
        data = json.loads(request.body.decode())
        print(data)

        response = requests.post("https://api.instagram.com/oauth/access_token", {
            "client_id": "280064384898783",
            "client_secret": "a78c114676e1103bf529af43a9648365",
            "grant_type": "authorization_code",
            "redirect_uri": "https://localhost:4200/pay/",
            "code": data["code"]
        })

        res = json.loads(response.text)



        if (response.status_code == 200):

            url = f"https://graph.instagram.com/{res['user_id']}/media"
            params = {
                "fields": "id,caption,media_url,media_type,permalink,thumbnail_url,timestamp,username",
                "access_token": res["access_token"]
            }

            user_info = requests.get(url, params=params)

            return JsonResponse(
                json.loads(user_info.text)
            )
            
    
    return JsonResponse({})


