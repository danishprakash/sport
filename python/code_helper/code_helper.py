from bs4 import BeautifulSoup
import requests, sys, os

if sys.argv[1]:
    pageURL = sys.argv[1]
else:
    print('URL not specified')

title_list = pageURL.split('/')

if title_list[-1] == 'problem' or title_list[-1] == '0':
    del title_list[-1]

file_name = '_'.join(title_list[-1].split('-'))

file_ref = open((file_name+'.py'), 'w')
file_ref.write('# ' + pageURL)
file_ref.write('\n\n')
file_ref.close()
os.system('bash ./launch_file.sh ' + file_name + '.py')
