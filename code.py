import json

def read_file(name):
    data = ""
    with open(name, 'r') as f:
        data = f.read()
    return data

def balances_dict(data):
    balances_dict = {}
    for item in data["expenseData"]:
        date = item["startDate"]
        date, time = date.split("T")
        year, month, day = date.split("-")
        new_date = year + "-" + month + "-01" + "T" + time
        if new_date not in balances_dict:
            balances_dict[new_date] = 0
        balances_dict[new_date] -= item["amount"]

    for item in data["revenueData"]:
        date = item["startDate"]
        date, time = date.split("T")
        year, month, day = date.split("-")
        new_date = year + "-" + month + "-01" + "T" + time
        if new_date not in balances_dict:
            balances_dict[new_date] = 0
        balances_dict[new_date] += item["amount"]
    return balances_dict


def get_output_res(balances_dict):
    res = []
    dates_list = []
    for date, amount in balances_dict.items():
        item = dict(amount=amount, startDate=date)
        res.append(item)

    res = sorted(res, key=lambda d: d['startDate'])
    return dict(balance=res)

i1 = json.loads( read_file("1-input.json") )
i1_balances = get_output_res( balances_dict(i1) )
print(i1_balances)

i2 = json.loads( read_file("2-input.json") )
i2_balances = get_output_res( balances_dict(i2) )
print(i2_balances)