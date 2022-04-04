import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

x, y = sp.symbols("x y")

#calculo da funcao, func e a funcao em si e vx o valor do x
def funcao(func, vx):
    func = sp.sympify(func) #vai transformar a funcao q e uma string em uma funcao matematica com numero msm de vdd no python
    func = sp.lambdify(x, func) #vai transformar o func em praticamente um mini funcao onde o argumento e igual ao X
    return func(vx)

def soma_reimann(n_ret, func, intervA, intervB):
    #largura dos retângulos
    dx = (intervB-intervA)/n_ret

    #criando um conjunto de pontos para nosso cálculo
    x2 = np.linspace(intervA,intervB,N+1)

    # aplicando a função ao array x2 criado
    y2=funcao(func, x2)
    #y2 é um array com todos os elementos resultantes
    #da aplicação da função em x2

    #determinando o tamanho do gráfico 
    plt.figure(figsize=(7,5))
    #plotando nossa função
    plt.plot(x2,y2,'blue')

    #criando dois arrays de pontos para os retângulos
    x_right = x2[1:] 
    y_right = y2[1:]

    #plotando os retângulos
    plt.bar(x_right,y_right,width=-dx,alpha=0.2,align='edge',edgecolor='gray')
    plt.title('Gráfico 3: Soma de Riemann, N = {}'.format(n_ret))

    #calculando a soma das áreas
    x2 = np.linspace(dx,intervB,n_ret)
    riemann_sum = np.sum(funcao(func, x2) * dx)
    print("Área sobre a curva: ",riemann_sum)
    plt.show()

N = int(input('Digite o numero de retangulos: '))
interv_inicio = int(input('Digite o intervalo inicial: '))
interv_fim = int(input('Digite o intervalo final: '))
func = str(input('Digite a funcao: ')) #exemplo: 1 / (1 + x ** 2)

soma_reimann(N, func, interv_inicio, interv_fim)
