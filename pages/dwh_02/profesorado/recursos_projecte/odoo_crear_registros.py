import csv
import sys
import xmlrpc.client
from passlib.context import CryptContext

# === CONFIGURACIÓN DE CONEXIÓN A ODOO ===
url = "http://odoo:8069"
db = "odoo"
username = "jmorantllorca@gmail.com"
password = "almoines"  # asegúrate de que es correcta

# === ENCRIPTACIÓN DE CONTRASEÑAS ===
pwd_context = CryptContext(schemes=["pbkdf2_sha512"])

# === CONFIGURACIÓN DEL MODELO ===
# Cambiar esto según necesidad o pásalo como argumento
modelo_objetivo = "account.move.line"
campo_clave = "id"  # Para evitar duplicados
archivo_csv = "datos/facturas_panaderia_para_odoo_lineas.csv"  # Ruta al archivo CSV

# === CONEXIÓN A ODOO ===
common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid = common.authenticate(db, username, password, {})
if not uid:
    print("❌ Fallo de autenticación")
    sys.exit()

models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

# === LECTURA DEL CSV ===
with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data = {k: v.strip() for k, v in row.items() if v.strip()}


        campos_enteros = ['move_id', 'product_id', 'account_id']
        for campo in campos_enteros:
            if campo in data:
                data[campo] = int(data[campo])

        # Convertir campos decimales
        campos_decimales = ['price_unit', 'quantity']
        for campo in campos_decimales:
            if campo in data:
                data[campo] = float(data[campo])

        # Encriptar la contraseña si existe
        if 'password' in data:
            data['password'] = pwd_context.hash(data['password'])

        # Buscar duplicados por el campo clave
        if campo_clave in data:
            search_domain = [[(campo_clave, '=', data[campo_clave])]]
            exists = models.execute_kw(
                db, uid, password,
                modelo_objetivo, 'search',
                search_domain, {'limit': 1}
            )
            if exists:
                print(f"⚠️  Ya existe {modelo_objetivo} con {campo_clave}='{data[campo_clave]}'. Omitido.")
                continue

        # Crear el registro
        record_id = models.execute_kw(
            db, uid, password,
            modelo_objetivo, 'create',
            [data]
        )
        print(f"✅ {modelo_objetivo} creado con ID {record_id}")