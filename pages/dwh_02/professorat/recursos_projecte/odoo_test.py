import xmlrpc.client

url = "http://odoo:8069"  # o "http://odoo:8069" si estás dentro del contenedor
db = "odoo"
username = "jmorantllorca@gmail.com"
password = "almoines"  # asegúrate de que es correcta

print("Conectando a Odoo...")

common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})

if uid:
    print(f"Autenticación exitosa. UID: {uid}")
else:
    print("Fallo de autenticación. Verifica tus credenciales.")

# Prueba extra: listar partners
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
partners = models.execute_kw(
    db, uid, password,
    'res.partner', 'search_read',
    [[]], {'fields': ['name', 'email'], 'limit': 5}
)

print("Partners:")
for p in partners:
    print(p)