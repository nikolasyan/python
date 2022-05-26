placa = input("Placa: ")
ult = placa[len(placa)-1: len(placa)]
rodizio = {"1": "segunda",
           "2": "segunda",
           "3": "terca",
           "4": "terca",
           "5": "quarta",
           "6": "quarta",
           "7": "quinta",
           "8": "quinta",
           "9": "sexta",
           "0": "sexta"}
print(rodizio[ult])