from datetime import datetime

def execution_time(func):
  def wrapper(*args, **kwargs):
    initial_time = datetime.now()
    func(*args, **kwargs)
    final_time = datetime.now()
    time_elapsed =  final_time - initial_time
    print ("Execution time:", str(time_elapsed.total_seconds()), "seconds")
  return wrapper

# Normal Sintax
def saludo_normal_sintax(name="Liox"):
  print("Hola", name)

# Sugar Sintax
@execution_time
def loop():
  for _ in range(1,1000000):
    pass

@execution_time
def suma(a: int, b:int)-> int:
  return a + b

@execution_time
def saludo(name="Liox"):
  print("Hola", name)

def run():

  # Normal Sintax
  saludo_normal_sintax_var = execution_time(saludo_normal_sintax)
  saludo_normal_sintax_var("Pedro")

  # Sugar Sintax
  loop()
  suma(5,6)
  saludo()

if __name__ == "__main__":
  run()