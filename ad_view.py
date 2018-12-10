from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QVBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton

class mainView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # game statement
        self.gameWindow = QTextEdit()
        self.gameWindow.setReadOnly(True)

        # place
        self.placeWindow = QLineEdit()
        self.placeWindow.setFixedWidth(100)
        self.placeWindow.setReadOnly(True)

        # left Layout
        leftLayout = QGridLayout()
        leftLayout.addWidget(self.gameWindow,0,0)

        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(self.placeWindow)
        vboxLayout.addStretch(1)

        # enemy statement
        self.enemyWindow = QTextEdit()
        self.enemyWindow.setReadOnly(True)
        self.enemyWindow.setFixedHeight(60)
        self.enemyWindow.setFontPointSize(8)

        # user statement
        self.userWindow = QTextEdit()
        self.userWindow.setReadOnly(True)
        self.userWindow.setFixedHeight(60)
        self.userWindow.setFontPointSize(8)

        # button
        self.button_1 = QToolButton()
        self.button_1.setFixedSize(80,60)

        self.button_2 = QToolButton()
        self.button_2.setFixedSize(80, 60)

        self.button_3 = QToolButton()
        self.button_3.setFixedSize(80, 60)

        self.button_4 = QToolButton()
        self.button_4.setFixedSize(80, 60)

        # right Layout
        rightLayout = QGridLayout()
        rightLayout.addWidget(self.enemyWindow,0,0,1,2)
        rightLayout.addWidget(self.userWindow,1,0,1,2)
        rightLayout.addWidget(self.button_1,2,0)
        rightLayout.addWidget(self.button_2,2,1)
        rightLayout.addWidget(self.button_3,3,0)
        rightLayout.addWidget(self.button_4,3,1)

        # main Layout
        downLayout = QGridLayout()
        downLayout.addLayout(leftLayout, 0, 0)
        downLayout.addLayout(rightLayout, 0, 1)

        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(vboxLayout,0,0)
        mainLayout.addLayout(downLayout,1,0)

        self.setLayout(mainLayout)

        self.setWindowTitle("RPG GAME")

        self.setGeometry(300, 300, 1500, 1000)

        # 직업 별 스킬
        self.warrior_skill = ["강타", "슬래시", "삼연 베기", "유성검", "바람의 상처"]
        self.magican_skill = ["에너지 볼트", "파이어볼", "콜드빔", "라이트닝", "익스플로전"]
        self.hunter_skill = ["신비한 화살", "더블 샷", "차지 샷", "화살 비", "스나이핑"]

    # 버튼 문자 변경
    def button_text(self,text_1 = "",text_2 = "",text_3 = "",text_4 = ""):
        self.button_1.setText(text_1)
        self.button_2.setText(text_2)
        self.button_3.setText(text_3)
        self.button_4.setText(text_4)

    # 게임 크레딧
    def credit(self):

        self.gameWindow.setText("개발자 : 오현민, 안세홍")
        self.gameWindow.setAlignment(Qt.AlignCenter)

        self.button_text("메인으로")

    # 게임 메인화면
    def main2(self):
        self.gameWindow.setFontPointSize(15)
        self.gameWindow.setText("AD RPG GAME")
        self.gameWindow.setFontPointSize(10)
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.placeWindow.setText("")
        self.enemyWindow.setText("")
        self.userWindow.setText("")
        self.button_text("새 게임","불러오기","개발자들","종료")

    # 스크립트 시작
    def text_start(self,filename):
        f = open(filename,"r")
        self.current_script = filename
        self.lines = f.readlines()
        f.close()
        self.placeWindow.setText(filename[:-4])
        self.enemyWindow.clear()
        self.gameWindow.clear()
        self.button_text("다음 문장","스킵")
        self.gameWindow.append(self.lines[0])
        self.count = 1

    # 다음 문장
    def next(self):
        self.gameWindow.append(self.lines[self.count])
        self.count += 1
        if self.count == len(self.lines) :
            self.button_text("종료")

    # 스크립트 종료
    def script_end(self):
        if self.current_script == "prolog.txt":
            self.job_choice()
        elif self.current_script == "ending.txt" :
            self.main2()
        else:
            self.gameWindow.clear()
            self.village(11)

    # 직업 선택
    def job_choice(self):
        self.gameWindow.setAlignment(Qt.AlignCenter)
        self.gameWindow.setText("직업을 선택하십시오")
        self.button_text("전사","법사","궁수")

    # 마을에 있을 때
    def village(self,level):
        if level == 1 :
            self.placeWindow.setText("헤네시스")
            self.gameWindow.append("헤네시스에 도착하였습니다.\n여기저기 버섯이 가득하다.")
            self.button_text("다음 던전","상점","저장/불러오기","메인으로")
        elif level == 2:
            self.placeWindow.setText("아제로스")
            self.gameWindow.append("아제로스에 도착하였습니다. \n피곤이 몰려온다.")
            self.button_text("다음 던전","상점","저장/불러오기","메인으로")
        elif level == 3:
            self.placeWindow.setText("슬리피우드")
            self.gameWindow.append("슬리피우드에 도착하였습니다.\n주인공은 나른해지는 것 같다.")
            self.button_text("다음 던전", "상점", "저장/불러오기", "메인으로")
        elif level == 4:
            self.placeWindow.setText("오르비스")
            self.gameWindow.append("오르비스에 도착하였습니다.\n높은 곳이라 공기가 맑다.")
            self.button_text("다음 던전", "상점", "저장/불러오기", "메인으로")
        elif level == 5:
            self.placeWindow.setText("데마시아")
            self.gameWindow.append("데마시아에 도착하였습니다.\n멀리서 동상이 보인다.")
            self.button_text("다음 던전", "상점", "저장/불러오기", "메인으로")
        elif level == 6:
            self.placeWindow.setText("루테란")
            self.gameWindow.append("루테란에 도착하였습니다.\n실리안 왕자가 반겨줍니다.")
            self.button_text("다음 던전", "상점", "저장/불러오기", "메인으로")
        elif level == 7:
            self.placeWindow.setText("판데모니움")
            self.gameWindow.append("판데모니움에 도착하였습니다.\n주인공은 지쳐갑니다.")
            self.button_text("다음 던전", "상점", "저장/불러오기", "메인으로")
        elif level == 8:
            self.placeWindow.setText("발할라")
            self.gameWindow.append("발할라에 도착하였습니다.\n포근한 기분이 넘칩니다.")
            self.button_text("다음 던전", "상점", "저장/불러오기", "메인으로")
        elif level == 9:
            self.placeWindow.setText("아반트헤임")
            self.gameWindow.append("아반트헤임에 도착하였습니다.\n쓸쓸한 분위기가 감돕니다.")
            self.button_text("다음 던전", "상점", "저장/불러오기", "메인으로")
        elif level == 10:
            self.placeWindow.setText("마을")
            self.gameWindow.append("마을에 도착하였습니다.\n여정의 끝이 보입니다.")
            self.button_text("다음 던전", "상점", "저장/불러오기", "메인으로")
        else:
            self.placeWindow.setText("쿠파성")
            self.gameWindow.append("쿠파성에 도착하였습니다.\n주인공은 의지가 충만합니다.")
            self.button_text("마지막 던전", "상점", "저장/불러오기", "메인으로")
    # 유저 스테이터스 갱신
    def user_text(self,job,level,cu_hp,hp,cu_mp,mp,gold):
        self.userWindow.setText(job + "  레벨 : "+ str(level) + "  골드  : " + str(gold))
        self.userWindow.append("hp : " + str(cu_hp)+ "/" +str(hp) + "   mp : " +str(cu_mp)+ "/" + str(mp))

    # 세이브 로드 버튼
    def save_load(self):
        self.placeWindow.clear()
        self.gameWindow.clear()
        self.button_text("저장","불러오기","취소")

    # 세이브 로드 파일 출력
    def save_text(self):
        self.placeWindow.setText("저장")
        self.button_text("세이브 1","세이브 2","세이브 3","취소")

    def load_text_vill(self):
        self.placeWindow.setText("불러오기/마을")
        self.gameWindow.clear()
        self.button_text("세이브 1", "세이브 2", "세이브 3","취소")

    def load_text_main(self):
        self.placeWindow.setText("불러오기/메인")
        self.gameWindow.clear()
        self.button_text("세이브 1", "세이브 2", "세이브 3","취소")

    # 로드 실패
    def load_fail(self):
        if self.placeWindow.text() == "불러오기/마을" :
            self.save_load()
            self.gameWindow.setText("데이터가 없습니다.")
            self.gameWindow.append("불러오기에 실패했습니다.")
        else:
            self.gameWindow.setText("데이터가 없습니다.")
            self.gameWindow.append("불러오기에 실패했습니다.")
            self.button_text("불러오기","취소")

    # 상점
    def shop(self):
        self.placeWindow.setText("상점")
        self.gameWindow.append("상점에 들어왔습니다.")
        self.gameWindow.append("상점 주인 : \"체력 물약, 마나 물약 개당 100 골드.\"")
        self.button_text("체력물약","마나물약","나가기")

    # 구매
    def buy_text(self,item,bool):
        if bool:
            self.gameWindow.append("상점 주인 : " + "\"" + item + " 1개 구매 감사합니다.\"")
        else:
            self.gameWindow.append("상점 주인 : \"그 돈으로는 못 사요.\"")

    # 던전 입장
    def dungeon_enter(self,level):
        if level == 11:
            self.placeWindow.setText("파이널 스테이지")
            self.gameWindow.setText("마왕 쿠파와 조우하였습니다!")
            self.gameWindow.append("마왕 쿠파 : \"드디어 부활의 시간이 다가왔다!\"")
            self.gameWindow.append("마왕 쿠파 : \"너를 집어삼키고 이 세계를 파멸로 이끌어주지!\"\n")
            self.gameWindow.append("주인공 : \"덤벼라 쿠파! 이번에야 말로 영원히 봉인해주마!\"")
        else:
            self.placeWindow.setText("스테이지" + str(level))
            self.gameWindow.setText("던전에 입장하였습니다.")
        self.button_text("공격","스킬","방어","아이템")

    # 몬스터 조우
    def battle(self,monster,count,level,hp):
        self.gameWindow.append(monster+" 이/가 나타났습니다.   " + "(" +str(count) + "/10)")
        self.enemyWindow.setText(monster + "  레벨 : " + str(level) + "\nhp : " + str(hp) + "/" + str(hp))

    # 보스 조우
    def boss_battle(self,boss,level,hp):
        self.enemyWindow.setText(boss+ "  레벨 : " + level + "\nhp : " + str(hp) + "/" + str(hp))

    # 몬스터 갱신
    def enemy_set(self,monster,level,cu_hp,hp):
        self.enemyWindow.setText(monster + "  레벨 : " + str(level) + "\nhp : " + str(cu_hp) + "/" + str(hp))

    # 행동 선택
    def action_choice(self):
        self.gameWindow.append("")
        self.gameWindow.append("행동을 선택해주세요.")

    # 아이템 클릭
    def item_click(self,hp,mp,sword):
        if sword :
            self.button_text("체력물약"+str(hp) + "개","마나물약"+str(mp)+"개","용사의검","뒤로")
        else:
            self.button_text("체력물약"+str(hp)+"개","마나물약"+str(mp)+"개","뒤로")

    # 뒤로 클릭
    def back(self):
        self.button_text("공격", "스킬", "방어", "아이템")

    # 행동 후 출력
    def action_text(self,action,monster = "",mon_damage = 0,damage = 0):
        if action == "공격":
            self.gameWindow.append("주인공의 공격!")
            self.gameWindow.append(monster + " 은/는 " + str(damage) + "의 데미지를 입었다.")
            self.gameWindow.append(monster + "의 공격!")
            self.gameWindow.append("주인공은 " + str(mon_damage) + "의 데미지를 입었다.")

        elif action == "방어":
            self.gameWindow.append("주인공의 방어!")
            self.gameWindow.append("주인공은 방어하고있다.")
            self.gameWindow.append(monster + "의 공격!")
            self.gameWindow.append("주인공은 " + str(mon_damage) + "의 데미지를 입었다.")

        elif action == "체력물약":
            self.gameWindow.append("주인공은 체력물약을 사용했다!")
            self.gameWindow.append(monster + "의 공격!")
            self.gameWindow.append("주인공은" + str(mon_damage) + "의 데미지를 입었다.")

        elif action == "마나물약":
            self.gameWindow.append("주인공은 마나물약을 사용했다!")
            self.gameWindow.append(monster + "의 공격!")
            self.gameWindow.append("주인공은" + str(mon_damage) + "의 데미지를 입었다.")

        elif action == "강타":
            self.gameWindow.append("주인공은 강타를 사용했다!")
            self.gameWindow.append(monster + " 은/는 " + str(damage) + "의 데미지를 입었다.")
            self.gameWindow.append(monster + "의 공격!")
            self.gameWindow.append("주인공은 " + str(mon_damage) + "의 데미지를 입었다.")

        elif action == "슬래시":
            self.gameWindow.append("주인공은 슬래시를 사용했다!")
            self.gameWindow.append(monster + " 은/는 " + str(damage) + "의 데미지를 입었다.")
            self.gameWindow.append(monster + "의 공격!")
            self.gameWindow.append("주인공은 " + str(mon_damage) + "의 데미지를 입었다.")

        elif action == "삼연 베기":
            self.gameWindow.append("주인공은 삼연 베기를 사용했다!")
            self.gameWindow.append(monster + " 은/는 " + str(damage) + "의 데미지를 입었다.")
            self.gameWindow.append(monster + "의 공격!")
            self.gameWindow.append("주인공은 " + str(mon_damage) + "의 데미지를 입었다.")

        elif action == "유성검":
            self.gameWindow.append("주인공은 유성검을 사용했다!")
            self.gameWindow.append(monster + " 은/는 " + str(damage) + "의 데미지를 입었다.")
            self.gameWindow.append(monster + "의 공격!")
            self.gameWindow.append("주인공은 " + str(mon_damage) + "의 데미지를 입었다.")

        elif action == "바람의 상처":
            self.gameWindow.append("주인공은 바람의 상처를 사용했다!")
            self.gameWindow.append(monster + " 은/는 " + str(damage) + "의 데미지를 입었다.")
            self.gameWindow.append(monster + "의 공격!")
            self.gameWindow.append("주인공은 " + str(mon_damage) + "의 데미지를 입었다.")

        elif action == "에너지 볼트":
            self.gameWindow.append("주인공은 에너지 볼트를 사용했다!")
            self.gameWindow.append(monster + " 은/는 " + str(damage) + "의 데미지를 입었다.")
            self.gameWindow.append(monster + "의 공격!")
            self.gameWindow.append("주인공은 " + str(mon_damage) + "의 데미지를 입었다.")

        elif action == "파이어볼":
            self.gameWindow.append("주인공은 파이어볼을 사용했다!")
            self.gameWindow.append(monster + " 은/는 " + str(damage) + "의 데미지를 입었다.")
            self.gameWindow.append(monster + "의 공격!")
            self.gameWindow.append("주인공은 " + str(mon_damage) + "의 데미지를 입었다.")

        elif action == "콜드빔":
            self.gameWindow.append("주인공은 콜드빔을 사용했다!")
            self.gameWindow.append(monster + " 은/는 " + str(damage) + "의 데미지를 입었다.")
            self.gameWindow.append(monster + "의 공격!")
            self.gameWindow.append("주인공은 " + str(mon_damage) + "의 데미지를 입었다.")

        elif action == "라이트닝":
            self.gameWindow.append("주인공은 라이트닝을 사용했다!")
            self.gameWindow.append(monster + " 은/는 " + str(damage) + "의 데미지를 입었다.")
            self.gameWindow.append(monster + "의 공격!")
            self.gameWindow.append("주인공은 " + str(mon_damage) + "의 데미지를 입었다.")

        elif action == "익스플로전":
            self.gameWindow.append("주인공은 익스플로전 사용했다!")
            self.gameWindow.append(monster + " 은/는 " + str(damage) + "의 데미지를 입었다.")
            self.gameWindow.append(monster + "의 공격!")
            self.gameWindow.append("주인공은 " + str(mon_damage) + "의 데미지를 입었다.")

        elif action == "신비한 화살":
            self.gameWindow.append("주인공은 신비한 화살을 사용했다!")
            self.gameWindow.append(monster + " 은/는 " + str(damage) + "의 데미지를 입었다.")
            self.gameWindow.append(monster + "의 공격!")
            self.gameWindow.append("주인공은 " + str(mon_damage) + "의 데미지를 입었다.")

        elif action == "더블 샷":
            self.gameWindow.append("주인공은 더블 샷을 사용했다!")
            self.gameWindow.append(monster + " 은/는 " + str(damage) + "의 데미지를 입었다.")
            self.gameWindow.append(monster + "의 공격!")
            self.gameWindow.append("주인공은 " + str(mon_damage) + "의 데미지를 입었다.")

        elif action == "차지 샷":
            self.gameWindow.append("주인공은 차지 샷을 사용했다!")
            self.gameWindow.append(monster + " 은/는 " + str(damage) + "의 데미지를 입었다.")
            self.gameWindow.append(monster + "의 공격!")
            self.gameWindow.append("주인공은 " + str(mon_damage) + "의 데미지를 입었다.")

        elif action == "화살 비":
            self.gameWindow.append("주인공은 화살 비를 사용했다!")
            self.gameWindow.append(monster + " 은/는 " + str(damage) + "의 데미지를 입었다.")
            self.gameWindow.append(monster + "의 공격!")
            self.gameWindow.append("주인공은 " + str(mon_damage) + "의 데미지를 입었다.")

        elif action == "스나이핑":
            self.gameWindow.append("주인공은 스나이핑을 사용했다!")
            self.gameWindow.append(monster + " 은/는 " + str(damage) + "의 데미지를 입었다.")
            self.gameWindow.append(monster + "의 공격!")
            self.gameWindow.append("주인공은 " + str(mon_damage) + "의 데미지를 입었다.")

        elif action == "용사의검":
            self.gameWindow.append("주인공은 용사의검을 사용했다!")
            self.gameWindow.append("그러나 아무일도 일어나지 않았다!")
            self.gameWindow.append("마왕 : \"이 정도로는 봉인되지 않는다!\"")
            self.gameWindow.append(monster + "의 공격!")
            self.gameWindow.append("주인공은 " + str(mon_damage) + "의 데미지를 입었다.")

    # 유저 체력 0
    def gameover(self):
        self.gameWindow.append("주인공은 쓰러졌다.\n")
        self.gameWindow.append("게임 오버")
        self.button_text("메인으로")

    # 몬스터 체력 0
    def enemy_kill(self,monster,gold,count):
        self.gameWindow.append(monster+" 은/는 쓰러졌다.")
        self.gameWindow.append(str(gold) +"의 골드를 획득했다.")
        self.gameWindow.append("")
        if count != 10:
            self.button_text("전진한다")
        else:
            self.gameWindow.append("")
            self.gameWindow.append("던전을 클리어하였습니다.")
            self.gameWindow.append("레벨 업!")
            if self.placeWindow.text()[-1] == "1" or self.placeWindow.text()[-1] == "3" or self.placeWindow.text()[-1] == "5" or self.placeWindow.text()[-1] == "7" or self.placeWindow.text()[-1] == "9":
                self.gameWindow.append("새로운 스킬을 획득했습니다!")
            self.button_text("탈출한다")

    # 스킬 클릭 시
    def skill_text(self,job,level):
        num = int(level/2)
        if job == "전사":
            if num == 0 :
                pass
            elif num == 1 :
                self.button_text(self.warrior_skill[0],"","","취소")
            elif num == 2 :
                self.button_text(self.warrior_skill[0],self.warrior_skill[1],"","취소")
            elif num == 3 :
                self.button_text(self.warrior_skill[0],self.warrior_skill[1],self.warrior_skill[2],"취소")
            else:
                self.button_text(self.warrior_skill[0], self.warrior_skill[1], self.warrior_skill[2], "다음")
        elif job == "법사":
            if num == 0 :
                pass
            elif num == 1 :
                self.button_text(self.magican_skill[0],"","","취소")
            elif num == 2 :
                self.button_text(self.magican_skill[0],self.magican_skill[1],"","취소")
            elif num == 3 :
                self.button_text(self.magican_skill[0],self.magican_skill[1],self.magican_skill[2],"취소")
            else:
                self.button_text(self.magican_skill[0], self.magican_skill[1], self.magican_skill[2], "다음")
        elif job == "궁수":
            if num == 0 :
                pass
            elif num == 1 :
                self.button_text(self.hunter_skill[0],"","","취소")
            elif num == 2 :
                self.button_text(self.hunter_skill[0],self.hunter_skill[1],"","취소")
            elif num == 3:
                self.button_text(self.hunter_skill[0],self.hunter_skill[1],self.hunter_skill[2],"취소")
            else:
                self.button_text(self.hunter_skill[0], self.hunter_skill[1], self.hunter_skill[2], "다음")

        else:
            if num == 0 :
                pass
            elif num == 1 :
                self.button_text(self.warrior_skill[0],"","","취소")
            elif num == 2 :
                self.button_text(self.warrior_skill[0],self.magican_skill[1],"","취소")
            elif num == 3:
                self.button_text(self.warrior_skill[0],self.magican_skill[1],self.hunter_skill[2],"취소")
            else:
                self.button_text(self.warrior_skill[0], self.magican_skill[1], self.hunter_skill[2], "다음")
    def next_skill(self,job,level):
        num = int(level / 2)
        if job == "전사":
            if num == 4 :
                self.button_text(self.warrior_skill[3],"","","취소")
            else:
                self.button_text(self.warrior_skill[3],self.warrior_skill[4],"","취소")
        elif job == "법사":
            if num == 4:
                self.button_text(self.magican_skill[3], "", "", "취소")
            else:
                self.button_text(self.magican_skill[3], self.magican_skill[4], "", "취소")
        elif job == "궁수":
            if num == 4:
                self.button_text(self.hunter_skill[3], "", "", "취소")
            else:
                self.button_text(self.hunter_skill[3], self.hunter_skill[4], "", "취소")
        else:
            if num == 4:
                self.button_text(self.magican_skill[3], "", "", "취소")
            else:
                self.button_text(self.magican_skill[3], self.warrior_skill[4], "", "취소")

    # 마나 부족 시
    def mp_not(self):
        self.gameWindow.append("마나가 부족합니다.")

    # 용사의 검 미사용
    def no_use_sword(self):
        self.gameWindow.append("마왕 : \"그런 무기론 나를 쓰러뜨릴 수 없다!\"")
        self.action_choice()

    # 보스 처치
    def boss_kill(self):
        self.gameWindow.clear()
        self.gameWindow.setText("주인공은 용사의검을 사용했다!")
        self.gameWindow.append("용사의검이 빛나기 시작했다!")
        self.gameWindow.append("마왕 쿠파: \"젠장! 이렇게 당하다니!!!!")
        self.gameWindow.append("마왕 쿠파의 봉인에 성공하였습니다!")
        self.button_text("엔딩")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    game = mainView()
    game.show()
    sys.exit(app.exec_())
