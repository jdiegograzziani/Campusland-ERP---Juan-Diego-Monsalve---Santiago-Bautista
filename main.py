import os
from datetime import datetime
from json_functions import (
    crear_archivos_iniciales, cargar_usuarios, cargar_rutas,
    guardar_usuarios, guardar_rutas, guardar_todo,
    crear_backup, restaurar_backup, verificar_integridad,
    menu_gestion_archivos
)

# Inicializar archivos y cargar datos al inicio
crear_archivos_iniciales()
usuarios = cargar_usuarios()
rutas = cargar_rutas()

# Verificar integridad al inicio
print("🚀 Iniciando Sistema Campuslands...")
if verificar_integridad():
    print("✅ Sistema listo para usar")
else:
    print("⚠️  Sistema iniciado con advertencias")

salones = ["Salon A", "Salon B", "Salon C", "Salon D", "Salon E", "Salon F"]

def registrar_camper():
    print ("------- Registro de Camper -------")
    cc = input("Ingrese el # de identificacion del Camper a registrar: ").strip()
    nombre = input("Ingrese solo el NOMBRE del Camper: ")
    apellido = input("Ingrese el APELLIDO del Camper: ")
    direccion = input("Ingrese la direccion de residencia del Camper: ")
    acudiente = input("Ingrese el NOMBRE del acudiente del Camper (padre/madre/abuelo/tutor): ")
    celular = input("Ingrese el # de telefono del Camper: ").strip()
    fijo = input("Ingrese el # de telefono fijo del Camper: ").strip()

    camper = usuarios["campers"]

    if cc in camper:
        print("Este Camper ya esta registrado...")
        return False
    
    camper[cc] ={
        "cc": cc,
        "nombre": nombre,
        "apellido": apellido,
        "direccion": direccion,
        "acudiente": acudiente,
        "celular": celular,
        "fijo": fijo,
        "estado": "En Proceso", 
        "riesgo": "Bajo",  # Agregado el campo riesgo
        "ruta": {
            "rutaActiva":"N/A",
            "modulos":{
                "nodejs":{
                    "nota_teo":0.0,
                    "nota_prac":0.0,
                    "nota_quices":0.0,
                    "nota_final":0.0,
                    "final":"N/A",
                },
                "java":{
                    "nota_teo":0.0,
                    "nota_prac":0.0,
                    "nota_quices":0.0,
                    "nota_final":0.0,
                    "final":"N/A",
                },
                "netcore":{
                    "nota_teo":0.0,
                    "nota_prac":0.0,
                    "nota_quices":0.0,
                    "nota_final":0.0,
                    "final":"N/A",
                },
                "fundamentos_programacion":{
                    "nota_teo":0.0,
                    "nota_prac":0.0,
                    "nota_quices":0.0,
                    "nota_final":0.0,
                    "final":"N/A",
                },
                "programacion_web":{
                    "nota_teo":0.0,
                    "nota_prac":0.0,
                    "nota_quices":0.0,
                    "nota_final":0.0,
                    "final":"N/A",
                },
                "programacion_formal":{
                    "nota_teo":0.0,
                    "nota_prac":0.0,
                    "nota_quices":0.0,
                    "nota_final":0.0,
                    "final":"N/A",
                },
                "bases_de_datos":{
                    "nota_teo":0.0,
                    "nota_prac":0.0,
                    "nota_quices":0.0,
                    "nota_final":0.0,
                    "final":"N/A",
                },
                "backend":{
                    "nota_teo":0.0,
                    "nota_prac":0.0,
                    "nota_quices":0.0,
                    "nota_final":0.0,
                    "final":"N/A",
                },
            },
        },
    }
    print(f"Camper {nombre} {apellido} registrado exitosamente!")
    guardar_usuarios(usuarios)  # Guardar después de registrar

def registrar_trainer():
    print("------- Registro de Trainer -------")
    cc = input("Ingrese el # de identificacion del Trainer a registrar: ").strip()
    nombre = input("Ingrese solo el NOMBRE del Trainer: ")
    apellido = input("Ingrese el APELLIDO del Trainer: ")
    direccion = input("Ingrese la direccion de residencia del Trainer: ")
    celular = input("Ingrese el # de celular del Trainer: ").strip()
    fijo = input("Ingrese el # de telefono fijo del Trainer: ").strip()

    trainer = usuarios["trainers"]

    if cc in trainer:
        print ("Este Trainer ya esta registrado...")
        return False
    
    trainer[cc] = {
        "cc": cc,
        "nombre": nombre,
        "apellido": apellido,
        "direccion": direccion,
        "celular": celular,
        "fijo": fijo,
        "ruta": None,
        "salon": salones,
    }
    print(f"Trainer {nombre} {apellido} registrado exitosamente!")
    guardar_usuarios(usuarios)  # Guardar después de registrar

def registrar_coordinador():
    print("------- Registro de Coordinador -------")
    print("Aviso: Este Rol de usuario posee acceso a todas las funciones administrativas del programa")
    cc = input("Ingrese el # de identificacion del Coordinador a registrar: ").strip()
    coordinador = usuarios["coordinadores"]

    if cc in coordinador:
        print ("Este coordinador ya esta registrado...")
        return False
    
    nombre = input("Ingrese solo el NOMBRE del Coordinador: ")
    apellido = input("Ingrese el APELLIDO del Coordinador: ")
    direccion = input("Ingrese la direccion de residencia del Coordinador: ")
    celular = input("Ingrese el # de celular del Coordinador: ").strip()
    fijo = input("Ingrese el # de telefono fijo del Coordinador: ").strip()
    
    coordinador[cc] = {
        "cc": cc,
        "nombre": nombre,
        "apellido": apellido,
        "direccion": direccion,
        "celular": celular,
        "fijo": fijo
    }
    print(f"Coordinador {nombre} {apellido} registrado exitosamente!")
    guardar_usuarios(usuarios)  # Guardar después de registrar

def acceso_coordinador():
    # Funcion para que solo CC de coordinadores registrados puedan acceder a asignacion de clases
    coordinador = usuarios["coordinadores"]
    cc = input("Ingrese el CC de coordinador: ").strip()
    if cc not in coordinador:
        print("Este CC no pertenece a un usuario con funcion de coordinador!")
        return False
    elif cc in coordinador:
        nombre = coordinador[cc]["nombre"]
        apellido = coordinador[cc]["apellido"]
        print(f"Acceso otorgado, Coordinador '{nombre}, {apellido}'")
        return True

def cambiar_estado():
    while True:
        print("------- Cambio de Estado Campers -------")
        print("-- SOLO COORDINADORES PUEDEN ACCEDER A ESTA FUNCION -- ")

        if not acceso_coordinador():
            return

        camper = usuarios["campers"]
        trainer = usuarios["trainers"]
        cc = input("Ingrese el # de identificacion de camper: ").strip()
        if cc not in camper:
            print("Este Camper no esta registrado!")
            return False
        elif cc in trainer:
            print(f"Este CC:'{cc}' pertenece a un Trainer, introduce un # de Camper... ")
            return False
        
        print(f"Estado actual del camper {camper[cc]['nombre']}: {camper[cc]['estado']}")
        print("Ingrese el nuevo rango del camper")
        print("1. En proceso")
        print("2. Inscrito")
        print("3. Aprobado")
        print("4. Cursando")
        print("5. Graduado")
        print("6. Expulsado")
        print("7. Retirado")
        print("8. Salir")
        opcion = input(":")
        match opcion:
            case "1":
                camper[cc]["estado"] = "En proceso"
                print("Estado cambiado exitosamente!")
                guardar_usuarios(usuarios)  # Guardar cambio de estado
                break
            case "2":
                camper[cc]["estado"] = "Inscrito"
                print("Estado cambiado exitosamente!")
                guardar_usuarios(usuarios)  # Guardar cambio de estado
                break
            case "3":
                camper[cc]["estado"] = "Aprobado"
                print("Estado cambiado exitosamente!")
                guardar_usuarios(usuarios)  # Guardar cambio de estado
                break
            case "4":
                camper[cc]["estado"] = "Cursando"
                print("Estado cambiado exitosamente!")
                guardar_usuarios(usuarios)  # Guardar cambio de estado
                break
            case "5":
                camper[cc]["estado"] = "Graduado"
                print("Estado cambiado exitosamente!")
                guardar_usuarios(usuarios)  # Guardar cambio de estado
                break
            case "6":
                camper[cc]["estado"] = "Expulsado"
                print("Estado cambiado exitosamente!")
                guardar_usuarios(usuarios)  # Guardar cambio de estado
                break
            case "7":
                camper[cc]["estado"] = "Retirado"
                print("Estado cambiado exitosamente!")
                guardar_usuarios(usuarios)  # Guardar cambio de estado
                break
            case "8":
                break

def eliminar_ruta(cc):
    for ruta, info in rutas.items():
        if cc in info["campers"]:
            info["campers"].remove(cc)

def calcular_nota_final(nota_teo, nota_prac, nota_quices):
    # Formula: 30% teorico, 60% practico, 10% quices
    nota_final = (nota_teo * 0.3) + (nota_prac * 0.6) + (nota_quices * 0.1)
    return round(nota_final, 2)

def determinar_resultado(nota_final):
    if nota_final >= 60:
        return "Aprobado"
    else:
        return "Reprobado"

def calificar_modulo(cc, modulo):
    camper = usuarios["campers"]
    
    print(f"------- Calificando {modulo.replace('_', ' ').title()} -------")
    print(f"Estudiante: {camper[cc]['nombre']} {camper[cc]['apellido']}")
    
    try:
        print("Ingrese la nota de la Prueba Teorica (0-100): ")
        nota_teo = float(input(":"))
        if not 0 <= nota_teo <= 100:
            print("La nota debe estar entre 0 y 100")
            return
            
        print("Ingrese la nota de la Prueba Practica (0-100): ")
        nota_prac = float(input(":"))
        if not 0 <= nota_prac <= 100:
            print("La nota debe estar entre 0 y 100")
            return
            
        print("Ingrese la nota de los Quices (0-100): ")
        nota_quices = float(input(":"))
        if not 0 <= nota_quices <= 100:
            print("La nota debe estar entre 0 y 100")
            return
        
        # Calcular nota final
        nota_final = calcular_nota_final(nota_teo, nota_prac, nota_quices)
        resultado = determinar_resultado(nota_final)
        
        # Guardar las notas
        camper[cc]["ruta"]["modulos"][modulo]["nota_teo"] = nota_teo
        camper[cc]["ruta"]["modulos"][modulo]["nota_prac"] = nota_prac
        camper[cc]["ruta"]["modulos"][modulo]["nota_quices"] = nota_quices
        camper[cc]["ruta"]["modulos"][modulo]["nota_final"] = nota_final
        camper[cc]["ruta"]["modulos"][modulo]["final"] = resultado
        
        print(f"Nota final: {nota_final}")
        print(f"Resultado: {resultado}")
        
        # Si aprueba y nota >= 60, cambiar estado a Aprobado automáticamente
        if nota_final >= 60 and camper[cc]["estado"] in ["En proceso", "Inscrito"]:
            camper[cc]["estado"] = "Aprobado"
            print("Estado del estudiante cambiado automáticamente a 'Aprobado'")
        
        # Guardar los cambios
        guardar_usuarios(usuarios)
            
    except ValueError:
        print("Por favor ingrese un número válido")

def asignar_ruta():
    print("------- Asignación de Clases -------")
    print("-- SOLO COORDINADORES PUEDEN ACCEDER A ESTA FUNCION --")

    if not acceso_coordinador():
        return

    camper = usuarios["campers"]
    cc = input("Ingrese el CC del estudiante: ").strip()
    if cc not in camper:
        print("Este camper no esta registrado...")
        return False
    
    print(f"Ingrese la opcion que necesita para el estudiante: '{camper[cc]['nombre']}' con CC {cc} ")
    print("Al seleccionar Ruta de Estudio, el Trainer y el Salon se asignan automaticamente")
    print("1. Asignar Ruta de Estudio")
    print("2. Calificar Modulo (Calificar Ruta Activa)")
    print("3. Salir")

    opcion = input(":")
    match opcion:
        case "1": 
           while True:
            print("Ingrese el numero de la ruta")
            print("1. Ruta NodeJS")
            print("2. Ruta Java")
            print("3. Ruta Netcore")
            print("4. Fundamentos de Programacion")
            print("5. Programacion web")
            print("6. Programacion formal")
            print("7. Bases de datos")
            print("8. Backend")
            print("9. Retirar Ruta Activa")
            print("0. Volver")
            ruta = input(":")

            rutas_map = {
                "1": "nodejs",
                "2": "java", 
                "3": "netcore",
                "4": "fundamentos_programacion",
                "5": "programacion_web",
                "6": "programacion_formal", 
                "7": "bases_de_datos",
                "8": "backend"
            }

            if ruta in rutas_map:
                eliminar_ruta(cc)
                ruta_seleccionada = rutas_map[ruta]
                camper[cc]["ruta"]["rutaActiva"] = ruta_seleccionada
                camper[cc]["estado"] = "Cursando"  # Cambiar estado automáticamente
                rutas[ruta_seleccionada]["campers"].append(cc)
                rutas[ruta_seleccionada]["historial"].append(cc)
                print(f"Ruta {ruta_seleccionada.replace('_', ' ').title()} asignada exitosamente!")
                print("Estado del estudiante cambiado a 'Cursando'")
                guardar_todo(usuarios, rutas)  # Guardar ambos diccionarios
                break
            elif ruta == "9":
                eliminar_ruta(cc)
                camper[cc]["ruta"]["rutaActiva"] = "N/A"
                print("Ruta activa retirada")
                guardar_todo(usuarios, rutas)  # Guardar cambios
                break
            elif ruta == "0":
                break

        case "2":
            ruta_activa = camper[cc]["ruta"]["rutaActiva"]
            if ruta_activa == "N/A":
                print("El estudiante no tiene una ruta activa asignada")
                return
            
            calificar_modulo(cc, ruta_activa)

        case "3":
            return False

def asignar_trainer():
    print("------- Asignar Trainers y Salones -------")
    print("-- Esta funcion es solo para Coordinadores --")
    if not acceso_coordinador():
        return
    
    trainer = usuarios["trainers"]
    cc = input("Ingrese el CC de trainer a asignar clase y salon: ").strip()
    if cc not in trainer:
        print("Este CC de trainer no está registrado...")
        return False
    
    print("Seleccione la ruta para asignar al trainer")
    print("1. Ruta NodeJS")
    print("2. Ruta Java")
    print("3. Ruta Netcore")
    print("4. Fundamentos de Programacion")
    print("5. Programacion web")
    print("6. Programacion formal")
    print("7. Bases de datos")
    print("8. Backend")
    print("9. Retirar Ruta Activa")
    print("0. Volver")
    ruta = input(":")

    # Mostrar salones disponibles
    print("Seleccione un salon:")
    for i, salon in enumerate(salones, 1):
        print(f"{i}. {salon}")
    
    try:
        salon_idx = int(input("Salon: ")) - 1
        if 0 <= salon_idx < len(salones):
            salon_seleccionado = salones[salon_idx]
        else:
            print("Salon inválido")
            return
    except ValueError:
        print("Selección inválida")
        return

    rutas_map = {
        "1": "nodejs",
        "2": "java",
        "3": "netcore", 
        "4": "fundamentos_programacion",
        "5": "programacion_web",
        "6": "programacion_formal",
        "7": "bases_de_datos",
        "8": "backend"
    }

    if ruta in rutas_map:
        ruta_seleccionada = rutas_map[ruta]
        rutas[ruta_seleccionada]["trainer"] = f"{trainer[cc]['nombre']} {trainer[cc]['apellido']}"
        rutas[ruta_seleccionada]["salon"] = salon_seleccionado
        trainer[cc]["ruta"] = ruta_seleccionada
        print(f"Trainer asignado exitosamente a {ruta_seleccionada.replace('_', ' ').title()} en {salon_seleccionado}")
        guardar_todo(usuarios, rutas)  # Guardar cambios
    elif ruta == "9":
        # Retirar trainer de todas las rutas
        for r in rutas.values():
            if r["trainer"] == f"{trainer[cc]['nombre']} {trainer[cc]['apellido']}":
                r["trainer"] = None
                r["salon"] = None
        trainer[cc]["ruta"] = None
        print("Trainer retirado de todas las rutas")
        guardar_todo(usuarios, rutas)  # Guardar cambios

def generar_reportes():
    print("------- Reportes -------")
    print("-- SOLO COORDINADORES PUEDEN ACCEDER A ESTA FUNCION --")
    
    if not acceso_coordinador():
        return
    
    while True:
        print("\nSeleccione el tipo de reporte:")
        print("1. Reporte de Campers por Estado")
        print("2. Reporte de Rutas y Asignaciones") 
        print("3. Reporte de Trainers")
        print("4. Reporte de Notas por Camper")
        print("5. Reporte de Campers en Riesgo")
        print("6. Gestión de Archivos y Backups")
        print("7. Reporte consolidado de Trainers y rutas a JSON")
        print("8. Volver")
        
        opcion = input(":")
        
        match opcion:
            case "1":
                reporte_campers_estado()
            case "2":
                reporte_rutas()
            case "3":
                reporte_trainers()
            case "4":
                reporte_notas_camper()
            case "5":
                reporte_campers_riesgo()
            case "6":
                menu_gestion_archivos()
            case "7":
                reporte_trainers_rutas()
            case "8":
                break

def reporte_campers_estado():
    print("\n===== REPORTE DE CAMPERS POR ESTADO =====")
    camper = usuarios["campers"]
    
    if not camper:
        print("No hay campers registrados")
        return
    
    # Agrupar por estado
    estados = {}
    for cc, info in camper.items():
        estado = info["estado"]
        if estado not in estados:
            estados[estado] = []
        estados[estado].append(info)
    
    for estado, lista in estados.items():
        print(f"\n--- {estado.upper()} ({len(lista)} campers) ---")
        for camper_info in lista:
            print(f"CC: {camper_info['cc']} - {camper_info['nombre']} {camper_info['apellido']} - Ruta: {camper_info['ruta']['rutaActiva']}")

def reporte_rutas():
    print("\n===== REPORTE DE RUTAS Y ASIGNACIONES =====")
    
    for ruta, info in rutas.items():
        print(f"\n--- {ruta.replace('_', ' ').upper()} ---")
        print(f"Trainer: {info['trainer'] if info['trainer'] else 'Sin asignar'}")
        print(f"Salon: {info['salon'] if info['salon'] else 'Sin asignar'}")
        print(f"Campers activos: {len(info['campers'])}")
        print(f"Total histórico: {len(info['historial'])}")
        
        if info['campers']:
            print("Estudiantes actuales:")
            camper = usuarios["campers"]
            for cc in info['campers']:
                if cc in camper:
                    print(f"  - {camper[cc]['nombre']} {camper[cc]['apellido']} (CC: {cc})")

def reporte_trainers_rutas():
    print("-------- TRAINERS REGISTRADOS -------")


    trainer = usuarios["trainers"]
    
    if not trainer:
        print("No hay trainers registrados")
        return
    
    for cc, info in trainer.items():
        print(f"\nCC: {cc}")
        print(f"Nombre: {info['nombre']} {info['apellido']}")
        print(f"Teléfono: {info['celular']}")
        print(f"Ruta asignada: {info['ruta'] if info['ruta'] else 'Sin asignar'}")

        print("--- RUTAS ACTIVAS Y TRAINERS ASIGNADOS A SU RESPECTIVO SALON ---")

    for ruta, info in rutas.items():
        print(f"\n--- {ruta.replace('_', ' ').upper()} ---")
        print(f"Trainer: {info['trainer'] if info['trainer'] else 'Sin asignar'}")
        print(f"Salon: {info['salon'] if info['salon'] else 'Sin asignar'}")
        print(f"Campers activos: {len(info['campers'])}")
        print(f"Total histórico: {len(info['historial'])}")


def reporte_trainers():
    print("\n===== REPORTE DE TRAINERS =====")
    trainer = usuarios["trainers"]
    
    if not trainer:
        print("No hay trainers registrados")
        return
    
    for cc, info in trainer.items():
        print(f"\nCC: {cc}")
        print(f"Nombre: {info['nombre']} {info['apellido']}")
        print(f"Teléfono: {info['celular']}")
        print(f"Ruta asignada: {info['ruta'] if info['ruta'] else 'Sin asignar'}")

def reporte_notas_camper():
    cc = input("Ingrese el CC del camper para ver sus notas: ").strip()
    camper = usuarios["campers"]
    
    if cc not in camper:
        print("Camper no encontrado")
        return
    
    info = camper[cc]
    print(f"\n===== REPORTE DE NOTAS - {info['nombre']} {info['apellido']} =====")
    print(f"CC: {cc}")
    print(f"Estado: {info['estado']}")
    print(f"Ruta Activa: {info['ruta']['rutaActiva']}")
    print(f"Riesgo: {info['riesgo']}")
    
    print("\nNotas por módulo:")
    for modulo, notas in info['ruta']['modulos'].items():
        if notas['nota_final'] > 0:  # Solo mostrar módulos con notas
            print(f"\n{modulo.replace('_', ' ').title()}:")
            print(f"  Teórico: {notas['nota_teo']}")
            print(f"  Práctico: {notas['nota_prac']}")
            print(f"  Quices: {notas['nota_quices']}")
            print(f"  Nota Final: {notas['nota_final']}")
            print(f"  Resultado: {notas['final']}")

def reporte_campers_riesgo():
    print("\n===== REPORTE DE CAMPERS EN RIESGO =====")
    camper = usuarios["campers"]
    
    campers_riesgo = []
    
    for cc, info in camper.items():
        # Determinar riesgo basado en notas
        riesgo_calculado = "Bajo"
        notas_bajas = 0
        
        for modulo, notas in info['ruta']['modulos'].items():
            if notas['nota_final'] > 0:  # Solo considerar módulos con notas
                if notas['nota_final'] < 60:
                    notas_bajas += 1
        
        if notas_bajas >= 2:
            riesgo_calculado = "Alto"
        elif notas_bajas == 1:
            riesgo_calculado = "Medio"
        
        # Actualizar riesgo del camper
        info['riesgo'] = riesgo_calculado
        
        if riesgo_calculado in ["Medio", "Alto"]:
            campers_riesgo.append((cc, info, riesgo_calculado))
    
    if not campers_riesgo:
        print("No hay campers en riesgo actualmente")
        return
    
    for cc, info, riesgo in campers_riesgo:
        print(f"\nCC: {cc}")
        print(f"Nombre: {info['nombre']} {info['apellido']}")
        print(f"Estado: {info['estado']}")
        print(f"Ruta: {info['ruta']['rutaActiva']}")
        print(f"Nivel de Riesgo: {riesgo}")

def mostrar_menu():
    while True:
        print("\n" + "="*40)
        print("------- Campuslands -------")
        print("="*40)
        print("1. Registrar Camper")
        print("2. Registrar Trainer")
        print("3. Registrar Coordinador")
        print("4. Cambiar Estado de Camper")
        print("5. Asignar Ruta de Estudio")
        print("6. Asignar Trainers y Salones")
        print("7. Reportes")
        print("8. Crear Backup de Seguridad")
        print("9. Salir")
        print("="*40)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_camper()
        elif opcion == "2":
            registrar_trainer()
        elif opcion == "3":
            registrar_coordinador()
        elif opcion == "4":
            cambiar_estado()
        elif opcion == "5":
            asignar_ruta()
        elif opcion == "6":
            asignar_trainer()
        elif opcion == "7":
            generar_reportes()
        elif opcion == "8":
            crear_backup()
        elif opcion == "9":
            # Crear backup automático al salir
            print("Creando backup automático antes de salir...")
            crear_backup()
            print("¡Gracias por usar el sistema Campuslands!")
            break
        else:
            print("Opción inválida. Por favor seleccione una opción válida.")

if __name__ == "__main__":
    mostrar_menu()