class Ave:
    def volar(self):
        print("El ave está volando.")


class Aguila(Ave):
    def volar(self):
        print("El águila está volando.")


class Pinguino(Ave):
    def nadar(self):
        print("El pingüino está nadando.")


def mostrar_vuelo(ave):
    ave.volar()


aguila = Aguila()
mostrar_vuelo(aguila)