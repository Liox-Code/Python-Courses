# GENERADORES
  # Generadores son el sugar sintax de los Iteradores

from time import sleep

def fibo_gen(max_number):
  n1 = 0
  n2 = 1
  counter = 0

  while True:
    if counter == 0:
      counter += 1
      yield n1
    elif counter == 1:
      counter += 1
      yield n2
    else:
      counter += 1
      aux = n1 + n2
      n1, n2 = n2, aux

      if max_number < aux:
        break

      yield aux

def run():
  # Generator Expression
  # Almacena todos los elementos en memoria, es como un LIST COMPREHENSION pero de generadores
  my_gen = (x*2 for x in range(0,21))

  print("Generator Expression")
  for element in my_gen:
    print(element,end=" ")
  print()

  # Fibonacci con Generadores
  print("Fibonacci con Generadores")
  fibonacci = fibo_gen(50)
  for element in fibonacci:
    print(element,end=" ")
    sleep(0.1)
  print()




if __name__ == '__main__':
  run()