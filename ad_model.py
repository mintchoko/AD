import random

class mainModel:
    def __init__(self):
        self.job = ""
        self.level = 0
        self.str = 0
        self.int = 0
        self.dex = 0
        self.hp = 0
        self.mp = 0
        self.gold = 400
        self.item_list = []
        self.current_hp = self.hp
        self.current_mp = self.mp
        self.item = ["체력물약", "마나물약"]
        self.mon_count = 0
        self.mon_name = ""
        self.mon_hp = 0
        self.mon_level = 0
        self.mon_str = 0
        self.mon_cu_hp = 0
        # 몬스터는 차후 수정
        self.enemy_list = ["슬라임","고블린","오크","트롤","골렘","와이번","거대박쥐","강아지","고양이"]
        self.warrior_skill = ["강타", "슬래시","삼연 베기","유성검","바람의 상처"]
        self.magician_skill = ["에너지 볼트","파이어볼","콜드빔","라이트닝","익스플로전"]
        self.hunter_skill = ["신비한 화살","더블 샷","차지 샷","화살 비","스나이핑"]

        # 마왕 스탯
        self.boss_name = "마왕"
        self.boss_hp = 2000
        self.boss_level = "??"
        self.boss_str = 40
        self.boss_cu_hp = self.boss_hp
        self.boss_count = 0

    # 유저 공격
    def attack(self):
        damage = random.randrange(self.str-1,self.str+3)
        self.mon_cu_hp -= damage
        return damage

    # 전사 스킬 1
    def wa_skill_1(self):
        damage = random.randrange(int(self.str * 1.3) - 1, int(self.str * 1.3) + 3)
        self.mon_cu_hp -= damage
        self.current_mp -= 5
        return damage

    # 전사 스킬 2
    def wa_skill_2(self):
        damage = random.randrange(int(self.str * 1.4) - 1, int(self.str * 1.4) + 3)
        self.mon_cu_hp -= damage
        self.current_mp -= 7
        return damage

    # 전사 스킬 3
    def wa_skill_3(self):
        damage = random.randrange(int(self.str * 1.6) - 1, int(self.str * 1.6) + 3)
        self.mon_cu_hp -= damage
        self.current_mp -= 10
        return damage

    # 전사 스킬 4
    def wa_skill_4(self):
        damage = random.randrange(int(self.str * 1.5) + int(self.int * 1.5) - 1, int(self.str * 1.5) + int(self.int * 1.5) + 3)
        self.mon_cu_hp -= damage
        self.current_mp -= 12
        return damage

    # 전사 스킬 5
    def wa_skill_5(self):
        damage = random.randrange(int(self.str * 1.5) + self.dex * 2 - 1, int(self.str * 1.5) + self.dex * 2 + 3)
        self.mon_cu_hp -= damage
        self.current_mp -= 20
        return damage

    # 법사 스킬 1
    def ma_skill_1(self):
        damage = random.randrange(int(self.int * 1.5) - 1, int(self.int * 1.5) + 3)
        self.mon_cu_hp -= damage
        self.current_mp -= 8
        return damage

    # 법사 스킬 2
    def ma_skill_2(self):
        damage = random.randrange(int(self.int * 1.6) - 1, int(self.int * 1.6) + 3)
        self.mon_cu_hp -= damage
        self.current_mp -= 10
        return damage

    # 법사 스킬 3
    def ma_skill_3(self):
        damage = random.randrange(int(self.int * 1.8) - 1, int(self.int * 1.8) + 3)
        self.mon_cu_hp -= damage
        self.current_mp -= 12
        return damage

    # 법사 스킬 4
    def ma_skill_4(self):
        damage = random.randrange(int(self.int * 2) - 1, int(self.int * 2) + 3)
        self.mon_cu_hp -= damage
        self.current_mp -= 15
        return damage

    # 법사 스킬 5
    def ma_skill_5(self):
        damage = random.randrange(int(self.int * 2.5) - 1, int(self.int * 2.5) + 3)
        self.mon_cu_hp -= damage
        self.current_mp -= 24
        return damage

    # 궁수 스킬 1
    def hu_skill_1(self):
        damage = random.randrange(int(self.dex * 1.2) + int(self.str * 0.6) - 1,int(self.dex * 1.2) + int(self.str * 0.6) +3)
        self.mon_cu_hp -= damage
        self.current_mp -= 6
        return damage

    # 궁수 스킬 2
    def hu_skill_2(self):
        damage = random.randrange(int(self.dex * 1.4) + int(self.str * 0.7) - 1,
                                  int(self.dex * 1.4) + int(self.str * 0.7) + 3)
        self.mon_cu_hp -= damage
        self.current_mp -= 9
        return damage

    # 궁수 스킬 3
    def hu_skill_3(self):
        damage = random.randrange(int(self.dex * 1.6) + int(self.str * 0.5) + int(self.int * 0.5) - 1,
                                  int(self.dex * 1.6) + int(self.str * 0.5) + int(self.int * 0.5) + 3)
        self.mon_cu_hp -= damage
        self.current_mp -= 12
        return damage

    # 궁수 스킬 4
    def hu_skill_4(self):
        damage = random.randrange(int(self.dex * 1.8) + self.str - 1,
                                  int(self.dex * 1.8) + self.str + 3)
        self.mon_cu_hp -= damage
        self.current_mp -= 18
        return damage

    # 궁수 스킬 5
    def hu_skill_5(self):
        damage = random.randrange(int(self.dex * 2.5) - 1,
                                  int(self.dex * 2.5) + 3)
        self.mon_cu_hp -= damage
        self.current_mp -= 25
        return damage

    # 몬스터 공격
    def enemy_attack(self):
        damage = random.randrange(self.mon_str-2,self.mon_str+1)
        self.current_hp -= damage
        return damage

    # 유저 가드
    def guard(self,damage):
        self.current_hp += int(damage/2)
        return damage - int(damage/2)

    # 아이템 구매
    def buy(self,itemname):
        if self.gold >= 100:
            self.gold -= 100
            self.item_list.append(itemname)
            return True
        else:
            return False
    # 아이템 사용
    def use(self,item):
        if item == "체력물약":
            self.current_hp += int(self.hp * 4/10)
            if self.current_hp > self.hp:
                self.current_hp = self.hp
            self.item_list.remove(item)

        else:
            self.current_mp += int(self.mp * 4 / 10)
            if self.current_mp > self.mp:
                self.current_mp = self.mp
            self.item_list.remove(item)

    # 골드 획득
    def earn(self):
        gold_list = [20,30,40]
        gold = random.choice(gold_list)
        self.gold += gold
        return gold

    # 직업 결정
    def job_set(self,jobName):
        self.job = jobName
        if self.job == "전사":
            self.warrior()
        elif self.job == "법사":
            self.magican()
        elif self.job == "궁수":
            self.hunter()
        else:
            self.mario()

    # 전사 스테이터스
    def warrior(self):
        self.level += 1
        self.str += 7
        self.int += 3
        self.dex += 5
        self.hp += 60
        self.mp += 15
        self.current_hp = self.hp
        self.current_mp = self.mp

    # 마법사 스테이터스
    def magican(self):
        self.level += 1
        self.str += 4
        self.int += 7
        self.dex += 4
        self.hp += 40
        self.mp += 40
        self.current_hp = self.hp
        self.current_mp = self.mp

    # 궁수 스테이터스
    def hunter(self):
        self.level += 1
        self.str += 5
        self.int += 3
        self.dex += 7
        self.hp += 50
        self.mp += 20
        self.current_hp = self.hp
        self.current_mp = self.mp

    # 히든 캐릭터 스테이터스
    def mario(self):
        self.level += 1
        self.str += 10
        self.int += 10
        self.dex += 10
        self.hp += 100
        self.mp += 50
        self.current_hp = self.hp
        self.current_mp = self.mp
    # 뉴 게임 시 정보 초기화
    def clear(self):
        self.job = ""
        self.level = 0
        self.str = 0
        self.int = 0
        self.dex = 0
        self.hp = 0
        self.mp = 0
        self.gold = 400
        self.item_list = []
        self.using_sword = False
        self.current_hp = self.hp
        self.current_mp = self.mp

    # 세이브
    def save(self,filename):
        f = open(filename, "w")
        item_list = ",".join(self.item_list) if len(self.item_list) > 0 else "없음"
        save_data = [self.job,self.level,self.str,self.int,self.dex,self.hp,self.mp,self.gold,item_list]
        for i in range(len(save_data)):
            if i != len(save_data) - 1:
                f.write(str(save_data[i]) + "\n")
            else:
                f.write(str(save_data[i]))

    # 로드
    def load(self,filename):
        f = open(filename,"r")
        load_data = f.readlines()
        if len(load_data) != 0:
            for i in range(len(load_data)):
                if '\n' in load_data[i]:
                    load_data[i] = load_data[i][:-1]

            self.job = load_data[0]
            self.level = int(load_data[1])
            self.str = int(load_data[2])
            self.int = int(load_data[3])
            self.dex = int(load_data[4])
            self.hp = int(load_data[5])
            self.mp = int(load_data[6])
            self.gold = int(load_data[7])
            list = load_data[8].split(",")
            self.item_list = []
            for i in list:
                if i != "없음":
                    self.item_list.append(i)
            self.current_hp = self.hp
            self.current_mp = self.mp
            return True
        else:
            return False

    # 던전 진행
    def dungeon(self):
        self.mon_count += 1
        self.mon_name = random.choice(self.enemy_list)
        self.mon_level = self.level
        self.mon_hp = self.mon_level * 20
        self.mon_cu_hp = self.mon_hp
        self.mon_str = self.mon_level * 3

    # 마지막 던전 출입
    def boss_dungeon(self):
        self.mon_name = self.boss_name
        self.mon_level = self.boss_level
        self.mon_hp = self.boss_hp
        self.mon_cu_hp = self.boss_hp
        self.mon_str = self.boss_str



