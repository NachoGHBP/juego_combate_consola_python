import random
import time

# Personajes
personajes = {
    "Scorpion": {"vida": 100, "ataque": 15},
    "Sub-Zero": {"vida": 100, "ataque": 15},
    "Raiden": {"vida": 100, "ataque": 15}
}

bienvenida = "Bienvenidos al Mortal Kombat"
print(bienvenida)
print("Elige tu Kombatiente:")
for p in personajes:
    print("-", p)

jugador_nombre = input(">>> ")
jugador = personajes.get(jugador_nombre)

if not jugador:
    print("Personaje no válido")
    exit()

# Enemigo aleatorio "IA"
enemigo_nombre = random.choice(list(personajes.keys()))
while enemigo_nombre == jugador_nombre:
    enemigo_nombre = random.choice(list(personajes.keys()))

enemigo = personajes[enemigo_nombre].copy()

print(f"\n {jugador_nombre} VS {enemigo_nombre} \n")

# Funciones
def atacar(atacante, defensor):
    daño = random.randint(atacante["ataque"] - 5, atacante["ataque"] + 5)
    defensor["vida"] -= daño
    print(f" Ataque causa {daño} de daño")

def especial(atacante, defensor):
    daño = random.randint(20, 30)
    defensor["vida"] -= daño
    print(f" ATAQUE ESPECIAL causa {daño} de daño")

# Juego
while jugador["vida"] > 0 and enemigo["vida"] > 0:
    print(f"\n Tu vida: {jugador['vida']} | Enemigo: {enemigo['vida']}")
    print("1. Atacar")
    print("2. Ataque especial")

    opcion = input(">>> ")

    if opcion == "1":
        atacar(jugador, enemigo)
    elif opcion == "2":
        especial(jugador, enemigo)
    else:
        print("Opción inválida")
        continue

    if enemigo["vida"] <= 0:
        break

    # Turno enemigo
    time.sleep(1)
    print("\n Turno del enemigo...")
    if random.random() < 0.7:
        atacar(enemigo, jugador)
    else:
        especial(enemigo, jugador)

# Resultado final
print("\n RESULTADO ")
if jugador["vida"] > 0:
    print(" ¡GANASTE! FATALITY ")
else:
    print(" PERDISTE...")