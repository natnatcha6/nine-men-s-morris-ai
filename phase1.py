import random

# ตัวกระดานตำแหน่งพิกัดต่างๆ
board = {
    "00": "X",
    "01": "X",
    "02": "X",
    "03": "X",
    "04": "X",
    "05": "X",
    "06": "X",
    "07": "X",
    "08": "X",
    "09": "X",
    "10": "X",
    "11": "X",
    "12": "X",
    "13": "X",
    "14": "X",
    "15": "X",
    "16": "X",
    "17": "X",
    "18": "X",
    "19": "X",
    "20": "X",
    "21": "X",
    "22": "X",
    "23": "X"
}

# พิกัดที่ต่อกัน3ตำแหน่งแล้วจะลบตัวฝั่งตรงข้ามได้
mill = {
    
    "00": [[board["09"], board["21"]], [board["01"], board["02"]]],
    "01": [[board["04"], board["07"]], [board["00"], board["02"]]],
    "02": [[board["14"], board["23"]], [board["00"], board["01"]]],
    "03": [[board["10"], board["18"]], [board["04"], board["05"]]],
    "04": [[board["01"], board["07"]], [board["03"], board["05"]]],
    "05": [[board["13"], board["20"]], [board["03"], board["04"]]],
    "06": [[board["11"], board["15"]], [board["07"], board["08"]]],
    "07": [[board["01"], board["04"]], [board["06"], board["08"]]],
    "08": [[board["12"], board["17"]], [board["06"], board["07"]]],
    "09": [[board["00"], board["21"]], [board["10"], board["11"]]],
    "10": [[board["03"], board["18"]], [board["09"], board["11"]]],
    "11": [[board["06"], board["15"]], [board["09"], board["10"]]],
    "12": [[board["08"], board["17"]], [board["13"], board["14"]]],
    "13": [[board["05"], board["20"]], [board["12"], board["14"]]],
    "14": [[board["02"], board["23"]], [board["12"], board["13"]]],
    "15": [[board["06"], board["11"]], [board["16"], board["17"]]],
    "16": [[board["19"], board["22"]], [board["15"], board["17"]]],
    "17": [[board["08"], board["12"]], [board["15"], board["16"]]],
    "18": [[board["03"], board["10"]], [board["19"], board["20"]]],
    "19": [[board["16"], board["22"]], [board["18"], board["20"]]],
    "20": [[board["05"], board["13"]], [board["18"], board["19"]]],
    "21": [[board["00"], board["09"]], [board["22"], board["23"]]],
    "22": [[board["16"], board["19"]], [board["21"], board["23"]]],
    "23": [[board["02"], board["14"]], [board["21"], board["22"]]]
}

#เช็คว่าแต่ละฝั่งมีเบี้ยเหลือเท่าไหร่บ้าง
playerPawn = {
    "1": 9,
    "2": 9
}

#เก็บจำนวนรอบ
round = 0
#เช็คว่าphase3เริ่มรึยัง
phase3StartFlag = False
#เช็คว่าphase3จบรึยัง
phase3EndFlag = False
#เช็คว่าเกมจบรึยัง
endGameFlag = False
#เช็คว่าผู้เล่นที่1เป็นคนเข้าphase3รึเปล่า
player1Phase3Flag = False

pawn = ["00", "01", "02", "03", "04", "05", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22","23"]

#ตำแหน่งที่เบี้ยเดินไปได้
movablePawn = {
    
    "00": ["09", "01"],
    "01": ["04", "00", "02"],
    "02": ["14", "01"],
    "03": ["10", "04"],
    "04": ["07", "01", "03", "05"],
    "05": ["04", "13"],
    "06": ["11", "07"],
    "07": ["04", "06", "08"],
    "08": ["12", "07"],
    "09": ["21", "00", "10"],
    "10": ["18", "03", "09", "11"],
    "11": ["15", "06", "10"],
    "12": ["17", "08", "13"],
    "13": ["20", "05", "12", "14"],
    "14": ["23", "02", "13"],
    "15": ["11", "16"],
    "16": ["19", "15", "17"],
    "17": ["12", "16"],
    "18": ["10", "19"],
    "19": ["22", "16", "18", "20"],
    "20": ["13", "19"],
    "21": ["09", "22"],
    "22": ["19", "21", "23"],
    "23": ["14", "22"]
}

#ฟังก์ชั่นสำหรับอัพเดทตัวในบอร์ดว่ามีตำแหน่งไหนใช้ไปแล้วบ้าง
def updateMill():
    global mill
    mill = {
        
        "00": [[board["09"], board["21"]], [board["01"], board["02"]]],
        "01": [[board["04"], board["07"]], [board["00"], board["02"]]],
        "02": [[board["14"], board["23"]], [board["00"], board["01"]]],
        "03": [[board["10"], board["18"]], [board["04"], board["05"]]],
        "04": [[board["01"], board["07"]], [board["03"], board["05"]]],
        "05": [[board["13"], board["20"]], [board["03"], board["04"]]],
        "06": [[board["11"], board["15"]], [board["07"], board["08"]]],
        "07": [[board["01"], board["04"]], [board["06"], board["08"]]],
        "08": [[board["12"], board["17"]], [board["06"], board["07"]]],
        "09": [[board["00"], board["21"]], [board["10"], board["11"]]],
        "10": [[board["03"], board["18"]], [board["09"], board["11"]]],
        "11": [[board["06"], board["15"]], [board["09"], board["10"]]],
        "12": [[board["08"], board["17"]], [board["13"], board["14"]]],
        "13": [[board["05"], board["20"]], [board["12"], board["14"]]],
        "14": [[board["02"], board["23"]], [board["12"], board["13"]]],
        "15": [[board["06"], board["11"]], [board["16"], board["17"]]],
        "16": [[board["19"], board["22"]], [board["15"], board["17"]]],
        "17": [[board["08"], board["12"]], [board["15"], board["16"]]],
        "18": [[board["03"], board["10"]], [board["19"], board["20"]]],
        "19": [[board["16"], board["22"]], [board["18"], board["20"]]],
        "20": [[board["05"], board["13"]], [board["18"], board["19"]]],
        "21": [[board["00"], board["09"]], [board["22"], board["23"]]],
        "22": [[board["16"], board["19"]], [board["21"], board["23"]]],
        "23": [[board["02"], board["14"]], [board["21"], board["22"]]]
    }

#เช็คว่าตำแหน่งที่เราลงไปเรียง3ตัวรึยัง
def checkMill(player, cdn):
    if mill[cdn][0].count(player) == 2 or mill[cdn][1].count(player) == 2:
        return True
    else:
        return False

#วางเบี้ย phase 1
def placePawn(player, cdn):
    board[cdn] = player
    updateMill()

#เช็คการเดิน phase 2 ว่าถูกต้องมั้ย
def move(player, st, end):
    while(True):
        print(end in movablePawn[st])
        if end in movablePawn[st] and board[end] == "X" and board[st] == player:
            movePawn(player, st, end)
            break
        else:
            print("Invalid movement please choose another set of starting and ending coordinate")
            st = input("starting point: ")
            end = input("ending point: ")

# เช็คการเดิน phase 3 ว่าถูกต้องมั้ย
def jump(player, st, end):
    while(True):
        if board[end] == "X":
            movePawn(player, st, end)
            break
        else:
            print("Invalid movement please choose another set of starting and ending coordinate")
            st = input("starting point: ")
            end = input("ending point: ")

#ฟังก์ชันการเดิน
def movePawn(player, st, end):
    board[st] = "X"
    board[end] = player
    updateMill()

#การลบตัว
def delete(i):
    boardOutput(board)
    print("You connected 3 straight point and can remove one of oppoents pawn!")
    while(True):
        cdn = input("Please input opponent's pawn cdn: ")
        if str(cdn) in board and board[cdn] == i:
            deletePawn(str(i), str(cdn))
            break
        else:
            print("Invalid cdn. Please use another cdn")

#ฟังก์ชันการลบตัว
def deletePawn(player, cdn):
    global phase3StartFlag
    global endGameFlag
    if board[cdn] == player:
        board[cdn] = "X"
        playerPawn[player] = playerPawn[player] - 1
        if playerPawn[player] == 3:
            phase3StartFlag = True
        elif playerPawn[player] == 2:
            endGameFlag = True
        print("Player pawn: ", playerPawn[player])
        return True
    else:
        return False

def autoDelete(player):
    boardOutput(board)
    print("You connected 3 straight point and can remove one of oppoents pawn!")
    while(True):
        cdn = randomPlace()
        if deletable(player, cdn):
            deletePawn(player, cdn)
            break

def randomPlace():
    return random.choice(list(board))

def randomMove(player):
    while(True):
        a = random.choice(list(board))
        if board[a] == player:
            b = random.choice(list(movablePawn[a]))
            break
    return a,b

def randomJump(player):
    while(True):
        a = random.choice(list(board))
        if board[a] == player:
            b = random.choice(list(board))
            if board[b] == "X":
                break
    return a,b


#เช็คว่าสามารถวางเบี้ยได้มั้ยใน phase 1
def placeable(player, cdn):
    if board[cdn] == "X":
        return True
    else:
        return False

#เช็คว่าสามารถเดินได้มั้ยใน phase 2
def movable(player, st, end):
    if end in movablePawn[st] and board[st] == player and board[end] == "X":
        return True
    else: 
        return False
#เช็คว่าลบได้มั้ย
def deletable(player, cdn):
    if board[cdn] == player:
        return True
    else:
        return False

#เช็คว่ากระโดดได้มั้ยใน phase 3
def jumpable(player, st , end):
    if board[st] == player and board[end] == "X":
        return True
    else:
        return False

#วาดกระดานออกมา
def boardOutput(board):
		
		print(board['00']+"(00)----------------------"+board['01']+"(01)----------------------"+board['02']+"(02)")
		print("|                           |                           |")
		print("|       "+board['03']+"(03)--------------"+board['04']+"(04)--------------"+board['05']+"(05)     |")
		print("|       |                   |                    |      |")
		print("|       |                   |                    |      |")
		print("|       |        "+board['06']+"(06)-----"+board['07']+"(07)-----"+board['08']+"(08)       |      |")
		print("|       |         |                   |          |      |")
		print("|       |         |                   |          |      |")
		print(board['09']+"(09)---"+board['10']+"(10)----"+board['11']+"(11)               "+board['12']+"(12)----"+board['13']+"(13)---"+board['14']+"(14)")
		print("|       |         |                   |          |      |")
		print("|       |         |                   |          |      |")
		print("|       |        "+board['15']+"(15)-----"+board['16']+"(16)-----"+board['17']+"(17)       |      |")
		print("|       |                   |                    |      |")
		print("|       |                   |                    |      |")
		print("|       "+board['18']+"(18)--------------"+board['19']+"(19)--------------"+board['20']+"(20)     |")
		print("|                           |                           |")
		print("|                           |                           |")
		print(board['21']+"(21)----------------------"+board['22']+"(22)----------------------"+board['23']+"(23)")
	
#เริ่มphase1
def autoPhase1():
    global round
    for round in range(9):
        print("round ",round+1)
        for i in range(2):
            boardOutput(board)
            while(True):
                cdn = randomPlace()
                if placeable(str(i), str(cdn)):
                    break
            placePawn(str(i+1), str(cdn))
            if checkMill(str(i+1), str(cdn)):
                if i == 0:
                    autoDelete("2")
                else:
                    autoDelete("1")
    print("This is the end of phase 1")

def phase1():
    global round
    for round in range(9):
        print("round ",round+1)
        for i in range(2):
            boardOutput(board)
            while(True):
                cdn = input("Please input cdn: ")
                if str(cdn) in board:
                    if board[str(cdn)] == 'X':
                        break
                    else:
                        print("The pawn has already placed on this cdn, please place on another cdn.")
            placePawn(str(i+1), str(cdn))
            if checkMill(str(i+1), str(cdn)):
                if i == 0:
                    delete("2")
                else:
                    delete("1")
    print("This is the end of phase 1")


#เริ่มphase2
def phase2():
    global round, phase3EndFlag, phase3StartFlag, player1Phase3Flag
    round += 1
    print("Welcome to Phase 2 of the game!")
    print("You can now move the pawn in the board next to their starting point.")
    print("Same rule applies.")
    while(True):
        round+=1
        print("round", round)
        for i in range(2):
            if player1Phase3Flag:
                player1Phase3Flag = False
                continue
            boardOutput(board)
            while(True):
                print("player ", i+1, " turn")
                st = input("Plase input starting point: ")
                end = input("Please input ending point: ")
                if str(st) in board and str(end) in board and board[st] == str(i+1) and board[end] == "X":
                    break
                else:
                    print("Invalid coordinate, please check your input.")
            move(str(i+1), str(st), str(end))
            if checkMill(str(i+1), str(end)):
                if i == 0:
                    delete("2")
                else: 
                    delete("1")
            if phase3StartFlag and phase3EndFlag == False:
                if i == 0:
                    phase3("2")
                    phase3EndFlag = True
                    break
                else:
                    print(i)
                    phase3("1")
                    phase3EndFlag = True  
                    player1Phase3Flag = True     
            elif endGameFlag:
                break
        if endGameFlag:
            break
    print("This game has ended!")
    print("Congrats to player ",i+1)

def autoPhase2():
    global round, phase3EndFlag, phase3StartFlag, player1Phase3Flag
    round += 1
    print("Welcome to Phase 2 of the game!")
    print("You can now move the pawn in the board next to their starting point.")
    print("Same rule applies.")
    while(True):
        round+=1
        print("round", round)
        for i in range(2):
            if player1Phase3Flag:
                player1Phase3Flag = False
                continue
            boardOutput(board)
            while(True):
                st,end = randomMove(str(i+1))
                print(st,end)
                if movable(str(i+1), str(st), str(end)):
                    break
            move(str(i+1), str(st), str(end))
            if checkMill(str(i+1), str(end)):
                if i == 0:
                    autoDelete("2")
                else: 
                    autoDelete("1")
            if phase3StartFlag and phase3EndFlag == False:
                if i == 0:
                    autoPhase3("2")
                    phase3EndFlag = True
                    break
                else:
                    print(i)
                    autoPhase3("1")
                    phase3EndFlag = True  
                    player1Phase3Flag = True    
            elif endGameFlag:
                break
        if endGameFlag:
            break
    boardOutput(board)
    print("This game has ended!")
    print("Congrats to player ",i+1)

#เริ่มphase 3พร้อมบอกว่า playerคนไหนเข้ามา
def phase3(player):
    global round
    round += 1
    print("Welcome to Phase 3 of the game!")
    print("You can now move the pawn in the board in any coordinate that's still an empty spot for one move.")
    print("Same rule applies.")
    print("round", round)
    boardOutput(board)
    while(True):
        st = input("Plase input starting point: ")
        end = input("Please input ending point: ")
        if str(st) in board and str(end) in board and board[st] == str(player) and board[end] == "X":
            break
        else:
            print("Invalid coordinate, please check your input.")
    jump(str(player), str(st), str(end))
    if checkMill(str(player), str(end)):
        if player == "1":
            delete("2")
        else: 
            delete("1")
            
def autoPhase3(player):
    global round
    round += 1
    print("Welcome to Phase 3 of the game!")
    print("You can now move the pawn in the board in any coordinate that's still an empty spot for one move.")
    print("Same rule applies.")
    print("round", round)
    boardOutput(board)
    while(True):
        st,end = randomJump(player)
        if str(st) in board and str(end) in board and board[st] == str(player) and board[end] == "X":
            break
    jump(str(player), str(st), str(end))
    if checkMill(str(player), str(end)):
        if player == "1":
            autoDelete("2")
        else: 
            autoDelete("1")


def main():
    # phase1()
    # phase2()
    autoPhase1()
    autoPhase2()

main()
            
