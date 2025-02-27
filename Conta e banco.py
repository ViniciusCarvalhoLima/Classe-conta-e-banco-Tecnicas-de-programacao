class Conta:
    def __init__(self, numero):
        self.__numero = numero
        self.__saldo = 0.0

    
    def creditar(self, valor:float) -> None:
        self.__saldo += valor

    def debitar(self, valor:float) -> None:
        self.__saldo -= valor

    def get_numero(self) -> str:
        return self.__numero

    def get_saldo(self) -> float:
        return self.__saldo
    

class Banco:
    def __init__(self):
        self.__contas = []
        self.__saldo = 0.0

    def cadastrar(self, conta: Conta) -> None:
        self.__contas.append(conta)

    def procurar(self, numero: str) -> Conta:
        for conta in self.__contas:
            if conta.get_numero() == numero:
                return conta
        return None

    def creditar(self, numero: str, valor: float) -> None:
        conta = self.procurar(numero)
        if conta is not None:
            conta.creditar(valor)

    def debitar(self, numero: str, valor: float) -> None:
        for conta in self.__contas:
            if conta.get_numero() == numero:
                if conta.saldo >= valor:
                    conta.saldo -= valor
                    return
                else:
                    raise ValueError("Saldo insuficiente para realizar o débito.")
        raise ValueError("Conta não encontrada.")

    def saldo(self, numero: str) -> float:
        for conta in self.__contas:
            if conta.get_numero() == numero:
                return self.__saldo
            else:
                raise ValueError("conta inexistente")

    def transferir(self, origem: str, destino: str, valor: float) -> None:
        conta_origem = None
        conta_destino = None
        
        for conta in self.__contas:
            if conta.get_numero() == origem:
                conta_origem = conta
            if conta.get_numero() == destino:
                conta_destino = conta

            if conta_origem is None:
                raise ValueError(f"Conta de origem '{origem}' não encontrada.")
            if conta_destino is None:
                raise ValueError(f"Conta de destino '{destino}' não encontrada.")
            if conta_origem.get_saldo() < valor:
                raise ValueError("Saldo insuficiente para a transferência.")
            if valor <= 0:
                raise ValueError("O valor da transferência deve ser positivo.")

            conta_origem.debitar(valor)
            conta_destino.creditar(valor)

        print(f"Transferência de {valor:.2f} realizada de {origem} para {destino}.")