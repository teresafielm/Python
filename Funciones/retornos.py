# Función de una sucesión geométrica 
def sumGeometric(a, r, n): 
   # Si el radio tiene un valor de uno 
   if r == 1: 
      return a * n 
   # Calcula la suma geométrica cuando el radio es diferente de uno 
   s = a * (1 - r ** n) / (1 - r) 
   #regresa el valor de s 
   return s

#Para importar una función realizada por alguien más se puede utilizar la palabra reservada import. 

#Con las versiones diferentes de Python, también se puede utilizar el siguiente código para permitir que la nueva función sea importada:
#if __name__ == "__main__": 
#   main() 


print (sumGeometric (3,3,4))
