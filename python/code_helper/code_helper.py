'''
    A little python script that takes in a problem URL from supported sites (gfg, hr, lc) 
    fetches the problem name and creates a file with name as that of the problem
    in the current directory with the problem link added as a comment(python)
    and launches the default editor to that file ready to code.
'''

from bs4 import BeautifulSoup
import requests, sys, os

'''
    Check if URL is provided or not.
'''
if len(sys.argv) < 2:
    print('URL not specified')
    exit()
else:
    pageURL = sys.argv[1]

'''
    Split the URL wrt '/' making it easier to parse the problem description.
'''
title_list = pageURL.split('/')

'''
    Removes empty items from the list
'''
title_list = [x for x in title_list if x]

'''
    Portals like leetcode and hackerrank have suffixes in the URLs such as 'problem' or 'description'
    This will check for such suffixes and delete them from the list.
'''
if title_list[-1] == 'problem' or title_list[-1] == '0' or title_list[-1] == 'description':
    del title_list[-1]

'''
    Splits the problem name wrt '-' and subsequently joins it with '_' for the file name.
'''
file_name = '_'.join(title_list[-1].split('-'))

'''
    Creates a file name using the string created in the previous step
    writes a comment with the problem URL on top.
    launches a shell script with the default editor to the file.
'''
file_ref = open((file_name+'.py'), 'w')
file_ref.write('# ' + pageURL)
file_ref.close()
os.system('bash ./launch_file.sh ' + file_name + '.py')
