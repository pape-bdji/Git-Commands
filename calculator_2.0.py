#Operation Dictionaries 

class calculator:
  def __init__(self):
    self.operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }

  #Define Method to add operations 
  def add_operation(self, symbole, function):
    self.operations[symbole] = function 

  #Define Method to calculate
  def calculate(self, x, symbole, y):
    if symbole not in self.operations:
      raise ValueError("Symbole d'opération invalide")
    if not (isinstance(x,(float,int))and isinstance(y,(int,float))):
      raise ValueError("Les valeurs entréés doivent etre des nombre")
    
    function = self.operations[symbole]
    try :
      result = function(x, y)
      return result
    except ZeroDivisionError:
      print("Error: Cannot divide by zero")
      raise

  def puissance(self, x, y):
    return math.pow(x, y)

  def logarithme(self, x):
    return math.log(x, y)

  def racine_carre(self, x):
    return math.sqrt(x)


add = calculator()
add.add_operation("**" , calculator.puissance)
add.add_operation("log" , calculator.logarithme)
add.add_operation("sqrt" , calculator.racine_carre)

while True:
  try:
    choix = input('voulez vous quitter ')
    if choix == "yes" :
      break
    else:
      x = int(input('veuillez entrer un nombre'))
      symbole = input('veuillez entrer un symbole')
      y = int(input('veuillez entrer un nombre'))
      calcul = add.calculate(x, symbole, y)
      print(calcul)
  except Exception as e:
    print(e)

    
