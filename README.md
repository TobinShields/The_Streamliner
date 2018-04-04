# The Streamliner v1.1.2
>"The Streamliner" is a simple Python utility that allows users to target a particular webpage or text file and filter all of the email addresses that contained within it. Written using Python 3, this tool is especially useful when distilling large web directories, cluttered or poorly formatted email lists, or web pages with mailto: links into a txt or csv file

### How to use:
Streamliner usage:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-u, --url          Provide the full URL to the target webpage that contains emails.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-f, --file         Provide the local path to the file that contains emails.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-e, --export       Type the name of the file you want to export (only .txt and .csv)  
  
**NOTE**: For both the URL and the file, the path must end in a text-based file extention such as .html or .txt. The program will throw errors otherwise.  
  
**Example Usage**:  
>the-streamliner.py --url https://www.exmaple.com/staff-directory.html --export staff-emails.txt  
>the-streamliner.py -f contact-page.txt -e contact-list.csv

**PRO TIP**: If the URL you are requesting isn't working, try saving the website locally (using ctrl + s on any page). If is still crashing or not finding email addresses, try literally just copying the entire page and throwing it into a raw txt file and running that through the program. 

## Disclamer
While “The Streamliner” is a fairly innocuous tool, it was built to help aid penetration testers during the information gathering phase of a project. While OSINT is not illegal, as always, be sure that you have the permission of whoever you are collecting information on. This should not be a very noisy program, but it will show that you requested a given page.

## Suport this project!
I am fairly new to Python. If you see a better way of doing something, then feel free to contribute and make this better! Also, if you want to add a feature or expand the functionality of this program then I would gladly welcome the additions. See the [changelog](https://github.com/TobinShields/The_Streamliner/blob/master/changelog.md) for information of version differences. 

A big thanks to our awesome contributors!:
* Trevor Warner
* Jacob Bickle

