# 2018/19 australian income tax brackets and tax rates
bracket1=18200
bracket2=37000
bracket3=90000
bracket4=180000
rate1=0.19
rate2=0.325
rate3=0.37
rate4=0.45

# user input
x = int(input('Enter taxable income: '))

def inc_tax (x):
    '''calculates tax based on income enterd'''
    if x<=bracket1:
        return 0
    elif x<=bracket2:
        return (x-bracket1)*rate1
    elif x<=bracket3:
        return (x-bracket2)*rate2+(bracket2-bracket1)*rate1
    elif x<=bracket4:
        return (x-bracket3)*rate3+(bracket3-bracket2)*rate2+(bracket2-bracket1)*rate1
    elif x>bracket4:
        return (x-bracket4)*rate4+(bracket4-bracket3)*rate3+(bracket3-bracket2)*rate2+(bracket2-bracket1)*rate1

# show results
print('Net income: ')
print(x-inc_tax(x))
print(' ')
print('Tax paid: ') 
print(inc_tax(x))
print(' ')
print('Effective tax rate: ')
print(inc_tax(x)/x)
