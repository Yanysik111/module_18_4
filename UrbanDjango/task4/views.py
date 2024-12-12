from django.shortcuts import render


# Create your views here.
def main_page(request):
    #headline = 'Главная страница'
    #text1 = 'Главная'
    #text2 = 'Магазин'
    #text3 = 'Корзина'
    #context = {'headline': headline,
              # 'text1': text1,
               #'text2': text2,
               #'text3': text3, }
    return render(request, 'fourth_task/sh1.html')


def first_page(request):
    #name = 'Игры'
    games = ['Atomic Heart', 'Cyberpank 2077', 'PayDay 2']
    #ret = 'Вернуться обратно'
    context = {#'name': name,
               'games': games}
               #'ret': ret, }
    return render(request, 'fourth_task/sh2.html', context)


def second_page(request):
    #text = 'Извините, Ваша корзина пуста'
    #ret = 'Вернуться обратно'
    #context = {'text': text,
               #'ret': ret, }
    return render(request, 'fourth_task/sh3.html')








