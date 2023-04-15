frutas = ["banana", "abacaxi", "melão", "abacate", "ameixa", "carambola", "pitaia", "pitanga", "acerola", "cajá"]
print("\nA lista de frutas completa é:")
print(frutas)
print("\nOs três primeiros itens da lista são:")
for fruta in frutas[0:3]:
    print(fruta.title())
print("\nOs quatro itens do meio da lista são:")
for fruta in frutas[3:7]:
    print(fruta.title())
print("\nOs três últimos itens da lista são:")
for fruta in frutas[7:10]:
    print(fruta.title())
