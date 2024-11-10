# PROJETO VALORANT

## Projetin criado por Froggie

###### A ideia desse projeto é pegar os dados dos torneios de Valorant pelo front, nos próprios forms e já enviar pro banco de dados, para trata-los como SQL.

##

## Tabelas

### Player

- Nick
  - É o nome do jogador no jogo.
- Team
  - É o nome do time que o jogador faz parte.
- Role
  - É a função dele, se ele é SENTINELA, DUELISTA, CONTROLADOR, INICIADOR ou FLEX.
- Camp
  - É o campeonato que o jogador jogou.
- Mapa
  - O mapa jogado na partida.
- Agent
  - O agente que foi jogado na partida.
- Round
  - A quantidade de round que teve a partida.
- Rating
  - Métrica que calcula o desempenho do jogador na rodada.
- KAST
  - Taxa de Kill, Assist, Survive e Trading.
- ADR
  - Média de dano por round do jogador.
- ACS
  - Média de dano por segundo do jogador.
- HS
  - Porcentagem de Headshot do jogador.
- Kill
  - Abates do jogador.
- Death
  - Mortes do jogador.
- Assist
  - Assistências do jogador.
- KDA
  - (Kill + Assist) / Death .
- KPR
  - Kill por Round -> Kill / Round.
- APR
  - Assist por Round -> Assist / Round .
- DPR
  - Death por Round -> Death / Round.
- Duels_Part
  - Participação em Duelos -> (Kills + Deaths) / Rounds.
- Sucess_Duels
  - Sucesso em Duelos -> Kills / (Kills + Deaths).
- FK (First Kill)
  - Primeiro Abate.
- FD (First Death)
  - Primeira Morte.
- FK_Part
  - Participações em FK da partida -> (FK + FD) / Rounds.
- FK_Sucess
  - Sucesso em FK -> FK / (FK + FD).
- FKPR
  - First Kill por Round -> FK / Round.
- FDPR
  - First Death por Round -> FD / Round.
- CL
  - Porcentagem de Clutches pelo jogador.
- CL_Win
  - Clutches Ganhos pelo jogador.
- CL_Played
  - Clutches Jogados pelo jogador.
- CL_Part
  - Participações em Clutches pelo jogador.
- CL_Sucess
  - Sucessos em Clutches pelo jogador.
- KMAX
  - Kill Máximo de um jogador.

### Team

- Team
  - Nome do time.
- Region
  - Região de onde o time é.
- Coach
  - Coach do time.
- Player
  - Jogadores do time.

### Tournaments

- Tournament
  - Torneio que está sendo avaliado
- Team
  - Times que estão jogando o torneio

## Links

Sigam meu [LinkedIn](https://www.linkedin.com/in/andleylct/).<br>
Sigam meu [Twitter](https://x.com/froggiebr/).

## Imagem ilustrativa

![This is an alt text.](/image/sample.webp "This is a sample image.")
