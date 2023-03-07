import requests
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
rates = response.json()

with open('rates.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=";")

    writer.writerow(["Currency", "Code", "Bid", "Ask"])

    for row in rates[0]["rates"]:
        writer.writerow([row["currency"], row["code"], row["bid"], row["ask"]])

print("Rates saved to rates.csv.")