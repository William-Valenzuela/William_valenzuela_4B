# Practica 5. Patrones de diseño

class Logger:
    # Creamos un atributo donde se guarda la instancia
    _instancia = None 

    # __new__ es el metodo que controla la creación del objeto antes de __init__
    # Sirve para asegurarnos de que solo exista una única instancia de la clase Logger
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)  # Creamos la instancia de Logger 
            # Agregamos un atributo "archivo" que apunta a un archivo físico
            # "a" significa append = Todo lo que se escriba se agrega al final del archivo
            cls._instancia.archivo = open("app.log", "a")
        return cls._instancia  # Devolvemos siempre la misma instancia
    
    def log(self, mensaje):
        # Simular un registro de logs
        self.archivo.write(mensaje + "\n")
        self.archivo.flush()  # Método para guardar en el disco

Logger1 = Logger()  # Creamos la primera y única instancia
Logger2 = Logger()  # Devuelve la misma instancia, sin crear una nueva

Logger1.log("Inicio de sesion en la aplicacion")
Logger2.log("El usuario se autentico")

# Comprobar que son el mismo objeto en memoria
print(Logger1 is Logger2)  # Devuelve True o False


# ----------------------------
# Actividad de la práctica
# ----------------------------
class Presidente:
    _instancia = None  # Necesario para controlar el Singleton
    
    def __new__(cls, nombre):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.nombre = nombre
            cls._instancia.historial = []
        return cls._instancia
    
    def accion(self, accion):
        evento = f"{self.nombre} {accion}"
        self.historial.append(evento)
        print(evento)

# Varios presidentes intentan tomar el poder
p1 = Presidente("AMLO")
p2 = Presidente("Peña Nieto")
p3 = Presidente("Fox") 

# Todos apuntan al mismo presidente
p1.accion("firmó decreto")
p2.accion("visitó España")
p3.accion("aprobó un presupuesto")

print("\nHistorial del presidente:")
print(p1.historial)

# Validación de Singleton
print(p1 is p2 is p3)  # True o False


# ----------------------------
# Preguntas y respuestas
# ----------------------------

# 1. ¿Qué pasaría si eliminas la verificación "if cls._instancia is None" en el método __new__?
#    -> Cada vez que se cree un objeto se generaría una nueva instancia,
#       rompiendo el patrón Singleton. Por ejemplo, Logger1 is Logger2 daría False.

# 2. ¿Qué significa el "True" en p1 is p2 is p3 en el método Singleton?
#    -> Significa que p1, p2 y p3 apuntan exactamente al mismo objeto en memoria,
#       es decir, todos representan la misma instancia del presidente.

# 3. ¿Es buena idea usar Singleton para todo lo que sea global? Menciona un ejemplo donde no sería recomendable.
#    -> No, no es buena idea. El Singleton solo es útil cuando realmente debe existir
#       una única instancia, como en un Logger o configuración global.
#       Ejemplo donde NO sería recomendable: representar usuarios conectados o
#       diferentes órdenes de compra, ya que cada una debe ser independiente.
