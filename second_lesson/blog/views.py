from django.http import HttpResponse
from django.shortcuts import render

items = {
    'Smartphone': {
        'id': 1,
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
    'Laptop': {
        'id': 2,
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
    'Keyboard': {
        'id': 3,
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
    'Mouse': {
        'id': 4,
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    }
}


def home(request):
    menu = ['home', 'about', 'posts',]
    data = {'menu': menu,
            'items': items}
    return render(request, 'blog/index.html', context=data)


def product(request, product_id):
    product_lst = [i for i in items if items[i]['id'] == product_id]

    return render(request, 'blog/product.html',
                  {'product_desc': items[product_lst[0]], 'product_name': product_lst[0]})


def about(request):
    return render(request, 'blog/about.html')
