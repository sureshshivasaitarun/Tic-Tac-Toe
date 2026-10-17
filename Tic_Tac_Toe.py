print("Welcome to Tic-Tac-Toe GAME")
table=["1","2","3","4","5","6","7",
       "8","9"]
def tablep(table):
    print(table[0],"|",table[1],"|",table[2])
    print("--+---+--")

    print(table[3],"|",table[4],"|",table[5])
    print("--+---+--")
    print(table[6],"|",table[7],"|",table[8])    
    return
X,O,C,V=0,0,0,0
S=((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
S1=[]
S2=[]
def ttt(table):
    global X,O,C,V,S,S1,S2
    tablep(table)
    if C == 0:
        if len(S1) == 5:
            print("DRAW MATCH")
            return
        X=int(input("Player 1 (X),choose a position (1-9): "))
        if table[X-1] == "X" or table[X-1] == "O":
            print("position already occupied")
            while table[X-1] == "X" or table[X-1] == "O":
                X=int(input("Player 1 (X),choose a position (1-9): "))
                table[X-1]="X"
                S1.append(X)
                for c in S:
                    if all(p in S1 for p in c):  
                        print(" X YOU WON")
                        tablep(table)
                        break
                else:
                    C=1
                    return ttt(table)
        elif table[X-1] not in ("X","O"):
            table[X-1]="X"
            S1.append(X)
            for c in S:
                if all(p in S1 for p in c):  
                    print("X YOU WON")
                    tablep(table)
                    break
            else:
                C=1
                return ttt(table)
    else:
        if len(S2) == 4:
            print("DRAW MATCH")
            return
        O=int(input(("Player 2 (O),choose a position (1-9): ")))
        if table[O-1] == "X" or table[O-1] == "O":
            print("position already occupied")
            while table[O-1] == "X" or table[X-1] == "O":
                O=int(input("Player 2 (O),choose a position (1-9): "))
                table[O-1]="O"
                S2.append(O)
                for c in S:
                    if all(p in S2 for p in c): 
                        print("O YOU WON")
                        tablep(table)
                else:
                    C=0
                ttt(table)
        elif table[O-1] != "X" or table[O-1] != "O":
                    table[O-1]="O"
                    S2.append(O)
                    for c in S:
                        if all(p in S2 for p in c): 
                            print("O YOU WON")
                            tablep(table)
                    else:
                        C=0
                    return ttt(table)
    return 
ttt(table)