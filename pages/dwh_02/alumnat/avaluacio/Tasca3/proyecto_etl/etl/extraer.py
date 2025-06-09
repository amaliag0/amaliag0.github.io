import pandas as pd
import xmlrpc.client

# Utilitza pandas i el métode read_csv
def extraer_csv(ruta):


# Utilitza sqlalchemy per llegir una taula de la base de dades
def extraer_mysql(tabla):


# Extrae datos de Odoo a través de XML-RPC.
def extraer_odoo(modelo, campos=None, filtro=None, limite=0):
    
    """
    Args:
        modelo (str): Nombre del modelo de Odoo (ej. 'res.users').
        campos (list): Lista de campos a recuperar (ej. ['id', 'name', 'email']).
        filtro (list): Filtro de búsqueda tipo dominio (ej. [['active', '=', True]]).
        limite (int): Número máximo de registros a devolver (0 = sin límite).

    Returns:
        pd.DataFrame: DataFrame con los resultados.
    """

    print(f"Conectando a Odoo API para extraer '{modelo}'...")

    # Configuración de conexión
    url = "http://odoo:8069"
    db = ""
    username = ""
    password = ""

    # Conectar a la API
    common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    uid = common.authenticate(db, username, password, {})
    if not uid:
        raise Exception("Error de autenticación con Odoo")

    models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

    # Filtro por defecto (todos)
    if filtro is None:
        filtro = []

    # Campos por defecto (solo 'id')
    if campos is None:
        campos = ['id']
    
    # Argumentos para la consulta
    kwargs = {'fields': campos}
    if limite > 0:
        kwargs['limit'] = limit

    results = models.execute_kw(
        db, uid, password,
        modelo, 'search_read',
        [filtro],
        kwargs
    )

    return pd.DataFrame(results)