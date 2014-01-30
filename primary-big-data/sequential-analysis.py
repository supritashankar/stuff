ss:project1.2 supritashankar$ vim solution.py 

#!/usr/bin/python
import sys
import re

def main(argv):
        pattern1 = re.compile(r'^en ')
        pattern2 = re.compile(r'^en [a-z]')
        pattern3 = re.compile(r'^en (Media|Special|Talk|User|User_talk|Project|Project_talk|File|File_talk|MediaWiki|MediaWiki_talk|Template|Template_talk|Help|Help_talk|Category|Category_talk|Portal|Wikipedia|Wikipedia_talk):')
        pattern4 = re.compile(r'\.(ico|jpg|gif|png|JPG|PNG|txt) [0-9]')
        pattern5 = re.compile(r'^en (Main_Page|Hypertext_Transfer_Protocol|404_error/|Favicon.ico|Search) [0-9]')
        data = []
        for line in sys.stdin:
            if pattern1.findall(line):
              if pattern3.findall(line) or pattern4.findall(line) or pattern5.findall(line) or pattern2.findall(line):
                continue

              data.append(line)
        print len(data)

if __name__ == "__main__":
        main(sys.argv)
