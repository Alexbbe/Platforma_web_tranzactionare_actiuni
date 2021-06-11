import finnhub
import json
from after_login.models import Transactions

def investment_update():
    client = finnhub.Client(api_key="c16dnhv48v6ppg7eoebg")
    with open('/home/alexbbe/Documents/pythonProject2/licenta3/companii.txt') as json_file:
        data = json.load(json_file)
        list1 = [(data[i]['displaySymbol'], data[i]['description']) for i in range(0, len(data))]
    trans = Transactions.objects.all()
    for tran in trans:
        for i in range(0, len(list1)):
            company1 = list1[i][1].title()
            if tran.company == company1:
                quote = client.quote(list1[i][0])
                tran.actual_invested = tran.quantity * quote['c']
                if tran.type == 'Sale':
                    tran.profit = tran.invested - tran.actual_invested
                elif tran.type == 'Purchased':
                    tran.profit = tran.actual_invested - tran.invested
                tran.save()





















