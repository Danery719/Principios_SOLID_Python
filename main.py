from srp import Usuario, UsuarioService, EmailService
from ocp import DescuentoEstudiante, DescuentoDocente, mostrar_precio
from lsp import Aguila, mostrar_vuelo
from isp import ImpresoraMultifuncional
from dip import ServicioCorreo, Notificacion


print("=== PRINCIPIOS SOLID EN PYTHON ===")

print("\n1. SRP - Responsabilidad Única")
usuario = Usuario("Danery", "danery@gmail.com")
UsuarioService().guardar_usuario(usuario)
EmailService().enviar_correo(usuario)

print("\n2. OCP - Abierto/Cerrado")
mostrar_precio(DescuentoEstudiante(), 100)
mostrar_precio(DescuentoDocente(), 100)

print("\n3. LSP - Sustitución de Liskov")
mostrar_vuelo(Aguila())

print("\n4. ISP - Segregación de Interfaces")
impresora = ImpresoraMultifuncional()
impresora.imprimir()
impresora.escanear()

print("\n5. DIP - Inversión de Dependencias")
servicio = ServicioCorreo()
notificacion = Notificacion(servicio)
notificacion.enviar_notificacion("Tu registro fue realizado correctamente.")