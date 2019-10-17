#327 QUINTERAC Front End Rapid Prototype (Assignment 2)
#The Xtreme Team
#Oct 18, 2019

import re
import os
def accNumDecOnly(string):
    restricted = re.compile(r'[^0-9]')
    string = restricted.search(string)
    return not bool(string)

#check if account num is valid
def accNumValid(accNum):
        if len(accNum) == 7: #length must be 7
            print("7")
            if accNum[0] != "0": #must not begin with zero
                print("8")
                if accNumDecOnly(accNum) == True:
                    print("9")
                    return 1
                else:
                    errorMsg("Account number must be decimals only")
                    return 0
            else:
                errorMsg("Accout number must not begin with a 0")
                return 0
        else:
            errorMsg("Account number must be 7 decimals long")
            return 0

#see if account number exists in vaf file
def accNumExists(accNum):
    exists = 0
    #Constant time check in dictionairy for account number
    if accNum in accountsList:
        exists = 1
    return exists

#get account balance and daily transaction information an account
#backend doesn't exist right no, so this is pseudo for this draft
# Transaction type 1= deposit, 2 = withdraw, 3 = transfer
def getAccBalance(accNum, transactionType):
    amount = 10000 #temp to allow testing
    dailyAmount = [0,0,0]
    amount = backendDict[accNum].amount
    dailyAmount.append(backendDict[accNum].dailyAmountDeposit)
    dailyAmount.append(backendDict[accNum].dailyAmountWithdraw)
    dailyAmount.append(backendDict[accNum].dailyAmountTransfer) 
    return amount, dailyAmount[transactionType-1]

#Update the amount you have put in or withdraw after a transaction for a specific account
# And update the daily amount you have used for each type of transaction
def updateDailyAmount(accNum, amount, transactionType):
    backendDict[accNum].amount += amount
    if transactionType == 1:
        backendDict[accNum].dailyAmountDeposit += amount
    elif transactionType == 2:
        backendDict[accNum].dailyAmountWithdraw += amount
    else:
        backendDict[accNum].dailyAmountTransfer += amount
    

#see if account name contains only alphanumeric characters
def accNameAlphaNum(string):
    restricted = re.compile(r'[^a-zA-Z0-9" "]')
    string = restricted.search(string)
    return not bool(string)

#see if account name is valid
def accNameValid(accName):
    if len(accName) >= 3 and len(accName) <= 30: #make sure name is correct length
        print("10")
        if accName[0] != " " or accName[-1] != " ": #must start and end with acceptable characters
            print("11")
            if accNameAlphaNum(accName) == True:
                return 1
            else:
                errorMsg("Alphanumeric characters only for account name")
                return 0
        else:
            errorMsg("Account name cannot start or end with a space/blank character")
            return 0
    else:
        errorMsg("Account name should be 3-30 alphanumeric characters long")
        return 0

#ERROR MESSAGES
def invalidInputA():
    print("Invalid input")

#ERROR MESSAGES
def invalidInputB(inputAction):
    print("Invalid input: " + inputAction)

#ERROR MESSAGES
def errorMsg(error):
    print(error)

#handle input from user
def handleKeyboardInput():
    action = input("Enter command: ")
    #take input, pass to action handler
    valid = actionHandler(action)
    if valid == 0:
        invalidInputB(action)

#login at beginning of session and initialize accounts and balances for the day
def login():
    global status
    #set status to login
    status = "login"
    print("Status: " + status)
    #Read the valid accounts file -> replace demofile.txt with valid accounts file
    global vaf
    vaf = open(r"C:\Users\hyper\source\repos\vaf.txt", "r")
    toWrite.clear() # Clear statements to write to tsf
    #Clear and initialize new hashtable/dictionairy 
    accountsList.clear()
    backendDict.clear()
    vaf.seek(0) 
    for x in vaf:
        accountsList[x.strip()] = 0
        backendDict[x.strip()] = Backend()
    # Loops through the file and reads every line (useful for reading accounts)
    #for x in vaf:
    #    print(x)

#logout method, logs out and writes all of the days transactions to the TSF
def logout():
    #set status to logout and write to tsf
    global status
    status = "logout"
    print("Status: " + status)
    vaf.close()
    tsf = open(r"C:\Users\hyper\source\repos\tsf.txt", "w+")  # Using "a" will append, "w" will overwrite
    for entry in toWrite:
        tsf.write(entry)
    tsf.write("EOS " + "0000000" + " " + "000" + " " + "0000000" + " " + "***\n") # end the tsf with an EOS transaction code (append to end)
    # Print TSF
    tsf.seek(0) 
    for line in tsf:
        print(line)
    # Close TSF
    tsf.close()
    print("\nWelcome") 
    print("Please Login to Begin Transactions") #Added to ensure user knows that they should login

#set status to ATM when specified
def setatm():
    global status
    status = "atm"
    print("Status: " + status)

#set status to AGENT when specified
def setagent():
    global status
    status = "agent"
    print("Status: " + status)

#create a new account
def createAccount(action):
    inputCommand = action.split(" ", 2);
    #Make sure length is 3 to avoid crashes (createacc, num, name)
    if len(inputCommand) == 3:
        accNum = inputCommand[1]
        accName = inputCommand[2]
        if accNumValid(accNum) == 1: #see if proposed account number meets all restrictions
            if accNumExists(accNum) == 0: #see if proposed account name meets all restrictions
                if accNameValid(accName) == 1:
                    print("12")
                    #write new account to VAF
                    vaf1 = open(r"C:\Users\hyper\source\repos\vaf.txt", "r")  # "a" will append, "w" will overwrite
                    lines = vaf1.readlines()
                    vaf1.close()
                    vaf1 = open(r"C:\Users\hyper\source\repos\vaf.txt", "w")
                    for line in lines:
                        if line.strip("\n") != "0000000": #temporarily update VAF without using backend, will be removed when back end is programmed
                            vaf1.write(line)
                    vaf1.close()
                    vaf1 = open(r"C:\Users\hyper\source\repos\vaf.txt", "a")
                    vaf1.write(accNum)
                    vaf1.write("\n" + "0000000")
                    vaf1.close()
                    # Save to tsf file
                    toWrite.append("NEW " + accNum + " " + "000" + " " + "0000000" + " " + accName+"\n")
                    print("Account " + accNum + " created successfully.")
                    return 1
                else:
                    return 0
            else:
                errorMsg("Account number exists")
                return 0
        else:
            return 0
    else:
        errorMsg("Not enough arguments. Please follow the format: createAccount 1234567 AccountName")
        return 0


# Note about delete - If you created a new account, you cannot delete it within the same session
# I, personally, thought this was a bug but in the requirements it says 'no transactions on this new account should be accepted this session'
# So, you know what, pretty good, close enough
# But if you wanted to know the reason, it's because login() opens the vaf.txt file and stores it in a variable vaf
# When you do createAccount(), it updates the vaf.txt file with the new account number, BUT the contents of the variable vaf is still the old vaf.txt
# So even though vaf.txt is new, vaf the variable still contains the old account numbers

#I think there's a restriction in DELETEACCOUNT that you can only delete an account with no money in it ... could be wrong, worth checking
#because it could be a restriction we have to work in

#delete an existing account
def deleteAccount(action):
    inputCommand = action.split(" ", 2);
    # Make sure length is 3 to avoid crashes (del, num, name)
    if len(inputCommand) == 3:
        accNum = inputCommand[1]
        accName = inputCommand[2]
        if accNumValid(accNum) == 1: #make sure account number is valid
            if accNumExists(accNum) == 1: #make sure account name is valid
                if accNameValid(accName) == 1:
                    print("12")
                    # delete the account successfully, write to VAF
                    vaf1 = open(r"C:\Users\hyper\source\repos\vaf.txt", "r")  # "a" will append, "w" will overwrite
                    lines = vaf1.readlines()
                    vaf1.close()
                    vaf1 = open(r"C:\Users\hyper\source\repos\vaf.txt", "w")
                    for line in lines:
                        if line.strip("\n") != str(accNum): #temporarily update VAF without using backend, will be changed
                            vaf1.write(line)
                    vaf1.close()
                    # Save to tsf file
                    toWrite.append("DEL " + accNum + " " + "000" + " " + "0000000" + " " + accName+"\n")
                    print("Account " + accNum + " deleted successfully.")
                    return 1
                else:
                    return 0
            else:
                errorMsg("Account number does not exist")
                return 0
        else:
            return 0
    else:
        errorMsg("Not enough arguments. Please follow the format: deleteAccount 1234567 AccountName")
        return 0

#deposit to an existing account
def deposit(action):
    print("Deposit")
    global status
    if status == "atm":
        limit = 200000 #from assignment requirements
    elif status == "agent":
        limit = 99999999 #from assignment requirements
    else:
        return 0
    inputCommand = action.split(" ", 2);
    # Make sure length is 3 to avoid crashes (dep, num, amount)
    if len(inputCommand) == 3:
        accNum = inputCommand[1]
        amount = inputCommand[2]
        if accNumValid(accNum) == 1: #make sure account number is valid ... i don't think we need this one, all it changes is error message
            if accNumExists(accNum) == 1: #make sure account actually exists
                if accNumDecOnly(amount) == True: #make sure amount is valid
                    if len(amount) >= 3 and len(amount) <= 8: #are these supposed to be <= or just <
                        currentAmount, dailyAmount = getAccBalance(accNum,1)                                               
                        if int(amount) <= min(limit,currentAmount,(500000-dailyAmount)):
                                toWrite.append("DEP " + accNum + " " + amount + " " + "0000000" + " " + "***"+"\n")
                                updateDailyAmount(accNum,int(amount),1)
                        else:
                            errorMsg("Amount exceeds the deposit limit")
                            return 0
                    else:
                        errorMsg("Amount should be between 3 and 8 decimal digits")
                        return 0
                else:
                    errorMsg("Amount should be decimals only")
                    return 0
            else:
                errorMsg("Account number does not exist")
                return 0
        else:
            return 0
    else:
        errorMsg("Not enough arguments. Please follow the format: deposit accountNumber amount")
        return 0


def withdraw(action):
    print("Withdraw")
    global status
    if status == "atm":
        limit = 200000 #from assignment requirements
    elif status == "agent":
        limit = 99999999 #from assignment requirements
    else:
        return 0
    inputCommand = action.split(" ", 2);
    # Make sure length is 3 to avoid crashes
    if len(inputCommand) == 3: #(wdr, accnum, amount)
        accNum = inputCommand[1]
        amount = inputCommand[2]
        if accNumValid(accNum) == 1: #not sure we need this, see deposit
            if accNumExists(accNum) == 1: #make sure acc number exists THIS IS THE IMPORTANT CHECK
                if accNumDecOnly(amount) == True: #make sure amount is decimal
                    if len(amount) >= 3 and len(amount) <= 8: #are these supposed to be <= or just <
                        currentAmount, dailyAmount = getAccBalance(accNum,2) 
                        if int(amount) <= min(limit,currentAmount,(500000-dailyAmount)): #check all restrictions
                            toWrite.append("WDR " + "0000000" + " " + amount + " " + accNum + " " + "***"+"\n")
                            updateDailyAmount(accNum,int(amount),2)
                                #WILL NEED TO WRITE NEW AMOUNT TO BACKEND AS WELL AS UPDATE THE DAILY
                        else:
                            errorMsg("Amount exceeds the withdrawal limit.")
                            return 0
                    else:
                        errorMsg("Amount should be between 3 and 8 decimal digits")
                        return 0
                else:
                    errorMsg("Amount should be decimals only")
                    return 0
            else:
                errorMsg("Account number does not exist")
                return 0
        else:
            return 0
    else:
        errorMsg("Not enough arguments. Please follow the format: withdraw accountNumber amount")
        return 0


def transfer(action):
    print("Transfer")
    global status
    if status == "atm":
        limit = 200000 #from assignment requirements
    elif status == "agent":
        limit = 99999999 #from assignment requirements
    else:
        return 0
    inputCommand = action.split(" ", 2);
    # Make sure length is 3 to avoid crashes
    if len(inputCommand) == 4: #(xfr, accnumout, accnumin, amount)
        accNumOut = inputCommand[1]
        accNumIn = inputCommand[2]
        amount = inputCommand[3]
        if accNumValid(accNumOut) == 1: #make sure all account numbers exist and are valid - may not need all these, see deposit
            if accNumExists(accNumOut) == 1:
                if accNumValid(accNumIn) == 1:
                    if accNumExists(accNumIn) == 1:
                        if accNumOut != accNumIn:
                            if accNumDecOnly(amount) == True:
                                if len(amount) >= 3 and len(amount) <= 8: #are these supposed to be <= or just < ???
                                    currentAmount, dailyAmount = getAccBalance(accNumOut,3) #get account information
                                    if int(amount) <= min(limit,currentAmount,(1000000-dailyAmount)): #check all restrictions to make sure account has money to withdraw
                                        toWrite.append("XFR " + accNumIn + " " + amount + " " + accNumOut + " " + "***"+"\n")
                                        updateDailyAmount(accNumOut,int(amount),3)

                                    else:
                                        errorMsg("Amount exceeds the withdrawal limit.")
                                        return 0
                                else:
                                    errorMsg("Amount should be between 3 and 8 decimal digits")
                                    return 0
                            else:
                                errorMsg("Amount should be decimals only")
                                return 0
                        else:
                            errorMsg("Account numbers shouldn't be the same")
                            return 0
                    else:
                        errorMsg("First account number does not exist")
                        return 0
                else:
                    return 0
            else:
                errorMsg("Second account number does not exist")
                return 0
        else:
            return 0
    else:
        errorMsg("Not enough arguments. Please follow the format: transfer accountNumberFrom accountNumberTo amount")
        return 0

# Handle action after it is inputted and processed through keyboard input, make sure action is valid given restrictions
def actionHandler(action):
    global status
    if action == "whereami":
        print("Action Handler")
        return 1
    if status == "logout":
        if action == "login": #can only login after logout
            login()
            return 1
        else:
            return 0
    elif status == "login":
        if action == "login":
            return 0
        elif action == "logout":
            logout()
            return 1
        elif action == "atm": #set to ATM mode
            setatm()
            return 1
        elif action == "agent": #set to AGENT mode
            setagent()
            return 1
        else:
            return 0
    elif status == "atm":
        if action == "logout":
            logout()
            return 1
        elif action == "atm": #can't do this in ATM
            return 0
        elif action == "agent": #can't do this in ATM
            return 0
        elif "createAccount" in action: #can't do this in ATM
            return 0
        elif "deleteAccount" in action: #can't do this in ATM
            return 0
        elif "deposit" in action: 
            deposit(action)
            return 1
        elif "withdraw" in action:
            withdraw(action)
            return 1
        elif "transfer" in action:
            transfer(action)
            return 1
        else:
            return 0
    elif status == "agent":
        if action == "logout":
            logout()
            return 1
        elif action == "atm": #can't do this in AGENT
            return 0
        elif action == "agent": #can't do this in AGENT
            return 0
        elif "createAccount" in action: #can't do this in AGENT
            createAccount(action)
            return 1
        elif "deleteAccount" in action: #can't do this in AGENT
            deleteAccount(action)
            return 1
        elif "deposit" in action: #can't do this in AGENT
            deposit(action)
            return 1
        elif "withdraw" in action: #can't do this in AGENT
            withdraw(action)
            return 1
        elif "transfer" in action: #can't do this in AGENT
            transfer(action)
            return 1
        else:
            return 0

#Backend class holds the amount each account has and how much 
# of the daily limit they have remaining for each transaction type
class Backend:
  def __init__(self):
    self.amount = 10000
    self.dailyAmountDeposit = 0
    self.dailyAmountWithdraw = 0
    self.dailyAmountTransfer = 0

#val = input("Enter your value: ")

# Main Function, runs continuously 

#           Main Description :
# The overall intention of the program is to implement all of the features of the front end
# and to provide a way to interact with the front end through a command line interface and 
# conduct full testing. Certain back end reliant features were simplified and replaced so that
# the front end could seamlessly work. Main program continuously processes user keyboard input 
# does programmed behaviour
# 1 input file vaf.txt containing a valid accounts file with any number of accounts is required in the working directory
# Accounts are added and removed from the file since backend is not coded yet
# 1 output file tsf.txt is required that is written by the program  on logout with the transaction from the day

# Run the program by typing the "this_file_name".py in the terminal in the working directory
# Shell scripts can be run on top of this program to feed  a sequence of commands into the program

if __name__ == "__main__":
    print(os.getcwd())
    status = "logout"
    print("Welcome")
    print("Please Login to Begin Transactions")
    accountsList = dict() # Use hashtable so that finding account number is constant time
    toWrite = [] # Transaction file statements to write after logout statement is executed
    backendDict = dict() #temporary backend dictionary only for testing frontend
    while 1:
        handleKeyboardInput()


#print(val)
