PI = 3.1416

radio = float(input("Ingrese el radio del círculo: "))

area = PI * (radio ** 2)

longitud = 2 * PI * radio
print("\n- Resultados -")
print(f"Radio: {radio}")
print(f"Área: {area:.2f}")
print(f"Longitud: {longitud:.2f}")