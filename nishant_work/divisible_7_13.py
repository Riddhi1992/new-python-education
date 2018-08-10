# Divisible program in a range 324 to 444372

def div(min,max):
    lis_num = []
    if min > 0 and max > 0:
        try:
            for num in range(min, max+1):
                if num % 7 == 0 and num % 13 == 0:
                    lis_num.append(num)
            return lis_num
        except(TypeError):
            err = 'value must be positive'
            return err
    else:
        return 'negative value not allow'

x = div(324, 444372)
print(x)