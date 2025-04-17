import random
def game_engine(count):
    is_win = False
    correct_num = random.randint(1, 100)
    for i in range(count):
        player_num = int(input("Nhap so ban doan "))
        if player_num == correct_num:
            print(f"You are correct after {i+1} times")
            is_win = True
            break
        else:
            if player_num > correct_num:
                print("So ban dang doan lon hon correct_num")
            else:
                print("So ban dang doan nho hon correct_num")
    print(f"So dung la: {correct_num}")
    return is_win
def choose_level():
    print(""" Co 3 levels de chon:
    \t 1 - easy - ban co 9 luot choi
    \t 2 - medium - ban co 6 luot choi
    \t 3 - hard - ban co 4 luot choi""")
    level = 1
    while True:
        level = int(input("Nhap level ban muon choi!"))
        if 1<=level <= 3:
            break
    return 9 if level == 1 else 6 if level == 2 else 4


if __name__ == "__main__":
    total_plays = 0
    total_wins = 0
    while True:
        total_plays +=1
        game_level = choose_level()
        if game_engine(game_level):
            total_wins += 1
        tieptuc = input("Ban co muon tiep tuc choi khong? <n/N to stop").lower()
        if tieptuc == 'n':
            break
    print(f"So lan choi: {total_plays}")
    print(f"So lan thang: {total_wins}")