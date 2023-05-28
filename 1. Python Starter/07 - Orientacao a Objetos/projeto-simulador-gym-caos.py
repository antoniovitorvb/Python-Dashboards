import random

class Academia:
    def __init__(self):
        self.halteres = [i for i in range(12, 37) if i % 2 == 0]
        self.suporte = {}
        self.organizar()

    def organizar(self): # suporte para os halteres
        self.suporte = {i: i for i in self.halteres}

    def listar_halteres(self): # lista os halteres disponiveis
        return [i for i in self.suporte.values() if i != 0]

    def listar_espacos(self): # lista espacos disponiveis para devolver o halter
        return [i for i, j in self.suporte.items() if j == 0]

    def pegar_halter(self, peso):
        halter_pos = list(self.suporte.values()).index(peso)
        halter_key = list(self.suporte.keys())[halter_pos]
        self.suporte[halter_key] = 0
        return peso

    def devolver_halter(self, pos, peso):
        self.suporte[pos] = peso

    def calc_caos(self):
        num_caos = [i for i, j in self.suporte.items() if i != j]
        return len(num_caos)/len(self.suporte)

class Usuario:
    def __init__(self, tipo, academia):
        self.tipo = tipo.lower() # "Maromba" organiza, "Frangolino" bagunça
        self.academia = academia
        self.peso = 0

    def iniciar_treino(self):
        lista_pesos = self.academia.listar_halteres()

        self.peso = random.choice(lista_pesos)
        self.academia.pegar_halter(self.peso)

    def finalizar_treino(self):
        # procura espaços disponíveis no suporte
        espacos = self.academia.listar_espacos()

        if self.tipo == "maromba":

            # se a posicao do peso certo estiver vazia
            if self.peso in espacos: 
                self.academia.devolver_halter(pos = self.peso, peso = self.peso)
            
            else:
                pos = random.choice(espacos) # coloca aleatoriamente no que tiver disponivel
                self.academia.devolver_halter(pos = pos, peso = self.peso)
        
        if self.tipo == "frangolino":
            pos = random.choice(espacos) # coloca aleatoriamente no que tiver disponivel
            self.academia.devolver_halter(pos = pos, peso = self.peso)

        self.peso = 0 # zera o peso do USUARIO

gym = Academia()

usuarios = []

for i in range(10): # 10 usuarios maromba
    usuarios.append(Usuario("maromba", gym))

# 1 usuario frangolino
usuarios.append(Usuario("frangolino", gym))

for i in range(10):
    random.shuffle(usuarios) # embaralha a ordem que os usuarios treinam

    for user in usuarios:
        user.iniciar_treino()

    for user in usuarios:
        user.finalizar_treino()

print("Caos: {}%".format(round(gym.calc_caos()*100, 2)))
gym.suporte
# gym.calc_caos()