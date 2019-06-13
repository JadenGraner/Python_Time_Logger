import time
import sys
import os # Used for tag FUN (can all be deleted)
import re
# Jaden M Graner 2019
# Minimaly commented as it's pretty self explanitory

# v Always in seconds, needs to always be on line 9 so it can be written to properly #Previous time 16772.66533255577
total_time = 0
start_time = 0
Timestep = 0 # 0=seconds, 1=minutes, 2=hours

def Input_Splitter(Input):
    Input = [int(s) for s in Input.split() if s.isdigit()] # "S" is the Number being looked for for the grix dimentions (Returns Array of all Numbers found)
    Input = Input[0]
    return Input

def Get_Units(Timestep):
    if Timestep == 0:
        T = 'seconds'
    elif Timestep == 1:
        T = 'minutes'
    elif Timestep == 2:
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
    except Exception as e:
        print('Save FAILED, Data remaining local')
        print('Now would be a good time to wrte down your total time:')
        print('Total Time:', total_time, 'Seconds')
        print('Error:',e)

print('Welcome to the python data logger, enter "help" for a help menu or type "done" to stop')

Run = True
while Run == True:
    Input = input()
    if Input == 'help':
        print('')
        print('Saved time:',total_time,'seconds')
        print('Running time:',Running(),'seconds')
        print('Time is currently displayed in:',Get_Units(Timestep))
        print('')
        print('start  <-Start logging time')
        print('Stop   <-stop logging time')
        print('')
        print('add    <-Manually add time')
        print('sub    <-Manually subtract time')
        print('')
        print('show   <-Show current time')
        print('units  <-Change time units')
        print('wipe   <-Wipe stored data')


    elif Input == 'start':
        print('Now logging time')
        start_time = time.time()

    elif Input == 'stop':
        if start_time != 0:
            print('Stopping time logging')
            end_time = time.time()
            run_time = end_time - start_time
            total_time += run_time
            print('Time:',run_time)
            start_time = 0
            Save()
        else:
            print('~No time logged')

    elif Input == 'add':
        print('Enter Time to add in:',Get_Units(Timestep))
        Input = input()
        try:
            total_time += (Input_Splitter(Input)*(60**Timestep))
            print('Added:',(Input_Splitter(Input)*(60**Timestep)),'Seconds')
        except Exception as e:
            print('Invalid input')
            print('Error:',e)
        Save()

    elif Input == 'sub':
        print('Enter time to subtract in:',Get_Units(Timestep))
        Input = input()
        try:
            total_time -= (Input_Splitter(Input)*(60**Timestep))
            print('Removed:',(Input_Splitter(Input)*(60**Timestep)),'seconds')
        except Exception as e:
            print('Invalid input')
            print('Error:',e)
        Save()

    elif Input == 'show':
        print('Logged time:',total_time//(60**Timestep),Get_Units(Timestep))
        print('Runnning time:',Running()//(60**Timestep),Get_Units(Timestep))

    elif Input == 'units':
        print('Current unit is: ',Get_Units(Timestep))
        Picking = True
        while Picking == True:
            print('To chang enter 0,1,or 2 for seconds, minutes, and hours; or press c to cancel:')
            Input = input()
            if Input == 'C':
                Picking = False
            else:
                try:
                    New_Timestep = Input_Splitter(Input)
                    if (New_Timestep > 2):
                        print('Invalid input')
                        print('Current unit is still: ',T)
                    else:
                        Timestep = New_Timestep
                        print('Valid input')
                        print('Current unit is now: ',Get_Units(Timestep))
                        Picking = False
                except Exception as e:
                    print('Invalid input')
                    print('Current unit is still: ',T)
                    print('Error:',e)

    elif Input == 'done':
        Run = False
        if start_time != 0:
            end_time = time.time()
            run_time = end_time - start_time
            total_time += run_time
            print('Saved time:',run_time//(60**Timestep),Get_Units(Timestep))
            start_time = 0
        Save()

    elif Input == 'wipe':
        print('This will destroy all past saved data')
        print('Are you sure you want to do this?  y/n')
        Input = input()
        if Input == 'yes' or Input == 'y':
            total_time = 0
            Save()
            print('Time wiped')
        else:
            print('Time not wiped')

    else:
        print('Invalid input')
