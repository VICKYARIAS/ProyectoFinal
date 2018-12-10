#ARIAS RAMÍREZ VICTORIA ANGÉLICA
from Cuenta import*

class CuentaDeCredito(Cuenta):
  def __init__ (self,SaldoInicial, Sobregiro,TasadeInteres,tipo):
    Cuenta.__init__(self,SaldoInicial)

    self.__Sobregiro=Sobregiro
    
    self.__TasadeInteres= TasadeInteres
    
    self.__tipo=tipo                 

  def __str__(self):
    temp=Cuenta.__str__(self)
    temp+="\nLa cantidad de sobregiro con la que cuenta es de: " + str(self.__Sobregiro)
    temp+="\nLa tasa de interes que maneja esta tarjeta es de: " + str(self.__TasadeInteres)
    temp+="\nTipo de Tarjeta: "+str(self.__tipo)+"\n\n"
    return temp

  def getTipo(self):
    return self.__tipo
  
  def getSobregiro(self):
      return self.__Sobregiro

  def  retirar ( self, valor ):
        resultado = True
        
        if  self.cantidad < valor:

            # No hay saldo suficiente para cubrir la cantidad.
            # solicitado retirarse
            # Comprobar si hay suficiente en el sobregiro
            # protección (si existe)
            SobregiroNecesario = valor -  self.cantidad

            if  self.__Sobregiro < SobregiroNecesario:
                # No hay protección contra sobregiros o no es suficiente para cubrir
                # la cantidad necesaria
                print ( " No se pudo retirar,sobrepasa el límite " )
                resultado =  False
            else :
                # Sí, hay protección contra sobregiros y suficiente
                # para cubrir la cantidad
                self.cantidad =  0.0
                self.__Sobregiro-=SobregiroNecesario
                print("\nSe ha hecho un retiro de $"+ str(valor)+ " de su cuenta\n\n")


        else :     
            # Sí, hay saldo suficiente para cubrir la cantidad
            # Proceder como de costumbre
            self.cantidad =  self.cantidad - valor

            print("\nSe ha hecho un retiro de $"+ str(valor)+ " de su cuenta\n\n")
        
        return