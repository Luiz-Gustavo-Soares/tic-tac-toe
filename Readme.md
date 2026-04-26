# Jogo da Velha com Minimax

Este projeto é uma implementação do clássico **Jogo da Velha (Tic-Tac-Toe)** em Python, incluindo uma **IA baseada no algoritmo Minimax**, capaz de jogar de forma ótima contra o jogador.

---

## Funcionalidades

* Tabuleiro NxN (padrão 3x3)
* Jogador vs Computador
* IA utilizando algoritmo **Minimax**
* Verificação automática de:

  * Vitória
  * Empate
  * Fim de jogo
* Interface simples via terminal

---

## Como jogar

* Ao iniciar, escolha se deseja começar jogando (`s` para sim, `n` para não)
* O tabuleiro será exibido no terminal
* Escolha uma posição de **1 a 9**, conforme o esquema:

```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

* O jogador utiliza `X` e a IA utiliza `O`

---

## Sobre a IA

A IA utiliza o algoritmo **Minimax**, que:

* Explora todas as jogadas possíveis
* Assume que o jogador também joga de forma ótima
* Sempre escolhe a melhor jogada possível

Isso significa que:

* Você **não consegue vencer a IA** se ela jogar corretamente
* O melhor resultado possível contra ela é o empate
