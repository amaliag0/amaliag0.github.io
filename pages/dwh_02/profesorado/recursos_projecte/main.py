from etl import extraer, transformar, cargar

# ETL completo
if __name__ == "__main__":
    
    # EXTRAER
    df_csv = extraer.extraer_csv('datos/datos.csv')
    
    df__usuaris_odoo = extraer.extraer_odoo("res.users",['id', 'name', 'email'],None,0)
    df_moves = extraer.extraer_odoo('account.move',['id', 'invoice_date', 'move_type', 'state'],[]) #['move_type', '=', 'out_invoice'], ['state', '=', 'posted']
    df_move_lines = extraer.extraer_odoo('account.move.line',['id', 'move_id', 'product_id', 'quantity', 'price_unit'])
    df_productos = extraer.extraer_odoo('product.product',['id', 'name', 'default_code'])

    df_treballadors = extraer.extraer_mysql("treballadors")
    df_fixatges = extraer.extraer_mysql("fixatges")

    print(df_moves)
    print(df_move_lines)
    print(df_productos)
    
    
    # TRANSFORMAR
    print("PASAMOS A TRANSFORMAR LOS DATOS")

    df_ventas_agregadas = transformar.calcular_prevision_ventas(df_moves,df_move_lines,df_productos)
    #print(df_ventas_agregadas)


    df_usuaris_nets, df_mysql_solo = transformar.unificarUsuaris(df_treballadors, df__usuaris_odoo)
    #print(df_mysql_solo)
    #print(df_usuaris_nets)
    
    df_fixatges_nets = transformar.netejar_fixatges(df_usuaris_nets, df_fixatges)
    #print(df_fixatges_nets)

    # CARGAR

    #print("PASAMOS A CARGAR LOS DATOS")
    cargar.cargarTabla_postgres(df_fixatges_nets,"fixatges_nets")
    cargar.cargarTabla_postgres(df_usuaris_nets,"usuaris")
    cargar.cargarTabla_postgres(df_ventas_agregadas,"previsio")
    cargar.cargarTabla_postgres(df_productos,"productos")

    #print("ETL completado. Resultado final:")
    #print(df_final)

