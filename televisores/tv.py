class TV:
    _numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._control = None
        TV._numTV += 1

    def getMarca(self):
        return self._marca

    def getControl(self):
        return self._control

    def getPrecio(self):
        return self._precio

    def getVolumen(self):
        return self._volumen

    def getCanal(self):
        return self._canal

    def setMarca(self, marca):
        self._marca = marca

    def setControl(self, control):
        self._control = control

    def setPrecio(self, precio):
        self._precio = precio

    def setVolumen(self, volumen):
        if (self._estado and volumen <= 120 and volumen >= 1):
            self._volumen = volumen

    def setCanal(self, canal):
        if (self._estado and canal <= 120 and canal >= 1):
            self._canal = canal

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._canal = False

    def getEstado(self):
        return self._estado

    def canalUp(self):
        if (self._estado and self._canal != 120):
            self._canal += 1

    def canalDown(self):
        if (self._estado and self._canal != 1):
            self._canal -= 1

    def volumenUp(self):
        if (self._estado and self._volumen != 7):
            self._volumen += 1

    def volumenDown(self):
        if (self._estado and self._volumen != 0):
            self._volumen -= 1

    @staticmethod
    def setNumTV(num):
        TV._numTV = num