#Promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Duracion de crudos
Crudo_promedio = 5
crudo_dalto = 3.5

#Diferencia de duracion

diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#Calculando el procentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio / Crudo_promedio * 100
tiempo_vacio_dalto = 100 - dalto_curso*1000 // crudo_dalto / 10

#Calculando diferencia si los cursos duraran 10 horas
Tiempo_equivalente_en_10H_dalto = otros_cursos_promedio*1000 // dalto_curso / 100
Tiempo_equivalente_en_10H_otros_cursos = dalto_curso / otros_cursos_promedio *10

print('---------------')
print(f'El curso de Dalto dura un {diferencia_con_min}% menos que el más rápido')
print(f'El curso de Dalto dura un {diferencia_con_max}% menos que el más lento')
print(f'El curso de Dalto dura un {diferencia_con_promedio}% menos que el más promedio')
print('---------------')

print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Un curso promedio elimina un {tiempo_vacio_dalto}% de tiempo vacio')
print('---------------')

print (f'Ver 10h de este curso equivale a ver {Tiempo_equivalente_en_10H_dalto} horas de otros cursos')
print (f'Ver 10h de otros cursos equivale a ver {Tiempo_equivalente_en_10H_otros_cursos} horas de este cursos')
print('---------------')


