# II. Encontre os valores para a variável y, onde y = ax + xb – c. Para os valores de a, b e c serão os três últimos
# números de seu RU. Caso, algum número do RU seja igual a zero, subisti-tuí-lo pelo número 3. Realizar o plot dos
# resultados onde será x = 5; x = 7 e x = 9. Para o plot você precisará utilizar a biblioteca matplotlib apresentada em
# aula, colocar legenda no gráfico, alterar a cor dos gráficos( linhas ou pontos), nomear o eixo x, nomear o eixo y.

# importando bibliotecas a serem utilizadas
import matplotlib.pyplot as plt
import numpy as np

# armazenando os 3 últimos números do meu RU (o 'b' era 0, então mudei para 3)
a = 9
b = 3
c = 9
xpoints = np.array([5, 7, 9])  # utilizando Numpy para armazenar a lista com os valores de 'x'.

# realizando o cálculo para cada eixo x.
y1 = ((a * xpoints[0]) + (xpoints[0] * b)) - c
y2 = ((a * xpoints[1]) + (xpoints[1] * b)) - c
y3 = ((a * xpoints[2]) + (xpoints[2] * b)) - c
ypoints = np.array([y1, y2, y3])  # armazenando os resultados de 'y' em uma lista.

# fazendo o plot com as listas dos eixos 'x' e 'y', e estilizando linha do gráfico.
plt.plot(xpoints, ypoints, marker='o', ms='7', mfc='r',  linestyle='-.', c='#003267', linewidth='2', label='linha')

# personalizando o gráfico que apresentará os eixos 'x' e 'y'.
plt.xlabel('eixo x', size='10', loc='right')
plt.ylabel('eixo y', size='10', rotation=0, loc='top')
plt.title('Gráfico de linha')
plt.grid(color='#fcb414', linestyle=':', linewidth='1')
plt.legend(title='Legenda')
plt.text(5.1, 50.5, '51')
plt.text(7.1, 74.3, '75')
plt.text(9, 96.7, '99')
plt.show()  # exibindo o gráfico finalizado
