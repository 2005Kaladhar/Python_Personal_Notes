'''
Formula for calculating fibonacci series
Fn = Fn-1 + Fn-2


0 1 1 2 3 5 8 13 21
'''
def fabo_recur(num):
    if num == 0:
        return 0
    elif num ==1 :
        return 1
    else:
        return fabo_recur(num-1) + fabo_recur(num-2)


def fabo_iter(num):
    try:
        return __private__temp[num]
    except Exception as error:
        print(f"Entered Exception {error}")
        try:
            temp = globals()['__private__temp']
        except Exception as e :
            globals()['__private__temp'] = [0,1]
            temp = globals()['__private__temp']

    for i in range(len(temp)-1,num-1):
        temp.append(temp[i]+temp[i-1])
    return temp



