def clousureExample(numberA):
  def multiplier(numberB):
    return numberA * numberB
  return multiplier

def run():
  multiply_5 = clousureExample(5)
  multiply_6 = clousureExample(6)
  print("result:", multiply_5(2))
  print("result:", multiply_6(2))
  print("result:", multiply_6(multiply_5(2)))

if __name__ == "__main__":
  run()