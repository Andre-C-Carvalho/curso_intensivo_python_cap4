minhas_pizzas = ["mussarela", "calabreza", "quatro queijos", "portuguesa", "frango com catupiri"]
print("\nMinhas pizzas favoritas são:")
for pizza in minhas_pizzas:
    print(pizza.title())
rafa_pizzas = minhas_pizzas[:]
print("\nAs pizzas favoritas do Rafael são:")
for pizza in rafa_pizzas:
    print(pizza.title())
minhas_pizzas.append("peperoni")
rafa_pizzas.append("brasileira")
print("\nMinhas novas pizzas favoritas são:")
for pizza in minhas_pizzas:
    print(pizza.title())
print("\nAs novas pizzas favoritas do Rafael são:")
for pizza in rafa_pizzas:
    print(pizza.title())
