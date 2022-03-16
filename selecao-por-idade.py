#um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from datetime import datetime
print('\033[30;46m ---------- Confederação Nacional de Natação: ---------- \033[m')
nascimento = int(input('Digite o ano do seu nascimento:'))
idade = datetime.now().year - nascimento
if idade < 9:
    print('\033[30;43m Você tem {} anos e está na categoria MIRIM:\033[m'.format(idade))
elif idade <= 14:
    print('\033[30;43m Você tem {} anos e está na categoria INFANTIL:\033[m'.format(idade))
elif idade <= 19:
    print('\033[30;43m Você tem {} anos e está na categoria JÚNIOR:\033[m'.format(idade))
elif idade <= 25:
    print('\033[30;43m Você tem {} anos e está na categoria SÊNIOR:\033[m'.format(idade))
else:
    print('\033[30;43m Você tem {} anos e está na categoria MASTER:\033[m'.format(idade))
    