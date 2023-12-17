# To-do list
# ----------
import datetime, sys
TASKS_FILE = r'Your_File_Here.txt'

def AddTask():
  # Get task and deadline
  label    = input('What is this task called?')
  deadline = input('When is this task due?')

  # Add task to the file
  file = open(TASKS_FILE,'a')
  file.write(f'\n  - {label} | Due: {deadline}')

  # Close the file
  file.close()

# Prints all tasks to the screen
def PrintTask():
  # Open file
  file = open(TASKS_FILE,'r')

  # Print contents of file
  print('------------------------------------\n')
  print( file.read() )

  # Close the file
  file.close()

# Deletes specified task
def DeleteTask():
  # Open file
  file  = open(TASKS_FILE,'r')

  # Get unwanted task
  label = input('What is the name of the task you have completed?')
  
  new = ''
  # Remove all occurences of this label
  for line in list(file):

    # Detects the unwanted task
    if label in line[ 4: ]:continue

    # Otherwise keep this task
    new = f'{new}{line}'

  # Change file
  file = open(TASKS_FILE,'w')
  file.write(new)
  
  # Close the file
  file.close()

# Prints current date and time
print( str(datetime.datetime.now())[:-10] )
print(
'''
#/*******************************************\ \n
#                   T A S K S                  \n
#                  - - - - - -                 \n
#\*******************************************/''' )

mode = None
while mode != 'q':
  print('\n\nYou may press \'q\' to quit')
  mode = input('Type \'v\' to view tasks, \'w\' to add a task and \'d\' to delete a task')

  match mode:
    # Reads current tasks from file
    case 'v':PrintTask()

    # Deletes specified task
    case 'd':DeleteTask()
      
    # Adds task to file
    case 'w':AddTask()
    
    # Quit application
    case 'q':break
    
    # Handles misinputs
    case other:print('Command not recognised')

  print('\n\n\n')
  
print('Application was quit!')
