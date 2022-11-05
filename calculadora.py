import matplotlib.pyplot as plt

repeticion=int(input("Cuantas veces queres que se repita el codigo: "))
lista=[]
graf1x=[]
graf1y=[]
graf2y=[]
graf2x=[]
for i in range(0,repeticion):
    def variables():
        vel= float(input("ingrese la velocidad en m/s: "))
        while vel<0:
          vel= float(input("noooo negativo noo ingrese la velocidad devuelta en m/s y positivo: "))
          if vel>0:
            break
        cabal=float(input("ingrese la distancia del objeto 1 hasta el objeto 2(en metros): "))
        while cabal<0:
          cabal=float(input("noooooo negativo nooo ingrese la distancia del caballo hasta el auto devuelta (en metros y positivo): "))
          if cabal>0:
            break
        fren= float(input("ingrese a que velocidad el auto desacelera(expresalo en negativo): "))
        return calculos(vel, cabal, fren)
    def calculos(vel, cabal, fren):
        while fren>0:
            fren= float(input("NO se puede la desaceleracion numero positivo ponelo en negativo: "))
            if fren<0:
                break
        calc= 0-vel
        tie= calc/fren
        dist= 0+vel*tie+0.5*fren*(tie*tie)
        if dist>cabal:
            print("Te tragaste a un caballo de frente pobre de el :(")
            c = vel + (1/2)*(0-vel)
            c2 = cabal/c
            acel = (0-vel)/c2
            print("nececitabas frenar a ", acel, "m/s2 para no chocarte")
            print("lo chocaste en ",tie, "segundos")
            lista.append(acel)
            lista.append(tie)

        elif dist<=cabal:
            dist2=cabal-dist
            print("te quedaste a",dist2, "metros de chocar al caballo")
            print("Frenaste en ",tie, "segundos")
            lista.append(dist2)
            lista.append(tie)
        graf1y.append(tie)
        graf1x.append(dist)
        graf2x.append(cabal)
        graf2y.append(dist)
    variables()
width=0.25
plt.figure(1)
plt.bar(graf1y,graf1x, width=width, color="magenta")
plt.scatter(graf1y,graf1x, color="blue")
plt.plot(graf1y, graf1x, color="red")
plt.ylabel("Distancia")
plt.xlabel("Tiempo")
plt.title("Distancia sobre tiempo")
plt.show()

plt.figure(2)
plt.bar(graf2y, graf2x, color="magenta")
plt.scatter(graf2y,graf2x, color="blue")
plt.plot(graf2y,graf2x, color="red")
plt.ylabel("objeto 1")
plt.xlabel("objeto 2")
plt.title("Distancia objeto 1 a objeto 2")
plt.show()

