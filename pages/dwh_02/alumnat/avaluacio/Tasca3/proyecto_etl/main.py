from etl import extraer, transformar, cargar

# ETL completo
if __name__ == "__main__":
    
    # EXTRAER
    df_csv = extraer.extraer_csv('') # Ruta al documento CSV a leer
    df_odoo = extraer.extraer_odoo("",['id', 'name', 'email'],None,0) # Atributos: nombre del modelo de Odoo, Vector con los campos a leer, vector de filtrado, paámetro Limit
    df_mysql = extraer.extraer_mysql("") # Atributos: nombre de la tabla mysql


    print(df_csv)
    print(df_odoo)
    print(df_mysql)
    
    
    # TRANSFORMAR


    # CARGAR



