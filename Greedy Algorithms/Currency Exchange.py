"""
Given the currency denominations of a country

Find the MIN NOTES/COINS used to pay the amount provided
"""

notes = [1,2,5,10,20,50,100,200,500,2000]
cash_to_be_paid = 5548

def currency_exchange(denominations, amount):
    denominations.sort(reverse=True)
    result = {}
    for denomination in denominations:
        if amount >= denomination:
            count = amount//denomination
            result[denomination] = count
            amount %= denomination
    return sum(result.values())

print(f'min notes used = {currency_exchange(notes, cash_to_be_paid)}')

