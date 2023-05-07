from ViajeroFrecuente import ViajeroF
import csv
class ManejadorViajero:
    __listaviajero=[]

    def __init__(self):
        self.__listaviajero=[]

    def get_viajero (self, i):
        return self.__listaviajero[i]

    def cargarviajeros (self):
        archivo=open("Viajeros.csv")
        reader= csv.reader(archivo,delimiter=';')
        for fila in reader:
            viajero= ViajeroF(int(fila[0]), fila[1].strip(),fila[2].strip(),fila[3].strip(),int(fila[4]))
            self.__listaviajero.append(viajero)
    
    def obtener_viajero(self):
        numaux= int(input('Ingrese número de viajero '))
        i=0
        while self.__listaviajero[i].compararnumviajero(numaux) and i<len(self.__listaviajero):
            i+=1
        return i-1
    
    def viajeros_may_millas(self):
        lista_maymillas=[]
        viajeromill=self.__listaviajero[0]
        for fila in self.__listaviajero:
            if fila>viajeromill:
                viajeromill=fila
        for fila in self.__listaviajero:
            if fila.get_millas()==viajeromill.get_millas():
                lista_maymillas.append(fila)
        return lista_maymillas