#write your name and class into a file named intro.txt.
with open('intro.txt', 'w') as intro_file:
    intro_file.write("Name: John Doe\n")
    intro_file.write("Class: 10th Grade\n")
    


#create a file goals.txt and write 3 goals for this year.

with open('goals.txt', 'w') as goals_file:
    goals_file.write("1. Improve my math skills.\n")
    goals_file.write("2. Read at least 10 books.\n")
    goals_file.write("3. Participate in a school club.\n")

#Append "completed" to an existing file status.txt.
with open('status.txt', 'a') as status_file:
    status_file.write("completed\n")

#copy notes.txt to notes_backup.txt
with open('notes.txt', 'r') as notes_file:
    notes_content = notes_file.read()
with open('notes_backup.txt', 'w') as backup_file:
    backup_file.write(notes_content)

#rename temp.txt to final.txt
import os
os.rename('temp.txt', 'final.txt')

#Ask user for a filename and copy it to a backup folder.
import os
filename = input("Enter the filename to back up: ")
backup_folder = 'backup'
if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)
with open(filename, 'r') as original_file:
    content = original_file.read()
with open(os.path.join(backup_folder, filename), 'w') as backup_file:
    backup_file.write(content)
    