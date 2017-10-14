from bs4 import BeautifulSoup
import requests, sys, os

pageURL = sys.argv[1]
title_list = pageURL.split('/')
if title_list[-1] == 'problem':
    del title_list[-1]
file_name = '_'.join(title_list[-1].split('-'))

file_ref = open((file_name+'.py'), 'w')
file_ref.write('# ' + pageURL)
file_ref.write('\n\n')
file_ref.close()
os.system('bash ./launch_file.sh ' + file_name + '.py')
