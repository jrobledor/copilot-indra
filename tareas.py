def anadir_tarea(tareas, descripcion):
    """Anade una tarea pendiente a la lista."""
    tareas.append({"descripcion": descripcion, "completada": False})


def listar_tareas(tareas):
    """Muestra todas las tareas y su estado."""
    if not tareas:
        print("No hay tareas.")
        return

    for numero, tarea in enumerate(tareas, start=1):
        estado = "completada" if tarea["completada"] else "pendiente"
        print(f"{numero}. [{estado}] {tarea['descripcion']}")


def completar_tarea(tareas, numero):
    """Marca como completada la tarea indicada por su numero."""
    if numero < 1 or numero > len(tareas):
        return False

    tareas[numero - 1]["completada"] = True
    return True


def mostrar_menu():
    print("\n--- Lista de tareas ---")
    print("1. Anadir una tarea")
    print("2. Listar tareas")
    print("3. Marcar una tarea como completada")
    print("4. Salir")


def ejecutar_programa():
    tareas = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            descripcion = input("Escribe la tarea: ").strip()
            if descripcion:
                anadir_tarea(tareas, descripcion)
                print("Tarea anadida.")
            else:
                print("La tarea no puede estar vacia.")
        elif opcion == "2":
            listar_tareas(tareas)
        elif opcion == "3":
            listar_tareas(tareas)
            if tareas:
                try:
                    numero = int(input("Numero de la tarea: "))
                except ValueError:
                    print("Debes escribir un numero.")
                else:
                    if completar_tarea(tareas, numero):
                        print("Tarea completada.")
                    else:
                        print("Ese numero de tarea no existe.")
        elif opcion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    ejecutar_programa()
