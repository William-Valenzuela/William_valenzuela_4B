# Practica3. 
# Introducción al Polimorfismo
# Simular un sistema de cobro con múltiples opciones de pago.

class pago_tarjeta:
    def procesar_pago(self, cantidad):
        return f"Procesando pago de ${cantidad} con tarjeta bancaria"

class transferencia:
    def procesar_pago(self, cantidad):
        return f"Procesando pago de ${cantidad} con transferencia bancaria"

class deposito:
    def procesar_pago(self, cantidad):
        return f"Procesando pago de ${cantidad} mediante depósito"

class paypal:
    def procesar_pago(self, cantidad):
        return f"Procesando pago de ${cantidad} con PayPal"

# Instancias
metodos_pago = [pago_tarjeta(), transferencia(), deposito(), paypal()]

# Ejemplo de ejecución con la misma cantidad (polimorfismo básico)
for metodo in metodos_pago:
    print(metodo.procesar_pago(500))

# ACTIVIDAD: Procesar pago con diferentes cantidades
pago1 = pago_tarjeta()
pago2 = deposito()
pago3 = transferencia()
pago4 = paypal()

print(pago1.procesar_pago(100))  # 100 con tarjeta
print(pago3.procesar_pago(500))  # 500 con transferencia
print(pago4.procesar_pago(200))  # 200 con PayPal
print(pago2.procesar_pago(400))  # 400 con depósito


#Actividad de Notificaciones 
class NotificacionCorreo:
    def enviar_notificacion(self, mensaje):
        return f" Enviando correo con mensaje: '{mensaje}'"

class NotificacionSMS:
    def enviar_notificacion(self, mensaje):
        return f"Enviando SMS con mensaje: '{mensaje}'"

class NotificacionWhatsApp:
    def enviar_notificacion(self, mensaje):
        return f" Enviando WhatsApp con mensaje: '{mensaje}'"

class NotificacionPush:
    def enviar_notificacion(self, mensaje):
        return f" Enviando notificación Push con mensaje: '{mensaje}'"

notificaciones = [
    (NotificacionCorreo(), "Tu pedido fue confirmado"),
    (NotificacionSMS(), "Tu paquete ha sido enviado"),
    (NotificacionWhatsApp(), "Tu pedido está por llegar"),
    (NotificacionPush(), "Tu paquete fue entregado")
]

for canal, mensaje in notificaciones:
    print(canal.enviar_notificacion(mensaje))