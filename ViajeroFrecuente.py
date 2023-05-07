class ViajeroF:
    __num_viajero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 0

    def __init__(self, num, dni, nom, ape, millacum):
        self.__dni = dni
        self.__num_viajero = num
        self.__millas_acum = millacum
        self.__nombre = nom
        self.__apellido = ape
    
    def get_nomap(self):
        return (self.__nombre+" "+self.__apellido)
    
    def get_millas(self):
        return self.__millas_acum
    
    def __gt__(self,viajero):
        return self.__millas_acum>viajero.get_millas()
    
    def __add__(self,otro=100):
        self.__millas_acum+=otro
        return self.__millas_acum

    def __sub__(self,canje=100):
        if self.__millas_acum >= canje:
            self.__millas_acum -= canje
        else:
            print("No tiene la cantidad de millas necesarias para ese canje")
            print("Usted posee " + str(self.__millas_acum))
        return self.__millas_acum

    def compararnumviajero (self, num):
        return self.__num_viajero==num
        


