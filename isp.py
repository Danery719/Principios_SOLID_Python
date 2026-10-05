class Impresora:
    def imprimir(self):
        print("Imprimiendo documento.")


class Escaner:
    def escanear(self):
        print("Escaneando documento.")


class ImpresoraMultifuncional(Impresora, Escaner):
    pass


impresora = ImpresoraMultifuncional()

impresora.imprimir()
impresora.escanear()