try:
    num1 = int(input('Number: '))
    num2 = int(input('Number: '))
    print(num1 / num2)
except ZeroDivisionError:  # Nome do erro que aparece quando roda o programa
    print('ERROR: 0 (ZERO) cannot be the divisor')
except ValueError:
    print('ERROR: Use only numbers')
except:
    print('UNKNOWN ERROR: Something went Wrong')
