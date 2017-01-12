from teamwork_character_monster_info import * #케릭터(기사)의 인포메이션과  몬스터의 인포메이션.
from getch import getch #키보드 중 아무거나 누르면 다음 것으로 넘어감.
import random

def tutorial():
    print("--튜토리얼--")
    print("안녕하세요 기사 지망생님! 저는 당신을 도와줄 요정입니다. 다음화면으로 넘어가려면 아무 키나 눌러 주세요.(↓버튼을 추천합니다.)");getch()
    print("잘하셨어요. 이제 캐릭터 정보를 보는 방법을 알려드릴께요.");getch()
    Player = Knight('???')
    Player.Print_Info();getch()#케릭터의 인포메이션 출력
    print("당신의 이름은 정하지 않았기 때문에 '???'로 뜨지만 플레이중 기사 지망생님의 이름을 정해주시면 정하신 이름을 뜰것 입니다.")
    getch()
    print("당신의 직업은 기사 지망생 입니다.");getch()
    print("용기는 당신의 용기를 나타냅니다.");getch()
    print("체력은 말 그대로 당신의 체력을 나타내면 체력을 다 쓴다면 죽을 수도 있겠죠? 마나는 당신의 마나를 나타내고 마나를 사용하여 스킬을 쓸 수 있습니다.");getch()
    print("힘은 당신의 힘을 나타냅니다. 어떤 스킬인지에 따라 공격력이 다르게 나타 날 수 있으나 이 power를 기반으로 할 것입니다.");getch()
    print("지금까지 캐릭터 정보를 보는 방법이었습니다.");getch()
    print("지금까지 튜토리얼 이었습니다.","\n※ 몬스터와 싸울때 정수가 아닌 것을 눌렀을때 오류가 걸릴 수 있습니다.※\n\n\n",);getch()#튜토리얼 끝.


def first_test_site():#초반 스토리 설정.
    print ("???:난 기사가 되고 싶은 기사 지망생! 오늘은 수도에서 기사 시험이 있는날!");getch()
    print ("??? : 빨리 가야지!");getch()
    print ("\n\n--기사 시험장--")
    print ("??? : 앗 벌써 줄이 여기까지..");getch()
    print ("기다리는중.....");getch()
    print ("기다리는중.....");getch()
    print ("??? : 기다리고 기다리다, 드디어 내 순서가 되었어!\n\n");getch()
    print ("시험관 : 그래, 기사가 되고 싶다고? 그대 이름이 뭔가?");getch()
    print ("제 이름이요? 제 이름은...");getch()
    global Player#플레이어를 전역변수로 설정.
    name = input ("System : 기사님 당신의 이름은 무엇입니까? : ");getch()
    Player = Knight(name)#플레이어 이름 설정
    print (f"{Player.name}: 제 이름은 {Player.name}입니다.");getch()
    print(f"시험관 : 그래 {Player.name}. 기사란 무엇이라 생각하나?");getch()
    print(f"{Player.name} : 음.....싸울떄 앞에서 싸운는 사람??");getch()
    print(f"시험관 : (바보가 들어왔군) 그래 {Player.name} 전장 앞에서 싸우려면 용기가 중요하지?");getch()
    print(f"{Player.name} : 그...당연하죠!");getch()
    print(f"시험관 : 너의 용기를 확인해 보겠다")
    print (f"용기 : {Player.brave}")#플레이어 용기가 뜸
    print(f"시험관 : 넌 용기가 없군! 어떻게 그 용기를 가지고 여기까지 올 생각을 했는가! 적어도 용기가 5가 되야지! 일반몬스터 한마리도 못 잡아본 주제에!");getch()
    print(f"{Player.name} : 하지만, 그건 천천히 배워가면..");getch()
    print(f"시험관 : 됐고 다음!\n")

def start():#몬스터와 전투 초반 설정
    print(f"{Player.name} : 아..쫒겨났네..");getch()
    print(f"{Player.name} : 기사가 된다고 가출헀는데..여기서 집에 가면 더 혼날 것 같은데");getch()
    print(f"{Player.name} : 아까 시험관이 용기가 있어야 한다고 해야했고...일반몬스터 한마리도 못잡아 본 주제라고 했으니");getch()
    print(f"{Player.name} : 몬스터를 잡으면 용기가 늘어날려나?");getch()
    print(f"{Player.name} : 한번 몬스터를 잡으러 가보자!");getch()

def loby():#어디로 갈 지 선택하는 함수 정의
    while True:
        choose=input("\n어디로 가시겠습니까?\n1.황무지\n2.산악지대\n3.기사 시험장\n4.숙소\n5.캐릭터 정보\n\n")
        if choose == '1':
            waste_land()
        elif choose =='2':
            mountain()
        elif choose == '3':
            last_test_site()
            if Player.hp>=0 and Player.brave>=5:
                break
            else:
                pass
        elif choose == '4':
            print("\n아 온 몸이 풀리는 구나..")
            print("System : 체력과 마나가 모두 체워졌다!")
            Player.hp = Player.max_hp#체력 채워짐.
            Player.mp = Player.max_mp#마나 채워짐.
        elif choose == '5':
            Player.Print_Info()

        else : #번호에 없는 것을 선택했을 시
            print("System : 어디 갈건지도 몰라? 다시 선택하라구!!\n")

def waste_land():#황무지 함수
    print (f"\n{Player.name} : 음..여기가 몬스터가 나온다는 황무지인가?");getch()
    print (f"{Player.name} : 끙, 조금 어두워져버렸네, 이대로 괜찮을까나...");getch()
    waste_land_moster = [enemy("슬라임",15000,500,0), enemy("뱀파이어",10000,750,500) , enemy("와일드 캣",5000,1500,0),enemy("어스웜",10000,800,0) , enemy("레이지베어",20000,400,0)]
    monster = random.choice(waste_land_moster)
    print((f"\nSystem : {monster.name}이 나타났다!\n"));getch()
    print(f"{Player.name} : 헉 몬스터다! 잡을 준비를 해야지!",end='\n\n');getch()
    Player.attack(monster)
    if monster.hp<=0:#이길 시에는
        print("용기가 1 증가하였다!")
        Player.brave +=1#용기 1 상승
        print("최대 체력이 2000, 최대 마나가 500 증가하였다!")
        Player.max_hp += 2000
        Player.max_mp += 500
        print("힘이 200 증가하였다!")
        Player.power += 200
    else:
        pass

def mountain():
    print (f"\n{Player.name} : 음..여기가 황무지보다 더 쎈 몬스터가 나온다는 산악지대인가?");getch()
    print (f"{Player.name} : 끙, 조금 어두워져버렸네, 어두우니깐 바람소리조차 무섭다ㅠㅠ...");getch()
    mountain_monster = [enemy("슬라임",17000,700,0), enemy("뱀파이어",12000,1000,600) , enemy("와일드 캣",7000,2000,0),enemy("어스웜",12000,1000,0) , enemy("레이지베어",30000,600,0)]
    monster = random.choice(mountain_monster)
    print((f"\nSystem : {monster.name}이 나타났다!"));getch()
    print(f"{Player.name} : 헉 몬스터다! 어떡하지? 일단 덤벼보자!",end='\n\n');getch()
    Player.attack(monster)
    if monster.hp<=0:#이길 시에는
        print(f"용기가 1 증가하였다!")
        Player.brave +=1#용기 1 상승
        print(f"최대 체력이 4000, 최대 마나가 1000 증가하였다!")
        Player.max_hp += 4000
        Player.max_mp += 1000
        print("힘이 200 증가하였다!")
        Player.power += 200
    else:
        pass

def last_test_site():#보스몬스터와 전투 전
    print (f"{Player.name} : 시험관님!! 시험을 보러 왔습니다!");getch()
    print ("시험관 : 또 너냐! 이제 용기는 생긴거겠지?");getch()
    print ("시험관 : 너의 용기를 확인해 보겠다.");getch()
    print (f"용기 : {Player.brave}")
    if Player.brave <5:
        print("시험관 : 넌 용기가 없어 용기가 적어도 용기가 5는 되야지. 이정도 용기를 가지고 어떻게 기사시험을 볼 용기가 생긴게냐!!");getch()
        print("시험관 : 다음!");getch()
        print(f"{Player.name} : 또 쫒겨났네...");getch()
    else :
        print ("시험관 : 호, 용기가 생겼다 이건가? 좋아, 이제 기사가 될 수 있는 방법을 알려주지");getch()
        print (f"{Player.name} : 네!!(드디어 기사가 된다니!!)");getch()
        print ("시험관 : 기사시험은 바로 일명 보스몬스터라 불리는 골렘을 죽이는 것이다.");getch()
        print ("시험관 : 자 지금 바로 시작하지");getch()
        print (f"{Player.name} : 덜덜 일단 공격해보자!");getch()
        boss_monster = enemy("골렘",50000,1000,1000)#보스 몬스터의 설정
        Player.attack(boss_monster);getch()#보스 몬스터와의 전투

def epilogue():
    print(" --epilogue--")
    print(f" 기사 단장 : {Player.name}, 그대는 이 나라의 황제께 복종하며, 전투시 이 국가를 지키기 위하여 최선을 다할 것인가?");getch()
    print(f" {Player.name} : 네");getch()
    print(f" 기사 단장 : {Player.name}, 그대는 레이디을 존중하고 예의를 갖출 것인가?");getch()
    print(f" {Player.name} : 네");getch()
    print(f" 기사 단장 : {Player.name}, 그대는 전투시 물러서지 않고 싸울 용기가 충분하다고 생각하는가?");getch()
    print(f" {Player.name} : 네");getch()
    print(" 기사 단장 : 좋다 이제부터 그대를 이 나라의 정식기사로 임명하노라");getch()
    print(f" {Player.name} : 이렇게 나는 정식 기사가 되었다!");getch()
    print(f" {Player.name} : 부모님께 말씀드리면 자랑스러워 하시겠지?");getch()
    print(f" {Player.name} : 내 미래가 기대돼!");getch()
    print(f" {Player.name} : 이제 나에게 무슨 일이 일어날까?");getch()
    print(" ---끝---\n")
