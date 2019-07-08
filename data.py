from random import *

class data:#dana zawiera nr funkcjonalnosci licznik f i czas wparowadzenia

    def __init__(self, funct, cnt, time):
        self.funct = funct
        self.cnt = cnt
        self.time = time

class system:#cały system z funkcjonalnościami

    def __init__(self, functiolality_ = [], toFill_ = [], reg = 2, timVec = []):
        self.functionality = functiolality_
        self.toFill = toFill_#oblicznne potencjalne funkcjonalności do wprowadzenia
        self.regFunction = self.switchf(reg)
        self.timeVector = timVec
        self.timendex = 0

    def print_(self):#wypisz informacje o systemie
        for x in self.functionality:
            print("funkcjonalnosc: " + str(x.funct) + " miesiac: "+str(x.time)+"\n")
        if self.toFill:
            print("\nzaleglosci:\n")
            for x in self.toFill:
                print("funkcjonalnosc: " + str(x.funct) + " miesiac: " + str(x.time) + " cnt: "+str(x.cnt) + "\n")
        print("\n")

    def check(self,time):
        if self.timendex == len(self.timeVector):
            return False
        if self.timeVector[self.timendex] == time:
            self.timendex = self.timendex + 1
            return True
        else:
            return False

    def switchf(self, reg):
        if (reg == 3):
            return self.reg3
        elif (reg == 4):
            return self.reg4
        elif (reg == 5):
            return self.reg5
        elif (reg == 6):
            return self.reg6
        elif (reg == 7):
            return self.reg7
        elif (reg == 12):
            return self.reg12
        elif (reg == 10):
            return self.reg10
        else:
            return self.reg2

    def sumtime(self,time, a):
        sum = 0
        for x in a:
            sum = sum + time - x
        return sum

    def reg2(self, time):#najdłuższy łączny czas zalegania > krotność
        if(self.toFill):
            index = 0
            finindex = 0
            tmp = self.toFill[0]
            for x in self.toFill:
                tim1 = self.sumtime(time,x.time)
                tim2 = self.sumtime(time,tmp.time)
                if (tim1 > tim2):
                    tmp = x
                    finindex = index
                elif (tim1 == tim2):
                    if x.cnt > tmp.cnt:
                        tmp = x
                        finindex = index
                index = index +1
            self.functionality.append(data(tmp.funct,0,time))
            self.toFill.pop(finindex)

    def reg3(self, time):# krotność >najdłuższy łączny czas zalegania
        if(self.toFill):
            index = 0
            finindex = 0
            tmp = self.toFill[0]
            for x in self.toFill:
                tim1 = self.sumtime(time,x.time)
                tim2 = self.sumtime(time,tmp.time)
                if (x.cnt > tmp.cnt):
                    tmp = x
                    finindex = index
                elif (x.cnt == tmp.cnt):
                    if tim1 > tim2:
                        tmp = x
                        finindex = index
                index = index +1
            self.functionality.append(data(tmp.funct,0,time))
            self.toFill.pop(finindex)

    def reg4(self, time):#nadłuższy zwykły czas zalegania > krotność
        if (self.toFill):
            index = 0
            finindex = 0
            tmp = self.toFill[0]
            for x in self.toFill:
                tim1 = min(x.time)
                tim2 = min(tmp.time)
                if (tim1 < tim2):
                    tmp = x
                    finindex = index
                elif (tim1 == tim2):
                    if x.cnt > tmp.cnt:
                        tmp = x
                        finindex = index
                index = index + 1
            self.functionality.append(data(tmp.funct, 0, time))
            self.toFill.pop(finindex)

    def reg5(self, time):# krotność >nadłuższy zwykły czas zalegania >
        if (self.toFill):
            index = 0
            finindex = 0
            tmp = self.toFill[0]
            for x in self.toFill:
                tim1 = min(x.time)
                tim2 = min(tmp.time)
                if (tim1 < tim2):
                    tmp = x
                    finindex = index
                elif (tim1 == tim2):
                    if x.cnt > tmp.cnt:
                        tmp = x
                        finindex = index
                index = index + 1
            self.functionality.append(data(tmp.funct, 0, time))
            self.toFill.pop(finindex)

    def reg6(self, time):
        if (self.toFill):
            index = 0
            finindex = 0
            tmp = self.toFill[0]
            for x in self.toFill:
                tim1 = self.sumtime(time,x.time)
                tim2 = self.sumtime(time,tmp.time)
                if (tim1 < tim2):
                    tmp = x
                    finindex = index
                elif (tim1 == tim2):
                    if x.cnt > tmp.cnt:
                        tmp = x
                        finindex = index
                index = index + 1
            self.functionality.append(data(tmp.funct, 0, time))
            self.toFill.pop(finindex)

    def reg7(self,time):
        if (self.toFill):
            index = 0
            finindex = 0
            tmp = self.toFill[0]
            for x in self.toFill:
                tim1 = self.sumtime(time,x.time)
                tim2 = self.sumtime(time,tmp.time)
                if (tim1 > tim2):
                    tmp = x
                    finindex = index
                elif (tim1 == tim2):
                    if randrange(2):
                        tmp = x
                        finindex = index
                index = index + 1
            self.functionality.append(data(tmp.funct, 0, time))
            self.toFill.pop(finindex)

    def reg10(self, time):
        if (self.toFill):
            index = 0
            finindex = 0
            tmp = self.toFill[0]
            for x in self.toFill:
                if (x.cnt > tmp.cnt):
                    tmp = x
                    finindex = index
                elif (x.cnt == tmp.cnt):
                    if randrange(2):
                        tmp = x
                        finindex = index
                index = index + 1
            self.functionality.append(data(tmp.funct, 0, time))
            self.toFill.pop(finindex)

    def reg12(self, time):
        if (self.toFill):
            x = randrange(len(self.toFill))
            self.functionality.append(data(self.toFill[x].funct, 0, time))
            self.toFill.pop(x)

class allSystems:#wszyskkie systemy

    def __init__(self, probn, probnew, reg_, n_):
        self.probToNot = probn
        self.probToNew = probnew
        self.reg = reg_
        self.n = n_
        self.systems = []
        self.cnt = 0

    def readData(self,file, timeFile):#pbranie danych z pliku
        fileo = open(file, "r")
        #time, funct,
        max = 0
        maxt = 0
        self.n = int(fileo.readline())
        #self.systems = [system()]*self.n
        #wektor czasów z pdf
        timvec = self.getTimes(timeFile)
        for j in range(self.n):
            self.systems.append(system([],[],self.reg,timvec[j]))
            sys = self.systems[j]
            fileo.readline()
            n = int(fileo.readline())
            for i in range(n):
                line = fileo.readline().split()
                funct = int(line[0])
                time = int(line[1])
                if funct > max:
                    max = funct
                if time > maxt:
                    maxt = time
                self.systems[j].functionality.append(data(funct, 0, time))
        self.cnt = max + 1;
        fileo.close()
        return maxt
    def getTimes(self,timeFile):
        fileo = open(timeFile, "r")
        out = []
        for j in range(self.n):
            dat = fileo.readline().split(",")
            out.append([])
            for x in dat:
                out[j].append(int(x))
        fileo.close()
        return out
    def print_(self):
        cnt = 1
        for sys in self.systems:
            print("system " + str(cnt))
            sys.print_()
            cnt = cnt+1

    def computeToFill(self, time):
        for i  in range(self.n):
            for j  in range(self.n):
                if i is not j:
                    sys1f = self.systems[i].functionality
                    sys2f = self.systems[j].functionality
                    #fill = self.systems[j].toFill
                    diff = self.difference(sys1f,sys2f)
                    if not self.systems[i].toFill:
                        self.systems[i].toFill = diff
                    else:
                        for d in diff:
                            found = False
                            for f in self.systems[i].toFill:
                                if d.funct == f.funct:
                                    f.cnt = f.cnt +1
                                    f.time.append(d.time[0])
                                    found = True
                                    break
                            if found == False:
                                self.systems[i].toFill.append(d)


    def difference(self,sys1,sys2):
        diff = []
        found = False
        for one in sys2:
            found = False
            for sec in sys1:
                if one.funct == sec.funct:
                    found = True
                    break
            if found == False:
                diff.append(data(one.funct,one.cnt,[one.time]))
        return diff

    def update(self, time):
        for sys in self.systems:
            #p = randrange(10) + 1
            if(sys.check(time)):
                if sys.toFill:
                    sys.regFunction(time)
                    '''if p <= self.probToNew:
                        sys.functionality.append(data(self.cnt, 0, time))
                        self.cnt = self.cnt + 1
                    elif p > 10- self.probToNot:
                        continue
                    else:
                        sys.regFunction(time)'''
                else:
                    sys.functionality.append(data(self.cnt, 0, time))
                    self.cnt = self.cnt + 1

    def getSysFunctions(self,sys):
        dat = []
        for x in self.systems[sys].functionality:
            dat.append(x.funct)
        return dat

    def getSysTimes(self,sys):
        dat = []
        for x in self.systems[sys].functionality:
            Y = int(x.time/12)
            M = x.time % 12
            dat.append(2000 + Y+(M/100))
        return dat

    def getSysYval(self,sys):
        dat = []
        for x in range(1,len(self.systems[sys].functionality)+1):
            dat.append(x)
        return dat