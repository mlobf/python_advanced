"""Apenas uma abstracao de como pode ser implementado este processo
    de controle de total_de_creditos oriundo de free_games.
"""
from typing import List
from dataclasses import dataclass, field


@dataclass
class FreeGamesFinancial:
    """Armazena os dados financeiros relacionados aos jogos.
    """
    saldo_inicial: float
    descricao: str
    lista_jogadas: List[float] = field(default_factory=list)
    total_de_creditos: float = 0.0
    total_de_debitos: float = 0.0

    def __post_init__(self):
        """Valida os dados iniciais após a inicialização."""
        if self.saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
        if self.total_de_creditos < 0 or self.total_de_debitos < 0:
            raise ValueError(
                "Os totais de créditos e débitos não podem ser negativos.")


class FreeGamesFinancialManager:
    """Gerenciador para a classe FreeGamesFinancial."""

    def __init__(self, financial: FreeGamesFinancial):
        self.financial = financial

    def salva_status_no_mongodb(self):
        """Salva copia da jogada no mongoDb"""
        ...

    def adicionar_draw_state(self, valor: float) -> None:
        """Adiciona um valor à lista de jogadas."""
        if valor < 0:
            raise ValueError("O valor adicionado não pode ser negativo.")
        self.financial.lista_jogadas.append(valor)

    def adicionar_premios(self, valor: float) -> None:
        """Adiciona um prêmio ao total de créditos."""
        if valor < 0:
            raise ValueError("O valor do prêmio não pode ser negativo.")
        self.financial.total_de_creditos += valor

    def adicionar_pagamentos(self, valor: float) -> None:
        """Adiciona um pagamento ao total de débitos."""
        if valor < 0:
            raise ValueError("O valor do pagamento não pode ser negativo.")
        self.financial.total_de_debitos += valor

    def __repr__(self) -> str:
        """Mostra um resumo dos dados financeiros."""

        decricao = f"Descrição: {self.financial.descricao}"
        saldo_inicial = f"Saldo Inicial: {self.financial.saldo_inicial}"
        total_creditos = f"Total de Créditos: {self.financial.total_de_creditos}"
        total_debitos = f"Total de Débitos: {self.financial.total_de_debitos}"
        total_jogadas = f"Jogadas: {self.financial.lista_jogadas}"

        return (print(
            decricao + saldo_inicial + total_creditos+ total_debitos + total_jogadas + total_jogadas
        ))


# Exemplo de uso
try:
    financia = FreeGamesFinancial(
        saldo_inicial=100.0, descricao="Finanças de Jogos"
    )

    manager = FreeGamesFinancialManager(financia)
    manager.adicionar_draw_state(10.0)
    manager.adicionar_premios(50.0)
    manager.adicionar_pagamentos(20.0)
    manager.__repr__()

except ValueError as e:
    print(e)
