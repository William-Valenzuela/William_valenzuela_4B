Practica 1 clases, objetos y atributos 

# una clase en una plantilla o un molde 
# que define como sea un objeto 

class Persona:
    def _init_(self, nombre, edad): # Contrutor 
     self.nombre = nombre
     self.edad = edad

    def Presentarse(self):
       print(f"Hola mi nombre es {self.nombre} y mi edad es {self.edad}")
    
    def cumplir_anios(self):
       self.edad += 1
       print(f"Esta persona cumplio {self.edad} años")

#un objeto es una instancia creada a partir
#de una clase
estudiante1 = Persona("Diego", 18)
estudiante2 = Persona("pedro", 50)

#Asignar metodos a eos objetos (Acciones)
estudiante1.Presentarse()
estudiante1.cumplir_anios()


# Paso 1. Agrega un metodo cumplir_anios()
# que aumente en la edad

# INSTANCIA 
# Cada objeto creado de una clase es una isntancia 
# Podemos tener varias instancias que coexistan con sus 
# propios datos 
# Objeto = instancia de la clase
# Cada cez que se crea un obejto con clase() ee obtiene
# una instancia tiene sus propios datos qunque vengan 
# de la misma clase.

# Abstracion
# Representar solo lo inportante del mudno real,
# ocultando detalles incesesarios.

class automovil:
    def _init_(self, marca): # Contrutor 
     self.marca = marca
      
    def arrancar(self):
       print(f"{self.marca} arranco")

# Crear un objeto auto y asignar un marca
auto = automovil("Nissan")
auto.arrancar()

# Abstraccion: Nos centrmaos  solo en lo que inporta (acciones)
# que es arrancar el automovil, oculatando detallkes internos 
# como motor , transmision , tipo_comustible. 
# Enfoque solo en la accion del objeto.
# Objetivo es hacer que el codigo mas limpio y facil de usar.


#1. Crear una clase mascotas
#2. agregar minimo 4 atributosPractica 1.2
#1. Crear una clase mascotas
#2. agregar minimo 4 atributos
#3. definir al menos 4 metodos diferentes.
#4. crear 2 instancias de la clase
#5. llamar los motodos y aplicar abstraccion. (Agregar)

#1. Crear una clase mascotas
#2. agregar minimo 4 atributos
#3. definir al menos 4 metodos diferentes.
#4. crear 2 instancias de la clase
#5. llamar los metodos y aplicar abstraccion.

class Mascota:
    def __init__(self, nombre, especie, edad, color):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.color = color

    def presentarse(self):
        print(f"Soy {self.nombre}, un {self.especie} de color {self.color} y tengo {self.edad} años.")

    def comer(self, comida):
        print(f"{self.nombre} está comiendo {comida}.")

    def dormir(self):
        print(f"{self.nombre} está durmiendo... Zzz")

    def jugar(self, juguete):
        print(f"{self.nombre} está jugando con {juguete}.")

# Crear dos instancias
mascota1 = Mascota("Firulais", "Perro", 5, "café")
mascota2 = Mascota("Michi", "Gato", 3, "blanco")

# Llamar métodos
mascota1.presentarse()
mascota1.comer("croquetas")
mascota1.jugar("pelota")

mascota2.presentarse()
mascota2.dormir()
mascota2.jugar("ratón de juguete")

# Abstracción:
# Nos enfocamos en lo que hace la mascota (comer, dormir, jugar, presentarse),
# sin preocuparnos de los detalles internos de cómo realiza esas acciones.
