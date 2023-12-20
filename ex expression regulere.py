import re


exemple= '''P1 est un produit composé de P2 et P3
P2 est un produit élémentaire
P5 est un produit composé de P1 et P4
P4 est un produit élémentaire
P9 est un produit composé de P1, P6 et P4
P10 est un produit composé de P3 et P5
P11 est un produit composé de P5 et P3'''


search1 = re.findall(r"P[\d] est un produit élémentaire",exemple)
print(search1)

search2 = re.findall(r"P[\d]{1,} est un produit composé de P[\d], P[\d] et P[\d]",exemple)
print(search2)


search3 = re.findall(r"P[\d]{1,} est un produit composé de P[3,5] et P[3,5]",exemple)
print(search3)

search4 = re.findall(r"P[\d]{1,} est un produit composé de P[^2]",exemple)
print(search4)


search5 = re.findall(r"P9 est un produit composé de (.+)\n",exemple)
print(search5)