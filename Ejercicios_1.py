edad_juan = int(input("Ingrese la edad de Juan: "))

#Calcular las edades según las proporciones
edad_alberto = (2/3) * edad_juan
edad_ana = (4/3) * edad_juan
edad_mama = edad_juan + edad_alberto + edad_ana
#Mostrar los resultados
print("\n--- Edades ---")
print(f"Juan: {int(edad_juan)} años")
print(f"Alberto: {int(edad_alberto)} años")
print(f"Ana: {int(edad_ana)} años")
print(f"Mamá: {int(edad_mama)} años")