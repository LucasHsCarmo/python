class Conta:
    
    def __init__(self,conta,titular,saldo,limite):
        print("Construindo objeto... {}".format(self))
        self.conta = conta
        self.titular = titular
        self.saldo = saldo
        self.limite = limite