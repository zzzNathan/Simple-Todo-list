# To-do list
# ----------
import datetime, sys
TASKS_FILE = r'Your_file_here.txt'

def AddTask():
  # Get task and deadline
  label    = input('What is this task called?')
  deadline = input('When is this task due?')

  # Add task to the file
  file = open(TASKS_FILE,'a')
  file.write(f'\n  - {label} | Due: {deadline}')

  # Close the file
  file.close()

# Prints current date and time
print( str(datetime.datetime.now())[:-10] )

# Prints a nice heading
print(
'''
#/*******************************************\ \n
#                   T A S K S                  \n
#                  - - - - - -                 \n
#\*******************************************/''' )

mode = None
while mode != 'q':

  # Get mode of use from user
  print('\n\nYou may press \'q\' to quit')
  mode = input('Type \'v\' to view tasks and \'w\' to enter a new task')

  match mode:
    # Reads current tasks from file
    case 'v':
      file = open(TASKS_FILE,'r')
      print('------------------------------------\n')
      print( file.read() )
      file.close()
      
    # Adds task to file
    case 'w':AddTask()
    
    # Quit application
    case 'q':break
    
    # Handles misinputs
    case other:print('Command not recognised')

  print('\n\n\n')
  
print('Application was quit!')
