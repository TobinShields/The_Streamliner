#######################################
#
# The Streamliner v1.1
# Build By: Tobin Shields
#           Twitter - @TobinShields
#           Github  - https://github.com/TobinShields/
# Other Contributors:
#           Trevor Warner
#           Github  - https://github.com/trevor34/
#
#######################################

#Import libs
import re              # Allow the use of the findall() function
import urllib.request  # Allow to grab web URLS and Website Content
import csv             # Allow for the exporting to a csv file
import os              # Allow the program to make and remove files
import sys             # Allow to restart the program and grab more addresses
import argparse        # Allows the use of flags from the command line

# You can clean up the help lines if you want
parser = argparse.ArgumentParser(description='"The Streamliner" is a simple Python utility that allows users to target a particular webpage or text file and filter all of the email addresses that contained within it.') #
parser.add_argument('--url', help='path to url', type=str) # url flag
parser.add_argument('--file', help='path to file', type=str) # file flag
parser.add_argument('--export', help='name of file you want to export to with file extention (txt or csv)', type=str) # export flag

args = parser.parse_args() # Allows you to call arguments using args.[argument]
# Example: args.url

if not args.url == None and not args.file == None:
    '''If both --url and --file is used, the program is closed'''
    print("\n\tYou cannot use both --url and --file")
    exit()

# Print opening Banner
print("""
 _____ _            _____ _                            _ _
|_   _| |          /  ___| |                          | (_)
  | | | |__   ___  \ `--.| |_ _ __ ___  __ _ _ __ ___ | |_ _ __   ___ _ __
  | | | '_ \ / _ \  `--. \ __| '__/ _ \/ _` | '_ ` _ \| | | '_ \ / _ \ '__|
  | | | | | |  __/ /\__/ / |_| | |  __/ (_| | | | | | | | | | | |  __/ |
  \_/ |_| |_|\___| \____/ \__|_|  \___|\__,_|_| |_| |_|_|_|_| |_|\___|_|
                                                                 Verion 1.1

Fork, Share, and Support this project on github:
https://github.com/TobinShields/The_Streamliner
|===========================================================================|

"The Streamliner" is a simple Python utility that allows users to
target a particular webpage or text file and filter all of the email
addresses that contained within it. This tool is especially useful
when distilling large web directories, cluttered or poorly formatted
email lists, or web pages with mailto: links into a txt or csv file.
""")

#Choose between a URL and a saved HTML file
if args.url == None and args.file == None:
    file_choice = input("Do you want to filter a URL or a saved file? (url/file): ")
# If a flag was chosen
elif not args.url == None:
    file_choice = 'url'
else:
    file_choice = 'file'

# Pull Data from source listed
while True:
    # If they chose a URL
    if file_choice == "url":
        #Grab URL from user
        if not args.url == '':
            url = input("Page URL: ")
        else:
            url = args.url
        # Store HTML into a tmp file. This is removed during cleanup
        # This is done using the urllib.request lib
        urllib.request.urlretrieve(url, "site.tmp")
        # Store all data from that file into a var using open()
        file_contents = open("site.tmp").read()
        # Break out of the loop and move on
        break

    # If they chose a local file
    elif file_choice == "file":
        # Grab the name of the file fromt he user
        if args.file == None:
            file_name = input("What file do you want to filter?: ")
        else:
            file_name = args.file
        # Store document text as var
        file_contents = open(file_name).read()
        # Fixes a bug in restartPrompt
        temp = open("site.tmp")
        # Break out of the loop and move on
        break

    # If they did not type url or file (usually a typo)
    else:
        print("\n")
        print("You did not not enter a correct value. ")
        file_choice = input("Do you want to filter a URL or a saved file? (url/file): ")

# Using "re" lib define what pattern we are looking for and store those into a var
found_emails = re.findall(r'[\w\.-]+@[\w\.-]+', file_contents)

# Build an empty list to store all emails
email_list = []
# Loop through and find all emails and append them to the list
for email in found_emails:
    email_list.append(email)
# Remove all duplicates fromt he list
email_list = list(set(email_list))
# Print everything in the list, and sepereate each list item with a line break
print("\n")
print(*email_list, sep="\n")

# Show how many addresses were found and print a seperator
print("\n")
print("|======== A total of " + str(len(email_list)) + " email addresses were on this page ========|")

# Prompt to export to another file
print("\n")
if args.export == None:
    export = input("Do you want to export this list? (y/n): ")
else:
    export = 'y'

# Create the restart function that will be called at the end of building the file
def restartPrompt(file_type):
    print("The file has been exported as a file called " + full_file_name + ". Thanks for using The Streamliner!")
    print("\n")
    restart = input("Want to find more emails? (y/n): ")
    temp.close()
    file_contents.close()
    if restart == "y":
        # Clean up and remove the tmp file using the os lib
        os.remove("site.tmp")
        # Print 50 new lines to clear the screen
        print ("\n" * 50)
        # Restart the program using the sys lib
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        # Clean up and remove the temp file
        os.remove("site.tmp")
        exit()

# If they say yes to exporting
if export == "y":
    while True:
        # Build file name
        if args.export == None:
            file_type = input("What kind of fileype (txt/csv): ")
            file_name = input("What do you want to name the file? (Extension will be applied automatically): ")
            full_file_name = file_name + "." + file_type
        else:
            full_file_name = args.export
            file_type = args.export[-3:]

        # If txt is chosen, write it out
        if file_type == "txt":
            # Make the file and allow writing to it
            writeOut = open(full_file_name, "w")
            # Simple for loop that writes out each email as a new line to the .txt document
            for email in email_list:
                writeOut.write(email +"\n")
            # Close the connection and disable editing
            writeOut.close()
            # Restart the program
            restartPrompt(file_type)

        # If csv is chosen, write it out
        elif file_type == "csv":
            # Using the csv lib make the file and write out to a new line per entry
            with open(full_file_name, "w") as output:
                writer = csv.writer(output, lineterminator='\n')
                for val in email_list:
                    writer.writerow([val])
                # Restart the program
                restartPrompt(file_type)

        # If they did not type either txt or csv (usually a typo)
        else:
            print("Incorrect filetype, you must choose between txt and csv")

# If they say no to exporting
else:
    print("That's alright--Thanks for using the program!")
