from time import sleep

class FiboIter():

  def __init__ (self, max_number:int):
    self.max_number = max_number

  def __iter__ (self):
    self.n1 = 0
    self.n2 = 1
    self.counter = 0
    return self

  def __next__ (self):
    if self.counter == 0:
      self.counter += 1
      return self.n1
    elif self.counter == 1:
      self.counter += 1
      return self.n2
    else:
      self.counter += 1
      self.aux = self.n1 + self.n2
      # Normal Sintax Swap
        # self.n1 = self.n2
        # self.n2 = self.aux
      # Sugar Sintax Swap
      self.n1 , self.n2 = self.n2, self.aux

      if self.aux > self.max_number:
        raise StopIteration

      return self.aux

def run():
  # Creando un Iterador
  my_list = [1,2,3,4,5]
  my_iter = iter(my_list)

  ## Normal Sintax Iterando Interador
  # Iterando Iterador
  print("Iterando Iterador con loop While, Normal Sintax")
  while True:
    try:
      element = next(my_iter)
      print(element, end=" ")
    except StopIteration:
      print()
      break

  print("Iterando Lista con loop For, Sugar Sintax")
  #For no existe en Python es un Alias SUGAR SINTAX de el loop While de un iterador
  for element in my_list:
    print(element, end=" ")
  print()

  # Iter Fibonacci
  fibonacci = FiboIter(50)
  for element in fibonacci:
    print(element)
    sleep(0.25)


if __name__ == "__main__":
  run()