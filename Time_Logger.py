import time
import sys
import os # Used for tag FUN (can all be deleted)
import re
# Jaden M Graner 2019
# Minimaly commented as it's pretty self explanitory

# v Always in seconds, needs to always be on line 9 so it can be written to properly
total_time = 0
start_time = 0
Timestep = 1 # 1=seconds, 2=minutes, 3=hours

def Input_Splitter(Input):
    Input = [int(s) for s in Input.split() if s.isdigit()] # "S" is the Number being looked for for the grix dimentions (Returns Array of all Numbers found)
    Input = Input[0]
    return Input

def Get_Units(Timestep):
    if Timestep == 1:
        T = 'seconds'
    elif Timestep == 2:
        T = 'minutes'
    elif Timestep == 3:
        T = 'hours'
    return(T)

def Running():
    if start_time > 0:
        return(time.time()-start_time)
    else:
        return(0)
def Save():
    Path = os.path.dirname(os.path.realpath(__file__))
    Path = (Path+"/Time_Logger.py")
    try:
        with open(Path,'r') as File:
            Data = File.readlines()
        Data[8] = ('total_time = '+str(total_time)+'\n')
        with open(Path,'w') as File:
            File.writelines(Data)
        print('Saved Successfully')
    except:
        print('Save Failed, Data Remaining Local')
        print('Now would be a good time to wrte down your total time:')
        print('Total Time:', total_time, 'Seconds')

# Just For FUN v
Mem,Mem2 = 0,0
MemP = ['You used "Bad grammer"','You used "Mental deficiency"','You used "Confused mumble"']
MemL = ['*Its not very effective*','"Glancing blow!", data logger takes 5 damage','Data logger is impressed by your skills','It misses','This makes data logger very sad','The only person you hurt is yourself, you take 10 damage']
Texm = ['-Data Logger-','hp-----------','                 -Sweaty Nerd-','                  hp---       ','------------------------------']
# Just For FUN ^

print('Welcome to the python data logger, enter "help" for a help menue or type "done" to stop')

Run = True
while Run == True:
    Input = input()
    if Input == 'help':
        print('Total time:',total_time,'seconds')
        print('Running time:',Running(),'seconds')
        print('Time is currently in:',Get_Units(Timestep))
        print('Start logging time: start')
        print('Stop logging time: stop')
        print('Manually add time: add')
        print('Show current time: show')
        print('Change time units: units')
        print('Wipe stored data: delete')


    elif Input == 'start':
        start_time = time.time()

    elif Input == 'stop':
        if start_time != 0:
            end_time = time.time()
            run_time = end_time - start_time
            total_time += run_time
            print('Time:',run_time)
            start_time = 0
            Save()
        else:
            print('~No time logged')

    elif Input == 'add':
        if Timestep == 3:
            print('Enter Time in hours:')
            Input = input()
            try:
                total_time += (Input_Splitter(Input)*3600)
            except:
                print('Invalid input')
        elif Timestep == 2:
            print('Enter Time in minutes:')
            Input = input()
            try:
                total_time += (Input_Splitter(Input)*60)
            except:
                print('Invalid input')
        elif Timestep == 1:
            print('Enter Time in seconds:')
            Input = input()
            try:
                total_time += Input_Splitter(Input)
            except:
                print('Invalid input')
        Save()

    elif Input == 'show':
        if Timestep == 1:
            print('Logged time:',total_time)
            print('Runnning time:',Running())
        if Timestep == 2:
            print('Logged time:',total_time//60)
            print('Runnning time:',Running()//60)
        if Timestep == 3:
            print('Logged time:',total_time//3600)
            print('Runnning time:',Running()//3600)

    elif Input == 'units':
        T = Get_Units(Timestep)
        print('Current unit is: ',T)
        Picking = True
        while Picking == True:
            print('To chang enter 1,2,or 3 for seconds, minutes, and hours; or press c to cancel:')
            Input = input()
            if Input == 'C':
                Picking = False
            else:
                try:
                    New_Timestep = Input_Splitter(Input)
                    if (New_Timestep < 1) or (New_Timestep > 3):
                        print('Invalid input')
                        print('Current unit is still: ',T)
                    else:
                        Timestep = New_Timestep
                        T = Get_Units(Timestep)
                        print('Valid input')
                        print('Current unit is now: ',T)
                        Picking = False
                except:
                    print('Invalid input')
                    print('Current unit is still: ',T)

    elif Input == 'done':
        Run = False

    elif Input == 'delete':
        print('This will destroy all past saved data')
        print('Are you sure you want to do this?  y/n')
        Input = input()
        if Input == 'yes' or Input == 'y':
            print('Oof')

    else: # All just FUN v
        rows, columns = os.popen('stty size', 'r').read().split()
        loop = int(rows[0]+rows[1])

        for i in range((loop//2-1)):
            print("\n")
        for i in range(loop):
            print("\033[F"+"\033[F")

        time.sleep(0.5)

        for i in Texm:
            print(i)
        print(MemP[Mem2]+"\n"+"\n")
        print('------------------------------')
        time.sleep(3)
        print("\033[F"+"\033[F"+MemL[Mem]+"\n")
        time.sleep(4)
        print("\n"+"\n"+'Welcome to the python data logger, enter "help" for a help menue or type "done" to stop')


        for i in range((loop//2)-2):
            print("\n")
        for i in range(loop-4):
            print("\033[F"+"\033[F")
        if start_time != 0:
            start_time += 2
        Mem += 1
        Mem2 += 1
        if Mem == len(MemL):
            Mem = 0
        if Mem2 == len(MemP):
            Mem2 = 0
