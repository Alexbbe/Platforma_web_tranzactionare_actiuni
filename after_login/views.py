from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from after_login.forms import UserEditForm, Transactions_Form
from after_login.models import Transactions
from after_login.functions import is_time_between, is_weekend
from accounts.models import MyUser
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta
import json
import finnhub
import requests

def calculate_capital_profit(email,id):
    a = MyUser.objects.get(email=email)
    companies = list(a.company_list)
    tran = Transactions.objects.all()
    invested = 0
    actual_invested = 0
    total_profit = 0
    for t in tran:
        if t.user_id == id:
            invested += t.invested
            actual_invested += t.actual_invested
            total_profit += t.profit
    money = a.money
    capital = money + actual_invested
    return money,invested,total_profit,capital,companies


with open('/home/alexbbe/Documents/pythonProject2/licenta3/companii.txt') as json_file:
    data = json.load(json_file)
    list1 = [(data[i]['displaySymbol'],data[i]['description']) for i in range(0 , len(data))]

companies_name = [list1[i][1].title() for i in range(0,len(list1))]
companies_symbols = [list1[i][0] for i in range(0,len(list1))]

finnhub_client = finnhub.Client(api_key="c16dnhv48v6ppg7eoebg")

# Create your views here.

@login_required(login_url='userlogin')
@cache_control(no_cache=True, must_revalidate=True , no_store=True )
def index(request):


    is_open = False
    if is_weekend() is False and is_time_between() is True:
        is_open = True
    data = calculate_capital_profit(email=request.user,id=request.user.id)
    companies = data[4]
    list_of_requests = list()
    form1 = Transactions_Form()
    if request.method == 'POST':
        form1 = Transactions_Form(request.POST)
        if form1.is_valid():
            instance1 = form1.save(commit=False)
            instance1.user = request.user
            instance1.save()

    for elem1 in companies:
        r = finnhub_client.company_profile2(symbol=elem1)
        r1 = finnhub_client.quote(symbol=elem1)
        list_of_requests.append((r,r1))

    context = {'info':list_of_requests,
               'search_list':companies_name,
               'trade':form1,
               'money':round(data[0],2),
               'invested':round(data[1],2),
               'profit': round(data[2],2),
               'capital':round(data[3],2),
               'market_open':is_open
               }

    return render(request,'after_login/index.html',context)

@login_required(login_url='login')
def market_news(request):

    r = requests.get('https://finnhub.io/api/v1/news?category=general&token=c16dnhv48v6ppg7eoebg')
    data = calculate_capital_profit(email=request.user,id=request.user.id)
    news = r.json()
    context = {
        'news':news,
        'money': round(data[0], 2),
        'invested': round(data[1], 2),
        'profit': round(data[2], 2),
        'capital': round(data[3], 2),

    }
    return render(request,'after_login/market_news.html',context)


@login_required(login_url='login')
def edit_user(request):

    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('index')

    else:
        form = UserEditForm()

    context = {
        'form': form,
        'search_list': companies_name,

    }
    return render(request, 'after_login/edit_user.html',context)


@login_required(login_url='login')
def user_info(request):
    data = calculate_capital_profit(email=request.user, id=request.user.id)
    user = request.user.money
    a = MyUser.objects.get(email=request.user)
    context = {
        'user': user,
        'money': round(data[0], 2),
        'invested': round(data[1], 2),
        'profit': round(data[2], 2),
        'capital': round(data[3], 2),
    }
    return render(request,'after_login/user_info.html',context)


@login_required(login_url='login')
def company_page(request):
    """
    On this page are the specific informations for
    a specific company!!
    """
    """check the time interval """

    now = datetime.now()
    timestamp_now = int(datetime.timestamp(now))
    time_24h = now + timedelta(hours=-24)
    timestamp_now_24h = int(datetime.timestamp(time_24h))
    # time_30days = now + timedelta(days=-30)
    # timestamp_30days = int(datetime.timestamp(time_30days))


    is_open = False
    if is_weekend() is False and is_time_between() is True:
        is_open = True


    time = datetime.now().time()
    if request.method == 'GET' or request.method == 'POST':
        company_get = request.GET.get('company')
        for elem in list1:
            if company_get.upper() == elem[1].upper():
                symbol1 = elem[0]


    quote = finnhub_client.quote(symbol=symbol1)
    df1 = pd.read_csv( f'https://finnhub.io/api/v1/stock/candle?symbol={symbol1}&resolution=D&from=1609459200&to={timestamp_now}&token=c16dnhv48v6ppg7eoebg&format=csv')
    df2 = pd.read_csv(f'https://finnhub.io/api/v1/stock/candle?symbol={symbol1}&resolution=5&from={timestamp_now_24h}&to={timestamp_now}&token=c16dnhv48v6ppg7eoebg&format=csv')

    list_of_dates1 = list()
    list_of_dates2 = list()
    for num in df1['t']:
        num = datetime.fromtimestamp(num)
        list_of_dates1.append(num)

    for num in df2['t']:
        num = datetime.fromtimestamp(num)
        list_of_dates2.append(num)




    date1 = pd.Series(list_of_dates1)
    date2 = pd.Series(list_of_dates2)

    fig = go.Figure(data=[go.Candlestick(x=date1,
                                         open=df1['o'],
                                         high=df1['h'],
                                         low=df1['l'],
                                         close=df1['c'])])
    str1 = fig.to_html(full_html=False, default_height=600, default_width=1000)

    fig = go.Figure(data=[go.Candlestick(x=date2,
                                         open=df2['o'],
                                         high=df2['h'],
                                         low=df2['l'],
                                         close=df2['c'])])
    str2 = fig.to_html(full_html=False, default_height=600, default_width=1000)



    company_api_desc = requests.get(f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol1}&apikey=RWLP0FCH73F5JTJA')
    r = finnhub_client.company_profile2(symbol=symbol1)
    company_api_desc_json = company_api_desc.json()
    form1 = Transactions_Form()
    a = MyUser.objects.get(email=request.user)
    if request.method == 'POST':
        form1 = Transactions_Form(request.POST)
        if form1.is_valid():
            instance1 = form1.save(commit=False)
            instance1.user = request.user
            # current_money = deepcopy(quote['c'])
            instance1.invested = form1.cleaned_data['quantity'] * float(quote['c'])
            instance1.actual_invested = instance1.invested
            instance1.profit = instance1.actual_invested - instance1.invested
            a.money = a.money - instance1.invested
            a.save()
            instance1.company = company_get
            instance1.save()

    money = a.money
    company_news = requests.get(f'https://finnhub.io/api/v1/company-news?symbol={symbol1}&from=2021-03-01&to=2021-03-09&token=c16dnhv48v6ppg7eoebg')
    company_news = company_news.json()
    data = calculate_capital_profit(email=request.user,id=request.user.id)
    context = {'company_info':company_api_desc_json,
               'search_list':companies_name,
               'symbol': r,
               'graph': str1,
               'graph1':str2,
               'trade': form1,
               'quote': quote,
               'money': money,
               'is_open': is_open,
               'company_news':company_news,
               'time':time,
               'money': round(data[0], 2),
                'invested': round(data[1], 2),
                 'profit': round(data[2], 2),
                'capital': round(data[3], 2)
               }

    return render(request,'after_login/company.html',context)

@login_required(login_url='login')
def portofolio(request):
    list_of_tran = list()
    tr1 = Transactions.objects.all()
    for p in Transactions.objects.raw('SELECT * FROM after_login_transactions'):
       list_of_tran.append(p.company)
    set1 = list(set(list_of_tran))
    lsit1 = list()
    for s in set1:
        total = 0
        for quer in Transactions.objects.raw('SELECT * FROM after_login_transactions'):
            if quer.company == s:
                total+=quer.quantity
        set2 = {'company':s,
                'quantity':total,
         }
        lsit1.append(set2)
    list_of_plm = list()
    for tran in tr1:
        list_of_plm.append(tran.company)
    data = calculate_capital_profit(email=request.user,id=request.user.id)
    context = {'tran':lsit1,
               'tr': list_of_plm,
               'money': round(data[0], 2),
               'invested': round(data[1], 2),
               'profit': round(data[2], 2),
               'capital': round(data[3], 2)
               }
    return render(request,'after_login/portofolio.html',context)


@login_required(login_url='login')
def tran(request,company):
    list_of_trans = list()
    for p in Transactions.objects.raw(f'SELECT * FROM after_login_transactions WHERE company="{company}"'):
        list_of_trans.append(p)
    data = calculate_capital_profit(email=request.user, id=request.user.id)
    context = {'trans': list_of_trans,
               'money': round(data[0], 2),
               'invested': round(data[1], 2),
               'profit': round(data[2], 2),
               'capital': round(data[3], 2)
               }

    return render(request, 'after_login/company_transactions.html',context)


@login_required(login_url='login')
def delete_transaction(request,id,company):
    record = Transactions.objects.get(id=id,company=company)
    a = MyUser.objects.get(email=request.user)
    a.money = a.money + record.actual_invested
    a.save()
    record.delete()
    return redirect(f'/portofolio/transactions/{company}')


@login_required(login_url='login')
def add_company(request):
    company = request.GET.get('company')
    current_User = MyUser.objects.get(email=request.user)
    list1 = list(set(current_User.company_list))
    list1.append(company)
    list1 = list(set(list1))
    current_User.company_list = list1
    current_User.save()
    return redirect('/index')


@login_required(login_url='login')
def del_company(request):
    company_del = request.GET.get('company_del')
    current_User = MyUser.objects.get(email=request.user)
    list1 = list(current_User.company_list)
    list1.remove(company_del)
    current_User.company_list = list1
    current_User.save()
    return redirect('/index')




