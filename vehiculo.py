class Vehiculo:
    DISTANCIA_BASE=12
    FACTOR_EMISION_GASOLINA=2.196
    FACTOR_EMISION_DIESEL=2.471
    def __init__(self, placa, color, marca, modelo, combustible, km, tanque, AC):
        self.placa = placa
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.km = km
        self.tanque = tanque
        self.Ac = AC
        self.encendido = True
        self.litros_consumidos = 0 

    # def encender(self):
    #     if self.encendido==False:
    #         self.encendido = True
    #     else:
    #         print("el vehiculo ya esta encendido")

    # def apagar(self):
    #     self.encendido = False

    def tocar_bocina(self):
        print("piii piii")

    def frenar(self):
        print("Frenando...")

    def obtener_combustible(self):
        return self.tanque

    def mostrar_vehiculo(self):
        print("la placa es " + self.placa)
        print("el color es " + self.color)
        print("la marca es "+ self.marca)
        print("el tipo de combustible es " + self.combustible)
        print("km"+ str(self.km))
        print("la capacidad del tanque es de lt"+ str(self.tanque))
        print("aire acondicionado...")
        if self.encendido==True:
            print("el auto esta encendido")
        else:
            print("el auto no esta encendido")

    def recorrer_distancia(self,distancia):
        if self.motor.esta_encendido():
            variante=self.obtener_variante()
            print("variante", str(variante))
            if distancia<(variante*self.tanque):
                self.km +=distancia
                total_litros=round(distancia/variante,2)
                self.litros_consumidos+=total_litros
                self.tanque -=total_litros
                print("recorriendo {} kilometros".format(distancia))
            else:
                print("necesita mas combustible")
        else:
            print("el vehiculo no esta encendido")

    def cargar_combustible(self,litros):
        self.tanque+=litros
        print("cargando combustible")
        print(self.tanque)
            #recorrer distancia
            #cargar combustible

    def calcular_CO2(self):
        variante=self.obtener_variante()
        litros_consumidos=(self.km/variante)
        if self.combustible=="Diesel":
            CO2=round(litros_consumidos*self.FACTOR_EMISION_DIESEL,2)
            #print("la cantidad de CO2 es de...", str(CO2),"Kg")
            return CO2
        else:
            CO2=round(litros_consumidos*self.FACTOR_EMISION_GASOLINA,2)
            #print("la cantidad de CO2 es de...", str(CO2),"Kg")
            return CO2

    def poner_motor(self, motor):
        self.motor=motor
        
    def obtener_variante(self):
        cilindrada=self.motor.obtener_cilindrada()
        print("cilindrada", str(cilindrada))
        if cilindrada==1000:
            return 12
        elif cilindrada==2000:
            return 10
        else:
            return 8

    def hay_combustible(self, distancia):
        variante=self.obtener_variante()
        if not distancia<(variante*self.tanque):
            return False
        else:
            return True

    def obtener_informe(self):
        informe="\n-----------------"
        informe +="\n INFORME FINAL-EMISION CO2"
        informe +="\n----------------"
        informe +="\n UD esta conduciendo un vehiculo marca {}, modelo {}, color {}".format(self.marca, self.modelo, self.color)
        informe +="\n Ha recorido un total de {}km de distancia".format(self.km)
        informe +="\n Ha consumido un total de {}ltrs de {}".format(self.litros_consumidos, self.combustible)
        informe +="\n fn su tanque tiene {}ltrs de {}".format(self.tanque,self.combustible)
        informe +="\n Se emitio a la atmosfera un total de {}kg de CO2".format(round(self.calcular_CO2()),2)
        return informe