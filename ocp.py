class Descuento:
    def calcular(self, precio):
        return precio


class DescuentoEstudiante(Descuento):
    def calcular(self, precio):
        return precio * 0.90


class DescuentoDocente(Descuento):
    def calcular(self, precio):
        return precio * 0.85


def mostrar_precio(descuento, precio):
    print(f"Precio final: S/ {descuento.calcular(precio):.2f}")


precio = 100

mostrar_precio(DescuentoEstudiante(), precio)
mostrar_precio(DescuentoDocente(), precio)