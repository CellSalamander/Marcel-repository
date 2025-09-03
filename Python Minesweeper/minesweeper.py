import random

def createTable():
    table = []
    for c in range(5):
        myrow = []
        for r in range(5):
           randomNumber =  random.randrange(10)
           
           if randomNumber % 2 == 0:
               randomChar = '-'
               myrow.append(randomChar)
           else:
               randomChar = '#'
               myrow.append(randomChar)
            
    
        table.append(myrow)
    return table

def displayTable(table):
    print("-----------------------------------------------------------\n")
    for i in table:
        print(i)

MyTable = createTable()
displayTable(MyTable)

def solveTable(myTable):
    rows , cols = len(myTable) , len(myTable[0])
    for r in range(5):
        
        for c in range(5):
            
            if myTable[r][c] == '-':
                bombcounter = 0
                for nextRow in range(-1,2):
                         
                    for nextColumn in range(-1,2):
                        
                       nr,nc = r+nextRow , c+nextColumn
                       
                       if (0 <= nr < rows) and (0 <= nc < cols) and (myTable[nr][nc] == '#'):
                           bombcounter += 1
                           

                
                myTable[r][c] = str(bombcounter)
                
    return myTable

MySolvedTable = solveTable(MyTable)
displayTable(MySolvedTable)
                            
                
                            
                    
            

        