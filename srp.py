class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo


class UsuarioService:
    def guardar_usuario(self, usuario):
        print(f"Usuario {usuario.nombre} guardado correctamente.")


class EmailService:
    def enviar_correo(self, usuario):
        print(f"Correo enviado a {usuario.correo}.")


usuario = Usuario("Danery", "danery@gmail.com")

usuario_service = UsuarioService()
email_service = EmailService()

usuario_service.guardar_usuario(usuario)
email_service.enviar_correo(usuario)
