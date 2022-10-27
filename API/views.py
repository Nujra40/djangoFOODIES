from django.http import JsonResponse
from django.shortcuts import render

import json

# Create your views here.
def orders(request):
    if request.method == 'POST':
        print('POST Request')

def authLogin(request, email, password):
    loginStatus = False
    with open('assets/users.json') as users:
        userCred = json.load(users)

        for user in userCred:
            if user['email'] == email and user['password'] == password:
                loginStatus = True
                break
    
    return JsonResponse({
        "loginStatus": loginStatus
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
            'password': data['password']
        })

        with open('assets/users.json', 'w') as users:
            json.dump(userCred, users)

    
    return JsonResponse({
        "signUpStatus": True
    })


