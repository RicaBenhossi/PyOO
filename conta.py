import decimal as dec


class Conta:
    # HERE LIMITE HAS A DEFAULT VALUE (100). IF SOMEONE INSTANCES CONTA WITHOUT PASSIN THE VALUE FOR LIMITE, IT WILL
    # ASSUME 100
    def __init__(self, numero, titular, saldo, limite=100):
        print(f"Construindo objeto. {self}")
        self.__numero = numero              # WITH __ YOU TURN THE ATTRIBUTE PRIVATE
        self.__titular = titular            # BUT, ALTHOUGH IT IS PRIVATE YOU STILL CAN ACCESS
        self.__saldo = dec.Decimal(saldo)   # PYTHON DOESN´T FORBID YOU, BUT WARN YOU THAT YOU SHOLD NOT DO IT
        self.__limite = limite              # BY SHOWING UNDERSCORES WHEN YOU CALL THESE ATTRIBUTES

    def extrato(self):
        print(f"O saldo da conta do titular {self.__titular} é de R${self.__saldo}.")

    def deposita(self, valor):
        self.__saldo += dec.Decimal(valor)
        print(f"Depósito de R${valor} realizado com sucesso.")

    def saca(self, valor):
        self.__saldo -= dec.Decimal(valor)
        print(f"Saque de R${valor} realizado com sucesso.")

    def transefere(self, valor: float, conta_destino: "Conta"):
        self.saca(dec.Decimal(valor))
        conta_destino.deposita(dec.Decimal(valor))
        print(f"Transferência realizada com sucesso.")
