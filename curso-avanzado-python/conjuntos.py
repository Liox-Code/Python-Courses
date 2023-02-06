# CONJUNTOS o SETS

def run():
  # -Los sets son inmutables
  # -Cada elemento del set es único, esto es que no se admiten duplicados, aun si durante la definición del set se agregan elementos repetidos pyhton solo guarda un elemento
  # -Los sets guardan los elementos en desorden
  
  # set de enteros
  my_set = {1, 3, 5}
  print(my_set)

  # set de diferentes tipos de datos
  my_set = {1.0, "Hi", (1, 4, 7)}
  print(my_set)

  # -add(): nos permite agregar elementos al set, si se intenta agregar un elemento existente simplemente python los ignorara
  # -update(): nos permite agregar múltiples elementos al set
  # -remove(): permite eliminar un elemento del set, en el caso en que no se encuentre presente dicho elemento, Python elevará un error
  # -discard(): permite eliminar un elemento del set, en el caso en que no se encuentre presente dicho elemento, Python dejará el set intacto, sin elevar ningún error.
  # -pop(): permite eliminar un elemento del set, pero lo hará de forma aleatoria.
  # -clear(): Limpia completamente el set, dejándolo vació.

  #ejemplo de operaciones sobre sets 
  my_set = {1, 2, 3} 
  print(my_set) #Output {1, 2, 3} 

  #añadiendo un elemento al set 
  my_set.add(4) 
  print(my_set) #Output {1, 2, 3, 4}

  #añadiendo varios elementos al set, python ignorará elementos repetidos 
  my_set.update([1, 5, 6]) 
  print(my_set) #Output {1, 2, 3, 4, 5, 6}

  # eliminado elementos del set 
  my_set.discard(1) 
  print(my_set) #Output {2, 3, 4, 5, 6}

  # borrando un elemento aleatorio 
  my_set.pop()
  print(my_set) #Output el set menos un elemento aleatorio 

  #limpiar el set 
  my_set.clear()
  print(my_set) # Output set()

  #usando listas para crear sets
  my_list = [1, 2, 3, 3, 4, 5]
  my_set = set(my_list)
  print(my_set)  #output {1, 2, 3, 4, 5}

  #usando tuplas para crear sets 
  my_tuple = ('hola', 'hola', 1, 2)
  my_set2 = set(my_tuple)
  print(my_set2) #Output {'hola', 1}

  my_set_uno = {3,4,5}
  my_set_dos = {5,6,7}

  # Operaciones con Sets "CONJUNTOS"
  # Union
  my_set_tres = my_set_uno | my_set_dos
  print("Union Sets (my_set_uno | my_set_dos):", my_set_tres)
  # Interseccion
  my_set_tres = my_set_uno & my_set_dos
  print("Interseccion Sets (my_set_uno & my_set_dos):", my_set_tres)
  # Diferencia
  my_set_tres = my_set_uno - my_set_dos
  print("Diferencia Sets (my_set_uno - my_set_dos):", my_set_tres)
  my_set_tres = my_set_dos - my_set_uno
  print("Diferencia Sets (my_set_dos - my_set_uno):", my_set_tres)
  # Diferencia Simetrica
  my_set_tres = my_set_uno ^ my_set_dos
  print("Diferencia Simetrica Sets (my_set_uno ^ my_set_dos):", my_set_tres)


  #Lista sin repetidos
  my_list_repetidos = [1,1,2,2,3,3,4,4,4,5]
  my_list_no_repetidos = list(set(my_list_repetidos))

  print("Lista sin Repetidos:", my_list_no_repetidos)




if __name__ == "__main__":
  run()