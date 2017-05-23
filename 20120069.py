def rule1(BINGO) :
    for x in range(0,5) :
        if (BINGO[x][0]+BINGO[x][1]+BINGO[x][2]+BINGO[x][3]+BINGO[x][4]) == 5:
            return True;
    return False;

def rule2(BINGO):
    for x in range(0,5) :
        if (BINGO[0][x]+BINGO[1][x]+BINGO[2][x]+BINGO[3][x]+BINGO[4][x]) == 5:
            return True;
    return False;

def rule3(BINGO):
    count1 = 0
    for x in range(0,5) :
        if BINGO[x][x] == 1:
            count1 = count1 + 1 
    if count1 == 5 :
        return True;

    count1 = 0
    for x in range(0,5):
        if BINGO[x][4-x] == 1:
            count1 = count1 + 1
    if count1 == 5 :
        return True;
    return False;

def rule4(BINGO):
    if (BINGO[0][0] and BINGO[0][4] and BINGO[4][0] and BINGO[4][4]) == 1:
        return True;
    return False;    

row = 5
col = 5

BINGOGOGO = []
BINGO = []

T = int(input())
for t in range(0,T):

    BINGOGOGO = []
    BINGO = []

    for i in range(0, row):
        row_input = input().split()
        row_input = [int(j) for j in row_input]
        BINGOGOGO.append(row_input)

        if i == 2 :
            BINGO.append([0,0,1,0,0])
        else :
            BINGO.append([0]*5)
            
    input_numbers = input().split()
    input_numbers = [int(j) for j in input_numbers]

    count_of_input = 0
    for number in input_numbers:

        count_of_input = count_of_input + 1

        for x in range(0,5):
            for y in range(0,5):
                if number == BINGOGOGO[x][y]:
                    BINGO[x][y] = 1
                
        if rule1(BINGO) == True:
            print(count_of_input)
            break

        if rule2(BINGO) == True:
            print(count_of_input)
            break


        if rule3(BINGO) == True:
            print(count_of_input)
            break

        if rule4(BINGO) == True:
            print(count_of_input)
            break
