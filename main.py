import random
import datetime

def choose_todays_word():
    with open('./dictionary/wordle_list.txt', 'r') as dst:
        words = dst.readlines()
        word = random.choice(words).strip()
        print(f"디버깅용 정답 : {word}")
        return word
#choose_todays_word()


def players_guess():
    with open('./dictionary/wordle_list.txt', 'r') as dst:
        words = [w.strip() for w in dst.readlines()] #  words = [] for w in dst.readlinea(): words.append(w.strip())    한줄로 줄인거
    while True:
        players_word = input('5자리 글자를 입력하세요')
        if len(players_word) != 5:
            continue
        if not players_word.isalpha():
            continue
        if players_word not in words:
            continue
        return players_word
                


#answer = choose_todays_word()#실행 시 디버깅용 정답과 answer가 다름.answer가 진짜 정답임을 유념하고 코딩
#player_input = players_guess() #리턴은 값만 받는 용도고 따로 선언 필요
#print(player_input)


def match_player_guess_and_answer(player_input, answer):
    result = []
    for i in range(0,5):    #0은 지워도 괜찮음
        if player_input[i] == answer[i]:    #[0:1]는 ~까지임
            result.append("green")
        elif player_input[i] in answer:
            result.append("yellow")
        else:
            result.append("grey")
    return result       #for 문에 넣으면 한번만 검사해서 틀림 ["grey"]처럼 나옴


def main():
    guess_count = 0
    answer = choose_todays_word()
    print(answer)
    
    while guess_count < 6:  #<= 5보다 <6이 더 명확함
        player_input = players_guess()
        feedback = match_player_guess_and_answer(player_input, answer)
        print(feedback)
        guess_count += 1
        if player_input == answer:
            print(f"Congrats! Clear in {guess_count}")
            break
        if guess_count == 6:
            print("Sorry you failed")
            break

main()