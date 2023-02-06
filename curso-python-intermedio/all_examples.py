DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

# List Comprehension and Dictionary Comprehension
# High Order Functions map, filter and reduce
# lambda

from functools import reduce

def filterData():
    print("****************************** FILTER DATA ******************************")
    all_python_devs = [worker["name"] for worker in DATA if worker["language"]=="python"]
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"],adults))
    old_people = list(map(lambda worker: {**worker , **{"old": worker["age"] > 70}},DATA))

    numbers = [2,2,2,2,2,2,2,2]
    result = reduce(lambda a, b: a * b ,numbers)

    print(all_python_devs)
    print(adults)
    print(old_people)
    print("El resultado es",result)

# MANEJO DE ERRORES
# Try, Except, Finally and Raise
# Assert

def divisors(number) :
    return [divisor for divisor in range(1,number+1) if number % divisor == 0]

def get_divisors():
    print("****************************** GET DIVISORS ******************************")
    # Try, Except, Finally and Raise
    try:
        num = int(input("Ingrese un numero: "))
        if num < 0:
            raise("El numero no puede ser negativo")
        print("Los divisores son:", divisors(num))
    except ValueError as ve:
        print("El error es", ve)
    finally:
        print("Finalizo el programa")

    # Assert
    num = input("Ingrese un numero: ")
    assert int(num) > 0 ,"El numero no puede ser negativo"
    assert num.isnumeric() ,"Debe ser un numero, no un texto"
    print("Los divisores son:", divisors(int(num)))

def run() :
    filterData()
    get_divisors()

if __name__ == "__main__":
    run()