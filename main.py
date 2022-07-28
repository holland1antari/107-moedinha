import moeda

p = float(input("digite o valor em R$:"))

moeda.linha()
print(f"o dobro de {p} é {moeda.dobro(p)}")
moeda.linha()
print(f"a metade de {p} é {moeda.metade(p)}")
moeda.linha()
print(f"aumentando 10%, temos:{moeda.aumentar(p,10)}")
moeda.linha()
print(f"diminuindo em 13%, temos{moeda.diminuir(p,13)}")
moeda.linha()
