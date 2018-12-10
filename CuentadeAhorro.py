#ARIAS RAMIREZ VICTORIA ANGÉLICA
from Cuenta import*
class CuentaDeAhorro(Cuenta):

  def __init__ (self,SaldoInicial,TasadeInteres,tipo):
    Cuenta.__init__(self,SaldoInicial)
    self.__TasadeInteres= TasadeInteres
    self.__tipo=tipo

  def getTipo(self):
    return self.__tipo

  def __str__(self):
    temp=Cuenta.__str__(self)
    temp+="\nLa tasa de interes que maneja esta tarjeta es de: " + str(self.__TasadeInteres)
    temp+="\nTipo de Tarjeta: "+str(self.__tipo)+"\n"
    return temp