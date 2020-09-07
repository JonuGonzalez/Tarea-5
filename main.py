cadena1 = '__servidor1'
cadena2 = '3servidor'
letra = 'abcdefghijklñmnopqrstuvwxyz'
numero = '1234567890'
def AFD(entrada):
    estado = 0
    for i in range(len(entrada)):
        if estado == 0:
            if  entrada[i] == '_':
                estado=1
            elif entrada[i] in letra:
                estado=2
            else:
                print('Cadena Invalida')
                return
        elif estado == 1:
            if  entrada[i] == '_':
                estado=1
            elif entrada[i] in letra:
                estado=3
            else:
                print('Cadena Invalida')
                return
        elif estado == 2:
            if  entrada[i] in letra:
                estado=2
            elif entrada[i] in numero:
                estado=4
            else:
                print('Cadena Invalida')
                return
        elif estado == 3:
            if  entrada[i] in letra:
                estado=3
            elif entrada[i] in numero:
                estado = 4
            else:
                print('Cadena Invalida')
                return
        elif estado == 4:
            print('Cadena Valida')

AFD(cadena1)
AFD(cadena2)