a = ['1','2','3','4','5','6','7','8']
print('string of numebers ',a)

t1 = time.time()
a = list( map(int,a) )
t2 = time.time()
print(f'int of numbers [{t2 - t1:.15f}]s ',a)