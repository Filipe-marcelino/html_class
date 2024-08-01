import random
print('numero sorteado: ',random.randint(0,10))

opcoes = ['filipe', 'cecilia','mickeias']
print('quem vai ganhar na mega-sena: ',random.choice(opcoes))

opcoes2 = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(opcoes2)

print(opcoes2)