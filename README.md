# 🍕 Pizzaria Delivery Cafarnaum - Otimização de Rotas com Algoritmo Genético

## 🚀 Descrição do Problema
Este projeto visa otimizar a rota de entregas de pizzas para uma pizzaria localizada na cidade de **Cafarnaum-BA**. O objetivo é reduzir o tempo e a distância total percorrida pelo entregador ao distribuir pizzas para diversos clientes espalhados pela cidade.

## 🎯 Objetivos Principais
- Encontrar a rota mais curta e eficiente possível para entregas.
- Reduzir significativamente o tempo total de entrega e custos associados.

## 📍 Locais Utilizados
Foram utilizados 18 pontos de entrega reais distribuídos pela cidade de Cafarnaum-BA. As coordenadas foram obtidas através do Google Maps.

## 🛠️ Metodologia Utilizada
O problema foi solucionado utilizando um **Algoritmo Genético**, implementado em Python com as bibliotecas `DEAP`, `geopy`, `matplotlib` e `folium`.

**Parâmetros principais:**
- Tamanho da População: 200 indivíduos
- Número de Gerações: 200 gerações
- Taxa de crossover (cruzamento): 80%
- Taxa de mutação: 20%

## 📈 Resultados Alcançados
Após executar o algoritmo, obteve-se os seguintes resultados comparativos:

| Método                             | Distância Total (km) |
|------------------------------------|----------------------|
| Média rota aleatória               | ~14.81 km            |
| Melhor rota aleatória obtida       | ~9.35 km             |
| **Algoritmo Genético otimizado**   | **~6.22 km** ✅      |

Observa-se claramente que o Algoritmo Genético obteve uma redução significativa na distância total da rota.

## 🗺️ Visualização dos Resultados
- **Mapa Interativo:** O arquivo `rota_otimizada_pizzaria.html` mostra a rota otimizada em um mapa interativo.
- **Gráfico Estático:** Um gráfico da rota otimizada também é exibido no terminal ao executar o script Python.

## 📦 Como executar o projeto (passo a passo):

```bash
# Clone o repositório
git clone https://github.com/leonardodevbr/fiap-tech-challenge tech-challenge

# Acesse o diretório
cd tech-challenge

# Crie e ative o ambiente virtual (recomendado)
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute o script
python main.py
```

## 📝 Conclusão
A solução implementada demonstrou claramente a eficiência do Algoritmo Genético na otimização da rota de entregas, proporcionando economia de tempo, recursos e aumento na satisfação dos clientes da Pizzaria Delivery Cafarnaum-BA.

## 💻 Desenvolvido por:
### Leonardo Nunes Oliveira
#### FIAP - Pós-graduação em IA para Devs