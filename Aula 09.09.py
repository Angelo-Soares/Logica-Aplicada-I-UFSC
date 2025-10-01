# Aula Funções

'''
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=0

def soma():
    c=a+b
    print(c)
    return c

def main():
    c=soma()
    d=c+1
    print(d)

if __name__ == '__main__':
    main()'''




#exercicio 2
'''
#imports
import numpy as np

x=np.random.rand(5)
w=np.random.rand(5)
b=1
v=0

def JuncaoAditiva():
    u=0
    print(x)
    print(w)
    for i in range(len(x)):
        v=x[i]*w[i]
        u=u+v
        print(v)
        print(u)
    u=u-b
    print(u)
    return u

def main():
    z=JuncaoAditiva()
    print(z)
    if (z>=0):
        y=1
        print(f'A rede neural foi ativada com valor igual a: {y}')
    elif(z<0):
        y=0
        print(f'A rede neural foi desligada com valor igual a: {y}')

if __name__ == '__main__':
    main()'''