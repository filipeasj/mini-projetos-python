import os
import time


class Cronometro:
    def __init__(self, horas=0, minutos=0, segundos=0):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def __repr__(self):
        return f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}"
    
    def incrementar(self):
        self.segundos += 1
        if self.segundos >=60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos >=60:
            self.minutos = 0
            self.horas += 1
    
    def zerar(self):
        self.horas = 0
        self.minutos = 0
        self.segundos = 0

    def start(self):
        while True:
            os.system('cls')
            print(self)
            self.incrementar()
            time.sleep(1)

cronometro1 = Cronometro()
cronometro1.start()