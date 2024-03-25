def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando un porcentaje al monto total de la compra.

    Args:
    - monto_total (float): Monto total de la compra.
    - porcentaje_descuento (float, optional): Porcentaje de descuento a aplicar. Por defecto es 10%.

    Returns:
    - float: Monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Llamadas a la función
monto_compra1 = 10
descuento1 = calcular_descuento(monto_compra1)
print("Descuento 1:", descuento1)
print("Monto final a pagar después del descuento 1:", monto_compra1 - descuento1)

monto_compra2 = 800
porcentaje_descuento2 = 15
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
print("Descuento 2:", descuento2)
print("Monto final a pagar después del descuento 2:", monto_compra2 - descuento2)
