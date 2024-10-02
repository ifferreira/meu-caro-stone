# meu-caro-stone
Detecção de faces em um vídeo.

Link para descrição da atividade:
https://rmnicola.github.io/m6-ec-encontros/meu-caro-stone/

Realizado com auxílio do código exemplo do professor, que pode ser encontrado em:
https://rmnicola.github.io/m6-ec-encontros/haar

# Como executar
Clone o repositório

    $ git clone https://github.com/ifferreira/meu-caro-stone


Instale as dependências

    $ cd meu-caro-stone/src
    $ pip install -r requirements.txt


Rode o projeto

    $ python main.py



# Perguntas Técnicas
## 2.1

O método de detecção escolhido foi o haarcascade. Ele é baseado em características pré-definidas - os classificadores treinados com características positivas e negativas de imagens - que são aplicadas sequencialmente. Esses classificadores processam a imagem em etapas, rejeitando rapidamente regiões que não são de interesse. Assim, se uma região é rejeitada em um estágio da cascata, ela não é processada nos estágios seguintes, o que acelera significativamente a detecção.

## 2.2
Classificação:
1. CNN(Convolutional Neural Network)
2. Haar Cascade
3. NN Linear
4. Filtros de correlação cruzada

Justificativa:

CNN:
- Viabilidade: Alta. Capaz de aprender padrões complexos e generalizar bem.
- Facilidade de implementação: Moderada. Requer conhecimento em deep learning, mas bibliotecas como Ultralytics facilitam.
- Versatilidade: Alta. Adapta-se a diversos cenários e variações de faces.

Haar Cascade:
- Viabilidade: Alta. Método tradicional e eficiente para detecção básica de faces.
- Facilidade de implementação: Alta. Simples de implementar com OpenCV.
- Versatilidade: Média. Limitado em cenários complexos e variações de pose.

NN Linear:
- Viabilidade: Baixa. Não adequado para padrões complexos como faces.
- Facilidade de implementação: Média. Simples de implementar, mas pouco eficaz.
- Versatilidade: Baixa. Muito limitado em suas aplicações.

Filtros de correlação cruzada:
- Viabilidade: Baixa. Não é específico para detecção de faces e requer definição de filtros específicos.
- Facilidade de implementação: Média. Pode ser implementado com OpenCV.
- Versatilidade: Baixa. Muito dependente da definição do filtro.

As CNNs, por sua capacidade de aprender características complexas das imagens, superam os outros métodos em termos de precisão e generalização. O Haar Cascade, embora mais simples, ainda é uma opção válida para aplicações menos exigentes. Os outros dois métodos, por sua natureza, são menos adequados para a tarefa de detecção de faces.

## 2.3
Classificação:
1. CNN
2. NN Linear
3. Haar cascade
4. Filtros de correlação cruzada

Justificativa:

CNNs
- As redes neurais convolucionais são especialmente eficazes para analisar imagens e extrair características relevantes, como as expressões faciais que indicam emoções.

NN Linear:
- Embora seja simples, não consegue capturar as complexidades das emoções humanas, que envolvem interações não lineares entre diferentes características faciais.

Haar Cascade:
- Desenvolvido para detecção de objetos em geral, não é especializado em identificar as sutilezas das expressões faciais.

Filtros de correlação cruzada:
- São ferramentas básicas de processamento de imagens e não possuem a capacidade de aprender e generalizar padrões complexos como as CNNs.

O melhor modelo para a detecção de emoções através da imagem de uma face é a CNN, pois ela é capaz de aprender padrões complexos e não-lineares em imagens, o que é essencial para a detecção de emoções. Os outros modelos, como Haar Cascade, NN Linear e filtros de correlação cruzada, são mais simples e não são capazes de aprender padrões complexos em imagens, o que pode limitar sua capacidade de detectar emoções com precisão.

## 2.4
As soluções apresentadas, como Haar Cascade e CNNs, são projetadas para analisar frames de forma isolada, não capturando a dinâmica entre eles, e portanto não sendo eficientes para perceber que em um frame a pessoa está feliz e isso influenciar na detecção do próximo frame. Dessa forma, para considerar variações entre frames e modelar sequências de emoções, uma alteração que poderia ser feita seria implementar uma abordagem temporal, com rastreamento de emoções ao longo do tempo. Ou, ainda, utilizar um algoritmo como o de fluxo óptico de Lucas-Kanade.

## 2.5
Vinicius Jr.