import pandas as pd
import mysql.connector
import requests
from sqlalchemy import create_engine
import xmlrpc.client

def extraer_csv(ruta):

    print("Leyendo CSV...")
    return pd.read_csv(ruta)

def extraer_mysql(tabla):

    print(f"Conectando a MySQL y leyendo la tabla '{tabla}'...")
    usuario = "root"
    contraseña = "root"
    host = "mysql"
    base_de_datos = "empresa"

    url = f"mysql+mysqlconnector://{usuario}:{contraseña}@{host}/{base_de_datos}"
    engine = create_engine(url)

    query = f"SELECT * FROM {tabla};"
    return pd.read_sql(query, con=engine)

def extraer_odoo_vieja(modelo):

    print("Conectando a Odoo API...")

    url = "http://odoo:8069"
    db = "odoo"
    username = "jmorantllorca@gmail.com"
    password = "c0719f658ed9a30a79e70e7ddac0dbf8aa01819d"

    common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

    results = models.execute_kw(
        db, uid, password,
        'res.partner', 'search_read',
        [[]],
        {'fields': ['name', 'email'], 'limit': 10}
    )
    return pd.DataFrame(results)

def extraer_odoo(modelo, campos=None, filtro=None, limite=0):
    
    """
    Extrae datos de Odoo a través de XML-RPC.

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
    db = "odoo"
    username = "jmorantllorca@gmail.com"
    password = "c0719f658ed9a30a79e70e7ddac0dbf8aa01819d"

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