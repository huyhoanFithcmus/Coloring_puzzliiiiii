from math import comb
from itertools import combinations, combinations_with_replacement, permutations
import time
from queue import PriorityQueue

# ==============================================

xCfg = [0, -1, -1, -1, 0, 1, 1, 1, 0]
yCfg = [0, -1, 0, 1, 1, 1, 0, -1, -1]

# ==============================================


def InputData(fileAddr):
    global info, adj, color, clauses, found, nrow, ncol, heur, cnt, invalid, visited, space
    info = list(list())
    adj = list(list())
    color = list(list())
    visited = list(list())
    invalid = list()
    clauses = list()
    space = set()
    found = 0
    heur = 0
    cnt = dict()

    f = open(fileAddr, "r")

    for line in f:
        info.append(line.split())

    nrow = len(info)
    ncol = len(info[0])

    for i in range(nrow):
        color.append(list())
        adj.append(list())
        visited.append(list())

        for j in range(ncol):
            info[i][j] = int(info[i][j])
            numAdj = 9
            if i == 0 or j == 0 or i == nrow-1 or j == ncol-1:
                if i in (0, nrow-1) and j in (0, ncol-1):
                    numAdj = 4
                else:
                    numAdj = 6

            adj[i].append(numAdj)
            color[i].append(0)
            visited[i].append(0)

    f.close()

# ==============================================


def convert(i, j):
    return (i*ncol + j + 1)

# ==============================================


def makeCNF():
    global heur, cnt, invalid

    for i in range(nrow):
        for j in range(ncol):
            if info[i][j] != -1:
                negCons = combinations(
                    [0, 1, 2, 3, 4, 5, 6, 7, 8], adj[i][j] - info[i][j] + 1)
                posCons = combinations(
                    [0, 1, 2, 3, 4, 5, 6, 7, 8], info[i][j] + 1)

                if negCons:
                    for choosen in negCons:
                        clause = list()

                        for k in choosen:
                            X = i + xCfg[k]
                            Y = j + yCfg[k]
                            if (X not in range(nrow)) or (Y not in range(ncol)):
                                break
                            id = convert(X, Y)
                            clause.append(id)

                        clause = sorted(clause)
                        if len(clause) == len(choosen) and clause not in clauses:
                            clauses.append(clause)
                            invalid.append(heur)
                            heur += 1

                if posCons:
                    for choosen in posCons:
                        clause = list()

                        for k in choosen:
                            X = i + xCfg[k]
                            Y = j + yCfg[k]
                            if (X not in range(nrow)) or (Y not in range(ncol)):
                                break
                            id = -convert(X, Y)
                            clause.append(id)

                        clause = sorted(clause)
                        if len(clause) == len(choosen) and clause not in clauses:
                            clauses.append(clause)
                            invalid.append(heur)
                            heur += 1

# ==============================================

def visualized():
    for row in info:
        for item in row:
            if item == -1:
                print(" . ", end="")
            else:
                print("", item, "", end="")
        print()

    for i in range(len(info[0])):
        print("===", end="")

    if not found:
        print("NO SOLUTION")
        return

    print(" 0 - Red / 1 - Blue")

    for row in color:
        for item in row:
            print("", item, "", end="")
        print()

# ==============================================


def Coloring(step, timeDelay):
    global heur
    q = list()

    if str(invalid) in space: 
        return
    space.add(str(invalid))

    for i in range(nrow):
        for j in range(ncol):
            if info[i][j] != -1:
                for k in range(9):
                    X = i + xCfg[k]
                    Y = j + yCfg[k]

                    if (X not in range(nrow)) or (Y not in range(ncol)):
                        continue

                    if not visited[X][Y]:
                        coord = convert(X, Y)
                        temp = calHeur(coord)
                        if temp < heur:
                            val = temp
                            q.append((val, coord, 1))

                        coord = -convert(X, Y)
                        temp = calHeur(coord)
                        if temp < heur:
                            val = temp
                            q.append((val, coord, 0))

    q.sort(key=lambda x: x[0], reverse=True)
    # print(q)

    for choosen in q:
        changed = list()

        for i in invalid:
            if choosen[1] in clauses[i]:
                changed.append(i)
        for i in changed:
            invalid.remove(i)

        preHeur = heur
        heur = choosen[0]
        temp = abs(choosen[1]) - 1
        color[temp//ncol][temp % ncol] = choosen[2]
        # print(step, choosen, visited, heur)
        visited[temp//ncol][temp%ncol] = 1

        if heur == 0:
            global found
            found = 1
            return

        # print(heur, choosen)
        Coloring(step+1, timeDelay)

        if found:
            return

        color[temp//ncol][temp % ncol] = (choosen[2]^1)
        visited[temp//ncol][temp%ncol] = 0
        heur = preHeur
        for i in changed:
            invalid.append(i)

# ==============================================


def calHeur(literal):
    res = 0

    for i in invalid:
        if literal in clauses[i]:
            res += 1

    return heur - res
