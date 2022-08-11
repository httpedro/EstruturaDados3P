def fatorial(numero):
    N=numero
    i = 2
    contador = 1
    if(N<=0):
        print("fatorial de ",N," é ", contador)
    else:
        while(i<=N):
            contador=contador*i
            i=i+1
        print("o fatorial de ",N," é igual a: ",contador)

print(fatorial(10))