import json
import datetime
import braintree
import datetime
from bottle import route, run, template



def setup():
    btconf = braintree.Configuration.configure(braintree.Environment.Sandbox,
        merchant_id="9bwqrvqmpknc9knm",
        public_key="7mnjdknsssqxzjwr",
        private_key="f741115b1048a4477e849ca953df94ab")
    return btconf

def listTransactions(clientToken=None,loadAmount=0):
    if loadAmount > 1000:
        return False
    collection = braintree.Transaction.search(
    braintree.TransactionSearch.customer_id == clientToken,
    braintree.TransactionSearch.created_at.between(
            datetime.datetime.now() - datetime.timedelta(days=365),
            datetime.datetime.now()
        )
    )
    #first
    response = []
    response.append(True) if loadAmount + sum([ int(x.amount) for x in collection if x.created_at.date() == datetime.date.today() ]) <= 500 else response.append(False)
    response.append(True) if loadAmount + sum([ int(x.amount) for x in collection if x.created_at.date() >= datetime.date.today() - datetime.timedelta(days=30) ]) <= 800 else response.append(False)
    response.append(True) if loadAmount + sum([ int(x.amount) for x in collection ]) <= 2000 else response.append(False)#as the original search is 365 anyways
    return False if False in response else True






'''
    - maximum 500 worth of loads per day
    - maximum 800 worth of loads per 30 days
    - maximum 2000 worth of loads per 365 days
    - maximum balance at any time 1000
'''


setup()
@route('/load/<client>/<amount>')
def index(client,amount):
    return {"response":listTransactions(client,int(amount))}
run(host='localhost', port=8080)
