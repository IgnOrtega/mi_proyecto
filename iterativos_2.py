# 1.Carga de Datos:
ventas = [
    {"fecha": "2025-05-16", "producto": "Azucar","cantidad":40,"precio":1800.0},
    {"fecha": "2025-05-16", "producto": "Carne","cantidad":34,"precio":800.0},
    {"fecha": "2025-05-16", "producto": "Sal","cantidad":17,"precio":800.0},
    {"fecha": "2025-05-16", "producto": "Detergente","cantidad":10,"precio":6000.0},
    {"fecha": "2025-05-17", "producto": "Azucar","cantidad":45,"precio":1800.0},
    {"fecha": "2025-05-17", "producto": "Carne","cantidad":30,"precio":8800.0},
    {"fecha": "2025-05-17", "producto": "Sal","cantidad":20,"precio":800.0},
    {"fecha": "2025-05-17", "producto": "Detergente","cantidad":15,"precio":5800.0},
    {"fecha": "2025-05-18", "producto": "Azucar","cantidad":34,"precio":1900.0},
    {"fecha": "2025-05-18", "producto": "Carne","cantidad":55,"precio":8800.0},
    {"fecha": "2025-05-18", "producto": "Sal","cantidad":10,"precio":800.0},
    {"fecha": "2025-05-18", "producto": "Detergente","cantidad":5,"precio":5800.0},
    {"fecha": "2025-05-19", "producto": "Azucar","cantidad":34,"precio":1800.0},
    {"fecha": "2025-05-19", "producto": "Carne","cantidad":10,"precio":8800.0},
    {"fecha": "2025-05-19", "producto": "Sal","cantidad":3,"precio":800.0},
    {"fecha": "2025-05-19", "producto": "Detergente","cantidad":8,"precio":5800.0}
]

# 2.Cálculo de Ingresos Totales:
sum_=0
for venta in ventas:
    sum_= sum_+venta["cantidad"]*venta["precio"]
print( f"2.Cálculo de ingresos totales: {sum_}")



# 3.Análisis del Producto Más Vendido
ventas_por_producto ={}
for venta_i in ventas:
    producto_i=venta_i["producto"]
    cantidad_i=venta_i["cantidad"]

    if not (producto_i in set(ventas_por_producto.keys())):
        ventas_por_producto[producto_i]=cantidad_i
        
    else:
        ventas_por_producto[producto_i]=ventas_por_producto[producto_i] + cantidad_i

 
current_qty=-1
for key_, values_ in ventas_por_producto.items():
    if current_qty< ventas_por_producto[key_]:
        lista_prod_max_vend=[]  # En el caso que tengamos más de un producto más vendido
        current_qty=ventas_por_producto[key_]
        lista_prod_max_vend.append(key_)
    elif current_qty == ventas_por_producto[key_]:
        lista_prod_max_vend.append(key_)
    else:
        pass
if len(lista_prod_max_vend)==1:
    print(f"3.Análisis del Producto Más Vendido: {lista_prod_max_vend[0]}")

elif len(lista_prod_max_vend)>=1:
    print(f"3.Análisis del Producto Más Vendido: {lista_prod_max_vend}")

else:
    print(f"3.Análisis del Producto Más Vendido: La lista ventas no tiene compras")

# 4.Promedio de Precio por Producto:
precios_por_producto={}
for venta_i in ventas:
    product_key_=venta_i["producto"]
    qty_value_=venta_i["cantidad"]
    venta_value_=venta_i["precio"]*venta_i["cantidad"]

    if not (product_key_ in set(precios_por_producto.keys())):
        precios_por_producto[product_key_]=(venta_value_,qty_value_)
        
    else:
        ventas_producto, qty_producto=precios_por_producto[product_key_]
        precios_por_producto[product_key_]=(ventas_producto+venta_value_
                                            ,qty_producto+qty_value_)

prom_por_producto={}
for product_key_, (venta_value_,qty_value_) in precios_por_producto.items():
    prom_por_producto[product_key_] = venta_value_/qty_value_   # Recordar que las claves de un diccionario son únicas
print(f"4.Promedio de Precio por Producto: {prom_por_producto}")


# 5.Ventas por Día:
ingresos_por_dia={}
for venta_i in ventas:
    fecha_i=venta_i["fecha"]
    precio_unitario_i=venta_i["precio"]
    cantidad_i=venta_i["cantidad"]

    if not (fecha_i in set(ingresos_por_dia.keys())):
        ingresos_por_dia[fecha_i]=cantidad_i*precio_unitario_i    
    else:
        ingresos_por_dia[fecha_i]=ingresos_por_dia[fecha_i]+cantidad_i*precio_unitario_i            
print(f"5.Ventas por Día: {ingresos_por_dia}")

# 6.Representación de Datos:
resumen_ventas={}

for venta_i in ventas:
    product_key_=venta_i["producto"]
    qty_value_=venta_i["cantidad"]
    venta_value_=venta_i["precio"]*venta_i["cantidad"]

    if not (product_key_ in set(resumen_ventas.keys())):
        resumen_ventas[product_key_]={"cantidad_total":qty_value_,
                                      "ingresos_totales":venta_value_}
    else:
        qty_accum_producto, ventas_accum_producto=resumen_ventas[product_key_]["cantidad_total"], resumen_ventas[product_key_]["ingresos_totales"]
        resumen_ventas[product_key_]={"cantidad_total":qty_value_+qty_accum_producto,
                                      "ingresos_totales":venta_value_+ventas_accum_producto}        

for product_key_ in resumen_ventas.keys():
    qty_value_=resumen_ventas[product_key_]["cantidad_total"]
    venta_value_=resumen_ventas[product_key_]["ingresos_totales"]    
    resumen_ventas[product_key_]["precio_promedio"]=venta_value_/qty_value_
print(f"6.Representación de Datos: {resumen_ventas}")


