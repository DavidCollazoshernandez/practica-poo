class Personaje:
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        """El método atributos imprime los atributos del personaje en un formato legible."""
        print(f"{self.nombre}")
        print(f"  Fuerza: {self.fuerza}")
        print(f"  Inteligencia: {self.inteligencia}")
        print(f"  Defensa: {self.defensa}")
        print(f"  Vida: {self.vida}")

    def subir_nivel(self, fuerza, inteligencia, defensa):
        """El método subir_nivel aumenta los atributos del personaje según los valores proporcionados."""
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        """El método esta_vivo verifica si el personaje sigue vivo (vida > 0)."""
        return self.vida > 0
    
    def __morir(self):
        """El método morir establece la vida del personaje a 0, indicando que ha muerto."""
        self.vida = 0
        print(f"{self.nombre} ha muerto.")

    def daño (self, enemigo):
        """Método que cálcula el daño que hace un enemigo al personaje"""
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        """Método atacar (calcula daño,enemigo, se lo resta al enemigo y maneja la muerte"""
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(f"{self.nombre} ataca a {enemigo.nombre} y le causa {daño} puntos de daño.")
        if enemigo.esta_vivo():
            print(f"{enemigo.nombre} tiene {enemigo.vida} puntos de vida restantes.")
        else:   
            enemigo.__morir()

"""Crearemos una clase que herede de personaje"""
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
            opcion = int(input("Elige arma (1) Acero Valyrio daño 8, (2) Matadragones daño 10: "))
            if opcion == 1:
                self.espada = 8
            elif opcion == 2:
                self.espada = 10
            else:
                print("Número incorrecto")

    def atributos(self):
        super().atributos()
        print("· Espada:", self.espada)

    def daño(self, enemigo):
            return self.fuerza * self.espada - enemigo.defensa
    
class Mago(Personaje):
        def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
            super().__init__(nombre, fuerza, inteligencia, defensa, vida)
            self.libro = libro

        def atributos(self):
            super().atributos()
            print("· Libro:", self.libro)

        def daño(self, enemigo):
            return self.inteligencia * self.libro - enemigo.defensa

    
jugador_1 = Guerrero("Guts", 20, 10, 10, 100, 5)
jugador_2 = Mago("Vanessa", 15, 15, 10, 100, 5)

def combate(jugador_1, jugador_2):
        turno = 0
        print("¡Comienza el combate!")
        while jugador_1.esta_vivo() and jugador_2.esta_vivo():
            print("\nTurno", turno)
            print(">>> Acción de", jugador_1.nombre, ":")
            jugador_1.atacar(jugador_2)
            print(">>> Acción de", jugador_2.nombre, ":")
            jugador_2.atacar(jugador_1)
            turno += 1
        if jugador_1.esta_vivo():
            print("\nHa ganado", jugador_1.nombre)
        elif jugador_2.esta_vivo():
            print("\nHa ganado", jugador_2.nombre)
        else:
            print("\nEmpate")
combate(jugador_1, jugador_2)


