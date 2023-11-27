> **Aluno:** Jonatan Felipe Hartmann\
> **Disciplina**: EEL7123-08235 - Tópicos Avançados em Sistemas Digitais

**Otimização da operação de exponenciação em vetores de 4 bits**

Neste trabalho, buscou-se otimizar a operação de exponenciação em um vetor de 4 bits, sendo x², x³ e x⁴ as operações abordadas. Além disso, também pensou-se em analisar a progressão do número de vetores finais necessários para realizar estas operações.
Dessa forma, foram utilizadas duas maneiras para tal otimização, sendo:

- Distribuição de bits: consiste em juntar dois bits iguais e colocar uma representação sua na próxima posição.
- Combinação de bits utilizando tabela verdade: permite que bits semelhantes em uma posição sejam analisados combinacionalmente a fim de otimizar sua soma, várias combinações foram usadas.

Além disso, foi também analisada a possibilidade de usar a Recodificação de Booth para otimização, entretanto, como a recodificação faz uso de bits negativos, deveria ser utilizado complemento de 2 para sua representação, aumentando consideravelmente o atraso para calcular a operação. Logo, foi necessário descartar essa alternativa.

Após otimizar as tabelas, notou-se que para um binário de 4 bits, a quantidade n de vetores a serem somados para elevar esse número à uma certa potência, é exatamente o mesmo número que o expoente determinado

Apesar desse resultado, ao comparar com o resultado da operação ao cubo de um número de 5 bits (dado durante a disciplina), nota-se que para um número Y de 5 bits a progressão não é a mesma. Isso foi considerado visto que para Y² é preciso 3 vetores, e para Y³ é necessário 5.
