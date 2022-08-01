print("""
                 Calculadora de IMC
""")

n=input("\t Introduzca su primer nombre: ")
c1=len(n)
if c1 <2:
    print("Ingrese un nombre valido")
if c1>2:
     apa=input("\t Introduzca su apellido paterno: ")
     c2=len(apa)

if c2<2:
    print("Ingrese un nombre valido")
if c1>2:
    ama=input("\t Introduzca su apellido materno: ")
    c3=len(ama)

if c3<2:
    print("Ingrese un dato valido")
if c3>2:
    e=int(input("\t ¿Cuántos años tiene?: "))
    
if e<0:
    print("Ingrese un dato valido")
if e>0:
    p=float(input("\t ¿Cuál es su peso en Kg?: "))

if p<0:
    print("Ingrese un dato valido")
if p>0:
    est=float(input("\t Introduce tu altura en metros: "))

if est<0:
    print("Ingrese un dato correcto")
if est>0:
    print("\t Nombre: "+n)
    print("\t Apellidos: "+apa, end=' ')
    print(ama)
    print("\t Edad: ",+e, "años")
    print("\t Peso: ",+p,"Kg")
    print("\t Estatura: ",+est,"m")
    print(f"\t Tu indice de masa coorporal es: {p/est**2:2f}")