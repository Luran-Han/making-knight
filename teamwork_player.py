from teamwork_story_line import *

def game():
    while True:
        introduction = input("1. 튜토리얼\n2. 게임시작\n3. 게임 나가기\n")
        if introduction == '1':
            tutorial()
            continue
        elif introduction == '2':
            first_test_site()
            start()
            loby()
            epilogue()
            continue
        elif introduction =='3':
            break
        else :
            print("다시 선택해 주세요")


game()
