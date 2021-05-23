class nqueen:
    def __init__(self):
        self.matrix=[]
        self.symbols=[]
        self.repeated=[]
        self.n=0
        self.check=0
        self.counter=0
    #Get size of N
    def getsize(self):
        size1=int(input("Enter size of matrix:"))
        self.n=size1
        # Creating 2d array of n*n size
        self.matrix=[['#' for x in range(self.n)] for y in range(self.n)]
        self.repeated=[['#' for x in range(self.n)] for y in range(self.n)]

    #Function to print the matrix
    def printmatrix(self):
        i=0
        j=0
        for i in range(self.n):
            j=0
            for j in range(self.n):
                print(self.matrix[i][j]," ",end="")
            print("\n")
        print("\n")

    #Function to fill row & column
    def fillrowandcol(self,row,col,symbol):
        i=0
        ## Filling particular row
        for i in range(self.n):
            if(self.matrix[row][i]=='#'):
                self.matrix[row][i]=symbol

        ## Filling particular column
        i=0
        for i in range(self.n):
            if(self.matrix[i][col]=='#'):
                self.matrix[i][col]=symbol
    #Function to fill diagonals
    def filldiagonals(self,row,column,symbol):
        self.matrix[row][column]=0
        i=row
        j=column
        while(i>=0 and j>=0):
            if(self.matrix[i][j] =='#'):
                self.matrix[i][j]=symbol
            i=i-1
            j=j-1

        i=row
        j=column
        while(i<self.n and j<self.n):
            if(self.matrix[i][j]=='#'):
                self.matrix[i][j]=symbol
            i=i+1
            j=j+1

        i=row
        j=column
        while(i>=0 and j<self.n):
            if(self.matrix[i][j]=='#'):
                self.matrix[i][j]=symbol
            i=i-1
            j=j+1

        i=row
        j=column
        while(i<self.n and j>=0):
            if(self.matrix[i][j]=='#'):
                self.matrix[i][j]=symbol
            i=i+1
            j=j-1
    # Function to check either any queen is in same row and column
    def checkrowandcol(self,row,col):
        chk=False
        ##Check row if it contains '*'
        if('*' not in self.matrix[row]):
            chk=True
        if(chk==True):
            #Check column if it contains '*'
            i=0

            for i in range(self.n):

                if('*' == self.matrix[i][col]):
                    chk=False
                    break

        return chk
    # Function to check diagonals
    def checkdiagonals(self,row,column):
        i=row
        j=column
        chk=True
        while(i>=0 and j>=0):
            if(self.matrix[i][j] =='*'):
                chk=False
                break
            i=i-1
            j=j-1
        if(chk==True):
            i=row
            j=column
            while(i<self.n and j<self.n):
                if(self.matrix[i][j]=='*'):
                    chk=False
                    break
                i=i+1
                j=j+1

            if(chk==True):

                i=row
                j=column
                while(i>=0 and j<self.n):
                    if(self.matrix[i][j]=='*'):
                        chk=False
                        break
                    i=i-1
                    j=j+1

                if(chk==True):

                    i=row
                    j=column
                    while(i<self.n and j>=0):
                        if(self.matrix[i][j]=='*'):
                            chk=False
                            break
                        i=i+1
                        j=j-1
        return chk

    # Check if row contains '#'
    def checkrowelements(self,row):
        chk=False
        i=0

        if('#' in self.matrix[row]):
            chk=True

        return chk

    def checkfunction(self):
        i=1
        j=0
        check=False
        for i in range(1,self.n):

            if('#' not in self.matrix[i]):
                check=True
                return check
                break

        if(check==False):

            if(self.counter<self.n):
                self.repeated[self.counter][0]=1
                self.counter+=1

            j=0
            for i in range(1,self.n):

                for j in range(self.n):
                    self.repeated[i][j]='#'
            print("True all below ",0," does not have *")
            print(self.repeated)
            return check
            #print(self.repeated)



    def backtrack(self,row):
        self.check+=1
        i=0
        j=0

        self.printmatrix()
        lines=self.getrow(row)
        x1=row-lines
        x1=abs(x1)

        h=row-x1
        x3=h
        if(lines==0):
            x3=row+1





        if(h==(self.n-1)):
            x3=h-1


        row1=0
        #print("X3 = ",x3," lines = ",lines," x1 = ",x1," row = ",row)
        for m in range(0,x3):

            for i in range(self.n):
                for j in range(self.n):
                    if(self.matrix[i][j]==row ):
                        self.matrix[i][j]='#'
            h=0
            for h in range(self.n):
                if(self.matrix[row][h]=='*'):

                    #print(i,h)
                    self.matrix[row][h]='#'
                    print("After back tracking:")
                    self.printmatrix()
                    self.repeated[row][h]=h
                    row1=row
                    row=row-1
                    break

            m=0
            n=0
            chk4=False
            for m in range(0,self.n):
                #print(row1,m)
                if(self.matrix[row1][m]=='#'):
                    if(self.repeated[row1][m]=='#'):
                        #if(chk4==True):
                        #print("Row = ",row1," column = ",m)
                        lines=row1
                        self.fun3(row1)
                        return row1

                        break

        x1=self.checkfunction()
        if(x1==False):
            lines=0
            x=0

            #for x in range(self.n):
            #    if(self.matrix[lines][x]=='#'):

        #print("Lines = ",lines)
        return lines


    def fun3(self,row):
        i=0
        j=0
        #print("Row = ",row)

        #print(" row = ",row," is ",self.repeated[row])
        for i in range(row+1,self.n):

            for j in range(self.n):
                self.repeated[i][j]='#'

        #print("After '#'",self.repeated[row])





    def getrow(self,row):
        i=0
        line=-1
        chk=False
        for i in range(self.n):
            j=0
            for j in range(self.n):
                if(self.matrix[i][j]=='#'):
                    chk=True
                    break
            if(chk==True):
                line=i

                if(line>=row):
                    line=row
                break

        if(line==-1):
            line=0


        return line


    def readyfun(self):
        i=0
        j=0
        for i in range(self.n):
            for j in range(self.n):
                if(self.matrix[i][j]!='*'):
                    self.matrix[i][j]=0
        i=0
        j=0
        for i in range(self.n):
            for j in range(self.n):
                if(self.matrix[i][j]=='*'):
                    self.matrix[i][j]=1

        print("Final result for N = ",self.n," is : (1 is for queen) \n Note: In previous prints i used '*' to indicate queen and I used numbers for my instance for backtracking\n ")
        self.printmatrix()


    def mainfun(self):
        i=0
        j=0

        while i in range(self.n):



            #print("Lines = ",lines)
            check5=False

            check=self.checkrowelements(i)
            h1=0
            if(check==False):

                if((i-1)<0):
                    i=0
                else:
                    i=i-1

                i=self.backtrack(i)

                if(i==0):
                    m=0
                    for m in range(self.n):
                        if(self.matrix[i][m]=='*'):
                            self.matrix[i][m]='#'
                            break
                    m=0
                    for m in range(self.n):
                        if(self.repeated[i][m]=='#'):
                            h1=m
                            #print(" line = ",i," col = ",m)
                            i=0
                            check5=True
                            #print("True")
                            break
                #print("Row = ",row," Column = ",col," i  = ",i)
            j=0
            if(check5==True):
                #print("Check 5 is True")
                self.fillrowandcol(0,h1,0)
                self.filldiagonals(0,h1,0)
                self.matrix[0][h1]='*'
                #print("After filling for i =",0," and j = ",h1)
                self.printmatrix()
            j=0
            #print(" value of i = ",i," and  h1 = ",h1)
            while j <self.n:
                #print(i)

                print(i,j)
                check1=self.checkrowandcol(i,j)
                check2=self.checkdiagonals(i,j)
                #print("For i = ",i," j = ",j," Check1 = ",check1," Check2  = ",check2)
                if(check1==True and check2==True):
                    if(self.repeated[i][j]=='#'):
                        #print("Row = ",i," Col = ",j)
                        #print("Filling for  i =",i," and for j = ",j)
                        self.fillrowandcol(i,j,i)
                        self.filldiagonals(i,j,i)
                        self.matrix[i][j]='*'
                        self.printmatrix()

                        break
                j=j+1
            i=i+1
        self.readyfun()


obj1=nqueen()
obj1.getsize()
obj1.mainfun()


