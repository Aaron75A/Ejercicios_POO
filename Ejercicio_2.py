horas_trabajadas = 48
tarifa_hora = 5000
porcentaje_retencion = 12.5 
salario_bruto = horas_trabajadas * tarifa_hora

retencion = (porcentaje_retencion / 100) * salario_bruto

salario_neto = salario_bruto - retencion

print("- Resultados -")
print(f"Salario bruto: ${salario_bruto:,.0f}")
print(f"Retención en la fuente (12.5%): ${retencion:,.0f}")
print(f"Salario neto: ${salario_neto:,.0f}")