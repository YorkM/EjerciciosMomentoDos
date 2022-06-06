class Cuenta:
    def __init__(self, cuenta, saldo):
        self.numero_cuenta=cuenta
        self.saldo=saldo
    
    def get_saldo(self):
        return self.saldo

    def get_numero(self):
        return  self.cuenta


    def set_saldo(self,saldo):
        self.saldo=saldo

    def set_numero(self,numero):
        self.cuenta=numero