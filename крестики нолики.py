win_state = False
playing_fied = list(range(1,10))
counter = 0
all_positions = []
all_win_coords = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(2,4,6),(0,4,8))
while win_state == False:
    for index in range(0,7,3):
        print(playing_fied[index],playing_fied[index +1],playing_fied[index +2])
    if counter == 9:
        print("ничья")
        break
    if counter  %2==0:
        player = "0"
    else:
        player = "X"
    counter += 1
    print(f"ход игрока {player} ") 
    valid = False
    while valid == False:
        position = int(input(f"куда хотите поставить {player}:  "))
        if position in all_positions:
            print("такая клетка занята")
        else:
            
            all_positions.append(position)
            playing_fied[position -1] = player
            valid = True
    if counter >= 4:
        for number_one, number_two, number_three in all_win_coords:
            if playing_fied[number_one] == playing_fied[number_two] == playing_fied[number_three]:
                print(f"игрок {player} победил!")
                win_state = True
            
