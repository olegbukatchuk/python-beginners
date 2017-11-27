def echo(user, lang, sys):
    print('User:', user, 'Languege:', lang, 'Platform:', sys)

echo('Mike', 'Python', 'Windows')
echo(lang='Python', sys='MacOS', user='Anne')

def mirror(user='Carole', lang='Python'):
    print('\nUser:', user, 'Language:', lang)

mirror()
mirror(lang='Java')
mirror(user='Anna')
mirror('Oleg', 'C++')
