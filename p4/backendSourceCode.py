#p4 - 327
# REMINDER - AMOUNTS AND THEIR LIMITS ARE IN DECIMALS - BE SURE TO ADD TWO EXTRA ZEROS
# WE USE A DICTIONARY (HASHMAP IN PYTHON) TO STORE DAILY TRANSAC LIMITS

# the slides say "A newly created account must have a new unused account number"
# Does that mean not being currently used or never used at all?
# If never used at all, we have to use a hashmap to store all account numbers that were used
# We currently use a hashmap following the above assumption
# Store all accounts that were ever used, alongside their name
accountsHash = {}

#clear mergedTSF file to rewrite to it
def clearMasterTSF():
    open('mergedTSF.txt', 'w').close()

#copy all smaller tsf into mergedTSF
def mergeTSF():
    tsfLIST = 3
    for i in range(1,4):
        tsf = open(str("tsf"+str(i)+".txt"),"r")
        lines = tsf.readlines()
        for line in lines:
            newTSF = open(str('mergedTSF.txt'),"a")
            if line != '':
                if line[:3] != 'EOS':
                    newTSF.write(line)
            newTSF.close()
        newTSF = open(str('mergedTSF.txt'), "a")
        newTSF.write("EOS 0000000 000 0000000 ***")
        newTSF.close()

#handle the actions that are on the new tsf
def handleTSF():
    tsf = open('mergedTSF.txt', 'r')
    lines = tsf.readlines()
    # Use dictionaries as hashmaps to store the transac limi
    dailyDepLimit = {}
    dailyWithLimit = {}
    dailyTransfLimit = {}
    for line in lines:
        #tsfLine = line.split(' ')
        action = line[:3]
        accANum = line[4:11]
        iNEW = line.index(' ', 12)
        amount = int(line[12:iNEW])
        iNEW2 = line.index(' ', iNEW+1)
        accBNum = line[iNEW+1: iNEW2]
        accName = line[iNEW2+1:]
        if action == 'DEP':
            depositPure(accANum, amount)
        elif action == 'WDR':
            withdrawPure(accANum, amount)
        elif action == 'XFR':
            transferPure(accANum, amount, accBNum)
        elif action == 'NEW':
            create(accANum, accName)
        elif action == 'DEL':
            delete(accANum)
'''
In addition to the existing deposit/withdraw/transfer functions, I made depositPure, withdrawPure, transferPure.
These assume that the frontend checked with the backend before sending the transaction to the TSF, which means that
all information will be correct, and I'm pretty sure this is how we're going to have to do it because the backend doesn't
update stuff in real time. 
'''

def deposit(toAccNum, amount):
    if amount <= 200000:
        checkLimit = dailyDepLimit[toAccNum] + amount
        if checkLimit <= 500000:
            maf = open("MAF.txt", "w")
            lines = maf.readlines()
            for line in lines:
                mafAccNum = line[:7]
                if mafAccNum == toAccNum:
                    mafLine = line.split(" ", 2)
                    mafAccName = mafLine[2]
                    mafAmountBalance = mafLine[1] + amount
                    maf.write(mafAccNum + " " + mafAmountBalance + " " + mafAccName)
                    dailyDepLimit[toAccNum] = dailyDepLimit[toAccNum] + amount
                    break
            maf.close()
        else:
            print("Exceeded daily deposit limit")
    else:
        print("Exceeded single deposit limit")



def withdraw(fromAccNum, amount):
    if amount <= 100000:
        checkLimit = dailyWithLimit[fromAccNum] + amount
        if checkLimit <= 500000:
            maf = open("MAF.txt", "w")
            lines = maf.readlines()
            for line in lines:
                mafAccNum = line[:7]
                if mafAccNum == fromAccNum:
                    mafLine = line.split(" ", 2)
                    mafAccName = mafLine[2]
                    mafAmountBalance = mafLine[1] - amount
                    if mafAmountBalance >= 0:
                        maf.write(mafAccNum + " " + mafAmountBalance + " " + mafAccName)
                        dailyWithLimit[fromAccNum] = dailyWithLimit[fromAccNum] + amount
                    else:
                        print("Error - insufficient funds")
                    break
            maf.close()
        else:
            print("Exceeded daily withdraw limit")
    else:
        print("Exceeded single withdraw limit")


def transfer(toAccNum, amount, fromAccNum):
    if amount <= 1000000:
        # Note: there is only a limit for transferring OUT of an account
        checkLimit = dailyTransfLimit[fromAccNum] + amount
        if checkLimit <= 1000000:
            maf = open("MAF.txt", "w")
            lines = maf.readlines()
            for line in lines:
                mafAccNum = line[:7]
                if mafAccNum == fromAccNum:
                    mafLine = line.split(" ", 2)
                    mafAccName = mafLine[2]
                    mafAmountbalance = mafLine[1] - amount
                    if mafAmountbalance >= 0:
                        maf.write(mafAccNum + " " + mafAmountbalance + " " + mafAccName)
                        dailyTransfLimit[fromAccNum] = dailyTransfLimit[fromAccNum] + amount
                    else:
                        print("Error - insufficient funds")
                    break
            for line in lines:
                mafAccNum = line[:7]
                if mafAccNum == toAccNum:
                    mafLine = line.split(" ", 2)
                    mafAccName = mafLine[2]
                    mafAmountbalance = mafLine[1] + amount
                    maf.write(mafAccNum + " " + mafAmountBalance + " " + mafAccName)
                    # I include the line below to remind y'all that we do NOT need a daily limit for the TO account
                    #dailyDepLimit[toAccNum] = dailyDepLimit[toAccNum] + amount
            maf.close()
        else:
            print("Exceeded daily transfer limit")
    else:
        print("Exceeded single transfer limit")

#Deposit to account
#Assumes perfect conditions - checked beforehand?
def depositPure(accNum, amount):
    maf = open("MAF.txt", "r")
    lines = maf.readlines()
    maf.close()
    write = 0
    maf = open("MAF.txt", "w")
    for line in lines:
        num = line[:7]
        i2 = line.index(' ', 9)
        balance = int(line[8:i2])
        name = line[i2+1:]
        if int(num) == int(accNum):
            newBalance = int(balance) + int(amount)
            newLine = str(accNum) + ' ' + str(newBalance) + ' ' + str(name)
            maf.write(newLine)
        else:
            maf.write(line)

#Withdraw from account
#Assumes perfect conditions - checked beforehand?
def withdrawPure(accNum, amount):
    maf = open("MAF.txt", "r")
    lines = maf.readlines()
    maf.close()
    write = 0
    maf = open("MAF.txt", "w")
    for line in lines:
        num = line[:7]
        i2 = line.index(' ', 9)
        balance = int(line[8:i2])
        name = line[i2+1:]
        if int(num) == int(accNum):
            newBalance = int(balance) - int(amount)
            newLine = str(accNum) + ' ' + str(newBalance) + ' ' + str(name)
            maf.write(newLine)
        else:
            maf.write(line)

#Transfer - calls deposit and withdraw
#Assumes perfect conditions - checked beforehand?
def transferPure(toAccNum, amount, fromAccNum):
    depositPure(toAccNum, amount)
    withdrawPure(fromAccNum, amount)

def updateAccountsHash():
    maf = open("MAF.txt", "r")
    lines = maf.readlines()
    for line in lines:
        mafLine = line.split(" ", 2)
        mafAccNum = mafLine[0]
        mafAccName = mafLine[2]
        # Associate account name with account number
        accountsHash[mafAccNum] = mafAccName

# Use this function if deleted account numbers can be used for create
#Create account
def create(accNum, accName):
    #this needs to be sorted by account number when we create an account num
    if 'accNum' not in accountsHash:
        maf = open("MAF.txt", "r")
        lines = maf.readlines()
        maf.close()
        write = 0
        open('MAF.txt', 'w').close()
        maf = open("MAF.txt", "w")
        for line in lines:
            tNum = int(line[:7])
            if int(accNum) < tNum and write == 0:
                maf.write(accNum + " " + "000" + " " + accName)
                write = 1
            maf.write(line)
        if write == 0:
            maf.write(accNum + " " + "000" + " " + accName)
        maf.close()

#Delete account
def delete(accNum):
    maf = open("MAF.txt", "r")
    lines = maf.readlines()
    count = 0
    found = 0
    for line in lines:
        tempNum = line[:7]
        if tempNum == accNum:
            index = count
            found = 1
        count +=1
    if found ==1:
        del lines[index]
        maf.close()
        open('MAF.txt', 'w').close()
        maf = open('MAF.txt',"a")
        for line in lines:
            maf.write(line)
        maf.close()
    

#def createNewMAF():
#    oldMaf = open('MAF.txt', 'w')


    #maf = open('MAF.txt', 'w')


#mainline

clearMasterTSF()
mergeTSF()
handleTSF()