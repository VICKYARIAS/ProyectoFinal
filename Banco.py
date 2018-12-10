#ARIAS RAMIREZ VICTORIA ANGÉLICA
from Cliente import *
class  Banco:
  def __init__(self,nom,ubic):

    self.__nombre=nom
    
    self.__ubicacion=ubic
    
    self.clientes=[]
  
  #nuevo métodos para que el banco pueda tener más de un cliente

  def AñadirCliente(self,cliente):
    self.clientes.append(cliente)
    print("Se ha agregado un nuevo cliente ")
    


  #Método para poder eliminar un cliente de la lista de clientes

  def EliminarCliente(self,cliente):

    if cliente in self.clientes:  
        self.clientes.remove(cliente)
        print("Se ha eliminado un cliente")
    else:
        print("El cliente no existe")


  def getCliente (self,index):
    return self.clientes[index]
    
  def getClientes (self):
    return self.clientes

 #Método que muestra toda la información de los cloientes que hay en el banco
  def  infoClientes ( self ):
    print("\n\t\t *Información de los clientes*\n")
    print("Cantidad de clientes que tiene el" + str(self.__nombre)+ ":" + str(len(self.clientes)))

    if len(self.clientes)!=0:
            print("Clientes registrados en el banco: ","\n")
            temp=""
            for i in range(len(self.clientes)):

              temp="Cliente "+str(i+1)+"\n\n"
              temp+="Nombre del cliente: "+clientes[i].getNombre()+"\n"
              temp+="Número de cuentas: "+str(len(self.clientes[i].getCuentas()))+"\n"
              print(temp)
    else:
            print("No hay clientes registrados en el Banco Patito")


  def __str__(self):
  
    cadena+=" El nombre del Banco es:" +str(self.__nombre)
    cadena+="\n Su Ubicación es: "+str(self.__ubicacion)
    return cadena
