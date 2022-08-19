# Desenvolver a classe calculadora que faça qualquer operação matemática utilizando dois números inteiros,
# sendo os dois últimos número de seu RU. Caso o RU termine com zero, substituí-lo pelo número 1. Sendo as possíveis
# operações matemáticas: soma, subtração, multiplicação, divisão, exponenciação e módulo. Para isto, o algoritmo deverá
# ter um MENU que possíbilite ao usuário escolher qual o tipo de operação que se deseja realizar. Apresentar todas as
# operações matemáticas da calculadora funcionando!

class Calculadora:  # criando classe para calculadora.
    def __init__(self, ligada):
        self.ligada = ligada  # atributo criado para controlar o estado da calculadora(ligada ou desligada).

    def menu(self):  # método que mostra os tipos de operações e faz o cálculo escolhido pelo usuário.
        while self.ligada:  # o loop funciona somente se a calculadora estiver "ligada"(self.ligada = True).
            print(' /+-*/ Calculadora /+-*/')

            num1 = int(input('Digite o primeiro número: \n'))  # armazena o 1º número que será calculado
            operacao = input('Escolha uma operação: \n+ -> Adição | - -> Subtração | * -> Multiplicação\n'
                             '/ -> Divisão | ^ -> Potência | % -> Módulo\n')  # armazena a operação escolhida
            num2 = int(input('Digite o segundo número: \n'))  # armazena o 2º número que será calculado

            # condicional que faz o cálculo de acordo com a operação escolhida pelo usuário.
            if operacao == '+':
                print(f'\n{num1} + {num2} = {num1+num2}\n')
            elif operacao == '-':
                print(f'\n{num1} - {num2} = {num1 - num2}\n')
            elif operacao == '*':
                print(f'\n{num1} x {num2} = {num1 * num2}\n')
            elif operacao == '/':
                print(f'\n{num1} / {num2} = {round(num1 / num2,4)}\n')
            elif operacao == '^':
                print(f'\n{num1} ^ {num2} = {num1 ** num2}\n')
            elif operacao == '%':
                print(f'\n{num1} % {num2} = {num1 % num2}\n')

            # verifica se o usuário deseja realizar outra operação
            operacao = input('Calcular novamente? s -> Sim | n -> Não\n').lower()
            if operacao == 'n':
                self.ligada = False  # se o usuário não quiser realizar mais cálculos, a calculadora será desligada.
            elif operacao != 's':
                print('Valor inválido, desligando calculadora...')
                self.ligada = False  # caso o valor seja inválido, a calculadora também será desligada.


# Instanciando objeto para utilização da calculadora
calculadora3000 = Calculadora(True)  # o estado da calculadora pode ser decidido através do parâmetro
calculadora3000.menu()  # após ligada, a calculadora irá executar o método que faz os cálculos.
