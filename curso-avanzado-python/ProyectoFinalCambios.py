import random

Jugando = True

Turno = True
J1Jugando = True
J2Jugando = False

Casilla = 0
CJ1=0
CJ2=0

dado = 0

while dado != 1:
  tiroInicial = 0
  while tiroInicial < 3:
    dado = random.randint(1,6)
    if dado == 1:
      break
    tiroInicial = tiroInicial + 1
    if tiroInicial >= 3:
      if Turno == J1Jugando:
        Turno = False
      else :
        Turno = True
      break
  if dado == 1:
    break

if Turno == J1Jugando:
  print('Comienza Jugador 1')
if Turno == J2Jugando:
  print('Comienza Jugador 2')

while  CJ1<50 and CJ2<50:

  if Turno == J1Jugando:
    print('******************** Turno Jugador 1 ********************')
  if Turno == J2Jugando:
    print('******************** Turno Jugador 2 ********************')

  dado = random.randint (1,6)

  print('Valor de lanzamiento de dado: ' + str(dado))

  if Turno == J1Jugando:
    CJ1= CJ1 + dado
    print('Casilla Jugador 1: ' + str(CJ1))
  if Turno == J2Jugando:
    CJ2 = CJ2 + dado
    print('Casilla Jugador 2: ' + str(CJ2))

  if CJ1%10==0 and Turno==J1Jugando:
    print('***** Casilla Jugador 1 es Multiplo de 10 *****')
    i1dado=random.randint (1,6)
    i2dado=random.randint (1,6)
    mul=i1dado*i2dado
    print("La multiplicacion ",i1dado,"*",i2dado,"= ?")
    Res=int(input("Introducir la respuesta "))
    if Res==mul:
      CJ1=CJ1+5
      print("Respuesta correcta avanza 5 casillas ")
      print("Avanza a la casilla ",CJ1)
      Turno=False
    else:
      print("Respuesta Incorrecta ")
      Turno=False
    continue

  if CJ2%10==0 and Turno==J2Jugando:
    print('***** Casilla Jugador 2 es Multiplo de 10 *****')
    i1dado=random.randint (1,6)
    i2dado=random.randint (1,6)
    mul=i1dado*i2dado
    print("La multiplicacion ",i1dado,"*",i2dado,"= ?")
    Res=int(input("Introducir la respuesta "))
    if Res==mul:
      CJ2=CJ2+5
      print("Respuesta correcta avanza 5 casillas ")
      print("Avanza a la casilla ",CJ2)
      Turno=True
    else:
      print("Respuesta Incorrecta ")
      Turno=True
    continue

  if Turno == J1Jugando:
    esPrimo = True
    for i in range(2, CJ1):
      if CJ1%i == 0:
        esPrimo = False
      
    if esPrimo:
      print('***** Casilla Jugador 1 es Numero Primo *****')
      i32dado=random.randint (1,6)
      i42dado=random.randint (1,6)
      if i32dado>=i42dado:
        print(" La resta de ",i32dado,"-",i42dado,"=?")
        res2=i32dado-i42dado
      elif i42dado>i32dado:
        print(" La resta de ",i42dado,"-",i32dado,"=?")
        res2=i42dado-i32dado
      resp2=int(input("introducir la respuesta "))
      if res2==resp2:
        print("Respuesta correcta avanzas 5 casillas ")
        CJ1=CJ1+5
        print("Avanza a la casilla ",CJ1)
        Turno=False
      else:
        print("Respuesta Incorrecta ")
        Turno=False
      continue

  if Turno == J2Jugando:
    esPrimo = True
    for i in range(2, CJ2):
      if CJ2%i == 0:
        esPrimo = False
      
    if esPrimo:
      print('***** Casilla Jugador 2 es Numero Primo *****')
      i32dado=random.randint (1,6)
      i42dado=random.randint (1,6)
      if i32dado>=i42dado:
        print(" La resta de ",i32dado,"-",i42dado,"=?")
        res2=i32dado-i42dado
      elif i42dado>i32dado:
        print(" La resta de ",i42dado,"-",i32dado,"=?")
        res2=i42dado-i32dado
      resp2=int(input("introducir la respuesta "))
      if res2==resp2:
        print("Respuesta correcta avanzas 5 casillas ")
        CJ2=CJ2+5
        print("Avanza a la casilla ",CJ2)
        Turno=True
      else:
        print("Respuesta Incorrecta ")
        Turno=True
      continue

  if CJ1!=0 and Turno==J1Jugando:
    if CJ1%10!=0:
      if CJ1%2==0:
        print('***** Casilla Jugador 1 es Par *****')
        i13dado=random.randint (1,6)
        i23dado=random.randint (1,6)
        if i13dado>=i23dado:
          print(" La division de ",i13dado,"/",i23dado,"=?")
          div=i13dado//i23dado
        elif i23dado>i13dado: 
          print(" La division de ",i23dado,"/",i13dado,"=?")
          div=i23dado//i13dado
        
        resu=int(input("Introducir la respuesta "))
        if resu==div:
          print("Respuesta correcta avanzas 7 casillas ")
          CJ1=CJ1+7
          print("Avanza a la casilla ",CJ1)
          Turno=False
        else:
          print("La respuesta es incorrecta ")
          Turno=False
      else:
        print('***** Casilla Jugador 1 es Impar *****')
        datos1=random.randint (1,10)
        datos2=random.randint (1,10)
        if datos1>=datos2:
          print(" La resta de ",datos1,"-",datos2,"=?")
          resta=datos1-datos2
        elif datos2>datos1:
          print(" La resta de ",datos2,"-",datos1,"=?")
          resta=datos2-datos1
        reso=int(input("Introducir la respuesta correcta: "))

        suma=datos1+datos2
        print(" La suma de ",datos1,"+",datos2,"=?")
        reso2=int(input("Introducir la respuesta correcta: "))

        if resta==reso and suma==reso2:
            CJ1=CJ1+3
            print("Respuesta correcta avanzas 3 casillas ")
            print("Avanza a la casilla ",CJ1)
            Turno=False
        else:
            print("Oh no hizo todos mal o falló en un uno, cambia turno ")
            Turno=False
    continue

  if CJ2!=0 and Turno==J2Jugando:
    if CJ2%10!=0:
      if CJ2%2==0:
        print('***** Casilla Jugador 2 es Par *****')
        i13dado=random.randint (1,6)
        i23dado=random.randint (1,6)
        if i13dado>=i23dado:
          print(" La division de ",i13dado,"/",i23dado,"=?")
          div=i13dado//i23dado
        elif i23dado>i13dado: 
          print(" La division de ",i23dado,"/",i13dado,"=?")
          div=i23dado//i13dado
        
        resu=int(input("Introducir la respuesta "))
        if resu==div:
          print("Respuesta correcta avanzas 7 casillas ")
          CJ2=CJ2+7
          print("Avanza a la casilla ",CJ2)
          Turno=True
        else:
          print("La respuesta es incorrecta ")
          Turno=True
      else:
        print('***** Casilla Jugador 2 es Impar *****')
        datos1=random.randint (1,10)
        datos2=random.randint (1,10)
        if datos1>=datos2:
          print(" La resta de ",datos1,"-",datos2,"=?")
          resta=datos1-datos2
        elif datos2>datos1:
          print(" La resta de ",datos2,"-",datos1,"=?")
          resta=datos2-datos1
        reso=int(input("Introducir la respuesta correcta: "))

        suma=datos1+datos2
        print(" La suma de ",datos1,"+",datos2,"=?")
        reso2=int(input("Introducir la respuesta correcta: "))

        if resta==reso and suma==reso2:
            CJ2=CJ2+3
            print("Respuesta correcta avanzas 3 casillas ")
            print("Avanza a la casilla ",CJ2)
            Turno=True
        else:
            print("Oh no hizo todos mal o falló en un uno, cambia turno ")
            Turno=True
    continue
  
if CJ1 >= 50 :
  print('Jugador 1 Gano!!!')
if CJ2 >= 50 :
  print('Jugador 2 Gano!!!')
