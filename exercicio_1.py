import requests


def get_data():
    url = "https://api.hgbrasil.com/finance?key=524d5dc0"
    data = requests.get(url)
    usd_value = data.json()["results"]["currencies"]["USD"]["buy"]
    eur_value = data.json()["results"]["currencies"]["EUR"]["buy"]

    user_value = float(input("Digite o valor em Reak=l: "))
    usd_parsed = user_value / usd_value
    eur_parsed = user_value / eur_value
    return f"Valor em Euro = R${eur_parsed:.2f}\n" \
           f"Valor em Dólares = R${usd_parsed:.2f}"
