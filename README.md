# Práctica POO

Práctica de Programación Orientada a Objetos en Python. Modela personajes de
combate con herencia, polimorfismo y un sistema de combate por turnos.

## Archivos

- `personaje.py`: clase base `Personaje` y sus subclases `Guerrero` y `Mago`,
  más una función `combate()` que simula una pelea por turnos.

## Clases

### `Personaje` (clase base)

Representa a un personaje genérico.

Atributos:
- `nombre` (str)
- `fuerza` (int)
- `inteligencia` (int)
- `defensa` (int)
- `vida` (int)

Métodos:
- `atributos()`: imprime nombre y atributos en formato legible.
- `subir_nivel(fuerza, inteligencia, defensa)`: suma los valores recibidos a
  los atributos correspondientes.
- `esta_vivo()`: devuelve `True` si `vida > 0`.
- `daño(enemigo)`: devuelve `self.fuerza - enemigo.defensa`.
- `atacar(enemigo)`: calcula el daño, se lo resta al enemigo, muestra el
  resultado y maneja la muerte si la vida llega a 0.
- `__morir()`: método privado que pone la vida en 0 y avisa que el personaje murió.

### `Guerrero(Personaje)`

Hereda de `Personaje` y añade el atributo `espada` (multiplicador de daño).

- `cambiar_arma()`: pide al usuario elegir un arma (Acero Valyrio = 8,
  Matadragones = 10) y actualiza `espada`.
- Sobrescribe `atributos()` para mostrar también la espada.
- Sobrescribe `daño(enemigo)`: `self.fuerza * self.espada - enemigo.defensa`.

### `Mago(Personaje)`

Hereda de `Personaje` y añade el atributo `libro` (multiplicador de daño).

- Sobrescribe `atributos()` para mostrar también el libro.
- Sobrescribe `daño(enemigo)`: `self.inteligencia * self.libro - enemigo.defensa`.

## Combate

La función `combate(jugador_1, jugador_2)` ejecuta un bucle por turnos donde
cada personaje ataca al otro hasta que uno muere. Al terminar indica quién ganó
o si fue empate.

Ejemplo incluido en el archivo:

```python
jugador_1 = Guerrero("Guts", 20, 10, 10, 100, 5)
jugador_2 = Mago("Vanessa", 15, 15, 10, 100, 5)
combate(jugador_1, jugador_2)
```

## Cómo ejecutar

Desde la carpeta del proyecto:

```bash
python3 personaje.py
```
