sedentario = 1.2
levemente = 1.375
moderadamente = 1.555
muito = 1.725
extremamente = 1.9

fisicamente = input('você se considera sedentario, levemente ativo, moderadamente ativo, muito ativo ou extremamente ativo?: ').strip().lower()
peso = float(input('qual seu peso? '))
altura = int(input('qual sua altura?(cm) '))
idade = int(input('qual sua idade? '))

tmb = (10 * peso) + (6.25 * altura) - (5 * idade) - 161

if fisicamente == 'sedentario':
    print(round(tmb * sedentario))
elif fisicamente == 'levemente':
    print(round(tmb * levemente))
elif fisicamente == 'moderadamente':
    print(round(tmb * moderadamente))
elif  fisicamente == 'muito':
    print(round(tmb * muito))
elif fisicamente == 'extremamente':
    print(round(tmb * extremamente))