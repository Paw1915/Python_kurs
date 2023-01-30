cheese1 = 'roquefort'
cheese2 = 'stilton'
cheese3 = 'brie'
cheese4 = 'gouda'
cheese5 = 'edam'
cheese6 = 'parmezan'
cheese7 = 'mozzarella'
cheese8 = "czechosłowacki ser z owczego mleka"
mintwaffer = "listek miętowy"

price1 = 12.50
price2 = 11.24
price3 = 9.30
price4 = 8.55
price5 = 11.00
price6 = 16.50
price7 = 14.00
price8 = 122.32
price9 = 100

weight1 = 2
weight2 = 1
weight3 = 1
weight4 = 1
weight5 = 1
weight6 = 3.5
weight7 = 1.3
weight8 = 2.2
weight9 = 0.2
#wszystko w zmiennych gdyby szef zmienił zdanie

priceTotal = (price1*weight1)+(price2*weight2)+(price3*weight3)+(price4*weight4)+(price5*weight5)+(price6*weight6)+(price7*weight7)+(price8*weight8)+(price9*weight9)

raport = f"Raport z zakupów: \n{cheese1}, {weight1} kg, {price1 * weight1} zł\n{cheese2}, {weight2} kg, {price2 * weight2} zł\n{cheese3}, {weight3} kg, {price3 * weight3} zł\n{cheese4}, {weight4} kg, {price4 * weight4} zł\n{cheese5}, {weight5} kg, {price5 * weight5} zł\n{cheese6}, {weight6} kg, {price6 * weight6} zł\n{cheese7}, {weight7} kg, {price7 * weight7} zł\n{cheese8}, {weight8} kg, {price8 * weight8} zł\n{mintwaffer}, {weight9} kg, {price9 * weight9} zł\nSuma zł: {priceTotal}"

print(raport)