'''#exercicio
#imports

import numpy as np

x=np.random.rand(5)
w=np.random.rand(5)
b=1
v=0
beta=0.25
a=0

def JuncaoAditiva():
    u=0

    for i in range(len(x)):
        v=x[i]*w[i]
        u=u+v
    u=u-b
    return u

def main():
    z=JuncaoAditiva()
    a=-1*beta*z
    y=1/(1+(np.exp(a)))

    print(f'A saida do neuronio é {y}')

if __name__ == '__main__':
    main()'''