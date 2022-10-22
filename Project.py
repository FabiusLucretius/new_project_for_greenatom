company = {
    "wage": {
        "101": 190900,
        "102": 77889,
        "103": 6675764
    },
    "MaterialCosts": {
        "201": 56756,
        "202": 56578,
        "203": 4435
    },
    "MarketingExpenses": {
        "301": 4576,
        "302": 767678,
        "303": 238734
    },
    "SocialInsurance": {
        "401": 96767,
        "402": 3479,
        "403": 236864
    }
}
def cost_items(number):
    for i in range(len(number)):
        if number[i] == search:
            return number[i + 1]
search = input()

