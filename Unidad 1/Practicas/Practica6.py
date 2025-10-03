# Practica 6: Patrones de diseño (Factory y Observer)
#
# INVESTIGACIÓN
# 
# Patrón Factory (Fábrica):
# - Es un patrón creacional que permite crear objetos sin exponer la lógica de creación al cliente.
# - La responsabilidad de decidir qué objeto crear se delega a una "fábrica".
# - Se usa cuando tenemos diferentes tipos de objetos con una misma interfaz/base.
# - Ejemplo: crear diferentes tipos de cuentas bancarias (ahorro, corriente) sin que el usuario
#   tenga que preocuparse por los detalles de implementación.
#
# Patrón Observer (Observador):
# - Es un patrón de comportamiento que define una relación "uno a muchos".
# - Cuando un objeto (Sujeto) cambia de estado, notifica automáticamente a todos sus "Observadores".
# - Se usa en sistemas de notificaciones, eventos y suscripciones.
# - Ejemplo: una cuenta bancaria que avisa por SMS o Email cuando se realiza un depósito o retiro.
#
# En este ejemplo se simula un banco donde:
# - Usamos Factory para crear diferentes tipos de cuentas (Ahorro o Corriente).
# - Usamos Observer para notificar al cliente de movimientos en su cuenta vía Email y SMS.
# EJEMPLO DE CÓDIGO

# FACTORY METHOD

class Cuenta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.observadores = []  # Lista de observadores registrados

    def registrar_observador(self, observador):
        """Permite que un observador se suscriba a la cuenta"""
        self.observadores.append(observador)

    def notificar(self, mensaje):
        """Informa a todos los observadores sobre un evento"""
        for obs in self.observadores:
            obs.actualizar(mensaje)

    def depositar(self, cantidad):
        """Depósito de dinero"""
        self.saldo += cantidad
        self.notificar(f"Depósito de ${cantidad} en la cuenta de {self.titular}. Saldo actual: ${self.saldo}")

    def retirar(self, cantidad):
        """Retiro de dinero"""
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            self.notificar(f"Retiro de ${cantidad} en la cuenta de {self.titular}. Saldo actual: ${self.saldo}")
        else:
            self.notificar(f"Fondos insuficientes en la cuenta de {self.titular}")


class CuentaAhorro(Cuenta):
    """Cuenta de ahorro con beneficios de intereses"""
    pass


class CuentaCorriente(Cuenta):
    """Cuenta corriente, más flexible para transacciones"""
    pass


# Fábrica que crea las cuentas según el tipo solicitado
class CuentaFactory:
    @staticmethod
    def crear_cuenta(tipo, titular, saldo=0):
        if tipo.lower() == "ahorro":
            return CuentaAhorro(titular, saldo)
        elif tipo.lower() == "corriente":
            return CuentaCorriente(titular, saldo)
        else:
            raise ValueError("Tipo de cuenta no válido")


# OBSERVER

class Observador:
    def actualizar(self, mensaje):
        raise NotImplementedError


class NotificacionEmail(Observador):
    """Observador que envía notificaciones por Email"""
    def actualizar(self, mensaje):
        print(f"[Email] {mensaje}")


class NotificacionSMS(Observador):
    """Observador que envía notificaciones por SMS"""
    def actualizar(self, mensaje):
        print(f"[SMS] {mensaje}")



# SIMULACIÓN DE CASO REAL


# Crear una cuenta usando el Factory
cuenta1 = CuentaFactory.crear_cuenta("ahorro", "William", 1000)

# Registrar observadores (Observer)
email = NotificacionEmail()
sms = NotificacionSMS()
cuenta1.registrar_observador(email)
cuenta1.registrar_observador(sms)

# Operaciones en la cuenta
cuenta1.depositar(500)   # Se notifica por Email y SMS
cuenta1.retirar(200)     # Se notifica por Email y SMS
cuenta1.retirar(2000)    # Intento fallido, también notificado
