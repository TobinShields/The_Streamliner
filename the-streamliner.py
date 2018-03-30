#######################################
#
# The Streamliner v1.0
# Build By: Tobin Shields
#           Twitter - @TobinShields
#           Github  - https://github.com/TobinShields/
#                      
#######################################

#Import libs
import re              # Allow the use of the findall() function
import urllib.request  # Allow to grab web URLS and Website Content
import csv             # Allow for the exporting to a csv file
import os              # Allow the program to make and remove files
import sys             # Allow to restart the program and grab more addresses

# Print opening Banner
print("""
 _____ _            _____ _                            _ _                 
|_   _| |          /  ___| |                          | (_)                
  | | | |__   ___  \ `--.| |_ _ __ ___  __ _ _ __ ___ | |_ _ __   ___ _ __ 
  | | | '_ \ / _ \  `--. \ __| '__/ _ \/ _` | '_ ` _ \| | | '_ \ / _ \ '__|
  | | | | | |  __/ /\__/ / |_| | |  __/ (_| | | | | | | | | | | |  __/ |   
  \_/ |_| |_|\___| \____/ \__|_|  \___|\__,_|_| |_| |_|_|_|_| |_|\___|_|                                   
                                                                 Verion 1.0

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
file_choice = input("Do you want to filter a URL or a saved file? (url/file): ")

# Pull Data from source listed
while True:
    # If they chose a URL
    if file_choice == "url":
        #Grab URL from user
        url = input("Page URL: ")
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
        file_name = input("What file do you want to filter?: ")
        # Store document text as var
        file_contents = open(file_name).read()
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
export = input("Do you want to export this list? (y/n): ")

# Create the restart function that will be called at the end of building the file
def restartPrompt(file_type):
    print("The file has been exported as a file called " + full_file_name + ". Thanks for using The Streamliner!")
    print("\n")
    restart = input("Want to find more emails? (y/n): ")
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
        file_type = input("What kind of fileype (txt/csv): ")
        file_name = input("What do you want to name the file? (Extension will be applied automatically): ")
        full_file_name = file_name + "." + file_type
        
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


