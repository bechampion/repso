import braintree
# -*- coding: iso-8859-15 -*-
import os,sys


'''
im guessing this will be the last step.
i liked the braintree protection for duplicated transactions, wonder if all payment gw
work like that
'''

dt = 22221788
client = "eyJ2ZXJzaW9uIjoyLCJhdXRob3JpemF0aW9uRmluZ2VycHJpbnQiOiIzM2VmMmYxYzhmZTgxZjJkYjU0MGVmNzQ0ZWZhZmQyOWY2ZjUyOThmNWQ1YWY4ZWQ0YTQ4YmUzNWViNDVlOGE3fGNyZWF0ZWRfYXQ9MjAxNy0wMi0wNFQxODowMToxNC41OTg0Njc2MzUrMDAwMFx1MDAyNm1lcmNoYW50X2lkPTlid3FydnFtcGtuYzlrbm1cdTAwMjZwdWJsaWNfa2V5PTdtbmpka25zc3NxeHpqd3IiLCJjb25maWdVcmwiOiJodHRwczovL2FwaS5zYW5kYm94LmJyYWludHJlZWdhdGV3YXkuY29tOjQ0My9tZXJjaGFudHMvOWJ3cXJ2cW1wa25jOWtubS9jbGllbnRfYXBpL3YxL2NvbmZpZ3VyYXRpb24iLCJjaGFsbGVuZ2VzIjpbXSwiZW52aXJvbm1lbnQiOiJzYW5kYm94IiwiY2xpZW50QXBpVXJsIjoiaHR0cHM6Ly9hcGkuc2FuZGJveC5icmFpbnRyZWVnYXRld2F5LmNvbTo0NDMvbWVyY2hhbnRzLzlid3FydnFtcGtuYzlrbm0vY2xpZW50X2FwaSIsImFzc2V0c1VybCI6Imh0dHBzOi8vYXNzZXRzLmJyYWludHJlZWdhdGV3YXkuY29tIiwiYXV0aFVybCI6Imh0dHBzOi8vYXV0aC52ZW5tby5zYW5kYm94LmJyYWludHJlZWdhdGV3YXkuY29tIiwiYW5hbHl0aWNzIjp7InVybCI6Imh0dHBzOi8vY2xpZW50LWFuYWx5dGljcy5zYW5kYm94LmJyYWludHJlZWdhdGV3YXkuY29tLzlid3FydnFtcGtuYzlrbm0ifSwidGhyZWVEU2VjdXJlRW5hYmxlZCI6dHJ1ZSwicGF5cGFsRW5hYmxlZCI6dHJ1ZSwicGF5cGFsIjp7ImRpc3BsYXlOYW1lIjoiamVycnljb3JwIiwiY2xpZW50SWQiOm51bGwsInByaXZhY3lVcmwiOiJodHRwOi8vZXhhbXBsZS5jb20vcHAiLCJ1c2VyQWdyZWVtZW50VXJsIjoiaHR0cDovL2V4YW1wbGUuY29tL3RvcyIsImJhc2VVcmwiOiJodHRwczovL2Fzc2V0cy5icmFpbnRyZWVnYXRld2F5LmNvbSIsImFzc2V0c1VybCI6Imh0dHBzOi8vY2hlY2tvdXQucGF5cGFsLmNvbSIsImRpcmVjdEJhc2VVcmwiOm51bGwsImFsbG93SHR0cCI6dHJ1ZSwiZW52aXJvbm1lbnROb05ldHdvcmsiOnRydWUsImVudmlyb25tZW50Ijoib2ZmbGluZSIsInVudmV0dGVkTWVyY2hhbnQiOmZhbHNlLCJicmFpbnRyZWVDbGllbnRJZCI6Im1hc3RlcmNsaWVudDMiLCJiaWxsaW5nQWdyZWVtZW50c0VuYWJsZWQiOnRydWUsIm1lcmNoYW50QWNjb3VudElkIjoiamVycnljb3JwIiwiY3VycmVuY3lJc29Db2RlIjoiRVVSIn0sImNvaW5iYXNlRW5hYmxlZCI6ZmFsc2UsIm1lcmNoYW50SWQiOiI5YndxcnZxbXBrbmM5a25tIiwidmVubW8iOiJvZmYifQ=="

def setup():
    btconf = braintree.Configuration.configure(braintree.Environment.Sandbox,
        merchant_id="9bwqrvqmpknc9knm",
        public_key="7mnjdknsssqxzjwr",
        private_key="f741115b1048a4477e849ca953df94ab")
    return btconf
# print braintree.ClientToken.generate()

def processPayment(customer=None):
    fake = "fake-valid-nonce"
    result = braintree.Transaction.sale({
    "amount": "1.00",
    "payment_method_nonce": fake,
    "customer_id": customer,
    "options": {
        "submit_for_settlement": True,
        }
    })
    return result

def listTransactions(clientToken=None):
    collection = braintree.Transaction.search(
    braintree.TransactionSearch.customer_id == clientToken
    )
    for transaction in collection.items:
        print transaction.amount
        print transaction.created_at

setup()
# print processPayment(dt)
listTransactions(dt)


'''
    - maximum 500 worth of loads per day
    - maximum 800 worth of loads per 30 days
    - maximum 2000 worth of loads per 365 days
    - maximum balance at any time 1000
'''













