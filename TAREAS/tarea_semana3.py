
def protocolo_seguro():
   protocolo = input("Ingrese el proprotocolo: ")

   seguros = ["HTTPS", "SSH", "SFTP"]
   inseguros = ["HTTP", "Telnet", "FTP"]

   if protocolo in seguros:
       print("El protocolo ", protocolo, " es seguro")
   elif protocolo in inseguros:
       print("El protocolo ", protocolo, " es inseguro")
   else:
       print("Protocolo desconocido")

def puertos ():
    puerto = input("Ingrese el puerto: ")
    match puerto:
        case "22":
            print("puerto ", puerto, ": SSH")
        case "80":
            print("puerto ", puerto, ": HTTP")
        case "443":
            print("puerto ", puerto, ": HTTPS")
        case "3306":
            print("puerto ", puerto, ": MySQL")
        case "3389":
            print("puerto ", puerto, ": RDP")
        case _:
            print("puerto ", puerto, ": Servicio desocnocido")

def direcciones():
    print("Las subredes de la direccion 192.168.1.0/29 son: ")
    for r in range(0,8):
        print(f"192.168.1.{r}")

def inventario():
    dispositivos = ["Router Cisco", "Switch HP", "Firewall Fortinet", "Servidor Dell"]
    for r,b in enumerate(dispositivos, start=1):
        print(r,".  ",b)

def cuenta():
    cont=5
    while cont>=1:
        print("Apagado en ",cont)
        cont-=1
    print("Apagando servidor")

def conexion():
    intento = 1
    maximo = 5
    conectado = False

    while intento <= maximo and not conectado:

        if intento == 3:
            conectado = True
            print(f"Intento {intento}: conectado")
        else:
            print(f"Intento {intento}: sin respuesta")
            intento += 1  # <-- IMPRESCINDIBLE

def puerto_cerrado():

    puertos = [21, 22, 23, 25, 80]
    estados = ["abierto", "abierto", "abierto", "cerrado", "abierto"]

    for r,b in zip(puertos, estados):
        if b != "cerrado":
            print(f"Puerto {r}: {b}")
        else:
            print(f"Primer puerto {b}: {r}")
            break

def filtrar():
    ips_log = ["10.0.0.5", "200.0.0.1", "10.0.0.8", "45.33.32.156", "10.0.0.10"]
    blacklist = ["200.0.0.1", "45.33.32.156"]
    cont = 0
    for r in ips_log:

        if r in blacklist:
            continue
        else:
            print(f"Procesando {r}")
            cont+=1
    print(f"Total prrocesadas {cont}")

def buscar():
    inventario = ["Router-01", "Switch-A", "Firewall-FW1", "Servidor-Web"]
    buscar = "Firewall-FW1"

    obj=input("Ingrese el nombre del dispositivo: ")

    for dispositivo in inventario:
        if obj == buscar:
            print("Dispositivo encontrado")
            break
    else:
        print("Dispositivo desconocido")

def validar():
    ip=input("Ingrese la direccion ip: ")
    octetos=ip.split(".")

    if len(octetos)!=4:
        print(f"El numero de octetos es invalido")
        return


    for r in octetos:
        if not r.isdigit():
            print("La direccion contiene caracteres invalidos")
            break
        b=int(r)
        if b <0 or b > 255:
            print("El rango de numeros es invalido")
            break
    print("La direccion ip es correcta")

protocolo_seguro()
puertos()
direcciones()
inventario()
cuenta()
conexion()
puerto_cerrado()
filtrar()
buscar()
validar()