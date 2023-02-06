#Jean Marco Fernandez Silva
#proyecto Final
import random
CJ1=0
CJ2=0
J1 =True
J2=False
while  CJ1<50 or CJ2<50 :
    Tu=True
    if Tu==J1:
        dado= random.randint (1,6)
        print("salio el dado",dado)
        if dado==1:
            for i in range (1,4):
                print("salio uno otra vez tira el dado")
                print("El dado salio", dado)
        else:
            Tu=False
        CJ1=CJ1+dado
        print("las casillas que avanzas es ",CJ1)
        print("es turno del jugador 2")
        if Tu==J2:
            dado= random.randint (1,6)
            print("salio el dado",dado)
            if dado==1:
                for i in range (1,4):
                    print("salio uno otra vez tira el dado")
                    print("El dado salio", dado)
            else:
                Tu=True
            CJ2=CJ2+dado
            print("las casillas que avanzas es ",CJ2)
            print("es turno del jugador 1")
    if CJ1%10==0 and J1==Tu:
        i1dado=random.randint (1,6)
        i2dado=random.randint (1,6)
        mul=i1dado*i2dado
        print("La multiplicacion ",i1dado,"*",i2dado,"=?")
        Res=int(input("Introducir la respuesta "))
        if Res==mul:
            CJ1=CJ1+5
            print("Respuesta correcta tienes 5 puntos mas ")
            print("las casillas que avanzas es ",CJ1)
            Tu=False
            print("Turno del Jugador 2")
        else:
            Tu=False
            print("Turno del Jugador 2")
    if CJ2%10==0 and Tu==J2:
        i1dado=random.randint (1,6)
        i2dado=random.randint (1,6)
        mul1=i1dado*i2dado
        print("La multiplicacion ",i1dado,"*",i2dado,"=?")
        Res1=int(input("Introducir la respuesta "))
        if Res1==mul1:
            CJ2=CJ2+5
            print("Respuesta correcta tienes 5 puntos mas ")
            print("las casillas que avanzas es ",CJ2)
            Tu=True
            print("Turno del Jugador 1")
        else:
            Tu=True
            print("Turno del Jugador 1")
    if CJ1%CJ1==0 and J1==Tu:
        i32dado=random.randint (1,6)
        i42dado=random.randint (1,6)
        if i32dado>i42dado:
            res2=i32dado-i42dado
            print(" La resta de ",i32dado,"-",i42dado,"=?")
            resp2=int(input("introducir la respuesta "))
            if res2==resp2:
                print("la respuesta es correcta ")
                CJ1=CJ1+5
                print("las casillas que avanzas es ",CJ1)
                Tu=False
                print("Turno del Jugador 2")
            else:
                Tu=False
                print("Turno del Jugador 2")
    if CJ2%CJ2==0 and Tu==J2:
        i12dado=random.randint (1,6)
        i22dado=random.randint (1,6)
        while i12dado>i22dado:
            res3=i12dado-i22dado
            print(" La resta de ",i12dado,"-",i22dado,"=?")
            resp3=int(input("introducir la respuesta "))
            if res3==resp3:
                print("la respuesta es correcta ")
                CJ2=CJ2+5
                print("las casillas que avanzas es ",CJ2)
                Tu=True
                print("Turno del Jugador 1")
            else:
                Tu=True
                print("Turno del Jugador 1")
    if CJ1%2==0 and J1==Tu:
        i13dado=random.randint (1,6)
        i23dado=random.randint (1,6)
        if i13dado>i23dado:
            div=i13dado//i23dado
            print("La division es ",i13dado,"/",i23dado, "=?")
            resu=int(input("Introducir la respuesta "))
            if resu==div:
                print("la respuesta es correcta ")
                CJ1=CJ1+7
                print("las casillas que avanzas es ",CJ1)
                Tu=False
                print("Turno del Jugador 2")
            else:
                print("la respuesta es incorrecta ")
                CJ1=CJ1+0
                print("las casillas que avanzas es ",CJ1)
                Tu=False
                print("Turno del Jugador 2")
    else:
        datos1=random.randint (1,10)
        datos2=random.randint (1,10)
        while datos1>datos2:
            resta=datos1-datos2
            print(" La resta de ",datos1,"-",datos2,"=?")
            reso=int(input("Introducir la respuesta correcta"))
            suma=datos1+datos2
            print(" La resta de ",datos1,"+",datos2,"=?")
            reso2=int(input("Introducir la respuesta correcta"))
            if resta==reso and suma==reso2:
                print("La respuesta esta correcta ")
                CJ1=CJ1+3
                print("las casillas que avanzas es ",CJ1)
                Tu=False
                print("Turno del Jugador 2")
            else:
                print(" oh no hizo todos mal o falló en un uno, cambia turno ")
                CJ1=CJ1+0
                print("las casillas que avanzas es ",CJ1)
                Tu=False
                print("Turno del Jugador 2")
    if CJ2%2==0 and J2==Tu:
        i13dado=random.randint (1,6)
        i23dado=random.randint (1,6)
        if i13dado>i23dado:
            div=i13dado//i23dado
            print("La division es ",i13dado,"/",i23dado, "=?")
            resu=int(input("Introducir la respuesta "))
            if resu==div:
                print("la respuesta es correcta ")
                CJ2=CJ2+7
                print("las casillas que avanzas es ",CJ2)
                Tu=True
                print("Turno del Jugador 1")
            else:
                print("la respuesta es incorrecta ")
                CJ2=CJ2+0
                print("las casillas que avanzas es ",CJ2)
                Tu=True
                print("Turno del Jugador 1")
    else:
        datos1=random.randint (1,10)
        datos2=random.randint (1,10)
        if datos1>datos2:
            resta=datos1-datos2
            print(" La resta de ",datos1,"-",datos2,"=?")
            reso=int(input("Introducir la respuesta correcta"))
            suma1=datos1+datos2
            print(" La resta de ",datos1,"+",datos2,"=?")
            reso2=int(input("Introducir la respuesta correcta"))
            if resta==reso and suma1==reso2:
                print("La respuesta esta correcta ")
                CJ2=CJ2+3
                print("las casillas que avanzas es ",CJ2)
                Tu=True
                print("Turno del Jugador 1")
            else:
                print(" oh no hizo todos mal o falló en un uno, cambia turno ")
                CJ2=CJ2+0
                print("las casillas que avanzas es ",CJ2)
                Tu=True
                print("Turno del Jugador 1")
if CJ1>CJ2:          
    print("El Ganador es el jugador 1")
else:
    print("El Ganador es el jugador 2")
    
    
        
        
    


    
    
