class numcomplexo:
    def __init__(self,com1,com2,com3):
        self.n1=com1
        self.n2=com2
        self.n3=com3

    def somar(self):
        soma=self.n1+self.n2+self.n3
        print(soma)

    def subtrair(self):
        subtracao=self.n1-self.n2-self.n3
        print(subtracao)

    def multiplicar(self):
        multiplicacao=self.n1*self.n2*self.n3
        print(multiplicacao)
    
    def dividir(self):
        divisao=self.n1/self.n2/self.n3
        print(divisao)

a=float(input("Qual número será a parte real do primeiro número complexo?"))
b=float(input("Qual número será a parte imaginária do primeiro número complexo?"))
c=float(input("Qual número será a parte real do segundo número complexo?"))
d=float(input("Qual número será a parte imaginária do segundo número complexo?"))
e=float(input("Qual número será a parte real do terceiro número complexo?"))
f=float(input("Qual número será a parte imaginária do terceiro número complexo??"))


com1=complex(a,b)
com2=complex(c,d)
com3=complex(e,f)

resultado=numcomplexo(com1, com2, com3)
print("O resultado da soma é:")
print(resultado.somar())
print("O resultado da subtração é:")
print(resultado.subtrair())
print("O resultado da multiplicação é:")
print(resultado.multiplicar())
print("O resultado da divisão é:")
print(resultado.dividir())