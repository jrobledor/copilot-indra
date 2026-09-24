def anadir_tarea(tareas, descripcion):
    """Añade una tarea pendiente a la lista."""
    tareas.append({"descripcion": descripcion, "completada": False})


def listar_tareas(tareas):
    """Muestra todas las tareas y su estado."""
    if not tareas:
        print("No hay tareas.")
        return

    for numeroDeTarea, tarea in enumerate(tareas, start=1):
        estado = "completada" if tarea["completada"] else "pendiente"
        print(f"{numeroDeTarea}. [{estado}] {tarea['descripcion']}")


def completar_tarea(tareas, numeroDeTarea):
    """Marca como completada la tarea indicada por su número."""
    if numeroDeTarea < 1 or numeroDeTarea > len(tareas):
        return False

    tareas[numeroDeTarea - 1]["completada"] = True
    return True


def mostrar_menu():
    print("\n--- Lista de tareas ---")
    print("1. Añadir una tarea")
    print("2. Listar tareas")
    print("3. Marcar una tarea como completada")
    print("4. Salir")


def ejecutar_programa():
    tareas = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            descripcion = input("Escribe la tarea: ").strip()
            if descripcion:
                anadir_tarea(tareas, descripcion)
                print("Tarea añadida.")
            else:
                print("La tarea no puede estar vacía.")
        elif opcion == "2":
            listar_tareas(tareas)
        elif opcion == "3":
            listar_tareas(tareas)
            if tareas:
                try:
                    numeroDeTarea = int(input("Número de la tarea: "))
                except ValueError:
                    print("Debes escribir un número.")
                else:
                    if completar_tarea(tareas, numeroDeTarea):
                        print("Tarea completada.")
                    else:
                        print("Ese número de tarea no existe.")
        elif opcion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    ejecutar_programa()
