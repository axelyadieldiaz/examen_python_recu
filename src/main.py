#Observacion -> no se devera usar metodos como sum(),min(),max().
# se podra usar for, while, insert, split,join,append -> solo los metodos que se vio en clase

# 1. la funcion recibe como parametro un array y devera devolver el numero mayor del array
def numero_mayor(arr):
    if len(arr) == 0:
        return None  
    mayor = arr[0]
    for elemento in arr:
        if elemento > mayor:
            mayor = elemento

    
            mayor = elemento   
    return mayor
  

# 2. la funcion recibe un string la funcion devera devolver el string ivertido ejem:entrada=hola, devuleve=aloh
def inverso(txt):
    return ''.join(reversed(txt))

# 3. la funcion recibe un string y devuelve si la plabara es un palindromo True si no devuelve False: palindromo que se lee igual de derecha a izquierda y viceversa ejm: entrada=reconocer es palindromo se le igual de izquierda a derecha y viciversa
def palindromo(txt):
    txt = txt.replace(" ", "").lower()
    
    return txt == txt[::-1]


# 4. la funcion recibe como parametro una letra y devuelve si la letra ingresada es vocal o consonante el mensaje devera ser si es vocal = 'es vocal' si es consonante 'es consonante'
def es_vocal(letra):
    # Convertir la letra a minúsculas
  letra = letra.lower()

    # Verificar si la entrada es una sola letra
  if len(letra) == 1:
      if letra in 'aeiou':
          return 'es vocal'
      else:
          return 'es consonante'
  else:
      return 'No es una letra válida'

# Ejemplos de uso:
print(es_vocal('a'))  
print(es_vocal('B'))  
print(es_vocal('ab')) 
