class Pessoa:
    def __init__(self, nome , idade):     #construtor com seus parametros
              self.nome  = nome
              self.idade = idade
    
    def setNome(self,nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade

class PessoaFisica(Pessoa):
    def __init__(self, CPF, nome, idade):
        super().__init__(nome, idade)
        self.CPF = CPF

    def getCPF(self):
         return self.CPF
         
    def setCPF(self, CPF):
        self.CPF = CPF
    
a = PessoaFisica('40909090', nome = 'PEDRO', idade=22)

print(a.getCPF())
print(a.getIdade())
print(a.getNome())