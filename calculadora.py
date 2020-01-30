class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1=numero1
        self.numero2=numero2

    def sumar(self):
        try:
            respuesta=(self.numero1+self.numero2)
            print("la suma de {}+{} es... {}".format(self.numero1, self.numero2, respuesta))
        except TypeError:
            print("El tipo de dato debe ser numerico")
        except:
            print("Error al sumar")

    def restar(self):
        try:
            respuesta=(self.numero1-self.numero2)
            print("la resta de {}-{} es... {}".format(self.numero1, self.numero2, respuesta))
        except TypeError:
            print("El tipo de dato debe ser numerico")
        except:
            print("Error al restar")

    def multiplicar(self):
        try:
            respuesta=self.numero1*self.numero2
            print("la multiplicacion de {}*{} es... {}".format(self.numero1, self.numero2, respuesta))
        except TypeError:
            print("El tipo de dato debe ser numerico")
        except:
            print("Error al multiplicar")

    def dividir(self):
        try:
            respuesta=(self.numero1/self.numero2)
            print("la division de {}/{} es... {}".format(self.numero1, self.numero2, respuesta))
        except ZeroDivisionError:
            print("No se puede dividir entre 0")
        except TypeError:
            print("El tipo de dato debe ser numerico")
        except:
            print("Error al dividir")

    def sacar_exponente(self):
        try:
            respuesta=(self.numero1**self.numero2)
            print("El exponente de {}**{} es... {}".format(self.numero1,self.numero2, respuesta))
        except TypeError:
            print("El tipo de dato debe ser numerico")
        except:
            print("Error al sacar exponente")