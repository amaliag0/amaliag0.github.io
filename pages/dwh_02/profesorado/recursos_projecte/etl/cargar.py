from sqlalchemy import create_engine

def cargar_postgres(df):
    engine = create_engine('postgresql://odoo:odoo@odoo-db:5432/datawarehouse')
    df.to_sql('datos_unificados', con=engine, if_exists='replace', index=False)

def cargarTabla_postgres(df_limpio,nombreTabla):
    
    # Configura la conexión a PostgreSQL
    usuario = "odoo"
    contraseña = "odoo"
    host = "odoo-db"
    base_de_datos = "datawarehouse"

    url = f"postgresql+psycopg2://{usuario}:{contraseña}@{host}/{base_de_datos}"
    engine = create_engine(url)

    # Exportar a tabla nueva o reemplazar si ya existe
    df_limpio.to_sql(nombreTabla, engine, if_exists='replace', index=False)
