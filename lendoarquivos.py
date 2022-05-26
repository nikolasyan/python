f = open("demofile.txt", "a")
f = open("demofile.txt", "a")
i = 0
while i <=5:
    a = input("Digite 5 textos: ")
    i = i+1
    f.write(a)
f.close()
f = open("demofile.txt", "r")    
arquivo = f.readline()
print(arquivo)
