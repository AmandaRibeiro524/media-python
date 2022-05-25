print('Média do aluno')
#Números decimais devem possuir ponto "." no lugar da vírgula
a1= float(input('Insira a nota da A1: ')) 
a2= float(input('Insira a nota da A2: '))
p1= float(input('Insira a nota da P1: '))
p2= float(input('Insira a nota da P2: '))

media= (a1+a2+p1+(p2*2))/5
print('media=', media)

if media >=6: 
  print('PASSEI NESSA MERDA!')
else: 
  print('DP, choro, grito e depressão')
