for i in range(10,100):
    summ = i%10 + i//10
    summ += summ**2
    if summ == i:
        print(i)