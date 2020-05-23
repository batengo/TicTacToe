zellen = list("_" * 9)
x_turn = True
counter_x = 0
counter_o = 0
zellen = [zellen[0:3], zellen[3:6], zellen[6:9]]
x_koordinate = 0
y_koordinate = 0


# horizontal
def check_row(char):
    for i in range(3):
        if zellen[i][0] == zellen[i][1] == zellen[i][2] == char:
            return True
            break
    else:
        return False


# vertikal
def check_col(char):
    for i in range(3):
        if zellen[0][i] == zellen[1][i] == zellen[2][i] == char:
            return True
            break
    else:
        return False


# diagonal
def check_dia(char):
    return char == zellen[0][0] == zellen[1][1] == zellen[2][2] or char == zellen[0][2] == zellen[1][1] == zellen[2][0]    


# eingegebene Koordinaten in zwei Variablen
def get_coordinates(): 
    global x_koordinate, y_koordinate
    try:
        koordinaten = input("Koordinaten eingeben: > ").split()
        x_koordinate, y_koordinate = int(koordinaten[0]), int(koordinaten[1])
        if not 1 <= x_koordinate <= 3 or not 1 <= y_koordinate <= 3:
            print("Coordinates should be from 1 to 3!")
            x_koordinate = 0
        else:
            print_coordinates(x_koordinate, y_koordinate)
    except:
       print("You should enter numbers!")


# Ausgabe des gegenwärtigen Spielfeldes
def print_table():
    print("-" * 9)
    for i in range(3):
        print("|", " ".join(zellen[i]), "|")
    print("-" * 9)


# Änderung des Spielfeldes gemäß eingegebener Koordinaten
def print_coordinates(x, y):
    global x_koordinate, x_turn
    index_höhe = [2, 1, 0]
    if zellen[index_höhe[y - 1]][x - 1] == "_":
        if x_turn:
            zellen[index_höhe[y - 1]][x - 1] = "X"
            x_turn = False
        else:
            zellen[index_höhe[y - 1]][x - 1] = "O"
            x_turn = True
        print_table()
        x_koordinate = 0
    else:
        print("This cell is occupied! Choose another one!")
        x_koordinate = 0
        get_coordinates()


# Analyse des Spielfeldes bezüglich der Gewinner
def print_analysis():
    if check_row("X") or check_col("X") or check_dia("X"):
        print("X wins")
    elif check_row("O") or check_col("O") or check_dia("O"):
        print("O wins")
    elif not "_" in zellen:
        print("Draw")

# Ist True, wenn einer gewonnen hat
is_finished = False

print_table()

while not is_finished:
    get_coordinates()
    is_finished = any([check_row("X"), check_col("X"), check_dia("X"), check_row("O"), check_col("O"), check_dia("O")]) or not ("_" in zellen[0] or "_" in zellen[1] or "_" in zellen[2])

print_analysis()
