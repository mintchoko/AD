import sys
from ad_model import mainModel
from ad_view import mainView

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton
from PyQt5.QtWidgets import QApplication, QWidget

class mainController:
    def __init__(self):
        self.model = mainModel()
        self.view = mainView()
        self.view.button_1.clicked.connect(self.button1_func)
        self.view.button_2.clicked.connect(self.button2_func)
        self.view.button_3.clicked.connect(self.button3_func)
        self.view.button_4.clicked.connect(self.button4_func)


    # 게임 시작
    def startGame(self,app):
        self.view.main2()
        self.view.show()
        sys.exit(app.exec_())

    # 버튼 1 이벤트 연결 함수
    def button1_func(self):
        b1 = self.view.button_1
        if b1.text() == "메인으로":
            self.view.main2()

        elif b1.text() == "새 게임":
            self.model.clear()
            self.view.text_start("prolog.txt")

        elif b1.text() == "다음 문장":
            self.view.next()

        elif b1.text() == "종료":
            self.view.script_end()

        elif b1.text() == "전사":
            self.model.job_set("전사")
            self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                self.model.current_mp, self.model.mp,self.model.gold)
            self.view.gameWindow.clear()
            self.view.village(self.model.level)

        elif b1.text() == "예":
            pass

        elif b1.text() == "저장":
            self.view.save_text()

        elif b1.text() == "세이브 1":
            if self.view.placeWindow.text() == "저장":
                self.model.save("save1.txt")
                self.view.village(self.model.level)
            else:
                a = self.model.load("save1.txt")
                if a:
                    self.view.village(self.model.level)
                    self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                        self.model.current_mp, self.model.mp,self.model.gold)
                else:
                    self.view.load_fail()

        elif b1.text() == "불러오기":
            self.view.load_text_main()

        elif b1.text() == "체력물약":
            a = self.model.buy("체력물약")
            self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                self.model.current_mp, self.model.mp, self.model.gold)
            self.view.buy_text("체력물약",a)

        elif b1.text() == "다음 던전":
            self.view.dungeon_enter(self.model.level)
            self.model.mon_count = 0
            self.model.dungeon()
            self.view.battle(self.model.mon_name,self.model.mon_count,self.model.mon_level,self.model.mon_hp)
            self.view.action_choice()

        elif b1.text() == "마지막 던전":
            self.view.dungeon_enter(self.model.level)
            self.model.boss_dungeon()
            self.view.boss_battle(self.model.boss_name,self.model.boss_level,self.model.boss_hp)
            self.view.action_choice()
        elif b1.text() == "공격":

            damage = self.model.attack()
            mon_damage = self.model.enemy_attack()
            self.view.action_text("공격",self.model.mon_name,mon_damage,damage)
            if self.model.mon_cu_hp > 0 and self.model.current_hp > 0:
                self.view.enemy_set(self.model.mon_name, self.model.mon_level, self.model.mon_cu_hp, self.model.mon_hp)
                self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                    self.model.current_mp, self.model.mp, self.model.gold)
                self.view.action_choice()
            elif self.model.current_hp <= 0:
                self.view.user_text(self.model.job, self.model.level, 0, self.model.hp,
                                    self.model.current_mp, self.model.mp, self.model.gold)
                self.view.enemy_set(self.model.mon_name, self.model.mon_level, self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                self.view.gameover()
                self.model.clear()
            elif self.model.mon_cu_hp <= 0 :
                if self.view.placeWindow.text() == "파이널 스테이지":
                    self.view.no_use_sword()
                    self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                        self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                else:
                    gold = self.model.earn()
                    self.view.enemy_kill(self.model.mon_name, gold, self.model.mon_count)
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level, 0, self.model.mon_hp)
                    if self.model.mon_count == 10:
                        if self.model.job == "전사":
                            self.model.warrior()
                        elif self.model.job == "법사":
                            self.model.magican()
                        elif self.model.job == "궁수":
                            self.model.hunter()
                    self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
        elif b1.text() == "강타":
            if self.model.current_mp >= 5:
                self.view.back()
                damage = self.model.wa_skill_1()
                mon_damage = self.model.enemy_attack()
                self.view.action_text("강타", self.model.mon_name, mon_damage, damage)
                if self.model.mon_cu_hp > 0 and self.model.current_hp > 0:
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level, self.model.mon_cu_hp,
                                        self.model.mon_hp)
                    self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.action_choice()
                elif self.model.current_hp <= 0:
                    self.view.user_text(self.model.job, self.model.level, 0, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                        self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    self.view.gameover()
                    self.model.clear()
                elif self.model.mon_cu_hp <= 0:
                    if self.view.placeWindow.text() == "파이널 스테이지":
                        self.view.no_use_sword()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                            self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    else:
                        gold = self.model.earn()
                        self.view.enemy_kill(self.model.mon_name, gold, self.model.mon_count)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level, 0, self.model.mon_hp)
                        if self.model.mon_count == 10:
                            if self.model.job == "전사":
                                self.model.warrior()
                            elif self.model.job == "법사":
                                self.model.magican()
                            elif self.model.job == "궁수":
                                self.model.hunter()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
            else:
                self.view.mp_not()

        elif b1.text() == "에너지 볼트":
            if self.model.current_mp >= 8:
                self.view.back()
                damage = self.model.ma_skill_1()
                mon_damage = self.model.enemy_attack()
                self.view.action_text("에너지 볼트", self.model.mon_name, mon_damage, damage)
                if self.model.mon_cu_hp > 0 and self.model.current_hp > 0:
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level, self.model.mon_cu_hp,
                                        self.model.mon_hp)
                    self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.action_choice()
                elif self.model.current_hp <= 0:
                    self.view.user_text(self.model.job, self.model.level, 0, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                        self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    self.view.gameover()
                    self.model.clear()
                elif self.model.mon_cu_hp <= 0:
                    if self.view.placeWindow.text() == "파이널 스테이지":
                        self.view.no_use_sword()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                            self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    else:
                        gold = self.model.earn()
                        self.view.enemy_kill(self.model.mon_name, gold, self.model.mon_count)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level, 0, self.model.mon_hp)
                        if self.model.mon_count == 10:
                            if self.model.job == "전사":
                                self.model.warrior()
                            elif self.model.job == "법사":
                                self.model.magican()
                            elif self.model.job == "궁수":
                                self.model.hunter()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
            else:
                self.view.mp_not()

        elif b1.text() == "신비한 화살":
            if self.model.current_mp >= 7:
                self.view.back()
                damage = self.model.hu_skill_1()
                mon_damage = self.model.enemy_attack()
                self.view.action_text("신비한 화살", self.model.mon_name, mon_damage, damage)
                if self.model.mon_cu_hp > 0 and self.model.current_hp > 0:
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level, self.model.mon_cu_hp,
                                        self.model.mon_hp)
                    self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.action_choice()
                elif self.model.current_hp <= 0:
                    self.view.user_text(self.model.job, self.model.level, 0, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                        self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    self.view.gameover()
                    self.model.clear()
                elif self.model.mon_cu_hp <= 0:
                    if self.view.placeWindow.text() == "파이널 스테이지":
                        self.view.no_use_sword()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                            self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    else:
                        gold = self.model.earn()
                        self.view.enemy_kill(self.model.mon_name, gold, self.model.mon_count)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level, 0, self.model.mon_hp)
                        if self.model.mon_count == 10:
                            if self.model.job == "전사":
                                self.model.warrior()
                            elif self.model.job == "법사":
                                self.model.magican()
                            elif self.model.job == "궁수":
                                self.model.hunter()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
            else:
                self.view.mp_not()

        elif b1.text() == "유성검":
            if self.model.current_mp >= 12:
                self.view.back()
                damage = self.model.wa_skill_4()
                mon_damage = self.model.enemy_attack()
                self.view.action_text("유성검", self.model.mon_name, mon_damage, damage)
                if self.model.mon_cu_hp > 0 and self.model.current_hp > 0:
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level, self.model.mon_cu_hp,
                                        self.model.mon_hp)
                    self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.action_choice()
                elif self.model.current_hp <= 0:
                    self.view.user_text(self.model.job, self.model.level, 0, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                        self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    self.view.gameover()
                    self.model.clear()
                elif self.model.mon_cu_hp <= 0:
                    if self.view.placeWindow.text() == "파이널 스테이지":
                        self.view.no_use_sword()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                            self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    else:
                        gold = self.model.earn()
                        self.view.enemy_kill(self.model.mon_name, gold, self.model.mon_count)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level, 0, self.model.mon_hp)
                        if self.model.mon_count == 10:
                            if self.model.job == "전사":
                                self.model.warrior()
                            elif self.model.job == "법사":
                                self.model.magican()
                            elif self.model.job == "궁수":
                                self.model.hunter()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
            else:
                self.view.mp_not()

        elif b1.text() == "라이트닝":
            if self.model.current_mp >= 12:
                self.view.back()
                damage = self.model.ma_skill_4()
                mon_damage = self.model.enemy_attack()
                self.view.action_text("라이트닝", self.model.mon_name, mon_damage, damage)
                if self.model.mon_cu_hp > 0 and self.model.current_hp > 0:
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level, self.model.mon_cu_hp,
                                        self.model.mon_hp)
                    self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.action_choice()
                elif self.model.current_hp <= 0:
                    self.view.user_text(self.model.job, self.model.level, 0, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                        self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    self.view.gameover()
                    self.model.clear()
                elif self.model.mon_cu_hp <= 0:
                    if self.view.placeWindow.text() == "파이널 스테이지":
                        self.view.no_use_sword()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                            self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    else:
                        gold = self.model.earn()
                        self.view.enemy_kill(self.model.mon_name, gold, self.model.mon_count)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level, 0, self.model.mon_hp)
                        if self.model.mon_count == 10:
                            if self.model.job == "전사":
                                self.model.warrior()
                            elif self.model.job == "법사":
                                self.model.magican()
                            elif self.model.job == "궁수":
                                self.model.hunter()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
            else:
                self.view.mp_not()

        elif b1.text() == "화살 비":
            if self.model.current_mp >= 8:
                self.view.back()
                damage = self.model.hu_skill_4()
                mon_damage = self.model.enemy_attack()
                self.view.action_text("화살 비", self.model.mon_name, mon_damage, damage)
                if self.model.mon_cu_hp > 0 and self.model.current_hp > 0:
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level, self.model.mon_cu_hp,
                                        self.model.mon_hp)
                    self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.action_choice()
                elif self.model.current_hp <= 0:
                    self.view.user_text(self.model.job, self.model.level, 0, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                        self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    self.view.gameover()
                    self.model.clear()
                elif self.model.mon_cu_hp <= 0:
                    if self.view.placeWindow.text() == "파이널 스테이지":
                        self.view.no_use_sword()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                            self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    else:
                        gold = self.model.earn()
                        self.view.enemy_kill(self.model.mon_name, gold, self.model.mon_count)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level, 0, self.model.mon_hp)
                        if self.model.mon_count == 10:
                            if self.model.job == "전사":
                                self.model.warrior()
                            elif self.model.job == "법사":
                                self.model.magican()
                            elif self.model.job == "궁수":
                                self.model.hunter()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
            else:
                self.view.mp_not()

        elif b1.text() == "뒤로":
            self.view.back()

        elif "개" in b1.text() and ("0" not in b1.text() or "10" in b1.text()):
            self.model.use("체력물약")
            mon_damage = self.model.enemy_attack()
            self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                self.model.current_mp, self.model.mp, self.model.gold)
            self.view.action_text("체력물약",self.model.mon_name,mon_damage)
            if self.model.current_hp > 0:
                self.view.action_choice()
                self.view.back()
            elif self.model.current_hp <= 0:
                self.view.gameover()
                self.model.clear()

        elif b1.text() == "메인으로":
            self.view.main2()

        elif b1.text() == "전진한다":
            self.model.dungeon()
            self.view.battle(self.model.mon_name, self.model.mon_count, self.model.mon_level, self.model.mon_hp)
            self.view.action_choice()
            self.view.back()

        elif b1.text() == "탈출한다":
            if self.model.level != 11:
                self.view.gameWindow.clear()
                self.view.enemyWindow.clear()
                self.view.village(self.model.level)
            else:
                self.view.gameWindow.clear()
                self.view.enemyWindow.clear()
                self.view.village(self.model.level)
                present = ["용사의검", "체력물약", "체력물약", "체력물약", "마나물약", "마나물약", "마나물약"]
                self.model.item_list.extend(present)
                self.view.text_start("shop.txt")

        elif b1.text() == "엔딩":
            self.view.text_start("ending.txt")


    # 버튼 2 이벤트 연결 함수
    def button2_func(self):
        b2 = self.view.button_2
        if b2.text() == "불러오기":
            if self.view.button_1.text() == "저장":
                self.view.load_text_vill()
            else:
                self.view.load_text_main()

        elif b2.text() == "스킵":
            self.view.script_end()

        elif b2.text() == "법사":
            self.model.job_set("법사")
            self.view.user_text(self.model.job,self.model.level,self.model.current_hp,self.model.hp,
                                self.model.current_mp,self.model.mp,self.model.gold)
            self.view.gameWindow.clear()
            self.view.village(self.model.level)

        elif b2.text() == "아니오":
            pass

        elif b2.text() == "세이브 2":
            if self.view.placeWindow.text() == "저장":
                self.model.save("save2.txt")
                self.view.village(self.model.level)
            else:
                a = self.model.load("save2.txt")
                if a:
                    self.view.village(self.model.level)
                    self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                else:
                    self.view.load_fail()

        elif b2.text() == "상점":
            self.view.shop()

        elif b2.text() == "취소":
            self.view.main2()

        elif b2.text() == "마나물약":
            a = self.model.buy("마나물약")
            self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                self.model.current_mp, self.model.mp, self.model.gold)
            self.view.buy_text("마나물약",a)

        elif b2.text() == "뒤로":
            self.view.back()

        elif b2.text() == "스킬":
            self.view.skill_text(self.model.job,self.model.level)

        elif "개" in b2.text() and "0" not in b2.text():
            self.model.use("마나물약")
            mon_damage = self.model.enemy_attack()
            self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                self.model.current_mp, self.model.mp, self.model.gold)
            self.view.action_text("마나물약", self.model.mon_name, mon_damage)
            if self.model.current_hp > 0:
                self.view.action_choice()
                self.view.back()
            elif self.model.current_hp <= 0:
                self.view.gameover()
                self.model.clear()

        elif b2.text() == "슬래시":
            if self.model.current_mp >= 7:
                self.view.back()
                damage = self.model.wa_skill_2()
                mon_damage = self.model.enemy_attack()
                self.view.action_text("슬래시", self.model.mon_name, mon_damage, damage)
                if self.model.mon_cu_hp > 0 and self.model.current_hp > 0:
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level, self.model.mon_cu_hp,
                                        self.model.mon_hp)
                    self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.action_choice()
                elif self.model.current_hp <= 0:
                    self.view.user_text(self.model.job, self.model.level, 0, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                        self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    self.view.gameover()
                    self.model.clear()
                elif self.model.mon_cu_hp <= 0:
                    if self.view.placeWindow.text() == "파이널 스테이지":
                        self.view.no_use_sword()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                            self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    else:
                        gold = self.model.earn()
                        self.view.enemy_kill(self.model.mon_name, gold, self.model.mon_count)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level, 0, self.model.mon_hp)
                        if self.model.mon_count == 10:
                            if self.model.job == "전사":
                                self.model.warrior()
                            elif self.model.job == "법사":
                                self.model.magican()
                            elif self.model.job == "궁수":
                                self.model.hunter()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
            else:
                self.view.mp_not()

        elif b2.text() == "파이어볼":
            if self.model.current_mp >= 10:
                self.view.back()
                damage = self.model.ma_skill_2()
                mon_damage = self.model.enemy_attack()
                self.view.action_text("파이어볼", self.model.mon_name, mon_damage, damage)
                if self.model.mon_cu_hp > 0 and self.model.current_hp > 0:
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level, self.model.mon_cu_hp,
                                        self.model.mon_hp)
                    self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.action_choice()
                elif self.model.current_hp <= 0:
                    self.view.user_text(self.model.job, self.model.level, 0, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                        self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    self.view.gameover()
                    self.model.clear()
                elif self.model.mon_cu_hp <= 0:
                    if self.view.placeWindow.text() == "파이널 스테이지":
                        self.view.no_use_sword()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                            self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    else:
                        gold = self.model.earn()
                        self.view.enemy_kill(self.model.mon_name, gold, self.model.mon_count)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level, 0, self.model.mon_hp)
                        if self.model.mon_count == 10:
                            if self.model.job == "전사":
                                self.model.warrior()
                            elif self.model.job == "법사":
                                self.model.magican()
                            elif self.model.job == "궁수":
                                self.model.hunter()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
            else:
                self.view.mp_not()

        elif b2.text() == "더블 샷":
            if self.model.current_mp >= 9:
                self.view.back()
                damage = self.model.hu_skill_2()
                mon_damage = self.model.enemy_attack()
                self.view.action_text("더블 샷", self.model.mon_name, mon_damage, damage)
                if self.model.mon_cu_hp > 0 and self.model.current_hp > 0:
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level, self.model.mon_cu_hp,
                                        self.model.mon_hp)
                    self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.action_choice()
                elif self.model.current_hp <= 0:
                    self.view.user_text(self.model.job, self.model.level, 0, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                        self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    self.view.gameover()
                    self.model.clear()
                elif self.model.mon_cu_hp <= 0:
                    if self.view.placeWindow.text() == "파이널 스테이지":
                        self.view.no_use_sword()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                            self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    else:
                        gold = self.model.earn()
                        self.view.enemy_kill(self.model.mon_name, gold, self.model.mon_count)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level, 0, self.model.mon_hp)
                        if self.model.mon_count == 10:
                            if self.model.job == "전사":
                                self.model.warrior()
                            elif self.model.job == "법사":
                                self.model.magican()
                            elif self.model.job == "궁수":
                                self.model.hunter()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
            else:
                self.view.mp_not()

        elif b2.text() == "바람의 상처":
            if self.model.current_mp >= 20:
                self.view.back()
                damage = self.model.wa_skill_5()
                mon_damage = self.model.enemy_attack()
                self.view.action_text("바람의 상처", self.model.mon_name, mon_damage, damage)
                if self.model.mon_cu_hp > 0 and self.model.current_hp > 0:
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level, self.model.mon_cu_hp,
                                        self.model.mon_hp)
                    self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.action_choice()
                elif self.model.current_hp <= 0:
                    self.view.user_text(self.model.job, self.model.level, 0, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                        self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    self.view.gameover()
                    self.model.clear()
                elif self.model.mon_cu_hp <= 0:
                    if self.view.placeWindow.text() == "파이널 스테이지":
                        self.view.no_use_sword()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                            self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    else:
                        gold = self.model.earn()
                        self.view.enemy_kill(self.model.mon_name, gold, self.model.mon_count)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level, 0, self.model.mon_hp)
                        if self.model.mon_count == 10:
                            if self.model.job == "전사":
                                self.model.warrior()
                            elif self.model.job == "법사":
                                self.model.magican()
                            elif self.model.job == "궁수":
                                self.model.hunter()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
            else:
                self.view.mp_not()

        elif b2.text() == "익스플로전":
            if self.model.current_mp >= 24:
                self.view.back()
                damage = self.model.ma_skill_5()
                mon_damage = self.model.enemy_attack()
                self.view.action_text("익스플로전", self.model.mon_name, mon_damage, damage)
                if self.model.mon_cu_hp > 0 and self.model.current_hp > 0:
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level, self.model.mon_cu_hp,
                                        self.model.mon_hp)
                    self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.action_choice()
                elif self.model.current_hp <= 0:
                    self.view.user_text(self.model.job, self.model.level, 0, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                        self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    self.view.gameover()
                    self.model.clear()
                elif self.model.mon_cu_hp <= 0:
                    if self.view.placeWindow.text() == "파이널 스테이지":
                        self.view.no_use_sword()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                            self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    else:
                        gold = self.model.earn()
                        self.view.enemy_kill(self.model.mon_name, gold, self.model.mon_count)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level, 0, self.model.mon_hp)
                        if self.model.mon_count == 10:
                            if self.model.job == "전사":
                                self.model.warrior()
                            elif self.model.job == "법사":
                                self.model.magican()
                            elif self.model.job == "궁수":
                                self.model.hunter()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
            else:
                self.view.mp_not()

        elif b2.text() == "스나이핑":
            if self.model.current_mp >= 25:
                self.view.back()
                damage = self.model.hu_skill_5()
                mon_damage = self.model.enemy_attack()
                self.view.action_text("스나이핑", self.model.mon_name, mon_damage, damage)
                if self.model.mon_cu_hp > 0 and self.model.current_hp > 0:
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level, self.model.mon_cu_hp,
                                        self.model.mon_hp)
                    self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.action_choice()
                elif self.model.current_hp <= 0:
                    self.view.user_text(self.model.job, self.model.level, 0, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                        self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    self.view.gameover()
                    self.model.clear()
                elif self.model.mon_cu_hp <= 0:
                    if self.view.placeWindow.text() == "파이널 스테이지":
                        self.view.no_use_sword()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                            self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    else:
                        gold = self.model.earn()
                        self.view.enemy_kill(self.model.mon_name, gold, self.model.mon_count)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level, 0, self.model.mon_hp)
                        if self.model.mon_count == 10:
                            if self.model.job == "전사":
                                self.model.warrior()
                            elif self.model.job == "법사":
                                self.model.magican()
                            elif self.model.job == "궁수":
                                self.model.hunter()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
            else:
                self.view.mp_not()


    # 버튼 3 이벤트 연결 함수
    def button3_func(self):
        b3 = self.view.button_3
        if b3.text() == "개발자들":
            self.view.credit()

        elif b3.text() == "궁수":
            self.model.job_set("궁수")
            self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                self.model.current_mp, self.model.mp,self.model.gold)
            self.view.gameWindow.clear()
            self.view.village(self.model.level)

        elif b3.text() == "저장/불러오기":
            self.view.save_load()

        elif b3.text() == "취소":
            self.view.gameWindow.clear()
            self.view.village(self.model.level)

        elif b3.text() == "세이브 3":
            if self.view.placeWindow.text() == "저장":
                self.model.save("save3.txt")
                self.view.village(self.model.level)
            else:
                a = self.model.load("save3.txt")
                if a:
                    self.view.village(self.model.level)
                    self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                else:
                    self.view.load_fail()

        elif b3.text() == "나가기":
            self.view.village(self.model.level)

        elif b3.text() == "뒤로":
            self.view.back()

        elif b3.text() == "방어":
            mon_damage = self.model.enemy_attack()
            damage = self.model.guard(mon_damage)
            self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                self.model.current_mp, self.model.mp, self.model.gold)
            self.view.action_text("방어",self.model.mon_name,damage)
            if self.model.current_hp > 0:
                self.view.action_choice()
            elif self.model.current_hp <= 0:
                self.view.gameover()
                self.model.clear()

        elif b3.text() == "삼연 베기":
            if self.model.current_mp >= 10:
                self.view.back()
                damage = self.model.wa_skill_3()
                mon_damage = self.model.enemy_attack()
                self.view.action_text("삼연 베기", self.model.mon_name, mon_damage, damage)
                if self.model.mon_cu_hp > 0 and self.model.current_hp > 0:
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level, self.model.mon_cu_hp,
                                        self.model.mon_hp)
                    self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.action_choice()
                elif self.model.current_hp <= 0:
                    self.view.user_text(self.model.job, self.model.level, 0, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                        self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    self.view.gameover()
                    self.model.clear()
                elif self.model.mon_cu_hp <= 0:
                    if self.view.placeWindow.text() == "파이널 스테이지":
                        self.view.no_use_sword()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                            self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    else:
                        gold = self.model.earn()
                        self.view.enemy_kill(self.model.mon_name, gold, self.model.mon_count)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level, 0, self.model.mon_hp)
                        if self.model.mon_count == 10:
                            if self.model.job == "전사":
                                self.model.warrior()
                            elif self.model.job == "법사":
                                self.model.magican()
                            elif self.model.job == "궁수":
                                self.model.hunter()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
            else:
                self.view.mp_not()

        elif b3.text() == "콜드빔":
            if self.model.current_mp >= 12:
                self.view.back()
                damage = self.model.ma_skill_3()
                mon_damage = self.model.enemy_attack()
                self.view.action_text("콜드빔", self.model.mon_name, mon_damage, damage)
                if self.model.mon_cu_hp > 0 and self.model.current_hp > 0:
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level, self.model.mon_cu_hp,
                                        self.model.mon_hp)
                    self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.action_choice()
                elif self.model.current_hp <= 0:
                    self.view.user_text(self.model.job, self.model.level, 0, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                        self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    self.view.gameover()
                    self.model.clear()
                elif self.model.mon_cu_hp <= 0:
                    if self.view.placeWindow.text() == "파이널 스테이지":
                        self.view.no_use_sword()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                            self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    else:
                        gold = self.model.earn()
                        self.view.enemy_kill(self.model.mon_name, gold, self.model.mon_count)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level, 0, self.model.mon_hp)
                        if self.model.mon_count == 10:
                            if self.model.job == "전사":
                                self.model.warrior()
                            elif self.model.job == "법사":
                                self.model.magican()
                            elif self.model.job == "궁수":
                                self.model.hunter()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
            else:
                self.view.mp_not()

        elif b3.text() == "차지 샷":
            if self.model.current_mp >= 12:
                self.view.back()
                damage = self.model.hu_skill_3()
                mon_damage = self.model.enemy_attack()
                self.view.action_text("차지 샷", self.model.mon_name, mon_damage, damage)
                if self.model.mon_cu_hp > 0 and self.model.current_hp > 0:
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level, self.model.mon_cu_hp,
                                        self.model.mon_hp)
                    self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.action_choice()
                elif self.model.current_hp <= 0:
                    self.view.user_text(self.model.job, self.model.level, 0, self.model.hp,
                                        self.model.current_mp, self.model.mp, self.model.gold)
                    self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                        self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    self.view.gameover()
                    self.model.clear()
                elif self.model.mon_cu_hp <= 0:
                    if self.view.placeWindow.text() == "파이널 스테이지":
                        self.view.no_use_sword()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level,
                                            self.model.mon_cu_hp if self.model.mon_cu_hp > 0 else 0, self.model.mon_hp)
                    else:
                        gold = self.model.earn()
                        self.view.enemy_kill(self.model.mon_name, gold, self.model.mon_count)
                        self.view.enemy_set(self.model.mon_name, self.model.mon_level, 0, self.model.mon_hp)
                        if self.model.mon_count == 10:
                            if self.model.job == "전사":
                                self.model.warrior()
                            elif self.model.job == "법사":
                                self.model.magican()
                            elif self.model.job == "궁수":
                                self.model.hunter()
                        self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                            self.model.current_mp, self.model.mp, self.model.gold)
            else:
                self.view.mp_not()

        elif b3.text() == "용사의검":
            if self.model.mon_cu_hp > 0:
                mon_damage = self.model.enemy_attack()
                self.view.action_text("용사의검", self.model.mon_name, mon_damage)
                self.view.action_choice()
                self.view.user_text(self.model.job, self.model.level, self.model.current_hp, self.model.hp,
                                    self.model.current_mp, self.model.mp, self.model.gold)
            else:
                self.view.boss_kill()


    # 버튼 4 이벤트 연결 함수
    def button4_func(self):
        b4 = self.view.button_4
        if b4.text() == "종료":
            self.view.close()

        elif b4.text() == "메인으로":
            self.view.main2()

        elif b4.text() == "아이템":
            hp_count = 0
            mp_count = 0
            sword = False
            for i in self.model.item_list:
                if i == "체력물약":
                    hp_count += 1
                elif i == "마나물약":
                    mp_count += 1
                else:
                    sword = True
            self.view.item_click(hp_count,mp_count,sword)

        elif b4.text() == "취소":
            if self.view.placeWindow.text() == "불러오기/메인":
                self.view.main2()
            elif self.view.placeWindow.text() == "저장" or self.view.placeWindow.text() == "불러오기/마을":
                self.view.village(self.model.level)
            else:
                self.view.back()

        elif b4.text() == "다음":
            self.view.next_skill(self.model.job,self.model.level)

        elif b4.text() == "뒤로":
            self.view.back()
