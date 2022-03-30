import random
from uuid import uuid4
from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def homepage(request):
    password = random.randint(1,100)
    return render(request,"generator/index.html",context={'password':password})

def password(request):
    chars = ['a','b','c','d', 'e', 'f' ,'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's' ,'t' ,'u' ,'v' ,'w' ,'x' ,'y' ,'z']
    length = int(request.GET.get('length',12)) # берем значение length из get запроса # http://127.0.0.1:8000/password/?length=12, значение по умолчанию 12 если в запросе не была передана length
    if request.GET.get("uppercase"):
        chars.extend([x.upper() for x in chars]) #Добавляем элементы  списка в список
        # если в запросе есть uppercase то расширяем список символов
    if request.GET.get("special"):
        chars.extend(['@','#','!','$','%','^','&','*','@','#','!','$','%','^','&','*',]) #Добавляем элементы  списка в список
        # если в запросе есть special то расширяем список символов

    if request.GET.get("numbers"):
        chars.extend([str(x) for x in range(1,10 + 1)]) #Добавляем элементы  списка в список
        # если в запросе есть numbers то расширяем список символов
    password = ''
    for x in range(length):
        password += random.choice(chars)
    return render(request,'generator/pass.html',context={'password':password})


