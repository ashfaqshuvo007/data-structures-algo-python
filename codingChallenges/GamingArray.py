game_array = [5, 4, 1]
turn = 0
max_number = 0
games = int(input("Enter number of games to play: "))
for g in range(0, games):
    for i in game_array:
        if i>max_number:
            turn += 1
            m=i
    print('ANDY') if turn % 2 == 0 else print("BOB")