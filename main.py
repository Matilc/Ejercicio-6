import os
from ManejadorViajeros import ManejadorViajero
def menu_opciones():
    print("Menú de opciones:")
    print("1. Consultar cantidad de millas totales")
    print("2. Acumular millas")
    print("3. Canjear millas")
    print("4. Salir")

if __name__=='__main__':
    mv=ManejadorViajero()
    mv.cargarviajeros()
    print ("Los viajeros con mayores millas son")
    may_millas=mv.viajeros_may_millas()
    for viajero in may_millas:
        print (viajero.get_nomap())
    i=mv.obtener_viajero()
    print (i)
    viajeroaux=mv.get_viajero(i)
    opc=None
    while opc!='4':
        os.system('cls')
        menu_opciones()
        opc=input("Ingrese la opción elegida: \n")
        os.system('cls')
        if opc=='1':
            print ('La cantidad de Millas que posee son: '+str(viajeroaux.get_millas()))
            aux=input("\nIngrese cualquier tecla para continuar\n")
        if opc=='2':
            millasaux=int(input("Ingrese las millas a sumar:\n"))
            print ('Sus millas totales son '+str(viajeroaux+millasaux))
            aux=input("\nIngrese cualquier tecla para continuar\n")
        if opc=='3':
            millasaux=int(input("Ingrese las millas a canjear:\n"))
            print ('Sus millas totales son '+str(viajeroaux-millasaux))
            aux=input("\nIngrese cualquier tecla para continuar\n")
        
    print("Gracias por usar el sistema")