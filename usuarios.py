import funciones as fu

def usuario(nombre, clave):
    fu.registrar_usuario(nombre, clave)
    return()

if __name__ == '__main__':
    usuario('luis', 'luis')