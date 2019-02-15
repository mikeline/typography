from django.shortcuts import render, redirect
import json
from . import tools
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from .forms import Prod, Typo
from django.urls import reverse
from urllib.parse import urlencode


def index(request):
    return render(request, "index.html")


def typos(request):
    json_data = tools.json_to_dict('templates/typo_list')
    return render(request, "typos.html", {'data': json_data})


def detail(request):
    data = request.GET
    key = data.get('key')
    key = tools.format_key(key)
    file = 'templates/' + key
    file = open(file, encoding='utf-8')
    file = dict(eval(file.read()))
    file.update({'key': key})
    return render(request, "detail.html", file)


def product(request):
    key = request.GET
    typo = key.get('typo')
    key = key.get('key')
    temp = typo
    typo = tools.format_key(typo)
    typo = 'templates/' + typo
    file = open(typo, encoding='utf-8')
    data = json.loads(file.read())
    new_dict = {}
    new_dict.update(data['typo']['prod'][key])
    new_dict.update({'key': temp})
    return render(request, "product.html", new_dict)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form': form})


def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('index')


@login_required(login_url='login')
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {'form': form})


@login_required(login_url='login')
def order(request):
    if request.method == 'POST':
        form = Prod(request.POST)
        if form.is_valid():
            file = open('temp.txt', encoding='utf-8')
            var = file.read()
            file.close()
            file = open(var, encoding='utf-8')
            data = dict(eval(file.read()))

            prod = form.cleaned_data
            id_prod = str(prod.get('name'))
            data['typo']['prod'].update({id_prod: prod})
            file.close()
            file = open(var, 'w', encoding='utf-8')
            data = json.dumps(data, ensure_ascii=False)
            file.write(data)
            file.close()
            return redirect('typos')
    else:
        var = request.GET
        var = 'templates/' + var.get('key')
        file = open('temp.txt', 'w', encoding='utf-8')
        file.write(var)
        file.close()

        form = Prod()
    return render(request, 'order.html', {'form': form})


@login_required(login_url='login')
def new_typo(request):
    if request.method == 'POST':
        form = Typo(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = str(data.get('name'))
            name = tools.format_key(name)

            adm_name = str(data.pop('first_name'))
            adm_last_name = str(data.pop('last_name'))
            adm_mid_name = str(data.pop('mid_name'))
            adm_birth_date = str(data.pop('birth_date'))

            link = 'templates/' + name
            file = open(link, 'w', encoding='utf-8')
            data.update({"admin": {"first_name": adm_name, "mid_name": adm_mid_name, "last_name": adm_last_name, "birth_date": adm_birth_date}})
            data.update({"prod": {}})
            format_data = {"typo": data}
            format_data = json.dumps(format_data, ensure_ascii=False)
            file.write(format_data)
            file.close()
            file = open('templates/typo_list', encoding='utf-8')
            temp = json.loads(file.read())
            typo_index = 0
            for key in temp:
                typo_index = key
            typo_index = int(typo_index) + 1
            typo_index = str(typo_index)
            temp.update({typo_index: name})
            temp = json.dumps(temp, ensure_ascii=False)
            file.close()
            file = open('templates/typo_list', 'w', encoding='utf8')
            file.write(temp)

            return redirect('typos')
    else:
        form = Typo()
    return render(request, 'new_typo.html', {'form': form})


@login_required(login_url='login')
def delete(request):
    key = request.GET
    typo = key.get('typo')
    key = key.get('key')
    db = 'templates/' + typo
    file = open(db, encoding='utf-8')
    data = json.loads(file.read())
    del data['typo']['prod'][key]
    file.close()
    file = open(db, 'w', encoding='utf-8')
    data = json.dumps(data, ensure_ascii=False)
    file.write(data)
    base_url = reverse('detail')
    query_string = urlencode({'key': typo})
    url = '{}?{}'.format(base_url, query_string)
    return redirect(url)
