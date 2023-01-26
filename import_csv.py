'''
for future ref: pandas r a much better, quicker, cleaner way of doing this.
it even outputs smth that is easier to read.
idk y they made us do all this but they did.
'''
#%%
'''
in this task, we were supposed to produce all of this in the form of functions.
the actual way this was supposed to be done will be found at the bottom'''
import csv

with open('user_details.csv', 'r') as csv_file: #opening and naming the file csv_file. the 'r' is telling it what mode to open it as. with means it will open and close alone.
    csv_read = csv.reader(csv_file, delimiter=',') #telling it to read everything and that it is all seperated by a comma
    for lines in csv_read: #now can start cleaning each bit of info if want to
#        print(lines) #just printing what the for loop is doing
        username = lines[4].split('@')[0] #performing cleaning function for line 4 to produce just the username from the email. cleaning is called transforming in tech world.
        print(lines[1], lines[2] + ', ' + username) #[] is index so u dont need to write .index.

#%%
'''
now we are going to write to new file using the above.
when u run this it shd open a new file that it created for u to add the new info to.
'''
import csv # import csv package
# import pandas as pd # import package pandas with alias pd

with open('user_details.csv', 'r') as csv_file: # opens the user details csv file in reading mode 'r'.
    csv_read = csv.reader(csv_file, delimiter=',') # creates a variable that represents reading the file, with the data seperated by ','.
    with open('new_details.csv', 'w') as csv_new_file: # creates a new csv file with name parsed in in write mode 'w'.
        csv_write = csv.writer(csv_new_file, delimiter=',') # creates a variable that represents the ability to write to the file.
        for lines in csv_read: # for loop that iterates through each row in the file, where 'lines' represents each row of information.
            username = lines[4].split('@')[0] # cleaning the email column, splitting at '@' to get everything in front of it.
            row = [lines[1], lines[2], username] # combines the individual columns into a list.
            csv_write.writerow(row) # writes each row to the new file.

# with open('user_details.csv', 'a') as csv_file:
#     csv_read = csv.reader(csv_file, delimiter=',')
#     csv_writer = csv.writer(csv_file, delimiter=',')
#     for lines in csv_read:
#         username = lines[4].split('@')[0]
#         # print(lines[1], lines[2], username)
#         row = [lines[1], lines[2], username]
#         csv_write.writerow(row)


#%%
'''
Mode	Description
'r'	This is the default mode. It Opens file for reading.
'w'	This Mode Opens file for writing. If file does not exist, it creates a new file. If file exists it truncates the file.
'x'	Creates a new file. If file already exists, the operation fails.
'a'	Open file in append mode. If file does not exist, it creates a new file.
't'	This is the default mode. It opens in text mode.
'b'	This opens in binary mode.
'+'	This will open a file for reading and writing (updating)
'''

#%%
'''
same thing but using functions:
'''



import csv #importing package

def open_file(file_name):
    with open(file_name, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        new_list_of_lists = []
        for line in csvreader:
            new_list_of_lists.append(line)
        return new_list_of_lists

def transform_csv(file_name):
    old_data = open_file(file_name)
    clean_data = []
    for lines in old_data:
        username = lines[4].split('@')[0]
        row = [lines[1], lines[2], username]
        clean_data.append(row)
    return clean_data

def write_csv(old_file, new_file):
    with open(new_file, "w") as csv_writer:
        csvwriter = csv.writer(csv_writer)
        csvwriter.writerows(transform_csv(old_file))

write_csv("user_details.csv", "new_file.csv")

