# PCO138A

1 - Utilizando um sensor ultrassônico, meça a distância de algum objeto no intervalo de 5 segundos. 

Caso a distancia entre a leitura atual e a nova distância seja maior que 20 centímetros,  
a esp deve enviar por mqtt um programa desenvolvido em python com uma mensagem de alteração 
de posição de objeto. O programa deve imprimir no console a alteração de posição, após a impressão 
deve enviar uma mensagem para a esp indicando que ela deve parar a leitura, e piscar o led da própria 
esp, indicando que ela parou as leituras. Um buzzer deve ser acionado quando a leitura parar.
