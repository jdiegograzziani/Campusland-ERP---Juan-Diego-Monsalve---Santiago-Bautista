# Funciones para persistencia de datos con JSON

import json
import os
from datetime import datetime

# Nombres de los archivos JSON
ARCHIVO_USUARIOS = "usuarios.json"
ARCHIVO_RUTAS = "rutas.json"
ARCHIVO_BACKUP = "backup_campuslands.json"
ARCHIVO_TRAINERS = "reporte_datos_trainer.json"

def crear_archivos_iniciales():
    """Crea los archivos JSON iniciales si no existen"""
    
    # Estructura inicial de usuarios
    usuarios_inicial = {
        "campers": {},
        "trainers": {},
        "coordinadores": {}
    }
    
    # Estructura inicial de rutas
    rutas_inicial = {
        "nodejs": {"trainer": None, "salon": None, "campers": [], "historial": []},
        "java": {"trainer": None, "salon": None, "campers": [], "historial": []},
        "netcore": {"trainer": None, "salon": None, "campers": [], "historial": []},
        "fundamentos_programacion": {"trainer": None, "salon": None, "campers": [], "historial": []},
        "programacion_web": {"trainer": None, "salon": None, "campers": [], "historial": []},
        "programacion_formal": {"trainer": None, "salon": None, "campers": [], "historial": []},
        "bases_de_datos": {"trainer": None, "salon": None, "campers": [], "historial": []},
        "backend": {"trainer": None, "salon": None, "campers": [], "historial": []}
    }
    
    # Crear archivo de usuarios si no existe
    if not os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, 'w', encoding='utf-8') as f:
            json.dump(usuarios_inicial, f, indent=4, ensure_ascii=False)
        print(f"Archivo {ARCHIVO_USUARIOS} creado.")
    
    # Crear archivo de rutas si no existe
    if not os.path.exists(ARCHIVO_RUTAS):
        with open(ARCHIVO_RUTAS, 'w', encoding='utf-8') as f:
            json.dump(rutas_inicial, f, indent=4, ensure_ascii=False)
        print(f"Archivo {ARCHIVO_RUTAS} creado.")

    # Crear archivo de datos trainer si no existe
    if not os.path.exists(ARCHIVO_TRAINERS):
        with open(ARCHIVO_TRAINERS, "w", encoding="utf-8") as f:
            json.dump(rutas_inicial, f, indent=4, ensure_ascii=False)
        print(f"Archivo {ARCHIVO_TRAINERS} creado.")


def cargar_usuarios():
    """Carga los datos de usuarios desde el archivo JSON"""
    try:
        if os.path.exists(ARCHIVO_USUARIOS):
            with open(ARCHIVO_USUARIOS, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            print(f"Archivo {ARCHIVO_USUARIOS} no encontrado. Creando estructura inicial...")
            crear_archivos_iniciales()
            return cargar_usuarios()
    except json.JSONDecodeError as e:
        print(f"Error al leer {ARCHIVO_USUARIOS}: {e}")
        print("Creando respaldo y archivo nuevo...")
        if os.path.exists(ARCHIVO_USUARIOS):
            os.rename(ARCHIVO_USUARIOS, f"{ARCHIVO_USUARIOS}.corrupted")
        crear_archivos_iniciales()
        return cargar_usuarios()
    except Exception as e:
        print(f"Error inesperado al cargar usuarios: {e}")
        return {"campers": {}, "trainers": {}, "coordinadores": {}}

def cargar_rutas():
    """Carga los datos de rutas desde el archivo JSON"""
    try:
        if os.path.exists(ARCHIVO_RUTAS):
            with open(ARCHIVO_RUTAS, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            print(f"Archivo {ARCHIVO_RUTAS} no encontrado. Creando estructura inicial...")
            crear_archivos_iniciales()
            return cargar_rutas()
    except json.JSONDecodeError as e:
        print(f"Error al leer {ARCHIVO_RUTAS}: {e}")
        print("Creando respaldo y archivo nuevo...")
        if os.path.exists(ARCHIVO_RUTAS):
            os.rename(ARCHIVO_RUTAS, f"{ARCHIVO_RUTAS}.corrupted")
        crear_archivos_iniciales()
        return cargar_rutas()
    except Exception as e:
        print(f"Error inesperado al cargar rutas: {e}")
        return {
            "nodejs": {"trainer": None, "salon": None, "campers": [], "historial": []},
            "java": {"trainer": None, "salon": None, "campers": [], "historial": []},
            "netcore": {"trainer": None, "salon": None, "campers": [], "historial": []},
            "fundamentos_programacion": {"trainer": None, "salon": None, "campers": [], "historial": []},
            "programacion_web": {"trainer": None, "salon": None, "campers": [], "historial": []},
            "programacion_formal": {"trainer": None, "salon": None, "campers": [], "historial": []},
            "bases_de_datos": {"trainer": None, "salon": None, "campers": [], "historial": []},
            "backend": {"trainer": None, "salon": None, "campers": [], "historial": []}
        }

def guardar_usuarios(usuarios):
    """Guarda los datos de usuarios en el archivo JSON"""
    try:
        with open(ARCHIVO_USUARIOS, 'w', encoding='utf-8') as f:
            json.dump(usuarios, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar usuarios: {e}")
        return False

def guardar_rutas(rutas):
    """Guarda los datos de rutas en el archivo JSON"""
    try:
        with open(ARCHIVO_RUTAS, 'w', encoding='utf-8') as f:
            json.dump(rutas, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar rutas: {e}")
        return False

def guardar_todo(usuarios, rutas):
    """Guarda tanto usuarios como rutas"""
    usuarios_guardado = guardar_usuarios(usuarios)
    rutas_guardado = guardar_rutas(rutas)
    
    if usuarios_guardado and rutas_guardado:
        print("✅ Datos guardados exitosamente.")
        return True
    else:
        print("❌ Error al guardar algunos datos.")
        return False

def crear_backup():
    """Crea un backup completo del sistema"""
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"backup_campuslands_{timestamp}.json"
        
        # Cargar todos los datos
        usuarios = cargar_usuarios()
        rutas = cargar_rutas()
        
        # Crear backup completo
        backup_data = {
            "fecha_backup": datetime.now().isoformat(),
            "version": "1.0",
            "usuarios": usuarios,
            "rutas": rutas
        }
        
        with open(backup_filename, 'w', encoding='utf-8') as f:
            json.dump(backup_data, f, indent=4, ensure_ascii=False)
        
        print(f"✅ Backup creado exitosamente: {backup_filename}")
        return backup_filename
    
    except Exception as e:
        print(f"❌ Error al crear backup: {e}")
        return None

def restaurar_backup(archivo_backup):
    """Restaura el sistema desde un archivo de backup"""
    try:
        if not os.path.exists(archivo_backup):
            print(f"❌ Archivo de backup no encontrado: {archivo_backup}")
            return False
        
        with open(archivo_backup, 'r', encoding='utf-8') as f:
            backup_data = json.load(f)
        
        # Validar estructura del backup
        if "usuarios" not in backup_data or "rutas" not in backup_data:
            print("❌ Archivo de backup no tiene la estructura correcta")
            return False
        
        # Restaurar datos
        usuarios_restaurado = guardar_usuarios(backup_data["usuarios"])
        rutas_restaurado = guardar_rutas(backup_data["rutas"])
        
        if usuarios_restaurado and rutas_restaurado:
            fecha_backup = backup_data.get("fecha_backup", "Fecha desconocida")
            print(f"✅ Backup restaurado exitosamente (Creado: {fecha_backup})")
            return True
        else:
            print("❌ Error al restaurar algunos datos")
            return False
    
    except Exception as e:
        print(f"❌ Error al restaurar backup: {e}")
        return False

def limpiar_archivos_temporales():
    """Limpia archivos temporales y corruptos"""
    try:
        archivos_limpiar = [
            f"{ARCHIVO_USUARIOS}.corrupted",
            f"{ARCHIVO_RUTAS}.corrupted"
        ]
        
        archivos_eliminados = 0
        for archivo in archivos_limpiar:
            if os.path.exists(archivo):
                os.remove(archivo)
                archivos_eliminados += 1
        
        if archivos_eliminados > 0:
            print(f"✅ {archivos_eliminados} archivo(s) temporal(es) eliminado(s)")
        
        return True
    except Exception as e:
        print(f"❌ Error al limpiar archivos temporales: {e}")
        return False

def verificar_integridad():
    """Verifica la integridad de los archivos de datos"""
    print("\n🔍 Verificando integridad de los datos...")
    
    usuarios_ok = False
    rutas_ok = False
    
    # Verificar usuarios
    try:
        usuarios = cargar_usuarios()
        if isinstance(usuarios, dict) and all(key in usuarios for key in ["campers", "trainers", "coordinadores"]):
            usuarios_ok = True
            print("✅ Archivo de usuarios: OK")
        else:
            print("❌ Archivo de usuarios: Estructura incorrecta")
    except Exception as e:
        print(f"❌ Archivo de usuarios: Error - {e}")
    
    # Verificar rutas
    try:
        rutas = cargar_rutas()
        if isinstance(rutas, dict) and len(rutas) > 0:
            rutas_ok = True
            print("✅ Archivo de rutas: OK")
        else:
            print("❌ Archivo de rutas: Estructura incorrecta")
    except Exception as e:
        print(f"❌ Archivo de rutas: Error - {e}")
    
    if usuarios_ok and rutas_ok:
        print("✅ Integridad del sistema: OK")
        return True
    else:
        print("❌ Problemas de integridad detectados")
        return False

def mostrar_estadisticas_archivos():
    """Muestra estadísticas de los archivos de datos"""
    try:
        usuarios = cargar_usuarios()
        rutas = cargar_rutas()
        
        print("\n📊 ESTADÍSTICAS DEL SISTEMA")
        print("=" * 40)
        print(f"Campers registrados: {len(usuarios['campers'])}")
        print(f"Trainers registrados: {len(usuarios['trainers'])}")
        print(f"Coordinadores registrados: {len(usuarios['coordinadores'])}")
        print(f"Rutas disponibles: {len(rutas)}")
        
        # Contar campers por ruta
        print("\nCampers por ruta:")
        for ruta, info in rutas.items():
            activos = len(info['campers'])
            historicos = len(info['historial'])
            print(f"  {ruta.replace('_', ' ').title()}: {activos} activos, {historicos} históricos")
        
        # Tamaño de archivos
        if os.path.exists(ARCHIVO_USUARIOS):
            size_usuarios = os.path.getsize(ARCHIVO_USUARIOS)
            print(f"\nTamaño archivo usuarios: {size_usuarios} bytes")
        
        if os.path.exists(ARCHIVO_RUTAS):
            size_rutas = os.path.getsize(ARCHIVO_RUTAS)
            print(f"Tamaño archivo rutas: {size_rutas} bytes")
            
    except Exception as e:
        print(f"Error al mostrar estadísticas: {e}")

# Función de utilidad para manejo de menús de archivos
def menu_gestion_archivos():
    """Menú para gestión de archivos y backups"""
    while True:
        print("\n" + "="*50)
        print("🗃️  GESTIÓN DE ARCHIVOS Y BACKUPS")
        print("="*50)
        print("1. Crear Backup")
        print("2. Restaurar Backup")
        print("3. Verificar Integridad")
        print("4. Mostrar Estadísticas")
        print("5. Limpiar Archivos Temporales")
        print("6. Volver al Menú Principal")
        print("="*50)
        
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case "1":
                crear_backup()
            case "2":
                archivo = input("Ingrese el nombre del archivo de backup: ")
                restaurar_backup(archivo)
            case "3":
                verificar_integridad()
            case "4":
                mostrar_estadisticas_archivos()
            case "5":
                limpiar_archivos_temporales()
            case "6":
                break
            case _:
                print("❌ Opción inválida")

if __name__ == "__main__":
    # Test de las funciones
    print("🧪 Probando funciones JSON...")
    crear_archivos_iniciales()
    verificar_integridad()
    mostrar_estadisticas_archivos()