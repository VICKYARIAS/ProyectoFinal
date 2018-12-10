import sys
import os
from Banco import*
from Cliente import*
from CuentaDeAhorro import*
from CuentaDeCredito import*
import matplotlib.pyplot as plt
import random as r
import math as m


class MenuUsuario:
#ARIAS RAMIREZ VICTORIA ANGÉLICA

  def __init__ (self,nombre,ubicacion):

    self.banco = Banco(nombre,ubicacion)
    self.cliente=None
    self.cuenta=None
    self.CuentasCredito=[]
    self.CuentasAhorro=[]
    self.Mujeres=[]
    self.Hombres=[]

    self.Bienvenida= "\n******* Bienvenido ***********\n"

    self.opciones={

      "1": self.CrearunCliente,
      "2": self.IngresaraunCliente,
      "3": self.salir
    }
    self.opciones2={

      "1": self.retirar,
      "2": self.depositar,
      "3": self.ConsultarSaldo,
      "4": self.EliminarCuenta,
      "5": self.CorrerBanco,
      "6": self.salir
    }

    

  def MenuPrincipal(self):
    print("\n\n\t~~~~~~~~~Banco Patito~~~~~~~~")
    print("\n\n *Bienvenido* ","\n")
    print("Elija la opción adecuado a lo que desa: ","\n")

    self.CorrerBanco()

  def MostrarMenuBanco(self):
    print (""" 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     Menú del banco:
    1 Crear un Cliente
    2 Ingresar a la información de un Cliente
    3 Salir""")
  #Éste método muestra el menú y responde a las elecciones

  def CorrerBanco(self):
    
    while True:
      self.MostrarMenuBanco()

      opcion= input("\nEliga una opciòn:")

      accion= self.opciones.get(opcion)

      if accion:
         accion()
      
      else:
        print("\n{0} no es una opción válida" "\n\nElija otro opción".format(opcion))

     
#Este método agrega un cliente al banco
# después lo manda crear una cuenta
  def CrearunCliente(self):
      print("\nEligió agregar un Ciente \n"+"\n Llene los siguientes datos:"+ "\n")
      nombre=input("Nombre del cliente: ")
      edad=str(input("Edad: "))
      direccion=input("Dirección: ")
      sexo=input("Presione M si es sexo Masculino y F si es sexo Femenino"+"\nSexo: " )

      self.cliente=Cliente(nombre,direccion,edad,sexo)

      while sexo!="M" and sexo!="F" :
        sexo=input("Presione M si es sexo Masculino y F si es sexo Femenino  ")
      if sexo=="M":
        self.Hombres.append(self.cliente)
      if sexo=="F":
        self.Mujeres.append(self.cliente)

      print("****Datos del cliente: \n*****")
      print(self.cliente)
      self.banco.AñadirCliente(self.cliente)

      
      
      print("\nDespués de ingresar los datos del cliente debe crear una cuenta. ")
      print("\n Por favor eliga la opción adecuada para crear la cuenta del cliente:")

      self.AgregarunaCuenta()
 #Clegir igresar a un cliente específico 
 #para poder así ingresar a sus datos     
  def IngresaraunCliente(self):
    clientes=self.banco.getClientes()
    if len(clientes)!=0:
      print("Clientes registrados en el banco: ","\n")
      temp=""
      for i in range(len(clientes)):

        temp="Cliente "+str(i+1)+"\n\n"
        temp+="Nombre del cliente: "+clientes[i].getNombre()+"\n"
        temp+="Número de cuentas: "+str(len(clientes[i].getCuentas()))+"\n"
        print(temp)
      ver_cliente=input("Indique que número de cliente es al que quiere ingresar"+" o presione 'x' para volver al menú del banco\n")
      if ver_cliente.lower()=="x":
        self.CorrerBanco()
      else:
        for i in range(len(clientes)):
          if int(ver_cliente)==i+1:
            self.cliente=clientes[i]
            men=""
            men+="Nombre del cliente: "+ clientes[i].getNombre()+"\n"
            print("\nCuentas del cliente "+"\n")
            for j in range(len(clientes[i].cuentas)):
              men=men+"Cuenta "+str(j)+": " +str(clientes[i].cuentas[j].getTipo()+"\n")
              print(men)
            opcion=input("¿Desea ingresar a la información de sus cuentas?\n"+"1.Si\n "+"2.No \n")
            while opcion!="1" and opcion!="2" :
              opcion=input("Ingreso una opción incorrecta, vuelva a elegir"+"\n")
            if opcion=="1":
              clientes[i].infoCuentas()
            if opcion=="2":
              opcion=input("Elija la opción adecuada: \n"+"1.Acceder a una cuenta\n "+"2.Agregar más cuentas  \n"+"3.Regresar al Menu del Banco\n")
              while opcion!="1" and opcion!="2" and opcion!="3":
                opcion=input("Ingreso una opción incorrecta, vuelva a elegir"+"\n")
              if opcion=="1":
                cuentas=self.cliente.getCuentas()
                for i in range(len(cuentas)):
                  cuenta=input("Indique el número de cuenta al que quiere acceder: ")
                  self.cuenta=cuentas[i]
                  print(self.cuenta)
                
                  print("Elija la opción adecuada: \n")
                  self.CorrerCuenta()
              if opcion=="2":
                self.AgregarunaCuenta()
              
              if opcion=="3":
                self.CorrerBanco() 
                  
    else:
     print("No hay clientes registrados en el Banco Patito")
     self.CorrerBanco() 
                  
#se abre después de haber ingresado a un cliente
#funciona para asignarle alguna cuenta
# al cliente que se había ingresado anteriormente
  def AgregarunaCuenta(self):
  
    msg="\nEligió agregar una cuenta "
    msg+="\n\nTipos de cuenta"
    msg+="\n1. Cuenta de Ahorro"
    msg+="\n2.Cuenta de Crédito"
    print(msg)
    tipo=input("\nElija el tipo de cuenta:")
    cuentas=[]
    while tipo!="1" and tipo!="2":
      tipo=input("\nEligió una opción incorrecta, por favor vuelva a elegir: ")
    if tipo=="1":
      print("\nPara crear la Cuenta de Ahorro inserte los siguientes datos: "+ "\n" )
      SaldoInicial=int(input("\nSaldo inicial: $ " ))
      TasadeInteres=int(input("Tasa de interés:"))
      Tipo="Cuenta de Ahorro"

      print("\nCUENTA REGISTRADA\n")
     
      print("Datos de la cuenta: \n ")

      self.cuenta=CuentaDeAhorro(SaldoInicial,TasadeInteres,Tipo)

      self.CuentasAhorro.append(self.cuenta)
     
      self.cliente.AñadirCuenta(self.cuenta)
      
      print(self.cuenta)

      opcion=input("¿Se agregaran más cuentas al cliente?\n"+"1.Si\n "+"2. No \n")

      while opcion!="1" and opcion!="2":
         opcion=input("Ingreso una opción incorrecta, vuelva a elegir"+"\n")
      if opcion=="1":
        self.AgregarunaCuenta()
      if opcion=="2":
        self.CorrerBanco()

     
      
    if tipo=="2":
      print("\nPara crear la Cuenta de Crédito inserte los siguientes datos: "+ "\n" )
      SaldoInicial=int(input("\nSaldo inicial: $ " ))
      TasadeInteres=int(input("Tasa de interés:"))
      Sobregiro=int(input("Sobregiro: $ "))
      Tipo="Cuenta de Crédito"
      self.cuenta=CuentaDeCredito(SaldoInicial, Sobregiro,TasadeInteres,Tipo)
      self.CuentasCredito.append(self.cuenta)

      print("\nCUENTA REGISTRADA\n")
      print("Datos de la cuenta: \n ")
      print(self.cuenta)
      self.cliente.AñadirCuenta(self.cuenta)
      opcion=input("¿Se agregaran más cuentas al cliente?\n"+"1.Si"+"\n2. No \n")
      while opcion!="1" and opcion!="2":
         opcion=input("Ingreso una opción incorrecta, vuelva a elegir"+"\n")
      if opcion=="1":
        self.AgregarunaCuenta()
      if opcion=="2":
        self.CorrerBanco()

  def EliminarCuenta(self):
     self.cliente.EliminarCuenta(self.cuenta)
     
  def MostrarMenuCuenta(self):
    print (""" 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Menú de la Cuenta
    1 Retirar
    2 Depositar
    3 Consultar Saldo
    4 Eliminar la cuenta
    5 Regresal al Menú del Banco
    6 Salir""")
  #Éste método muestra el menú y responde a las elecciones
  def CorrerCuenta(self):
    
    while True:
      self.MostrarMenuCuenta()

      opcion= input("\nEliga una opciòn:")

      accion= self.opciones2.get(opcion)

      if accion:
         accion()
      else:
        print("\n{0} no es una opción válida" "\n\nElija otro opción".format(opcion))
    
  #Método de la clase cuenta
  def retirar(self):

    cantidad= input("¿Qué cantidad desea reitrar?")
    self.cuenta.retirar(int(cantidad))
#Método de la clase cuenta
  def depositar(self):

    cantidad= input("\n¿Qué cantidad desea depositar?")
    self.cuenta.depositar(int(cantidad))
#Método  para ver la cantidad disponible
  def ConsultarSaldo(self):
    
    self.cuenta.getCantidad()
#con esto se acaba la interacción con el menú
  def salir(self):
    print("\n\n\t***Gracias por su preferencia, hasta luego.***")
    registros=self.banco.getClientes()
    with open("Registro_Clientes_Nuevos.txt","w") as archivo_01:
      for i in registros:
        archivo_01.write(i.__str__())
        archivo_01.write("\n") 
    archivo_01.close()

    self.TotaldeCuentas()
    self.Promedios()
    
    sys.exit(0)
  
  def TotaldeCuentas(self):
        CuentasCredito=len(self.CuentasCredito)
        CuentasAhorro=len(self.CuentasAhorro)
        TotalCuentas=CuentasCredito+CuentasAhorro
        archivo_2=open("Registro_Cuentas.txt","w")
        archivo_2.write("El total de las cuentas es: " + str(TotalCuentas))
        archivo_2.write("\n\nEl total de las cuentas de credito son: "+str(CuentasCredito))
        archivo_2.write("\n\nEl total de las cuentas de Ahorro son: "+str(CuentasAhorro))
        archivo_2.close 

        cantidades=([len(self.CuentasCredito),len(self.CuentasAhorro)])
        colores=("darkturquoise","hotpink")
        cuentas=("Cuentas de Crédito","Cuentas de Ahorro")
        valores=(0.1,0)
        plt.figure()
        plt.pie(cantidades,colors=colores,autopct="%1.1f%%", explode=valores)
        plt.axis("equal")
        plt.title("Total de Cuentas",fontsize=20)
        plt.legend(labels=cuentas,fontsize=13)
        
        
        
        plt.savefig("Gráfica_de_Cuentas.png")
        plt.show()
  
  def Promedios(self):
    clientes=self.banco.getClientes()
    Total_Clientes=len(clientes)
    Total_Clientes_Hombres=len(self.Hombres)
    Total_Clientes_Mujeres=len(self.Mujeres)

    Prom_Mujeres_Banco=Total_Clientes_Mujeres/Total_Clientes
    Prom_Hombres_Banco=Total_Clientes_Hombres/Total_Clientes
    archivo_1=open("Promedios.txt","w")
    archivo_1.write("El Promedio de mujeres en el banco es: " + str(Prom_Mujeres_Banco))
    archivo_1.write("\n\nEl Promedio de hombres en el banco es: " + str(Prom_Hombres_Banco))
    archivo_1.close

    cantidades=([len(self.Hombres),len(self.Mujeres)])
    colores=("royalBlue","darkmagenta")
    Clientes=("Hombres","Mujeres")
    valores=(0.1,0.1)
    plt.figure()
    plt.pie(cantidades,colors=colores,autopct="%1.1f%%", explode=valores)
    plt.axis("equal")
    plt.title("Total de Clientes",fontsize=20)
    plt.legend(labels=Clientes,fontsize=13)
    
    plt.savefig("Grafica_de_Clientes.png")
    plt.show()