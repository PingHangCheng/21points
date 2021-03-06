import random
import math


class players:
    def __init__(self, name):
        self.name = name
        self.C_keyval = []  # 因為有很多張，所以用list
        self.C_handCard = []
        self.C_point = 0  # 用來計算目前玩家手牌的的總點數

    def show(self):
        print(f"玩家姓名:{self.name}")
        print(f"手牌:{self.C_handCard}")
        print(f"每張牌的key值:{self.C_keyval}")
        print(f"總點數:{self.C_point}\n")

    def drain(self, C_keyval):
        self.C_keyval.append(C_keyval)
        self.NumCount()
        self.C_handCard.append(self.CardColor(C_keyval)+self.CardNum(C_keyval))

    def CardNum(self, C_keyval):    # 撲克牌數字
        numlist = ["A", "2", "3", "4", "5", "6",
                   "7", "8", "9", "10", "J", "Q", "K"]
        num = C_keyval % 13
        if num == 0:  # 若=0 代表num為13的倍數
            num = 13
        return numlist[num-1]

    def CardColor(self, C_keyval):  # 撲克牌花色
        color = ["♠", "♥", "♦", "♣"]
        while C_keyval > 52:  # 若有多副牌
            C_keyval -= 52
        colornum = int(C_keyval // 13)
        if C_keyval % 13 == 0:  # C_keyval為13的倍數時,colornumc會多+1
            colornum -= 1
        return color[colornum]

    def NumCount(self):  # 傳進來的i可能是傳進來的牌
        # 計算手牌點數，運用"字典"設定牌對應點數，A可做為1或11
        tem_C_point = 0
        tem_list = []

        dic1 = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
        dic2 = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

        for i in self.C_keyval:
            card = self.CardNum(i)
            if card == "A":
                tem_list.append(card)
            else:
                tem_list.insert(0, card)

        for i in tem_list:
            if tem_C_point + 11 <= 21:
                tem_C_point += dic1[i]
            else:
                tem_C_point += dic2[i]

        if tem_C_point > 21:  # 如果超過21點就歸零
            tem_C_point = 0
        self.C_point = tem_C_point  # 把暫時的點數放到正式的點數裡

# john = players("john")
# john.drain(30)
# john.drain(50)
# john.drain(14)
# john.show()


cards = []  # 牌堆
numlen = []  # 排堆的長度
user = []
my_cards = []  # 抽到的牌


def ChoiceCard():  # 選擇幾副牌 & 塞入牌堆
    cards_num = math.ceil(len(user)/3)
    numlen.append(len(str(52*cards_num)))
    for i in range(1, 52*cards_num+1, +1):  # 牌堆塞入牌
        cards.append(i)
    random.shuffle(cards)


user.append(players("John"))
user.append(players("Mary"))
user.append(players("Amos"))
user.append(players("Henry"))

ChoiceCard()
print(cards)


# def ColorAndNumList(x): #展示手牌list
#     list=[]
#     for i in range(len(my_cards[x])):
#         list.append(str(CardColor(my_cards[x][i]))+str(CardNum(my_cards[x][i])))
#     return list

# def Drain(i,x): #抽排
#     cards_num = len(cards)
#     num = cards[x-1]
#     cards.remove(num) #一進一出,總牌數不變
#     if i>-1:
#         my_cards[i].append(num)
#     else:
#         my_cards.append([num])
#     # 輸出
#     return (f"抽出: {CardColor(num)}{CardNum(num):2}")

def gamename():
    temp = input('請輸入玩家ID，以","分割: ').split(",")  # 切割過會是list
    for i in temp:
        user.append(players(i))

# gamename() 測試用
# for i in user:
#     i.show()


def GameStart():
    # 第一輪底牌
    # 方法一
    # for i in user:
    #     for j in range(2):#為了抽2張牌
    #         #方法a
    #         # i.drain(cards[0]) #選擇第一張牌
    #         # cards.pop(0) #刪除選擇的第一張牌
    #         #方法b
    #         i.drain(cards[0])
    #         cards.remove(cards[0])

    # 方法二
    for i in user:
        D = cards[0]
        D1 = cards[1]
        i.drain(D)
        i.drain(D1)
        cards.remove(D)
        cards.remove(D1)  # ?為什麼不是D，因為要抽的牌已存在變數D及D1
        i.show()
    # 第二輪抽牌
    for i in user:
        run = True  # 繼續抽牌
        while run:
            if i.C_point != 0:
                choose = input(f"{i.name}請選擇是否發牌？(1、叫牌 2、pass)")
                if choose == "1":
                    i.drain(cards[0])  # 選擇一張牌
                    cards.pop(0)
                    i.show()

                elif choose == "2":
                    run = False
                else:
                    print("請玩家僅輸入1或2")
            else:
                run = False


GameStart()
#print()


def GameEnd():
    # 製作排行榜
    # prizelist可為字典或二維陣列
    '''
    如果用字典型態處理大量相似的資料, 建議統一key值
    {"Num":1, "B":0}
    {"Num":2, "B":-1}
    '''
    prizelist = []  # 存入字典
    for i in user:
        print(f"{i.name}的點數:{i.C_point},牌組：{i.C_handCard}")
        if prizelist == []:
            prizelist.append({"point": i.C_point, "name": [i.name]}) #{point:21, name:XXX}
        else:  #prizelist不是空的
            templist = [i['point'] for i in prizelist] #建立單純點數的list
            if i.C_point in templist:#點數一樣時
                temp = templist.index(i.C_point)
                prizelist[temp]['name'].append(i.name)
            else: #點數沒有出現過的狀況
                for j in templist:
                    if i.C_point > j:#新的點數較大時
                        #templist是大至小排序，如：[5,3,1]如果找到，就break否則演變依序為
                        #[6,5,3,1][6,6,5,3,1][6,6,5,3,1]才不會一直將同樣的值加進來
                        temp = templist.index(j)
                        prizelist.insert(temp, {"point": i.C_point, "name": [i.name]})
                        break
                    elif j == templist[-1]: #新的點數較小時，j == templist[-1]每個都比一次
                        #templist[-1]指直接抓templist最後一個
                        #或i.C_point < templist[-1](較佳寫法，因為直接與最後一個比庵)假如C_point都小於templist裡的點數
                        prizelist.append({"point": i.C_point, "name": [i.name]})

            


    #print("開始頒獎")

    # print(Leaderboard)

GameEnd()
#print()
# 程式從這邊開始

# 選擇幾副撲克牌
# ChoiceCard()

# 輸入ID
# gamename()
# name= ["Nephi","巧克力","香草","紅豆","椰子","楓","桂","可可","草莓"]

# 選擇撲克牌
# GameStart()
# my_cards=[1,21,12,13,15,21,0,33,0]

# 名次輸出
# GameEnd()
