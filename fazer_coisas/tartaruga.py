import time
from turtle import shape, left, down, up, forward, right, setx, sety, speed

# Transforma o cursor em uma tartaruga
shape("turtle")  # Experimente “arrow”, “circle”, “square”, “triangle”, “classic”

# Escolhe a velocidade (número de 0 a 10)
speed(1)

# Abaixa a caneta
down()

# Desenha a letra P
left(90)  # Gira a tartaruga para a esquerda
forward(100)  # Anda pra frente
for i in range(3): 
   right(90)  # Gira a tartaruga para a direita
   forward(50)
up()  # Levanta a caneta


# Desenha a letra E
setx(60)  # Muda a posição no eixo x
sety(0)  # Muda a posição no eixo y

down()  # Abaixa a caneta
right(90)
forward(100)
right(90)
for i in range(3):
   up()
   setx(60)
   sety(i*50)
   down()
   forward(50)
up()  # Levanta a caneta

# Desenha a letra O duas vezes
left(90)
for i in range(2):
   up()
   setx(60 * (i+2))
   sety(0)
   for j in range(2):
      down()
      forward(100)
      right(90)
      forward(50)
      right(90)

# Aguarda antes de fechar
time.sleep(3)