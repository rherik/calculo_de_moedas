real = float(input('Quantos reais você tem? R$ '))
dolar = real * 0.19
euro = real * 0.16
iene = real * 20.60
bitcoins = real * 0.0000041
print('Com seu dinheiro você pode comprar: \nUS${:.2f} dolares, \n€{:.2f} euros, \n¥{:.2f} Ienes, \n₿{:.5f} Bitcoins'.format(dolar, euro, iene, bitcoins))

