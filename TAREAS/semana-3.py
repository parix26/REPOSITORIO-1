def ejercicio_1_1():
    """Es el protocolo seguro o inseguro?"""
    # DESCRIPCION:
    #   Seguros:   HTTPS, SSH, SFTP, FTPS
    #   Inseguros: HTTP, Telnet, FTP
    #   Cualquier otro -> "Desconocido".
    # PISTA: combine condiciones con "or", o use varios elif.
    print("\n--- Ejercicio 1.1: Protocolo seguro ---")

    protocolo = "HTTPS"   # cambie este valor para probar

    # TODO: complete el codigo aqui

    protocolo = "HTTP"

    if protocolo == "HTTPS" or protocolo == "SSH" or protocolo == "SFTP" or protocolo == "FTPS":
        print(f"El protocolo {protocolo} es SEGURO")

    elif protocolo == "HTTP" or protocolo == "Telnet" or protocolo == "FTP":
        print(f"El protocolo {protocolo} es INSEGURO")

    else:
        print(f"El protocolo {protocolo} es DESCONOCIDO")

    # SALIDA ESPERADA con protocolo = "HTTPS":
    # El protocolo HTTPS es SEGURO
    #
    # SALIDA ESPERADA con protocolo = "Telnet":
    # El protocolo Telnet es INSEGURO
    #
    # SALIDA ESPERADA con protocolo = "SMTP":
    # El protocolo SMTP es DESCONOCIDO




def ejercicio_1_2():
    """Categorizar uso de CPU."""
    # DESCRIPCION:
    #   < 50%       -> "Estado: NORMAL"
    #   50% - 79%   -> "Estado: ADVERTENCIA - monitorear"
    #   80% - 94%   -> "Estado: CRITICO - revisar procesos"
    #   >= 95%      -> "Estado: EMERGENCIA - intervenir YA"
    # PISTA: if / elif / else con operadores >= y <.
    print("\n--- Ejercicio 1.2: Uso de CPU ---")

    uso_cpu = 85   # porcentaje, entre 0 y 100

    # TODO: complete el codigo aqui

    print(f"Uso de CPU: {uso_cpu}%")

    if uso_cpu >= 95:
        print("Estado: EMERGENCIA - intervenir YA")

    elif uso_cpu >= 80:
        print("Estado: CRITICO - revisar procesos")

    elif uso_cpu >= 50:
        print("Estado: ADVERTENCIA - monitorear")

    else:
        print("Estado: NORMAL")

    # SALIDA ESPERADA con uso_cpu = 85:
    # Uso de CPU: 85%
    # Estado: CRITICO - revisar procesos


def ejercicio_1_3():
    """Tipo de puerto segun rango TCP/UDP."""
    # DESCRIPCION:
    #   0 - 1023        -> "Puerto bien conocido"
    #   1024 - 49151    -> "Puerto registrado"
    #   49152 - 65535   -> "Puerto dinamico/privado"
    #   fuera de 0-65535 -> "Puerto INVALIDO"
    print("\n--- Ejercicio 1.3: Tipo de puerto ---")

    puerto = 8080   # cambie este valor para probar

    # TODO: complete el codigo aqui

    puerto = 22
    if puerto >= 0 and puerto <= 1023:
        print(f"Puerto {puerto}: Puerto bien conocido")

    elif puerto >= 1024 and puerto <= 49151:
        print(f"Puerto {puerto}: Puerto registrado")

    elif puerto >= 49152 and puerto <= 65535:
        print(f"Puerto {puerto}: Puerto dinamico/privado")

    else:
        print(f"Puerto {puerto}: Puerto INVALIDO")

    # SALIDA ESPERADA con puerto = 8080:
    # Puerto 8080: Puerto registrado
    #
    # SALIDA ESPERADA con puerto = 22:
    # Puerto 22: Puerto bien conocido


def ejercicio_1_4():
    """Control de acceso por horario."""
    # DESCRIPCION:
    #   Permitir si TODAS:
    #     - rol == "admin"
    #     - 8 <= hora_actual <= 18
    #     - cuenta_bloqueada == False
    #   En cualquier otro caso: "Acceso denegado" indicando el motivo.
    # PISTA: operadores logicos "and" y "not", o ifs anidados.
    print("\n--- Ejercicio 1.4: Control de acceso ---")

    rol = "admin"
    hora_actual = 10
    cuenta_bloqueada = False

    # TODO: complete el codigo aqui

    rol = "admin"
    hora_actual = 10
    cuenta_bloqueada = False

    if rol != "admin":
        print("Acceso denegado - rol sin privilegios")

    elif hora_actual < 8 or hora_actual > 18:
        print("Acceso denegado - fuera de horario")

    elif cuenta_bloqueada:
        print("Acceso denegado - cuenta bloqueada")

    else:
        print("Acceso permitido")

    # SALIDA ESPERADA con los valores actuales:
    # Acceso permitido
    #
    # Pruebe cambiando: rol = "invitado"
    # Acceso denegado - rol sin privilegios


def ejercicio_1_5():
    """Clase de IP segun primer octeto (clasificacion historica)."""
    # DESCRIPCION:
    #   1 - 126   -> "Clase A"
    #   128 - 191 -> "Clase B"
    #   192 - 223 -> "Clase C"
    #   224 - 239 -> "Clase D (Multicast)"
    #   240 - 255 -> "Clase E (Experimental)"
    #   127       -> "Loopback"
    #   0 o > 255 -> "Octeto invalido"
    print("\n--- Ejercicio 1.5: Clase de IP ---")

    primer_octeto = 192   # cambie este valor para probar

    # TODO: complete el codigo aqui

    primer_octeto = 192

    if primer_octeto == 127:
        print(f"Octeto {primer_octeto} -> Loopback")

    elif primer_octeto <= 0 or primer_octeto > 255:
        print(f"Octeto {primer_octeto} -> Octeto invalido")

    elif primer_octeto >= 1 and primer_octeto <= 126:
        print(f"Octeto {primer_octeto} -> Clase A")

    elif primer_octeto >= 128 and primer_octeto <= 191:
        print(f"Octeto {primer_octeto} -> Clase B")

    elif primer_octeto >= 192 and primer_octeto <= 223:
        print(f"Octeto {primer_octeto} -> Clase C")

    elif primer_octeto >= 224 and primer_octeto <= 239:
        print(f"Octeto {primer_octeto} -> Clase D (Multicast)")

    else:
        print(f"Octeto {primer_octeto} -> Clase E (Experimental)")

    # SALIDA ESPERADA con primer_octeto = 192:
    # Octeto 192 -> Clase C
    #
    # SALIDA ESPERADA con primer_octeto = 127:
    # Octeto 127 -> Loopback


# =============================================================================
#  AUTOEVALUACION
# =============================================================================
#  Marque con una X los que pudo completar SIN ayuda:
#     [X] 1.1   [X] 1.2   [_] 1.3   [X] 1.4   [_] 1.5
# =============================================================================


# =============================================================================
#  MAIN
# =============================================================================
def main():
    print("=" * 60)
    print("PRACTICA - SEMANA 3 - PARTE 1: CONDICIONALES")
    print("=" * 60)

    ejercicio_1_1()
    ejercicio_1_2()
    ejercicio_1_3()
    ejercicio_1_4()
    ejercicio_1_5()

    print("\n" + "=" * 60)
    print("FIN PRACTICA 1 - Continuar con: practica_02_bucles_for.py")
    print("=" * 60)
    
if __name__ == "__main__":
    main()