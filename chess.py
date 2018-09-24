def Board(dict):
    print('')
    print(str(dict['A8''']) + '|' + str(dict['B8']) + '|' + str(dict['C8']) + '|' + str(dict['D8']) + '|' + str(dict['E8']) + '|' + str(dict['F8']) + '|' + str(dict['G8']) + '|' + str(dict['H8']) + '\n'\
        + '--- --- --- --- --- --- --- ---\n'\
        + str(dict['A7']) + '|' + str(dict['B7']) + '|' + str(dict['C7']) + '|' + str(dict['D7']) + '|' + str(dict['E7']) + '|' + str(dict['F7']) + '|' + str(dict['G7']) + '|' + str(dict['H7']) + '\n'\
        + '--- --- --- --- --- --- --- ---\n'\
        + str(dict['A6']) + '|' + str(dict['B6']) + '|' + str(dict['C6']) + '|' + str(dict['D6']) + '|' + str(dict['E6']) + '|' + str(dict['F6']) + '|' + str(dict['G6']) + '|' + str(dict['H6']) + '\n'\
        + '--- --- --- --- --- --- --- ---\n'\
        + str(dict['A5']) + '|' + str(dict['B5']) + '|' + str(dict['C5']) + '|' + str(dict['D5']) + '|' + str(dict['E5']) + '|' + str(dict['F5']) + '|' + str(dict['G5']) + '|' + str(dict['H5']) + '\n'\
        + '--- --- --- --- --- --- --- ---\n'\
        + str(dict['A4']) + '|' + str(dict['B4']) + '|' + str(dict['C4']) + '|' + str(dict['D4']) + '|' + str(dict['E4']) + '|' + str(dict['F4']) + '|' + str(dict['G4']) + '|' + str(dict['H4']) + '\n'\
        + '--- --- --- --- --- --- --- ---\n'\
        + str(dict['A3']) + '|' + str(dict['B3']) + '|' + str(dict['C3']) + '|' + str(dict['D3']) + '|' + str(dict['E3']) + '|' + str(dict['F3']) + '|' + str(dict['G3']) + '|' + str(dict['H3']) + '\n'\
        + '--- --- --- --- --- --- --- ---\n'\
        + str(dict['A2']) + '|' + str(dict['B2']) + '|' + str(dict['C2']) + '|' + str(dict['D2']) + '|' + str(dict['E2']) + '|' + str(dict['F2']) + '|' + str(dict['G2']) + '|' + str(dict['H2']) + '\n'\
        + '--- --- --- --- --- --- --- ---\n'\
        + str(dict['A1']) + '|' + str(dict['B1']) + '|' + str(dict['C1']) + '|' + str(dict['D1']) + '|' + str(dict['E1']) + '|' + str(dict['F1']) + '|' + str(dict['G1']) + '|' + str(dict['H1']) + '\n')


# abstract Piece Class
class Piece():
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.previousposition = '   '
        self.previouspiece = '   '
    def deletePiece(self, piece):
        boarddict[self.position] = piece.name
        del self
    def checkNewPosition(self, position):
        if boarddict[position] == '   ':
            self.previouspiece = boarddict[position]
            boarddict[self.position] = '   '
            boarddict[position] = self.name
            self.previousposition = self.position
            self.position = position
            return True
        elif boarddict[position][0] == 'B':
            if self.name[0] == 'W':
                for i in range(32):
                    if list[i].position == position:
                        list[i].position = '  '
                        list[i].previousposition = position
                        list[i].previouspiece = list[i].name
                    else:
                        list[i].previousposition = list[i].position
                        list[i].previouspiece = list[i].name
                self.previouspiece = boarddict[position]
                boarddict[self.position] = '   '
                boarddict[position] = self.name
                self.previousposition = self.position
                self.position = position
                return True
            else:
                print('Invalid Move 1')
                return False
        elif boarddict[position][0] == 'W':
            if self.name[0] == 'B':
                for i in range(32):
                    if list[i].position == position:
                        list[i].position = '  '
                        list[i].previousposition = position
                        list[i].previouspiece = list[i].name
                    else:
                        list[i].previousposition = list[i].position
                        list[i].previouspiece = list[i].name
                self.previouspiece = boarddict[position]
                boarddict[self.position] = '   '
                boarddict[position] = self.name
                self.previousposition = self.position
                self.position = position
                return True
            else:
                print('Invalid Move 2')
                return False

    def undoMove(self):
        # only able to undo 1 move
        for i in range(32):
            if list[i].previousposition == self.position:
                list[i].position = list[i].previousposition
                list[i].previousposition = '  '
                self.previouspiece = list[i].name
                list[i].previouspiece = self.name
        boarddict[self.position] = self.previouspiece
        boarddict[self.previousposition] = self.name
        x = self.position
        self.position = self.previousposition
        self.previousposition = x

class Rook(Piece):
    def move(self, position):
        dictkeys = boarddict.keys()
        keylist = []
        keylist.extend(iter(dictkeys))
        numInKeyList = 0
        if position in keylist:
            n = 0
            for s in keylist:
                if s == position:
                    numInKeyList = n

                n += 1

            if self.position[0] == position[0]:
                flag = True
                x = int(self.position[1]) - int(position[1])
                if x > 1:
                    for i in range(1, x):
                        if boarddict[keylist[numInKeyList - (8*i)]] != '   ':
                            flag = False
                    if flag:
                        if self.checkNewPosition(position):
                            return True
                    else:
                        print('Invalid Move 3')
                elif x < -1:
                    x = abs(x)
                    for i in range(1, x):
                        if boarddict[keylist[numInKeyList + (8*i)]] != '   ':
                            flag = False
                    if flag:
                        if self.checkNewPosition(position):
                            return True
                    else:
                        print('Invalid Move 4')
                elif x == 1 or x == -1:
                    if self.checkNewPosition(position):
                        return True
                else:
                    print('Invalid Move 5')

            elif self.position[1] == position[1]:
                flag = True
                x = ord(self.position[0]) - ord(position[0])
                if x > 1:
                    for i in range(1, x):
                        if boarddict[keylist[numInKeyList + i]] != '   ':
                            flag = False
                    if flag:
                        if self.checkNewPosition(position):
                            return True
                    else:
                        print('Invalid Move 6')
                elif x < -1:
                    x = abs(x)
                    for i in range(1, x):
                        if boarddict[keylist[numInKeyList - i]] != '   ':
                            flag = False
                    if flag:
                        if self.checkNewPosition(position):
                            return True
                    else:
                        print('Invalid Move 7')
                elif x == 1 or x == -1:
                    if self.checkNewPosition(position):
                        return True
                else:
                    print('Invalid Move 8')
            else:
                print('Invalid Move 9')

        else:
            print('Invalid Move 10')

    def attackablePositions(self):
        if self.position == '  ':
            return []
        attackablePositionsList = []
        dictkeys = boarddict.keys()
        keylist = []
        keylist.extend(iter(dictkeys))
        numInKeyList = 0
        if self.position in keylist:
            n = 0
            for s in keylist:
                if s == self.position:
                    numInKeyList = n
                n += 1
        x = ord(self.position[0]) - ord('A')
        if x > 0:
            for i in range(1, x+1):
                if boarddict[keylist[numInKeyList - i]] == '   ':
                    attackablePositionsList.append(keylist[numInKeyList - i])
                elif self.name[0] == 'W' and boarddict[keylist[numInKeyList - i]][0] == 'B':
                    attackablePositionsList.append(keylist[numInKeyList - i])
                    break
                elif self.name[0] == 'B' and boarddict[keylist[numInKeyList - i]][0] == 'W':
                    attackablePositionsList.append(keylist[numInKeyList - i])
                    break
                else:
                    break
        x2 = ord('H') - ord(self.position[0])
        if x2 > 0:
            for i in range(1, x2+1):
                if boarddict[keylist[numInKeyList + i]] == '   ':
                    attackablePositionsList.append(keylist[numInKeyList + i])
                elif self.name[0] == 'W' and boarddict[keylist[numInKeyList + i]][0] == 'B':
                    attackablePositionsList.append(keylist[numInKeyList + i])
                    break
                elif self.name[0] == 'B' and boarddict[keylist[numInKeyList + i]][0] == 'W':
                    attackablePositionsList.append(keylist[numInKeyList + i])
                    break
                else:
                    break

        y = 8 - int(self.position[1])
        if y > 0:
            for i in range(1, y+1):
                if boarddict[keylist[numInKeyList - (8*i)]] == '   ':
                    attackablePositionsList.append(keylist[numInKeyList - (8*i)])
                elif self.name[0] == 'W' and boarddict[keylist[numInKeyList - (8*i)]][0] == 'B':
                    attackablePositionsList.append(keylist[numInKeyList - (8*i)])
                    break
                elif self.name[0] == 'B' and boarddict[keylist[numInKeyList - (8*i)]][0] == 'W':
                    attackablePositionsList.append(keylist[numInKeyList - (8*i)])
                    break
                else:
                    break
        y2 = int(self.position[1]) - 1
        if y2 > 0:
            for i in range(1, y2+1):
                if boarddict[keylist[numInKeyList + (8*i)]] == '   ':
                    attackablePositionsList.append(keylist[numInKeyList + (8*i)])
                elif self.name[0] == 'W' and boarddict[keylist[numInKeyList + (8*i)]][0] == 'B':
                    attackablePositionsList.append(keylist[numInKeyList + (8*i)])
                    break
                elif self.name[0] == 'B' and boarddict[keylist[numInKeyList + (8*i)]][0] == 'W':
                    attackablePositionsList.append(keylist[numInKeyList + (8*i)])
                    break
                else:
                    break
        return attackablePositionsList

class Bishop(Piece):
    def move(self, position):
        dictkeys = boarddict.keys()
        keylist = []
        keylist.extend(iter(dictkeys))
        numInKeyList = 0
        if position in keylist:
            n = 0
            for s in keylist:
                if s == position:
                    numInKeyList = n

                n += 1

            x = ord(self.position[0]) - ord(position[0])
            y = int(self.position[1]) - int(position[1])

            if abs(x) == abs(y):
                flag = True
                if abs(x) == 1:
                    if self.checkNewPosition(position):
                        return True
                elif position[0] > self.position[0] and position[1] > self.position[1]:
                    for i in range(1, abs(x)):
                        if boarddict[keylist[numInKeyList + (7 * i)]] != '   ':
                            flag = False
                    if flag:
                        if self.checkNewPosition(position):
                            return True
                    else:
                        print('Invalid Move 11')

                elif position[0] < self.position[0] and position[1] > self.position[1]:
                    for i in range(1, abs(x)):
                        if boarddict[keylist[numInKeyList + (9 * i)]] != '   ':
                            flag = False
                    if flag:
                        if self.checkNewPosition(position):
                            return True
                    else:
                        print('Invalid Move 12')

                elif position[0] < self.position[0] and position[1] < self.position[1]:
                    for i in range(1, abs(x)):
                        if boarddict[keylist[numInKeyList - (7 * i)]] != '   ':
                            flag = False
                    if flag:
                        if self.checkNewPosition(position):
                            return True
                    else:
                        print('Invalid Move 13')

                elif position[0] > self.position[0] and position[1] < self.position[1]:
                    for i in range(1, abs(x)):
                        if boarddict[keylist[numInKeyList - (9 * i)]] != '   ':
                            flag = False
                    if flag:
                        if self.checkNewPosition(position):
                            return True
                    else:
                        print('Invalid Move 14')
            else:
                print('Invalid Move 15')
        else:
            print('Invalid Move 16')
    def attackablePositions(self):
        if self.position == '  ':
            return []
        attackablePositionsList = []
        dictkeys = boarddict.keys()
        keylist = []
        keylist.extend(iter(dictkeys))
        numInKeyList = 0
        if self.position in keylist:
            n = 0
            for s in keylist:
                if s == self.position:
                    numInKeyList = n
                n += 1

        for i in range(1, 8):
            if (numInKeyList - (7 * i)) >= 0:
                if boarddict[keylist[numInKeyList - (7 * i)]] == '   ':
                    attackablePositionsList.append(keylist[numInKeyList - (7 * i)])
                    if keylist[numInKeyList - (7 * i)][0] == 'H' or keylist[numInKeyList - (7 * i)][1] == '8':
                        break
                elif self.name[0] == 'W' and boarddict[keylist[numInKeyList - (7 * i)]][0] == 'B':
                    attackablePositionsList.append(keylist[numInKeyList - (7 * i)])
                    break
                elif self.name[0] == 'B' and boarddict[keylist[numInKeyList - (7 * i)]][0] == 'W':
                    attackablePositionsList.append(keylist[numInKeyList - (7 * i)])
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if (numInKeyList + (7*i)) < 64:
                if boarddict[keylist[numInKeyList + (7*i)]] == '   ':
                    attackablePositionsList.append(keylist[numInKeyList + (7*i)])
                    if keylist[numInKeyList + (7 * i)][0] == 'A' or keylist[numInKeyList + (7 * i)][1] == '1':
                        break
                elif self.name[0] == 'W' and boarddict[keylist[numInKeyList + (7*i)]][0] == 'B':
                    attackablePositionsList.append(keylist[numInKeyList + (7*i)])
                    break
                elif self.name[0] == 'B' and boarddict[keylist[numInKeyList + (7*i)]][0] == 'W':
                    attackablePositionsList.append(keylist[numInKeyList + (7*i)])
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            if (numInKeyList - (9*i)) >= 0:
                if boarddict[keylist[numInKeyList - (9*i)]] == '   ':
                    attackablePositionsList.append(keylist[numInKeyList - (9*i)])
                    if keylist[numInKeyList - (9 * i)][0] == 'A' or keylist[numInKeyList - (9 * i)][1] == '8':
                        break
                elif self.name[0] == 'W' and boarddict[keylist[numInKeyList - (9*i)]][0] == 'B':
                    attackablePositionsList.append(keylist[numInKeyList - (9*i)])
                    break
                elif self.name[0] == 'B' and boarddict[keylist[numInKeyList - (9*i)]][0] == 'W':
                    attackablePositionsList.append(keylist[numInKeyList - (9*i)])
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            if (numInKeyList + (9*i)) < 64:
                if boarddict[keylist[numInKeyList + (9*i)]] == '   ':
                    attackablePositionsList.append(keylist[numInKeyList + (9*i)])
                    if keylist[numInKeyList + (9 * i)][0] == 'H' or keylist[numInKeyList + (9 * i)][1] == '1':
                        break
                elif self.name[0] == 'W' and boarddict[keylist[numInKeyList + (9*i)]][0] == 'B':
                    attackablePositionsList.append(keylist[numInKeyList + (9*i)])
                    break
                elif self.name[0] == 'B' and boarddict[keylist[numInKeyList + (9*i)]][0] == 'W':
                    attackablePositionsList.append(keylist[numInKeyList + (9*i)])
                    break
                else:
                    break
            else:
                break

        return attackablePositionsList

class Knight(Piece):
    def move(self, position):
        dictkeys = boarddict.keys()
        keylist = []
        keylist.extend(iter(dictkeys))

        if position in keylist:

            x = ord(self.position[0]) - ord(position[0])
            y = int(self.position[1]) - int(position[1])

            if abs(x) == 1:
                if abs(y) == 2:
                    if self.checkNewPosition(position):
                        return True
            elif abs(x) == 2:
                if abs(y) == 1:
                    if self.checkNewPosition(position):
                        return True
            else:
                print('Invalid Move 17')
        else:
            print('Invalid Move 18')

    def attackablePositions(self):
        if self.position == '  ':
            return []
        attackablePositionsList = []
        dictkeys = boarddict.keys()
        keylist = []
        keylist.extend(iter(dictkeys))
        numInKeyList = 0

        if self.position in keylist:
            n = 0
            for s in keylist:
                if s == self.position:
                    numInKeyList = n
                n += 1

        positions = [-15, -6, 10, 17, 15, 6, -10, -17]
        for i in positions:
            if 0 <= numInKeyList + i < 64:
                if abs(ord(self.position[0]) - ord(keylist[numInKeyList + i][0])) == 1:
                    if abs(int(self.position[1]) - int(keylist[numInKeyList + i][1])) == 2:
                        if boarddict[keylist[numInKeyList + i]] == '   ':
                            attackablePositionsList.append(keylist[numInKeyList + i])
                        elif self.name[0] == 'W' and boarddict[keylist[numInKeyList + i]][0] == 'B':
                            attackablePositionsList.append(keylist[numInKeyList + i])
                        elif self.name[0] == 'B' and boarddict[keylist[numInKeyList + i]][0] == 'W':
                            attackablePositionsList.append(keylist[numInKeyList + i])

                elif abs(ord(self.position[0]) - ord(keylist[numInKeyList + i][0])) == 2:
                    if abs(int(self.position[1]) - int(keylist[numInKeyList + i][1])) == 1:
                        if boarddict[keylist[numInKeyList + i]] == '   ':
                            attackablePositionsList.append(keylist[numInKeyList + i])
                        elif self.name[0] == 'W' and boarddict[keylist[numInKeyList + i]][0] == 'B':
                            attackablePositionsList.append(keylist[numInKeyList + i])
                        elif self.name[0] == 'B' and boarddict[keylist[numInKeyList + i]][0] == 'W':
                            attackablePositionsList.append(keylist[numInKeyList + i])


        return attackablePositionsList

class Queen(Piece):
    def move(self, position):
        dictkeys = boarddict.keys()
        keylist = []
        keylist.extend(iter(dictkeys))
        numInKeyList = 0
        if position in keylist:
            n = 0
            for s in keylist:
                if s == position:
                    numInKeyList = n

                n += 1

            x = ord(self.position[0]) - ord(position[0])
            y = int(self.position[1]) - int(position[1])

            if abs(x) == abs(y):
                flag = True
                if abs(x) == 1:
                    if self.checkNewPosition(position):
                        return True

                elif position[0] > self.position[0] and position[1] > self.position[1]:
                    for i in range(1, abs(x)):
                        if boarddict[keylist[numInKeyList + (7 * i)]] != '   ':
                            flag = False
                    if flag:
                        if self.checkNewPosition(position):
                            return True
                    else:
                        print('Invalid Move 19')

                elif position[0] < self.position[0] and position[1] > self.position[1]:
                    for i in range(1, abs(x)):
                        if boarddict[keylist[numInKeyList + (9 * i)]] != '   ':
                            flag = False
                    if flag:
                        if self.checkNewPosition(position):
                            return True
                    else:
                        print('Invalid Move 20')

                elif position[0] < self.position[0] and position[1] < self.position[1]:
                    for i in range(1, abs(x)):
                        if boarddict[keylist[numInKeyList - (7 * i)]] != '   ':
                            flag = False
                    if flag:
                        if self.checkNewPosition(position):
                            return True
                    else:
                        print('Invalid Move 21')

                elif position[0] > self.position[0] and position[1] < self.position[1]:
                    for i in range(1, abs(x)):
                        if boarddict[keylist[numInKeyList - (9 * i)]] != '   ':
                            flag = False
                    if flag:
                        if self.checkNewPosition(position):
                            return True
                    else:
                        print('Invalid Move 22')
            elif self.position[0] == position[0]:
                flag = True
                x = int(self.position[1]) - int(position[1])
                if x > 1:
                    for i in range(1, x):
                        if boarddict[keylist[numInKeyList - (8*i)]] != '   ':
                            flag = False
                    if flag:
                        if self.checkNewPosition(position):
                            return True
                    else:
                        print('Invalid Move 23')
                elif x < -1:
                    x = abs(x)
                    for i in range(1, x):
                        if boarddict[keylist[numInKeyList + (8*i)]] != '   ':
                            flag = False
                    if flag:
                        if self.checkNewPosition(position):
                            return True
                    else:
                        print('Invalid Move 24')
                elif x == 1 or x == -1:
                    if self.checkNewPosition(position):
                        return True
                else:
                    print('Invalid Move 25')

            elif self.position[1] == position[1]:
                flag = True
                x = ord(self.position[0]) - ord(position[0])
                if x > 1:
                    for i in range(1, x):
                        if boarddict[keylist[numInKeyList - i]] != '   ':
                            flag = False
                    if flag:
                        if self.checkNewPosition(position):
                            return True
                    else:
                        print('Invalid Move 26')
                elif x < -1:
                    x = abs(x)
                    for i in range(1, x):
                        if boarddict[keylist[numInKeyList + i]] != '   ':
                            flag = False
                    if flag:
                        if self.checkNewPosition(position):
                            return True
                    else:
                        print('Invalid Move 27')
                elif x == 1 or x == -1:
                    if self.checkNewPosition(position):
                        return True
                else:
                    print('Invalid Move 28')
            else:
                print('Invalid Move 29')
        else:
            print('Invalid Move 30')

    def attackablePositions(self):
        if self.position == '  ':
            return []
        attackablePositionsList = []
        dictkeys = boarddict.keys()
        keylist = []
        keylist.extend(iter(dictkeys))
        numInKeyList = 0
        if self.position in keylist:
            n = 0
            for s in keylist:
                if s == self.position:
                    numInKeyList = n
                n += 1
        x = ord(self.position[0]) - ord('A')
        if x > 0:
            for i in range(1, x+1):
                if boarddict[keylist[numInKeyList - i]] == '   ':
                    attackablePositionsList.append(keylist[numInKeyList - i])
                elif self.name[0] == 'W' and boarddict[keylist[numInKeyList - i]][0] == 'B':
                    attackablePositionsList.append(keylist[numInKeyList - i])
                    break
                elif self.name[0] == 'B' and boarddict[keylist[numInKeyList - i]][0] == 'W':
                    attackablePositionsList.append(keylist[numInKeyList - i])
                    break
                else:
                    break
        x2 = ord('H') - ord(self.position[0])
        if x2 > 0:
            for i in range(1, x2+1):
                if boarddict[keylist[numInKeyList + i]] == '   ':
                    attackablePositionsList.append(keylist[numInKeyList + i])
                elif self.name[0] == 'W' and boarddict[keylist[numInKeyList + i]][0] == 'B':
                    attackablePositionsList.append(keylist[numInKeyList + i])
                    break
                elif self.name[0] == 'B' and boarddict[keylist[numInKeyList + i]][0] == 'W':
                    attackablePositionsList.append(keylist[numInKeyList + i])
                    break
                else:
                    break
        y = 8 - int(self.position[1])
        if y > 0:
            for i in range(1, y+1):
                if boarddict[keylist[numInKeyList - (8*i)]] == '   ':
                    attackablePositionsList.append(keylist[numInKeyList - (8*i)])
                elif self.name[0] == 'W' and boarddict[keylist[numInKeyList - (8*i)]][0] == 'B':
                    attackablePositionsList.append(keylist[numInKeyList - (8*i)])
                    break
                elif self.name[0] == 'B' and boarddict[keylist[numInKeyList - (8*i)]][0] == 'W':
                    attackablePositionsList.append(keylist[numInKeyList - (8*i)])
                    break
                else:
                    break
        y2 = int(self.position[1]) - 1
        if y2 > 0:
            for i in range(1, y2+1):
                if boarddict[keylist[numInKeyList + (8*i)]] == '   ':
                    attackablePositionsList.append(keylist[numInKeyList + (8*i)])
                elif self.name[0] == 'W' and boarddict[keylist[numInKeyList + (8*i)]][0] == 'B':
                    attackablePositionsList.append(keylist[numInKeyList + (8*i)])
                    break
                elif self.name[0] == 'B' and boarddict[keylist[numInKeyList + (8*i)]][0] == 'W':
                    attackablePositionsList.append(keylist[numInKeyList + (8*i)])
                    break
                else:
                    break

        for i in range(1, 8):
            if (numInKeyList - (7 * i)) >= 0:
                if boarddict[keylist[numInKeyList - (7 * i)]] == '   ':
                    attackablePositionsList.append(keylist[numInKeyList - (7 * i)])
                    if keylist[numInKeyList - (7 * i)][0] == 'H' or keylist[numInKeyList - (7 * i)][1] == '8':
                        break
                elif self.name[0] == 'W' and boarddict[keylist[numInKeyList - (7 * i)]][0] == 'B':
                    attackablePositionsList.append(keylist[numInKeyList - (7 * i)])
                    break
                elif self.name[0] == 'B' and boarddict[keylist[numInKeyList - (7 * i)]][0] == 'W':
                    attackablePositionsList.append(keylist[numInKeyList - (7 * i)])
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            if keylist[numInKeyList][0] == 'A':
                break
            if (numInKeyList + (7*i)) < 64:
                if boarddict[keylist[numInKeyList + (7*i)]] == '   ':
                    attackablePositionsList.append(keylist[numInKeyList + (7*i)])
                    if keylist[numInKeyList + (7 * i)][0] == 'A' or keylist[numInKeyList + (7 * i)][1] == '1':
                        break
                elif self.name[0] == 'W' and boarddict[keylist[numInKeyList + (7*i)]][0] == 'B':
                    attackablePositionsList.append(keylist[numInKeyList + (7*i)])
                    break
                elif self.name[0] == 'B' and boarddict[keylist[numInKeyList + (7*i)]][0] == 'W':
                    attackablePositionsList.append(keylist[numInKeyList + (7*i)])
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            if (numInKeyList - (9*i)) >= 0:
                if boarddict[keylist[numInKeyList - (9*i)]] == '   ':
                    attackablePositionsList.append(keylist[numInKeyList - (9*i)])
                    if keylist[numInKeyList - (9 * i)][0] == 'A' or keylist[numInKeyList - (9 * i)][1] == '8':
                        break
                elif self.name[0] == 'W' and boarddict[keylist[numInKeyList - (9*i)]][0] == 'B':
                    attackablePositionsList.append(keylist[numInKeyList - (9*i)])
                    break
                elif self.name[0] == 'B' and boarddict[keylist[numInKeyList - (9*i)]][0] == 'W':
                    attackablePositionsList.append(keylist[numInKeyList - (9*i)])
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            if keylist[numInKeyList][0] == 'H':
                break
            if (numInKeyList + (9*i)) < 64:
                if boarddict[keylist[numInKeyList + (9*i)]] == '   ':
                    attackablePositionsList.append(keylist[numInKeyList + (9*i)])
                    if keylist[numInKeyList + (9 * i)][0] == 'H' or keylist[numInKeyList + (9 * i)][1] == '1':
                        break
                elif self.name[0] == 'W' and boarddict[keylist[numInKeyList + (9*i)]][0] == 'B':
                    attackablePositionsList.append(keylist[numInKeyList + (9*i)])
                    break
                elif self.name[0] == 'B' and boarddict[keylist[numInKeyList + (9*i)]][0] == 'W':
                    attackablePositionsList.append(keylist[numInKeyList + (9*i)])
                    break
                else:
                    break
            else:
                break

        return attackablePositionsList

class King(Piece):
    def move(self, position):
        dictkeys = boarddict.keys()
        keylist = []
        keylist.extend(iter(dictkeys))

        if position in keylist:
            if abs(ord(self.position[0]) - ord(position[0])) == 1:
                if abs(int(position[1]) - int(self.position[1])) == 1 or int(position[1]) - int(
                        self.position[1]) == 0:
                    if self.checkNewPosition(position):
                        return True
            elif ord(self.position[0]) - ord(position[0]) == 0:
                if abs(int(position[1]) - int(self.position[1])) == 1:
                    if self.checkNewPosition(position):
                        return True
            else:
                print('Invalid Move 31')

        else:
            print('Invalid Move 32')

    def attackablePositions(self):
        if self.position == '  ':
            return []
        attackablePositionsList = []
        dictkeys = boarddict.keys()
        keylist = []
        keylist.extend(iter(dictkeys))
        numInKeyList = 0

        if self.position in keylist:
            n = 0
            for s in keylist:
                if s == self.position:
                    numInKeyList = n
                n += 1

        positions = [-9, -8, -7, 1, 9, 8, 7, -1]

        for i in positions:
            if 0 <= numInKeyList + i < 64 and (ord(self.position[0]) - ord(keylist[numInKeyList + i][0]) == 1 or ord(self.position[0]) - ord(keylist[numInKeyList + i][0]) == -1 or ord(self.position[0]) - ord(keylist[numInKeyList + i][0]) == 0) and (int(self.position[1]) - int(keylist[numInKeyList + i][1]) == 1 or int(self.position[1]) - int(keylist[numInKeyList + i][1]) == -1 or int(self.position[1]) - int(keylist[numInKeyList + i][1]) == 0):
                if boarddict[keylist[numInKeyList + i]] == '   ':
                    attackablePositionsList.append(keylist[numInKeyList + i])
                elif self.name[0] == 'W' and boarddict[keylist[numInKeyList + i]][0] == 'B':
                    attackablePositionsList.append(keylist[numInKeyList + i])
                elif self.name[0] == 'B' and boarddict[keylist[numInKeyList + i]][0] == 'W':
                    attackablePositionsList.append(keylist[numInKeyList + i])

        return attackablePositionsList


class Pawn(Piece):
    def move(self, position):
        dictkeys = boarddict.keys()
        keylist = []
        keylist.extend(iter(dictkeys))
        numInKeyList = 0
        if position in keylist:
            n = 0
            for s in keylist:
                if s == position:
                    numInKeyList = n

                n += 1

            if position[0] == self.position[0]:
                if self.name[0] == 'W' and int(self.position[1]) == 2 and int(position[1]) == 4:
                    flag = True
                    for i in range(2):
                        if boarddict[keylist[numInKeyList + (8*i)]] != '   ':
                            flag = False
                    if flag:
                        self.previouspiece = boarddict[position]
                        boarddict[self.position] = '   '
                        boarddict[position] = self.name
                        self.previousposition = self.position
                        self.position = position
                        return True
                    else:
                        print('Invalid Move 33')
                elif self.name[0] == 'B' and int(self.position[1]) == 7 and int(position[1]) == 5:
                    flag = True
                    for i in range(2):
                        if boarddict[keylist[numInKeyList - (8*i)]] != '   ':
                            flag = False
                    if flag:
                        self.previouspiece = boarddict[position]
                        boarddict[self.position] = '   '
                        boarddict[position] = self.name
                        self.previousposition = self.position
                        self.position = position
                        return True
                    else:
                        print('Invalid Move 34')
                elif self.name[0] == 'W' and (int(position[1]) - int(self.position[1]) == 1):
                    if boarddict[position] == '   ':
                        self.previouspiece = boarddict[position]
                        boarddict[self.position] = '   '
                        boarddict[position] = self.name
                        self.previousposition = self.position
                        self.position = position
                        return True
                    else:
                        print('Invalid Move 35')
                elif self.name[0] == 'B' and (int(self.position[1]) - int(position[1]) == 1):
                    if boarddict[position] == '   ':
                        self.previouspiece = boarddict[position]
                        boarddict[self.position] = '   '
                        boarddict[position] = self.name
                        self.previousposition = self.position
                        self.position = position
                        return True
                    else:
                        print('Invalid Move 36')
                else:
                    print('Invalid Move 37')

            elif self.name[0] == 'W' and abs(ord(position[0]) - ord(self.position[0])) == 1 and int(position[1]) - int(self.position[1]) == 1:
                if boarddict[position][0] == 'B':
                    self.previouspiece = boarddict[position]
                    boarddict[self.position] = '   '
                    boarddict[position] = self.name
                    self.previousposition = self.position
                    self.position = position
                    return True
                else:
                    print('Invalid Move 38')
            elif self.name[0] == 'B' and abs(ord(position[0]) - ord(self.position[0])) == 1 and int(self.position[1]) - int(position[1]) == 1:
                if boarddict[position][0] == 'W':
                    self.previouspiece = boarddict[position]
                    boarddict[self.position] = '   '
                    boarddict[position] = self.name
                    self.previousposition = self.position
                    self.position = position
                    return True
                else:
                    print('Invalid Move 39')
            else:
                print('Invalid Move 40')

    def attackablePositions(self):
        if self.position == '  ':
            return []
        attackablePositionsList = []
        dictkeys = boarddict.keys()
        keylist = []
        keylist.extend(iter(dictkeys))
        numInKeyList = 0

        if self.position in keylist:
            n = 0
            for s in keylist:
                if s == self.position:
                    numInKeyList = n
                n += 1

        positions1 = [7, 9]
        for i in positions1:
            if numInKeyList + i < 64:
                if self.name[0] == 'B' and boarddict[keylist[numInKeyList + i]][0] == 'W':
                    attackablePositionsList.append(keylist[numInKeyList + i])

        positions2 = [-7, -9]
        for i in positions2:
            if 0 <= numInKeyList + i:
                if self.name[0] == 'W' and boarddict[keylist[numInKeyList + i]][0] == 'B':
                    attackablePositionsList.append(keylist[numInKeyList + i])


        return attackablePositionsList

def checkforcheck():
    # 1 = Black King in Check, 2 = White King in Check, 0 = No Kings in Check
    # function ends when first king in check is found, assumes only 1 king will be in check at 1 time
    for i in range(32):
        for k in boarddict:
            if boarddict[k] == list[4].name:
                if len(list[i].attackablePositions()) > 0:
                    print(list[i].attackablePositions())
                if k in list[i].attackablePositions():
                    return 1
            if boarddict[k] == list[28].name:
                if k in list[i].attackablePositions():
                    return 2

    return 0

def checkforcheckmate():
    if checkforcheck() == 0:
        return False
    if checkforcheck() == 1:
        for i in range(16, 32):
            squares = list[i].attackablePositions()
            if len(squares) > 0:
                for p in squares:
                    if list[i].position != '  ':
                        if list[i].move(p):
                            if checkforcheck() != 1:
                                list[i].undoMove()
                                return False
                            else:
                                list[i].undoMove()

    elif checkforcheck() == 2:
        for i in range(16):
            squares = list[i].attackablePositions()
            if len(squares) > 0:
                for p in squares:
                    if list[i].position != '  ':
                        if list[i].move(p):
                            if checkforcheck() != 2:
                                list[i].undoMove()
                                return False
                            else:
                                list[i].undoMove()
    return True





boarddict = {
    'A8': 'BR1',
    'B8': 'BK1',
    'C8': 'BB1',
    'D8': 'BQu',
    'E8': 'BKi',
    'F8': 'BB2',
    'G8': 'BK2',
    'H8': 'BR2',
    'A7': 'BP1',
    'B7': 'BP2',
    'C7': 'BP3',
    'D7': 'BP4',
    'E7': 'BP5',
    'F7': 'BP6',
    'G7': 'BP7',
    'H7': 'BP8',
    'A6': '   ',
    'B6': '   ',
    'C6': '   ',
    'D6': '   ',
    'E6': '   ',
    'F6': '   ',
    'G6': '   ',
    'H6': '   ',
    'A5': '   ',
    'B5': '   ',
    'C5': '   ',
    'D5': '   ',
    'E5': '   ',
    'F5': '   ',
    'G5': '   ',
    'H5': '   ',
    'A4': '   ',
    'B4': '   ',
    'C4': '   ',
    'D4': '   ',
    'E4': '   ',
    'F4': '   ',
    'G4': '   ',
    'H4': '   ',
    'A3': '   ',
    'B3': '   ',
    'C3': '   ',
    'D3': '   ',
    'E3': '   ',
    'F3': '   ',
    'G3': '   ',
    'H3': '   ',
    'A2': 'WP1',
    'B2': 'WP2',
    'C2': 'WP3',
    'D2': 'WP4',
    'E2': 'WP5',
    'F2': 'WP6',
    'G2': 'WP7',
    'H2': 'WP8',
    'A1': 'WR1',
    'B1': 'WK1',
    'C1': 'WB1',
    'D1': 'WQu',
    'E1': 'WKi',
    'F1': 'WB2',
    'G1': 'WK2',
    'H1': 'WR2',
    }

objectdict = {
    'A8': 0,
    'B8': 1,
    'C8': 2,
    'D8': 3,
    'E8': 4,
    'F8': 5,
    'G8': 6,
    'H8': 7,
    'A7': 8,
    'B7': 9,
    'C7': 10,
    'D7': 11,
    'E7': 12,
    'F7': 13,
    'G7': 14,
    'H7': 15,
    'A6': 16,
    'B6': 17,
    'C6': 18,
    'D6': 19,
    'E6': 20,
    'F6': 21,
    'G6': 22,
    'H6': 23,
    'A5': 24,
    'B5': 25,
    'C5': 26,
    'D5': 27,
    'E5': 28,
    'F5': 29,
    'G5': 30,
    'H5': 31,
    'A4': 32,
    'B4': 33,
    'C4': 34,
    'D4': 35,
    'E4': 36,
    'F4': 37,
    'G4': 38,
    'H4': 39,
    'A3': 40,
    'B3': 41,
    'C3': 42,
    'D3': 43,
    'E3': 44,
    'F3': 45,
    'G3': 46,
    'H3': 47,
    'A2': 48,
    'B2': 49,
    'C2': 50,
    'D2': 51,
    'E2': 52,
    'F2': 53,
    'G2': 54,
    'H2': 55,
    'A1': 56,
    'B1': 57,
    'C1': 58,
    'D1': 59,
    'E1': 60,
    'F1': 61,
    'G1': 62,
    'H1': 63,
    }
listofkeys = []
for i in boarddict:
    listofkeys.append(boarddict[i])



# copyboarddict = dict(boarddict)
#
list = []
# for key, value in boarddict.items():
#     list.append(Queen(value, key))

list.append(Rook('BR1', 'A8'))
list.append(Knight('BK1', 'B8'))
list.append(Bishop('BB1', 'C8'))
list.append(Queen('BQu', 'D8'))
list.append(King('BKi', 'E8'))
list.append(Bishop('BB2', 'F8'))
list.append(Knight('BK2', 'G8'))
list.append(Rook('BR2', 'H8'))
list.append(Pawn('BP1', 'A7'))
list.append(Pawn('BP2', 'B7'))
list.append(Pawn('BP3', 'C7'))
list.append(Pawn('BP4', 'D7'))
list.append(Pawn('BP5', 'E7'))
list.append(Pawn('BP6', 'F7'))
list.append(Pawn('BP7', 'G7'))
list.append(Pawn('BP8', 'H7'))
list.append(Pawn('WP1', 'A2'))
list.append(Pawn('WP2', 'B2'))
list.append(Pawn('WP3', 'C2'))
list.append(Pawn('WP4', 'D2'))
list.append(Pawn('WP5', 'E2'))
list.append(Pawn('WP6', 'F2'))
list.append(Pawn('WP7', 'G2'))
list.append(Pawn('WP8', 'H2'))
list.append(Rook('WR1', 'A1'))
list.append(Knight('WK1', 'B1'))
list.append(Bishop('WB1', 'C1'))
list.append(Queen('WQu', 'D1'))
list.append(King('WKi', 'E1'))
list.append(Bishop('WB2', 'F1'))
list.append(Knight('WK2', 'G1'))
list.append(Rook('WR2', 'H1'))

# Board(boarddict)
# list[16].move('A4')
# Board(boarddict)
# list[24].move('A3')
# Board(boarddict)
# list[24].move('H3')
# Board(boarddict)
# list[20].move('E3')
# Board(boarddict)
# list[29].move('A6')
# Board(boarddict)
# list[29].move('B7')
# Board(boarddict)
# list[29].undoMove()
# Board(boarddict)


#
#
#
# print(list[50].position)
# print(list[15].attackablePositions())
player = 1
a = 0
while True:
    Board(boarddict)
    c = checkforcheck()
    if c == 1:
        print('Black King in Check')
    elif c == 2:
        print('White King in Check')
    if checkforcheckmate():
        print('Checkmate! Player ' + str(player) + ' wins!')
    if a % 2 == 0:
        player = 1
    elif a % 2 == 1:
        player = 2
    while True:
        piece = input('Player ' + str(player) + ', enter a piece name: ')
        if (piece in listofkeys) and ((player == 1 and piece[0] == 'W') or (player == 2 and piece[0] == 'B')):
            break
        else:
            print('Invalid Piece Name! Pick another...')
    p = 0
    for i in range(32):
        if list[i].name == piece:
            p = i


    while True:
        while True:
            pos = input('Player ' + str(player) + ', enter a position or enter "b" to pick another piece: ')
            if pos == 'b':
                break
            if list[p].move(pos):
                break
            else:
                print('Invalid Position! Pick another...')
                print(list[p].name, list[p].position, list[p].previousposition, list[p].previouspiece)
        if pos == 'b':
            break
        elif (player == 1) and (checkforcheck() in (1, 0)):
            break
        elif (player == 2) and (checkforcheck() in (2, 0)):
            break
        else:
            if checkforcheckmate():
                break
            list[p].undoMove()
            print('Invalid Move, King in Check')

    if checkforcheckmate():
        print('Checkmate')
        break
    if pos != 'b':
        a += 1

print('Player ' + str(a) + ' wins!')
Board(boarddict)
print(list[29].attackablePositions())
