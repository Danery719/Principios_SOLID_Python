class ServicioCorreo:
    def enviar(self, mensaje):
        print(f"Correo enviado: {mensaje}")


class Notificacion:
    def __init__(self, servicio):
        self.servicio = servicio

    def enviar_notificacion(self, mensaje):
        self.servicio.enviar(mensaje)


servicio = ServicioCorreo()
notificacion = Notificacion(servicio)

notificacion.enviar_notificacion("Tu registro fue realizado correctamente.")