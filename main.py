class MageOfAddition:
    def add(self, a, b):
        return a + b
class WarriorOfSubtraction:
    def subtract(self, a, b):
        return a - b

class RangerOfMultiplication:
    def multiply(self, a, b):
        return a * b

class ClericOfDivision:
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Divisão por zero não permitida!"

# Criação dos objetos (heróis)
mage = MageOfAddition()
warrior = WarriorOfSubtraction()
ranger = RangerOfMultiplication()
cleric = ClericOfDivision()

# Resolver o enigma mágico
# Substituam as variáveis x1, x2, x3, x4, x5 pelos valores apropriados para cada fórmula

def formula1():
    
    x1 = 10
    x2 = 5
    x3 = 4
    x4 = 2
    x5 = 3


    resultado = mage.add(x1, x2)
    resultado = ranger.multiply(resultado, x3)
    resultado = cleric.divide(resultado, x4)
    resultado1 = warrior.subtract(resultado, x5)
    print(f"Resultado Fórmula 1: {resultado1}")


# formula 2 
def formula2():
    
    x1 = 8
    x2 = 3
    x3 = 7
    x4 = 5
    x5 = 2

    resultado =  ranger.multiply(x1, x2)
    resultado = mage.add(resultado, x3)
    resultado = cleric.divide(resultado, x4)
    resultado2 = warrior.subtract(resultado, x5)

    print(f"Resultado da fórmula 2: {resultado2}")

#  
def formula3():

    x1 = 25
    x2 = 5
    x3 = 4
    x4 = 6
    x5 = 10

    resultado =  warrior.subtract(x1, x2)
    resultado = cleric.divide(resultado,x3)
    resultado = ranger.multiply(resultado, x4)
    resultado3 = mage.add(resultado, x5)

    print(f"Resultado da fórmula 3: {resultado3}")
# 4
def formula4():
    x1 = 9
    x2 = 2
    x3 = 4
    x4 = 3
    x5 = 5
    
    resultado =  mage.add(x2, x3)
    resultado = ranger.multiply(resultado,x1)
    resultado = cleric.divide(resultado, x4)
    resultado4 = warrior.subtract(resultado, x5)

    print(f"Resultado da fórmula 4: {resultado4}")


            
if __name__ == "__main__": 
    formula1()
    formula2()
    formula3()
    formula4()
        
