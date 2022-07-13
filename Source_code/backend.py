executeFinish = 0
info = list(list())
color = list(list())

def Execute(fileAddr, algorithm, timeDelay):
    global executeFinish 
    executeFinish = 0

    if algorithm == "PySAT": 
        ExecutePysat(fileAddr)
    
    if algorithm == "AStar":
        ExecuteAstar(fileAddr, timeDelay)
    
    if algorithm == "Backtracking":
        ExecuteBacktracking(fileAddr)
    
    if algorithm == "Brute force":
        ExecuteBruteForce(fileAddr)
        
    executeFinish = 1

def ExecutePysat(fileAddr):
    import Pysat as ut

    ut.InputData(fileAddr)
    global color, info
    info = ut.info
    color = ut.color
    ut.Coloring()
    ut.visualized()

def ExecuteBacktracking(fileAddr):
    import BackTracking as ut

    ut.InputData(fileAddr)

    global color, info
    info = ut.info
    color = ut.color
    
    ut.Coloring(0)
    ut.visualized()

def ExecuteBruteForce(fileAddr):
    import BruteForce as ut

    ut.InputData(fileAddr)

    global color, info
    info = ut.info
    color = ut.color
    
    ut.Coloring(0)
    ut.visualized()

def ExecuteAstar(fileAddr, timeDelay):
    import Astar as ut

    ut.InputData(fileAddr)

    global color, info
    info = ut.info
    color = ut.color
    
    ut.makeCNF()
    ut.Coloring(0, timeDelay)
    ut.visualized()