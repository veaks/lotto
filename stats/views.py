from django.shortcuts import render
import requests, lxml
from bs4 import BeautifulSoup
from stats.models import Draws


def list_draws(request):
    qs = Draws.objects.all()
    context = {'list_draws': qs}
    return render(request, 'list_draws.html', context)

def overall_stat(request):
    list_numbers1 = {}
    for i in range(1, 21):
        list_numbers1[i]=0
    list_numbers2 = {}
    for i in range(1, 21):
        list_numbers2[i]=0
    qs = Draws.objects.all()
    current = int(Draws.objects.first().number)
    latest = Draws.objects.filter(number__gt=current-40)
    latest = latest.order_by('number')
    for i in range(1, 21):
        for item in qs:
            if item.n1==i or item.n2==i or item.n3==i or item.n4==i:
                list_numbers1[i] += 1
            if item.n5==i or item.n6==i or item.n7==i or item.n8==i:
                list_numbers2[i] += 1
    context = {'list_numbers1': list_numbers1, 'list_numbers2': list_numbers2, 'latest': latest}
    return render(request, 'overall_stat.html', context)

def update(request):
    numbers = []
    results = []
    req =requests.get('https://www.stoloto.ru/4x20/archive/')
    soup = BeautifulSoup(req.text, 'lxml')
    for i in soup.find_all(class_='draw'):
        s = i.text.replace('\n', '')
        if len(s)==4:
            numbers.append(s)
    for i in soup.find_all(class_='container cleared'):
        s = i.text.replace('\n', '')
        results.append(s)
    latest_results = {}
    for i in range(len(numbers)-1):
        latest_results[int(numbers[i])] = results[i]
    current = Draws.objects.first().number
    for key, value in latest_results.items():
        if key > current:
            draw = Draws()
            draw.number = key
            draw.n1 = int(value[:2])
            draw.n2 = int(value[2:4])
            draw.n3 = int(value[4:6])
            draw.n4 = int(value[6:8])
            draw.n5 = int(value[8:10])
            draw.n6 = int(value[10:12])
            draw.n7 = int(value[12:14])
            draw.n8 = int(value[14:])
            draw.save()
    return render(request, 'update.html')