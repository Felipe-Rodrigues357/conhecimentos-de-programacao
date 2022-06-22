import datetime
ano = int(input('Digite o ano (Coloque 0 para analisar o ano atual): '))
if ano == 0:
    ano = datetime.date.today().year
if ano%4==0 and ano%100!=0 or ano%400==0:
    print("O Ano {} é Bissexto!".format(ano))
else:
    print("O Ano {} não é Bissexto!".format(ano))