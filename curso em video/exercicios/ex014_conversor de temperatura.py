opcao = 1
while opcao != 0 : 
    opcao = int(input('Opção:\n[1]Coverter de celcio para fareheit\n[2]Coverter de fareheit para celcio\n[0]sair\n'))
    if opcao == 1:
        print('=== Converter Celcio em fareheit ===')
        celcio = float(input('Qual é a temperatura atual em ºc? '))
        f = celcio * 1.8 +32
        print('A temperatura de {:.0f}ºc equivale a {:.0f} ºf \n'.format(celcio,f))
    elif opcao == 2:
        print('=== Converter fareheit em Celcio ===')
        fareheit = float(input('Qual é a temperatura atual em ºf? '))
        c = fareheit - 32/9
        print('A temperatura de {:.0f}ºf equivale a {:.0f} ºc \n'.format(fareheit, c))
    else: print('Opção inválida!\n')
else: print('Você saiu!')