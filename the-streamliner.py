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
import sys             # Allow to check if arguments are passed through
import argparse        # Allows the use of flags from the command line

# You can clean up the help lines if you want
parser = argparse.ArgumentParser(description='"The Streamliner" is a simple Python utility that allows users to target a particular webpage or text file and filter all of the email addresses that contained within it. This tool is especially useful when distilling large web directories, cluttered or poorly formatted email lists, or web pages with mailto: links into a txt or csv file.')
parser.add_argument('--url', help='Provide the full URL to the target webpage that contains emails.', type=str) # url flag
parser.add_argument('--file', help='Provide the local path to the file that contains emails.', type=str) # file flag
parser.add_argument('--export', help='Type the name of the file you want to export (only .txt and .csv)', type=str) # export flag

args = parser.parse_args() # Allows you to call arguments using args.[argument]

#No Arguments Provided
if not len(sys.argv) > 1:
    # Print out the opening banner with help
    print("""
 _____ _            _____ _                            _ _
|_   _| |          /  ___| |                          | (_)
  | | | |__   ___  \ `--.| |_ _ __ ___  __ _ _ __ ___ | |_ _ __   ___ _ __
  | | | '_ \ / _ \  `--. \ __| '__/ _ \/ _` | '_ ` _ \| | | '_ \ / _ \ '__|
  | | | | | |  __/ /\__/ / |_| | |  __/ (_| | | | | | | | | | | |  __/ |
  \_/ |_| |_|\___| \____/ \__|_|  \___|\__,_|_| |_| |_|_|_|_| |_|\___|_|
                                                            Verion 1.1.1

Fork, Share, and Support this project on github:
https://github.com/TobinShields/The_Streamliner

"The Streamliner" is a simple Python utility that allows users to target a
particular webpage or text file and filter all of the email addresses that
contained within it. This tool is especially useful when distilling large
web directories, cluttered or poorly formatted email lists, or web pages
with mailto: links into a txt or csv file.

    Streamliner usage:
    --url          Provide the full URL to the target webpage that contains emails.
    --file         Provide the local path to the file that contains emails.
    --export       Type the name of the file you want to export (only .txt and .csv)

    NOTE: For both the URL and the file, the path must end in a text-based
    file extention such as .html or .txt. The program will throw errors
    otherwise.

    Example Usage:
    the-streamliner.py -u https://www.exmaple.com/staff-directory.html -e staff-emails.txt

    """)

# If arguments were provided, run program
else:
    # If user entered a URL as an argument
    if args.url is not None:
        url = args.url
        # Store HTML into a tmp file. This is removed during cleanup. This is done using the urllib.request lib import
        urllib.request.urlretrieve(url, "site.tmp")
        # Store all data from that file into a var using open()
        file_contents = open("site.tmp").read()
        # Cleanup and remove the .tmp file
        os.remove("site.tmp")
    elif args.file is not None:
        file_name = args.file
        # Store document text as var
        file_contents = open(file_name).read()

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

    # If the user opted to export the file
    if args.export is not None:
        # Grab file name and the file type
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
            print("\n")
            print("Your file has been exported as saved as " + full_file_name)

        # If csv is chosen, write it out
        elif file_type == "csv":
            # Using the csv lib make the file and write out to a new line per entry
            # This code borrowed directly from python docs
            with open(full_file_name, "w") as output:
                writer = csv.writer(output, lineterminator='\n')
                for val in email_list:
                    writer.writerow([val])
            print("\n")
            print("Your file has been exported as saved as " + full_file_name)

        # Throw and error if its the wrong file type
        else:
            print("\n")
            print("ERROR EXPORTING:")
            print("You did not list a valid exportable file type. You may only export out to a .txt or .csv file. Your file was NOT exported. ")
