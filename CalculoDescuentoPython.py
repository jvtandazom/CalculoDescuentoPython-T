def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * porcentaje_descuento / 100
    return descuento

# Llamada a la función con solo el monto total de la compra
monto_compra_1 = 100
descuento_1 = calcular_descuento(monto_compra_1)
monto_final_1 = monto_compra_1 - descuento_1
print(f"Descuento aplicado: {descuento_1}, Monto final a pagar: {monto_final_1}")

# Llamada a la función con el monto total de la compra y un porcentaje de descuento especificado
monto_compra_2 = 100
porcentaje_descuento_2 = 15
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
monto_final_2 = monto_compra_2 - descuento_2
print(f"Descuento aplicado: {descuento_2}, Monto final a pagar: {monto_final_2}")