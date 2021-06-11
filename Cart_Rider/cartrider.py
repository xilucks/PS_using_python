import random
from typing import Sized


class Character:

    def __init__(self, speed):
        self.speed = speed


class Item:

    def __init__(self, item_type, speed_change):
        self.item_type = item_type
        self.speed_change = speed_change


class Player:
    def __init__(self, name):
        self.name = name  # 플레이어의 이름 저장
        self.speed = 0  # 플레이어의 속도: 선택한 character의 속도!
        self.round_speed = 0  # 아이템 적용 후 플레이어의 속도
        self.play_records = []  # 플레이어의 경기 기록: 라운드별 주행 시간[초]

    def add_play_record(self, record_in_hr):
        """
        - 플레이어의 경기 기록을 받아 저장합니다.
        - 시간 단위로 들어온 기록을 초 단위의 기록으로 변환해 저장해야합니다.
        - Game 클래스의 play_round() 함수에서 호출됩니다.
        """
        # TODO : 플레이어의 경기 기록을 초 단위로 변환해 저장해주세요.


class Game:

    def __init__(self):
        self.num_rounds = 3
        self.player_list = []  # 플레이어의 목록. 이후에 set_players를 이용해 수정
        self.item_list = []  # 아이템의 목록. 이후에 set_item_list를 이용해 수정
        self.character_list = []
        self.record_list = []  # 기록저장

    def set_players(self):
        """
        - 5명의 플레이어를 생성하는 함수입니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """
        print("******************* 게임 접속 *******************")
        # TODO : 사용자로부터 플레이어의 이름을 입력받아 Player 객체를 생성하고 플레이어 목록(self.player_list)에 추가해주세요.
        i = 1;
        while i < 6:
            name = input("Player{0}의 이름을 입력해주세요:".format(i))
            self.player_list.append(name)
            i += 1

    def start_game(self):
        """
        - 게임 규칙의 [게임 시작 전] 부분을 담당하는 함수입니다.
        - 3 종류의 캐릭터와 2 종류의 아이템을 초기화하고, 사용자의 입력을 받아 각 플레이어의 속도를 설정합니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """
        print("******************* 캐릭터 선택 *******************")
        # TODO (1): 범위 내의 속도를 가진 세 종류의 캐릭터를 생성해주세요.
        speed = []
        speed.append(random.randint(100, 180))
        speed.append(random.randint(100, 180))
        speed.append(random.randint(100, 180))
        # TODO (2): 사용자의 입력을 받아 플레이어의 고유 속도를 설정하고, 선택된 캐릭터의 속도를 출력해주세요.
        j = 0;
        while j < 5:
            n = int(input("{}의 캐릭터 선택 차례입니다. 1,2,3 중 하나의 값을 입력해주세요. ".format(self.player_list[j])))
            print("{}의 고유 속도는 시속 {}입니다.".format(self.player_list[j], speed[n - 1]))
            self.speed = speed[n - 1]
            j += 1

        # TODO (3): 두 종류의 아이템을 생성해 아이템 목록(self.item_list)에 추가해주세요.
        self.item_list.append("banana_slip")
        self.item_list.append("booster")

    def play_round(self):
        """
        - 게임 규칙의 [라운드 시작 전], [라운드 진행], [라운드 종료 후] 부분을 담당하는 함수입니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """

        #### [라운드 시작 전]
        # TODO (1) - 1: 트랙의 길이를 결정해 변수에 저장하고, 출력해주세요.
        track = random.randint(5, 30)
        print("이번 라운드의 트랙 길이는 {} km 입니다".format(track))
        # TODO (1) - 2: 5명의 플레이어에게 아이템을 랜덤하게 적용시키고, 적용된 아이템과 적용 후 플레이어의 속도를 출력해주세요.
        print("[아이템 적용]")
        k = 0;
        self.py_speed = []  # 플레이어 스피드 저장
        while k < 5:
            player = self.player_list[k]
            item = random.choice(self.item_list)
            if item == self.item_list[0]:
                comment = "때문에"
                emo = 'ㅜㅜ'
                self.round_speed = self.speed - random.randint(20, 40)
            else:
                comment = "덕분에"
                emo = '~~'
                self.round_speed = self.speed + random.randint(30, 60)
            print("Player", player, "는", item, comment, "시속", self.round_speed, "로 이번 트랙을 질주합니다! 화이팅", emo)
            self.py_speed.append((int)(self.round_speed))
            k += 1

        #### [라운드 진행] , [라운드 종료 후]
        # TODO (2) : 플레이어가 트랙을 도는 데 걸린 시간을 초 단위로 출력하고, 플레이어의 경기 기록에 추가해주세요. Player 클래스의 함수를 사용해야합니다.
        print("[경기 진행중...]")
        print("[라운드 결과]")
        k = 0;

        while k < 5:
            playernum = self.player_list[k]
            recode = track / (self.py_speed[k] / 3600)
            print("Player", playernum, " 의 주행 시간:", recode)
            self.record_list.append(recode)
            k += 1

    def game_result(self):
        """
        - 게임 규칙의 [게임 종료 후] 부분을 담당하는 함수입니다.
        - 1, 2, 3순위까지 플레이어의 이름과 합산기록을 출력합니다.
        - 동일 클래스의 game()에서 호출됩니다.
        - 파이썬의 sorted() 함수와 sort() 함수를 잘 이용하시면 편합니다. sorting key 등을 검색해보시기를 추천합니다.
        """
        # TODO : 사용자를 합산 기록 순으로 정렬하고, 상위 3명의 경기 기록 합산을 출력합니다.
        resultcount = 1
        count = 0
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        while count < 15:
            if (count % 5 == 0):
                a += self.record_list[count]
            elif (count % 5 == 1):
                b += self.record_list[count]
            elif (count % 5 == 2):
                c += self.record_list[count]
            elif (count % 5 == 3):
                d += self.record_list[count]
            elif (count % 5 == 4):
                e += self.record_list[count]
            count += 1
        i1 = 0
        self.list = [a, b, c, d, e]
        while i1 < 4:
            min = i1
            j1 = i1 + 1
            tmp = 0
            tmpname = ""
            while j1 < 5:
                if self.list[j1] <= self.list[min]:
                    min = j1
                j1 += 1

            tmp = self.list[i1]
            self.list[i1] = self.list[min]
            self.list[min] = tmp
            tmpname = self.player_list[i1]
            self.player_list[i1] = self.player_list[min]
            self.player_list[min] =tmpname


            i1 += 1

        while resultcount < 4:
            print(resultcount, "위: ", self.player_list[resultcount], "(총 주행 시간: ", self.list[resultcount], " 초)")
            resultcount += 1

    def game(self):
        """
        - 게임 운영을 위한 함수입니다.
        - 별도의 코드 작성이 필요 없습니다.
        """
        self.set_players()
        self.start_game()

        print("******************* 게임 시작 *******************")
        for i in range(3):
            print(f"============= ROUND {i + 1} =============")
            self.play_round()
            print()
        print()

        print("******************* 명예의 전당 *******************")
        self.game_result()


if __name__ == '__main__':
    """
      - 코드를 실행하는 부분입니다. 
      - 역시 별도의 코드 작성이 필요 없습니다. 
      """
    game = Game()
    game.game()
