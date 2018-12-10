#ARIAS RAMIREZ VICTORIA ANGÉLICA
import sys
class Cuenta:
  
  def __init__(self,cantidad):
   
    self.cantidad= cantidad
  
  def depositar(self,valor):
  
    if valor>0:
      print("\nSe ha hecho un depósito de $"+ str(valor)+ " de su cuenta\n\n")
  
  
      self.cantidad=self.cantidad+valor
      
    else:
  
      print("El valor a depositar es incorrecto")
    
  def retirar (self,valor):
    
    if valor>0:
      if valor<=self.cantidad:

        self.cantidad=self.cantidad-valor
        print("\nSe ha hecho un retiro de $"+ str(valor)+ " de su cuenta\n\n")
      else:
        print("Saldo insuficiente")
    else:
      print("Cantidad errónea")

  def getCantidad(self):
      print ("EL saldo de su tarjeta es: $" + str(self.cantidad))
  
  def __str__(self):
    #con ééste méétodo ya podemos imprimir llamando al objeto únicamente
    return "La cantidad de su cuenta es: " + str(self.cantidad)
