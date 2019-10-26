import random 

cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] 

def cartaSig(): 
    return random.choice(cartas)

def manoTotal(mano): 
    valores = [None, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10] 
    valorCarta = {k: v for k, v in zip(cartas, valores)} 

    print(valorCarta)

    total = sum([valorCarta[carta] for carta in mano if carta != 'A']) 

    contarAs = mano.count('A')
    
    for i in range(contarAs, -1, -1):
        if i == 0: 
            total = total + contarAs 
        elif total + (i * 11) + (contarAs - i) <= 21: 
            total = total + (i * 11) + contarAs - i 
            break

    return total

class Dealer(): 
    def __init__(self): 
        self.mano = [] 

    def rondaSig(self): 
        self.mano = [cartaSig(), cartaSig()]

    def get_manoTotal(self): 
        return manoTotal(self.mano)
    
    def determinar(self, total): 
        if total < 17: 
            return 'pedir' 
        else: 
            return 'quedarse'
    
    def make_play(self): 
        return self.determinar(self.get_manoTotal())