from logica.RaizCuadrada import RaizCuadrada

if __name__ == '__main__':
    num = float(input("Puedo hallar la raíz cuadrada a través del método de Herón ingresa un número:"))
    cant_iteraciones = int(input("Ingrese el número de iteraciones: "))

    raizCuadrada = RaizCuadrada(num, cant_iteraciones)
    raizCuadrada.calcular()
    raizCuadrada.imprimir()

