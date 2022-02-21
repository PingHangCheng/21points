import random
cards = [] #牌堆
numlen = []#排堆的長度
name = []
my_cards = [] #抽到的牌

def ChoiceCard() : #選擇幾副牌 & 塞入牌堆
    cards_num = int(input("玩幾副撲克牌? : "))
    numlen.append(len(str(52*cards_num)))
    for i in range(1,52*cards_num+1,+1): #牌堆塞入牌
        cards.append(i)
    random.shuffle(cards)
def CardNum(x):    # 撲克牌數字
    numlist=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    num = x%13
    if num==0: #若=0 代表num為13的倍數
        num=13
    return numlist[num-1]

def CardColor(x): # 撲克牌花色 
    color = ["♠","♥","♦","♣"]
    while x > 52:#若有多副牌
        x -= 52
    colornum = int(x // 13)
    if x % 13 == 0: # x為13的倍數時,colornumc會多+1
        colornum -= 1
    return color[colornum]

def ColorAndNumList(x): #展示手牌list
    list=[]
    for i in range(len(my_cards[x])):
        list.append(str(CardColor(my_cards[x][i]))+str(CardNum(my_cards[x][i])))
    return list

def Drain(i,x): #抽排
    cards_num = len(cards)
    num = cards[x-1]
    cards.remove(num) #一進一出,總牌數不變
    if i>-1:
        my_cards[i].append(num)
    else:
        my_cards.append([num])
    # 輸出  
    return (f"抽出: {CardColor(num)}{CardNum(num):2}")

def gamename():
    temp =input('請輸入玩家ID，以","分割: ').split(",")
    name.extend(temp)
   
def GameStart():
    # 第一輪底牌
    pass

    # 第二輪抽牌


def NumCount(i):
    #計算手牌點數，運用字典設定牌對應點數，A可做為1或11
    pass
def GameEnd():
    #製作排行榜
    pass
    print("開始頒獎")

    # print(Leaderboard)

#程式從這邊開始

#選擇幾副撲克牌
ChoiceCard()
  
#輸入ID  
gamename() 
# name= ["Nephi","巧克力","香草","紅豆","椰子","楓","桂","可可","草莓"]

#選擇撲克牌
GameStart()
# my_cards=[1,21,12,13,15,21,0,33,0]

#名次輸出
GameEnd()