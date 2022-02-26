import decimal as dec


class Conta:
    # HERE LIMITE HAS A DEFAULT VALUE (100). IF SOMEONE INSTANCES CONTA WITHOUT PASSIN THE VALUE FOR LIMITE, IT WILL
    # ASSUME 100
    def __init__(self, conta, titular, saldo, limite=100):
        print(f"Construindo objeto. {self}")
        self.__conta = conta              # WITH __ YOU TURN THE ATTRIBUTE PRIVATE
        self.__titular = titular            # BUT, ALTHOUGH IT IS PRIVATE YOU STILL CAN ACCESS
        self.__saldo = dec.Decimal(saldo)   # PYTHON DOESN´T FORBID YOU, BUT WARN YOU THAT YOU SHOLD NOT DO IT
        self.__limite = limite              # BY SHOWING UNDERSCORES WHEN YOU CALL THESE ATTRIBUTES

    def __permite_saque(self, valor_saque):
        disponivel_para_saque = self.__saldo + self.__limite
        return valor_saque <= disponivel_para_saque

    def extrato(self):
        print(f"O saldo da conta do titular {self.__titular} é de R${self.__saldo}.")

    def deposita(self, valor_deposito):
        if (valor_deposito > 0):
            self.__saldo += dec.Decimal(valor_deposito)
            print(f"Depósito de R${valor_deposito} realizado com sucesso.")
        else:
            print(f"Valor de R${valor_deposito} informado é inválido.")
            print("Informe um valor maior que 0.")

    def saca(self, valor):
        if (self.__permite_saque(valor)):
            self.__saldo -= dec.Decimal(valor)
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo sinsuficiente para o saque.")

    def transefere(self, valor: float, conta_destino: "Conta"):
        self.saca(dec.Decimal(valor))
        conta_destino.deposita(dec.Decimal(valor))
        print(f"Transferência realizada com sucesso.")

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular.title()

    @property
    def conta(self):
        return self.__conta

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @staticmethod
    def banco():
        return "341"

    @staticmethod
    def bancos():
        return {"BB": "001", "ITAU": "341", "NuBank": "260"}
