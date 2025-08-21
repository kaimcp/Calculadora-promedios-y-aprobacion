#Calculadora de promedio con tres notas eh indicar si aprueba o no ( >4 aprueba), Indicar si reprueba o aprueba.

def pedir_notas(numero):
    while True:
        try: 
            nota = float(input(f"Ingresa la nota {numero}: ")) 
            return nota    
        except ValueError:
            print("Caracter invalido, favor ingresar solo numeros")


nota1 =  pedir_notas(1)
nota2 =  pedir_notas(2)
nota3 =  pedir_notas(3)

promedio = round((nota1 + nota2 + nota3) /3, 2)

print(f"Tu promedio es: {promedio}")

if promedio > 4.0:
    print("Aprobaste el ramo")
else:
    print("Reprobaste el ramo, yei!")











