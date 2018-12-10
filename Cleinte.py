#ARIAS RAMIREZ VICTORIA ANGÉLICA
from Cuenta import*
class Cliente:

  def __init__(self,nomb,dire,edad,sexo):
  
    self.__nombre=nomb

    self.__direccion=dire
  
    self.__edad=edad

    self.sexo=sexo
  
    self.cuentas=[]

#nuevo métodos para que el cliente pueda tener más de una cuenta

  def AñadirCuenta(self,cuenta):
    self.cuentas.append(cuenta)
    print("El cliente "+self.__nombre+" agrego una nueva cuenta")

#Método para poder eliminar una cuenta de la lista de cuentas 

  def EliminarCuenta(self,cuenta):

    if cuenta in self.cuentas:  
        self.cuentas.remove(cuenta)
        print("El cliente "+self.__nombre+" ha eliminado una cuenta")
    else:
        print("La cuenta no existe")

  def getCuenta (self,index):
    for i in range(len(self.cuentas)):
      print (self.cuentas[index])

# imprime cuentas para ver toda la lista de las cuentas
  def  infoCuentas ( self ):
    print("\n\t\t *Información de las cuentas*\n")
    print("-Cantidad de cuentas que tiene: "+ str(len(self.cuentas))+"\n")
    for cuenta in self.cuentas:
      print(cuenta)


  def getNombre(self):
      return self.__nombre 

  def getCuentas(self):
      return self.cuentas 

  def getDireccion(self):
      return self.__direccion 
    
    #para poder ver que nuestra funcion set ha cambiado la direccióón
  
    
  def setDireccion(self,nuevadir):
  
      self.__direccion=nuevadir
    #aquí se implementó el set porque la dirección de un cliente puede modificarse en cualquier momento, sin embargo en los otros datos no es necesario porque son datos que no cambian-

   
  def __str__(self):
    
    temp="\n Nombre: "+str(self.__nombre)
    temp+="\n Direccion: "+str(self.__direccion)
    temp+="\n Edad: "+str(self.__edad)
    temp+="\n Sexo: "+ str(self.sexo)
   
    return temp