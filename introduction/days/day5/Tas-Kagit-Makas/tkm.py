import enum
from nis import match

print('Hoş Geldin, hamleni yap!')

moves = []

class player:
    def __init__(self, name) -> None:
        self.score = 0
        self.name = name

user = player('Sen')
robot = player('Robot')

# Game functions
# List previous actions

from random import randrange

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = [rock, paper, scissors]

def move(currentMove):      
    # ['Taş', 'Kağıt', 'Makas']
    robotMove = randrange(0, 3)
    currentMove = usermove - 1
    bothMoves = [currentMove, robotMove]

    winner = player('Hiç Kimse')

    print(bothMoves)

    if 0 in bothMoves and 2 in bothMoves:
        # 0 Wins
        if robotMove == 0:
            winner = robot
            robot.score += 1
        else:
            winner = user
            user.score += 1
        
    elif 1 in bothMoves and 0 in bothMoves:
        # 1 wins
        if robotMove == 1:
            winner = robot
            robot.score += 1
        else:
            winner = user
            user.score += 1
        
        
    elif 2 in bothMoves and 1 in bothMoves:
        # 2 wins
        if robot == 2:
            winner = robot
            robot.score += 1
        else:
            winner = user
            user.score += 1
    
    print(
        f'''
        Robot:\n{moves[robotMove]}\n
        User:\n{moves[currentMove]}

        ''')
        
    
    moves.append([currentMove, robot])
    print(f'KaZanaN {winner.name} \n')


""" robot.score < 5 and user.score < 5 """
while True: 
    usermove = input('(Taş= 1, Kağıt= 2, Makas= 3): ')
    while ['1','2','3'].__contains__(usermove):
        usermove = int(input('Yanlış değer girdiniz! (Taş= 1, Kağıt= 2, Makas= 3): '))
    usermove = int(usermove)
    move(usermove)

print(
f'''
Robot'un skoru: {robot.score}
Oyuncu'nun skoru: {user.score}
''')