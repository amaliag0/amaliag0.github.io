import pandas as pd
from datetime import datetime

def transformar_datos(df_csv, df_mysql):
    # Lógica de unión y limpieza de los datos
    df_csv['origen'] = 'csv'
    df_mysql['origen'] = 'mysql'
    return pd.concat([df_csv, df_mysql], ignore_index=True)

def calcular_prevision_ventas(df_moves,df_move_lines,df_productos):

    # Mes actual y mes anterior (a 1 año)
    hoy = pd.to_datetime(datetime.today())
    mes_actual = hoy.to_period('M')
    mes_pasado = (hoy - pd.DateOffset(years=1)).to_period('M')

    # Asegurar tipos
    df_moves['id'] = df_moves['id'].astype(int)
    df_move_lines['move_id'] = df_move_lines['move_id'].apply(lambda x: x[0] if isinstance(x, list) else x)
    df_move_lines['product_id'] = df_move_lines['product_id'].apply(lambda x: x[0] if isinstance(x, list) else x)

    # Unir líneas con facturas para obtener fechas
    df_ventas = df_move_lines.merge(df_moves, left_on='move_id', right_on='id', suffixes=('_line', '_factura'))

    # Calcular importe
    df_ventas['importe'] = df_ventas['quantity'] * df_ventas['price_unit']
    
    # Filtrar ventas válidas
    df_ventas = df_ventas[df_ventas['invoice_date'].notna()]
    df_ventas['fecha'] = pd.to_datetime(df_ventas['invoice_date'])

    # Añadir mes y año
    df_ventas['anio_mes'] = df_ventas['fecha'].dt.to_period('M')

    df_anyo_pasado = df_ventas[df_ventas['anio_mes'] == mes_pasado]
    
    # Agregar por producto y mes
    prevision = df_anyo_pasado.groupby('product_id')['quantity'].sum().reset_index()
    prevision.rename(columns={'quantity': 'prevision_cantidad'}, inplace=True)
    prevision['anio_mes'] = hoy

    return prevision


def unificarUsuaris(df_mysql_users,df_odoo_users):
    
    # Convertimos columnas claves si hace falta
    df_odoo_users['email'] = df_odoo_users['email'].astype(str).str.lower().str.strip()
    df_mysql_users['correu'] = df_mysql_users['correu'].astype(str).str.lower().str.strip()

    # Renombrar columnas para claridad
    df_mysql_users = df_mysql_users.rename(columns={'correu': 'email'})
    
    # Merge: mantener todos los usuarios de Odoo (left join)
    columnas_a_conservar = ['id_odoo','id_mysql','name','email','dni']
    df_unificado = df_odoo_users.merge(
        df_mysql_users,
        on='email',
        how='left',
        suffixes=('_odoo', '_mysql')
    )
    df_unificado = df_unificado[columnas_a_conservar]

    # Usuarios de MySQL que no están en Odoo
    df_mysql_extras = df_mysql_users[~df_mysql_users['email'].isin(df_odoo_users['email'])].copy()
    df_mysql_extras['advertencia'] = 'Usuario no encontrado en Odoo'

    return df_unificado, df_mysql_extras


def netejar_fixatges(df_usuarios, df_fixatges):
    
    # 1. Convertir columnas a datetime
    df_fixatges['entrada'] = pd.to_datetime(df_fixatges['entrada'], errors='coerce')
    df_fixatges['eixida'] = pd.to_datetime(df_fixatges['eixida'], errors='coerce')

    # 2. Unir fichajes con los usuarios para obtener el ID de Odoo
    df = df_fixatges.merge(
        df_usuarios[['id_mysql', 'id_odoo']],
        left_on='idusuari',
        right_on='id_mysql',
        how='left'
    )

    # 3. Eliminar fichajes que no tienen correspondencia con usuarios Odoo
    df = df[~df['id_odoo'].isna()].copy()

    # 4. Eliminar duplicados exactos
    df = df.drop_duplicates()

    # 4. Crear columna que indique si falta la salida
    df['salida_faltante'] = df['eixida'].isna()

    # 5. Calcular duración solo si hay entrada y salida
    df['duracion_horas'] = (df['eixida'] - df['entrada']).dt.total_seconds() / 3600
    df['duracion_horas'] = df['duracion_horas'].round(2)

    # 7. Renombrar y dejar solo columnas relevantes
    df = df.rename(columns={'id_odoo': 'id_empleado'})
    columnas_finales = ['id_empleado', 'entrada', 'eixida', 'salida_faltante', 'duracion_horas']
    return df[columnas_finales]
