#Practica 4: Herencia
#1.-Crear una clase ticket con los siguentes atributos atributos:
#1 id
#tipo (por ejemplo:sofware, prueba)
#prioridad (alta,media,baja)
#estado (por defecto "pendiente")
#2.- Crear dos tickets de ejemplo y mostrarlos por panatalla

# Practica 4: Herencia

class Ticket:
    def __init__(self, id, tipo, prioridad, estado="pendiente"):
        self.id = id
        self.tipo = tipo
        self.prioridad = prioridad
        self.estado = estado

    def mostrar_ticket(self):
        print(f"Ticket ID: {self.id}")
        print(f"Tipo: {self.tipo}")
        print(f"Prioridad: {self.prioridad}")
        print(f"Estado: {self.estado}")
        print("-" * 30)


# Clase Empleado
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def trabajar_en_ticket(self, ticket):
        print(f"El empleado {self.nombre} revisa el ticket {ticket.id}")


# Clase Desarrollador
class Desarrollador(Empleado):
    def trabajar_en_ticket(self, ticket):
        if ticket.tipo.lower() == "software":
            ticket.estado = "resuelto"   # corregido
            print(f"El ticket {ticket.id} fue resuelto por {self.nombre}")
        else:
            print("Este tipo de empleado no puede resolver el desarrollador")


# Clase Tester
class Tester(Empleado):
    def trabajar_en_ticket(self, ticket):
        if ticket.tipo.lower() == "prueba":
            ticket.estado = "resuelto"
            print(f"El ticket {ticket.id} de tipo 'prueba' fue resuelto por {self.nombre}")
        else:
            print(f"El tester {self.nombre} no puede resolver tickets de tipo '{ticket.tipo}'")


# Clase ProjectManager
class Project_manager(Empleado):
    def asignar_ticket(self, ticket, empleado):
        print(f"{self.nombre} asignó el ticket {ticket.id} al empleado {empleado.nombre}")
        empleado.trabajar_en_ticket(ticket)   # corregido


# Crear instancias de ejemplo
ticket1 = Ticket(1, "software", "alta")
ticket2 = Ticket(2, "prueba", "media")

developer1 = Desarrollador("Gustavo")
tester1 = Tester("Pablo")
pm1 = Project_manager("Susana")

pm1.asignar_ticket(ticket1, developer1)
pm1.asignar_ticket(ticket2, tester1)



# Menú 

tickets = [ticket1, ticket2]

while True:
    print("\n--- MENÚ ---")
    print("1. Crear un ticket")
    print("2. Ver tickets")
    print("3. Asignar tickets")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        id_ticket = len(tickets) + 1
        tipo = input("Tipo de ticket: ")
        prioridad = input("Prioridad: ")
        nuevo_ticket = Ticket(id_ticket, tipo, prioridad)
        tickets.append(nuevo_ticket)
        print("Ticket creado.")

    elif opcion == "2":
        for t in tickets:
            t.mostrar_ticket()

    elif opcion == "3":
        id_ticket = int(input("ID del ticket a asignar: "))
        for t in tickets:
            if t.id == id_ticket:
                empleado = input("Asignar a (developer/tester): ").lower()
                if empleado == "developer":
                    developer1.trabajar_en_ticket(t)
                elif empleado == "tester":
                    tester1.trabajar_en_ticket(t)
                else:
                    print("Empleado no válido.")
                break
        else:
            print("Ticket no encontrado.")

    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("Opción no válida.")
