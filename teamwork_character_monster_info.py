from getch import getch # 키보드 중 아무거나 누르면 다음 것으로 넘어감.
class Knight:#기사의 클래스

    job = "Knight"
    brave = 0
    hp = 15000
    mp = 2000
    power = 2500
    Skill_list = ("베기", "찌르기" , "연속베기", "원무")
    Skill_mp = [50,100,150,400]
    Skill_power = [power*0.5, power*0.75, power*0.8, power]#파워 순서 = 기본공격 = 베기 < 찌르기
    Skills = {"name" : Skill_list, "mp" : Skill_mp , "power" : Skill_power}
    max_hp = 15000
    max_mp = 4000


    def __init__(self,name):
        self.name=name #이름 설정

    def Print_Info(self):#케릭터 인포메이션
        print ('{:^30}'.format("---플레이어 정보---"))#중앙 정렬
        print('{:^30}'.format(f"이름 : {self.name}"))#이름 출력
        print('{:^30}'.format(f"직업 : {self.job}"))#직업 출력
        print('{:^30}'.format(f"힘 : {self.power}"))
        print('{:^30}'.format(f"용기 : {self.brave}"))#용기(레벨)출력
        print('{:^30}'.format(f"체력 : {self.hp} 마나 : {self.mp}"))#체력과 마나 출력
        print('{:^30}'.format(f"힘 : {self.power}\n"))#파워 출력

    def attack(self, enemy):#전투에 대한 함수.
        enemy.Print_Info()
        while True:#무조건 반복
            print("\n",'{:^30}'.format("--스킬 목록 --\n"))#스킬 목록 출력
            count = 1
            for skill in self.Skills["name"] :#
                print('{:^30}'.format("{}. {}".format(count,skill), end = ' '))
                count += 1
                print("")

            Select = input("\n공격 선택 : ")#공격 선택 창
            if Select not in ['1','2','3','4']:#스킬 내역에 없는 번호를 눌렀을 시.
                print("System : 공격할 줄 몰라? 죽으려고? 제대로 다시 해보라고!")
                continue#반복

            Select = int(Select)
            Selected_attack = self.Skills["name"][Select-1]

            print(f"\n{self.name}이 {Selected_attack}을 시전하였습니다!\n")#공격함
            enemy.hp -= self.Skills["power"][Select-1]
            self.mp -= self.Skills["mp"][Select-1]
            print(f"{enemy.name}의 체력 :  {enemy.hp}")#공격한 만큼 적의 체력이 깎임.

            print(f"\n{enemy.name}이(가) 공격하였습니다.")#적의 공격
            self.hp -= enemy.power
            enemy.hp += enemy.plus_hp

            print(f"{self.name}의 체력 : {self.hp}\n{self.name}의 마나 : {self.mp}\n")#마나 깎임.


            if enemy.hp<=0:#이길 시에는
                print(f"{enemy.name}을 물리쳤다!\n")
                break#나가기

            elif self.hp<=0: #질 시에는
                print(f"{self.name}이 치명적인 상처를 입었습니다.\n")
                self.brave -= 1#용기 1 하락
                break#나가기

            elif self.mp<=0:#마나가 없을 시에는
                print(f"{self.name}의 마나가 없습니다. 체력을 2000을 소모하여 소량의 마나를 회복합니다\n")
                self.hp -= 2000
                self.mp += 1000#마나 3000 상승.'''


class enemy:#몬스터의 클래스

    def __init__(self,name,hp,power,plus_hp) :
        self.name = name#몬스터 이름 설정
        self.hp = hp#몬스터 체력 설정
        self.power = power#몬스터 파워 설정
        self.plus_hp = plus_hp

    def Print_Info(self):#몬스터 인포메이션
        print ('{:^30}'.format("---몬스터 정보---"))
        print('{:^30}'.format(f"이름 : {self.name}"))#몬스터 이름 출력
        print('{:^30}'.format(f"체력 : {self.hp}"))#몬스터 체력 출력.
        print('{:^30}'.format(f"힘 : {self.power}"))

    """
    ("슬라임",'','200','0')
    ("뱀파이어",'','300','100')
    ("와일드 캣",'','400','0')
    ("어스웜",'','600','0')
    ("레이지베어",'','800','0')
    ("골렘",'','1000','0')
    """
