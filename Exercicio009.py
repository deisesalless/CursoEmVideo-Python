a = input('Digite algo: ')

print('Você digitou {}' .format(a))
print('O tipo primitivo desse valor é ', type(a))
print('Tem espaços? ', a.isspace())
print('É um numero? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumerico? ', a.isalnum())
print('É menusculo?', a.islower())
print('É letra maiuscula? ', a.isupper())
print('Está capitalizada? ', a.istitle())