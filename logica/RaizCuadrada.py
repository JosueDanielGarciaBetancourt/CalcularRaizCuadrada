class RaizCuadrada():
    def __init__(self, num, cant_iteraciones):
        self.num = num
        self.cant_iteraciones = cant_iteraciones
        self.x = 1.0

    def calcular (self):
        for self.k in range(1, self.cant_iteraciones+1):
            self.x = (self.x + self.num/self.x) / 2

    def imprimir (self):
         print(f"La raiz cuadrada de {self.num} después de {self.cant_iteraciones} iteraciones es {self.x}\n")