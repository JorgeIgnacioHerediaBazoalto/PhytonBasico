class Motor:
    def __init__(self, nro_serie, cilindrada):
        self.nro_serie=nro_serie
        self.cilindrada=cilindrada
        self.encendido=False
    def encender(self):
        if self.encendido==False:
            self.encendido=True
        else:
            print("el motor ya esta encendido")
    
    def apagar(self):
        self.encendido=False
    
    def esta_encendido(self):
        # if self.encendido==False:
        #     print("NO")
        # else:
        #     print("SI")
        return self.encendido
    
    def obtener_cilindrada(self):
        return self.cilindrada