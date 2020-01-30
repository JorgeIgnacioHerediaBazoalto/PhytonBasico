from motor import Motor
from vehiculo import Vehiculo
from simulador import Simulador
motorJ1=Motor("1GD5DFS8", 2000)
motorJ2=Motor("215SDA86", 1000)

auto1 = Vehiculo("6945EXY", "rojo", "Lamborguini", "2019", "Gasolina", 1200, 60.5, True)
auto2 = Vehiculo("1234JHG", "negro", "nissan", "2004", "Gasolina", 1300, 75.2, False)
auto3 = Vehiculo("9875JYS", "blanco", "Suzuky", "2008", "Diesel", 700, 99.9, True)

auto1.poner_motor(motorJ1)
auto2.poner_motor(motorJ2)
auto3.poner_motor(motorJ2)

vehiculos_list=[auto1, auto2, auto3]

s=Simulador(vehiculos_list)
s.iniciar_simulacion(2)


from calculadora import Calculadora
Nums=Calculadora("3",5)
#Nums.sacar_exponente()
#Nums.sumar()
#Nums.restar()
Nums.multiplicar()
#Nums.dividir()