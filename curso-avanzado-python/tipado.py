# Install MYPY: pip3 install mypy
# Run code with: mypy tipado.py --check-untyped-defs
# El (mypy tipado.py --check-untyped-defs) flag nos permite  ver errores de tipo

def is_palindrome(word:str) -> bool:
  word = word.replace(" ", "").lower()
  return word == word[::-1]

def run():
  print("Ana Ana")
  print(is_palindrome(1000))

if __name__ == "__main__":
  run()

