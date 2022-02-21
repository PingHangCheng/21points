import random
import math
class Players():
    def __init__(self, name):
        self.name = name #玩家名字
        self.C_keyval =[] #手牌，因為有很多張，所以用list
        self.C_handCard = []
        self.C_point = 0 #用來計算目前玩家手牌的總點數  
    
    def show(self):
        print(f"玩家姓名：{self.name}")
        print(f"手牌:{self.C_handCard}")
        print(f"每張牌的key值:{self.C_keyval}")
        print(f"總點數:{self.C_point}\n")

    def drain(self, C_keyval):
        self.C_keyval.append(C_keyval) #知道這個數字代表哪一張牌？這張牌代表？？？
        self.NumCount()
        self.C_handCard.append(self.CardColor(C_keyval) + self.CardNum(C_keyval))

    def CardNum(self, C_keyval):    # 撲克牌數字
        numlist=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        num = C_keyval % 13
        if num==0: #若=0 代表num為13的倍數
            num=13
        return numlist[num-1]

    def CardColor(self, C_keyval): # 撲克牌花色 
        color = ["♠","♥","♦","♣"]
        while C_keyval > 52:#若有多副牌
            C_keyval -= 52
        colornum = int(C_keyval // 13)
        if C_keyval % 13 == 0: # x為13的倍數時,colornumc會多+1
            colornum -= 1
        return color[colornum]
    
    #i是指def CardNum的回傳值("A"~"K")，再轉換點數
    #i是整個list(整個手牌帶進，重新算點數),還是只算傳進來的那張牌，兩者皆可
    #如果是整個牌，則不需i，則是self.C_keyval，如果是一張牌，則是i，應為 def NumCount(self, i):
    #計算手牌點數，運用字典設定牌對應點數，A可做為1或11
    def NumCount(self):    
        tem_c_point = 0
        tem_list = []
        dic1 = {"A":11, "2":2, "3":3, "4":4 ,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10, "J":10, "Q":10, "K":10}
        dic2 = {"A":1, "2":2, "3":3, "4":4 ,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10, "J":10, "Q":10, "K":10}
        
        for i in self.C_keyval:
            card = self.CardNum(i)
            if card == "A":
                tem_list.append(card)
            else:
                tem_list.insert(0, card)

        for i in tem_list:
            if tem_c_point + 11 <= 21: 
                tem_c_point += dic1[i]
            else:
                tem_c_point += dic2[i]
            
        if tem_c_point > 21: #如果超過21點，就會歸零
            tem_c_point = 0
        
        self.C_point = tem_c_point #把暫時的點數放到正式的點數裏

#測試單一player
# john = Players("john")
# john.drain(26)
# john.drain(45)
# john.drain(14)
# john.show()




cards = [] #牌堆
numlen = []#排堆的長度
user = []
my_cards = [] #抽到的牌

def ChoiceCard() : #選擇幾副牌 & 塞入牌堆
    cards_num = math.ceil(len(user) / 3)
    numlen.append(len(str(52*cards_num)))
    for i in range(1,52*cards_num+1,+1): #牌堆塞入牌
        cards.append(i)
    random.shuffle(cards)

user.append(Players("John"))
user.append(Players("Mary"))
user.append(Players("Amos"))
user.append(Players("Henry"))

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
    temp =input('請輸入玩家ID，以","分割: ').split(",") #切割過後，會是一個list
    for i in temp:
        user.append(Players(i))

#gamename() #測試用

# for i in user: #測試用
#     i.show()    

   
def GameStart():
    # 第一輪底牌
    for i in user:
        #for j in range(2): #為了抽2張
            # i.drain(cards[0]) #選擇第一張 
            # cards.pop(0)  #抽完即把第一張從牌堆去除
            D = cards[0]
            D1 = cards[1]
            i.drain(D) #選擇第一張
            i.drain(D1)
            cards.remove(D)
            cards.remove(D1) 
            i.show()      

    # 第二輪抽牌
    for i in user:
        run = True #繼續抽牌
        while run:
            if i.C_point == 0:
                run = False
            else:    
                choose = input(f"{i.name}請選擇是否發牌？(1、叫牌 2、pass)")
                if choose == "1":
                    i.drain(cards[0]) 
                    cards.pop(0)
                    i.show()

                elif choose == "2":
                    run = False
                
                else:
                    print("請玩家僅輸入1或2")

def GameEnd():
    #製作排行榜
    prizelist = [] #存入字典
    for i in user:
        print(f"{i.name} 的點數: {i.C_point},牌組:{i.C_handCard}")
        #{"Num":1,"B":0}
        #{"Num":2,"B":-1}
        if prizelist == []:
            prizelist.append({"point":i.C_point, "name":[i.name]})
        else: #prizelist不是空的
            templist = [i['point'] for i in prizelist] #建立單純點數的list
            if i.C_point in templist:#如果i.C_point出現在 templist
                temp = templist.index(i.C_point)
                prizelist[temp]["name"].append(i.name)
            else: #如果點數i.C_point沒有出現在templist
                for j in templist:
                    if i.C_point > j:#假如C_point 大於 templist裡的點數
                        temp = templist.index(j)
                        prizelist.insert(temp, {"point":i.C_point, "name":[i.name]})
                        break
                    elif j == templist[-1]:#或i.Cpoint < templist[-1]假如C_point都小於templist裡的點數
                       prizelist.append({"point":i.C_point, "name":[i.name]}) 

        
            

    
    print("開始頒獎")
    for i in range(len(prizelist)):
        print(f"第{i+1}名 {prizelist[i]['point']}點 {prizelist[i]['name']}")
    # print(Leaderboard)




GameStart()



GameEnd()
print()


#程式從這邊開始

#選擇幾副撲克牌
# ChoiceCard()
  
#輸入ID  
#gamename() 
# name= ["Nephi","巧克力","香草","紅豆","椰子","楓","桂","可可","草莓"]

#選擇撲克牌
#GameStart()
# my_cards=[1,21,12,13,15,21,0,33,0]

#名次輸出
#GameEnd()