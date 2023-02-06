import random
import unicodedata
import os

def get_random_word() :
  with open('./datos.txt','r', encoding='utf8') as datos:
    return random.choice(datos.read().split())

def run() :
  print("****************************** AHORCADO ******************************")
  
  is_word = False
  secret_word = get_random_word()
  response_word = ["_" for i in range(0,len(secret_word))]
  print(secret_word)

  while not is_word :
    input_character = input('Ingrese un character: ')
    for i, char in enumerate(list(secret_word)):
      guess_word = ''
      character = unicodedata.normalize('NFKD', char).encode('ASCII', 'ignore').decode()
      if input_character == character :
        response_word[i] = secret_word[i]
      guess_word = guess_word.join(response_word)
      if guess_word == secret_word :
        is_word = True
  
    for item in guess_word: 
      print(item, end= ' ')
    print()

if __name__ == "__main__":  
  os.system('clear')
  run()