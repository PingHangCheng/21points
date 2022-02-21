import random
import math 
class players: 
    def __init__(self,name): 
        self.name = name 
        self.C_keyval = [] #因為有很多張，所以用list 
        self.C_handCard = [] 
        self.C_point = 0 #用來計算目前玩家手牌的的總點數 

    def show(self):
        print(f"玩家姓名:{self.name}")
        print(f"手牌:{self.C_handCard}") 
        print(f"每張牌的key值:{self.C_keyval}") 
        print(f"總點數:{self.C_point}") 
        
        
    def drain(self,C_keyval): 
        self.C_keyval.append(C_keyval)
        self.NumCount()
        self.C_handCard.append(self.CardColor(C_keyval)+self.CardNum(C_keyval))
        
    def CardNum(self,C_keyval):    # 撲克牌數字
        numlist=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        num = C_keyval%13
        if num==0: #若=0 代表num為13的倍數
            num=13
        return numlist[num-1]

    def CardColor(self,C_keyval): # 撲克牌花色 
        color = ["♠","♥","♦","♣"]
        while C_keyval > 52:#若有多副牌
            C_keyval -= 52
        colornum = int(C_keyval // 13)
        if C_keyval % 13 == 0: # C_keyval為13的倍數時,colornumc會多+1
            colornum -= 1
        return color[colornum]
    
    def NumCount(self): #傳進來的i可能是傳進來的牌
    #計算手牌點數，運用"字典"設定牌對應點數，A可做為1或11
        tem_C_point = 0 
        tem_list = [] 
        
        dic1 = {"A":11,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}
        dic2 = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}
        
        for i in self.C_keyval: 
            card = self.CardNum(i)
            if card == "A": 
                tem_list.append(card)
            else: 
                tem_list.insert(0,card)
            
        for i in tem_list:
            if tem_C_point + 11 <= 21:
                tem_C_point += dic1[i]
            else: 
                tem_C_point += dic2[i]
            
        if tem_C_point > 21: #如果超過21點就歸零
            tem_C_point = 0 
        self.C_point = tem_C_point #把暫時的點數放到正式的點數裡
            
# john = players("john")
# john.drain(30)
# john.drain(50)
# john.drain(14)
# john.show()




cards = [] #牌堆
numlen = []#排堆的長度
user = []
my_cards = [] #抽到的牌




def ChoiceCard() : #選擇幾副牌 & 塞入牌堆
    cards_num = math.ceil(len(user)/3 )
    numlen.append(len(str(52*cards_num)))
    for i in range(1,52*cards_num+1,+1): #牌堆塞入牌
        cards.append(i)
    random.shuffle(cards)


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
    temp =input('請輸入玩家ID，以","分割: ').split(",") #切割過會是list
    for i in temp: 
        user.append(players(i))

# gamename() 測試用     
# for i in user: 
#     i.show()


   
def GameStart():
    # 第一輪底牌
    for i in user:
        i.drain(cards[0])
        cards.pop(0)
        i.show()

    # 第二輪抽牌
    for i in user:
        run = True
        while run:
            print(f"{i.name}")
            answer = input("請選擇是否發牌？(1、叫牌 2、pass)")
            if answer == 1:
                i.drain(cards[0])
                cards.pop(0)
            elif answer == 2:
                run = False
            else:
                run = False

def GameEnd():
    #製作排行榜
    pass
    #print("開始頒獎")

    # print(Leaderboard)

#程式從這邊開始
gamename()
ChoiceCard() 
print(cards)

GameStart()

print()  
#選擇幾副撲克牌
# ChoiceCard()
  
#輸入ID  
# gamename() 
# name= ["Nephi","巧克力","香草","紅豆","椰子","楓","桂","可可","草莓"]

#選擇撲克牌
# GameStart()
# my_cards=[1,21,12,13,15,21,0,33,0]

#名次輸出
# GameEnd()