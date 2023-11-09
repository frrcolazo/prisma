def obtener_medidas():
    unidad = input("Seleccione la unidad de medida de sus dimensiones:\n1 -> metros\n2 -> pies\n3 -> pulgadas\n4 -> centímetros")
    while unidad not in ["1", "2", "3", "4"]:
        unidad = input("Seleccione la unidad de medida de sus dimensiones:\n1 -> metros\n2 -> pies\n3 -> pulgadas\n4 -> centímetros")
    largo = float(input("Ingrese el largo de la superficie que va a usar: "))
    ancho = float(input("Ingrese el ancho de la superficie que va a usar: "))
    espesor = float(input("Ingrese el espesor de la superficie que va a usar: "))

    if unidad == "2":
        largo *= 0.3048
        ancho *= 0.3048
        espesor *= 0.3048
    elif unidad == "3":
        largo *= 0.0254
        ancho *= 0.0254
        espesor *= 0.0254
    elif unidad == "4":
        largo *= 0.01
        ancho *= 0.01
        espesor *= 0.01

    return largo, ancho, espesor

precio_tipo1 = 1000
precio_tipo2 = 900
precio_tipo3 = 800
precio_tipo4 = 700
precio_tipo5 = 600

nombre = input("Ingrese su nombre: ")
fecha = input("Ingrese la fecha en formaro dd/mm/aa: ")
try:
    largo, ancho, espesor = obtener_medidas()
except ValueError:
    print("EL VALOR INGRESADO ES INCORRECTO: ")
    largo, ancho, espesor = obtener_medidas()

volumen = round((largo * ancho * espesor), 2)

dosificacion = [["1:2:2", 3500, 246, 420, 0.67, 0.67, 220],
                ["1:2:3", 3000, 210, 350, 0.56, 0.84, 180],
                ["1:2:4", 2500, 175, 300, 0.48, 0.96, 170],
                ["1:3:4", 2000, 140, 260, 0.63, 0.84, 170],
                ["1:3:6", 1500, 105, 210, 0.50, 1.00, 160]]

despedicio_cemento = 1.05

tipo_concreto = input("Seleccione el número de la resistencia de concreto que desea:\n1 -> 1:2:2 = 3500 Psi = 246 Kg/cm2 \n2 -> 1:2:3 = 3000 Psi = 210 Kg/cm2\n3 ->1:2:4 = 2500 Psi = 175 Kg/cm\n4 ->1:3:4 = 2000 Psi = 140 Kg/cm\n5 ->1:3:6 = 1500 Psi = 105 Kg/cm ")
while tipo_concreto != "1" and tipo_concreto != "2" and tipo_concreto != "3" and tipo_concreto != "4" and tipo_concreto != "5":
    tipo_concreto = input("Seleccione el número de la resistencia de concreto que desea:\n1 -> 1:2:2 = 3500 Psi = 246 Kg/cm2 \n2 -> 1:2:3 = 3000 Psi = 210 Kg/cm2\n3 ->1:2:4 = 2500 Psi = 175 Kg/cm\n4 ->1:3:4 = 2000 Psi = 140 Kg/cm\n5 ->1:3:6 = 1500 Psi = 105 Kg/cm ")
if tipo_concreto == "1":
        cemento = round((volumen * dosificacion[0][3] * despedicio_cemento), 2)
        arena = round(volumen * dosificacion[0][4], 2)
        grava = round(volumen * dosificacion[0][5], 2)
        agua = round(volumen * dosificacion[0][6], 2)
        precio = volumen*precio_tipo1
elif tipo_concreto == "2":
        cemento = round((volumen * dosificacion[1][3] * despedicio_cemento), 2)
        arena = round(volumen * dosificacion[1][4], 2)
        grava = round(volumen * dosificacion[1][5], 2)
        agua = round(volumen * dosificacion[1][6], 2)
        precio = volumen * precio_tipo2
elif tipo_concreto == "3":
        cemento = round((volumen * dosificacion[2][3] * despedicio_cemento), 2)
        arena = round(volumen * dosificacion[2][4], 2)
        grava = round(volumen * dosificacion[2][5], 2)
        agua = round(volumen * dosificacion[2][6], 2)
        precio = volumen * precio_tipo3
elif tipo_concreto == "4":
        cemento = round((volumen * dosificacion[3][3] * despedicio_cemento), 2)
        arena = round(volumen * dosificacion[3][4], 2)
        grava = round(volumen * dosificacion[3][5], 2)
        agua = round(volumen * dosificacion[3][6], 2)
        precio = volumen * precio_tipo4
elif tipo_concreto == "5":
        cemento = round((volumen * dosificacion[4][3] * despedicio_cemento), 2)
        arena = round(volumen * dosificacion[4][4], 2)
        grava = round(volumen * dosificacion[4][5], 2)
        agua = round(volumen * dosificacion[4][6], 2)
        precio = volumen * precio_tipo5

print("---------------------------------------")
print("Nombre: ",nombre,"\nFecha: ",fecha,"\nCantidad de hormigón: ",volumen,"m3", "\nPrecio: $",round(precio,2))
print("---------------------------------------")

rta = 'Cliente:' + str(nombre) + ' Volumen: ' + str(volumen) + ' Precio ' + str(round(precio,2)) + ' Fecha: ' + fecha
f = open("Empresa.txt", "a")
f.write(rta + '\n')
f.close()
j = open("Cliente.txt", "w")
j.write("Nombre: " + nombre + '\n' + "Fecha: " + fecha + '\n' + 'Largo: ' + str(round(largo,2)) + 'm\n' + 'Ancho: ' + str(round(ancho,2)) + 'm\n' + 'Espesor: ' + str(round(espesor,2)) + 'm\n' + 'Cantidad de hormigón: ' + str(volumen) + 'm3\n' + "Precio : $" + str(round(precio,2)) + '\n')
j.close()
