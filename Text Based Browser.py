import sys
import os
import requests
from collections import deque
from bs4 import BeautifulSoup

args=sys.argv
if len(args) != 2:
    print("Error: Invalid number of command-line arguments")
    exit()
if(not os.path.exists(args[1])):
	os.mkdir(args[1])
wd = os.getcwd()
cwd = wd + '\\' + args[1]
saved_pages_set=set()
stack=deque()

while True:
	url = input()
	if(url == 'exit'):
		exit()
	try:
		if('https://' in url):
			req=requests.get(url)
			page_prefix=url[8:url.rindex('.')]
			fpath=os.path.join(cwd, page_prefix + '.txt')
			soup = BeautifulSoup(req.content, 'html.parser')
			parse_tags = ['p', 'a', 'h1', 'h2', 'h3', 'h3', 'h4', 'h5', 'h6', 'h7', 'ul', 'ol', 'li']
			clean_data = "\n".join([line.get_text().strip() for tag in parse_tags for line in soup.find_all(tag)])
			print(clean_data)
			with open(fpath, 'w', encoding='UTF-8') as f:
				f.write(clean_data)
			saved_pages_set.add(page_prefix)
			stack.append(page_prefix)


		elif(url in saved_pages_set):
			fpath=os.path.join(cwd, url + '.txt')
			with open(fpath,'r', encoding='UTF-8') as f:
				print(f.read())
			stack.append(url)

		elif('https://' not in url and url!='back'):
			req=requests.get('https://' + url)
			page_prefix=url[:url.rindex('.')]
			fpath=os.path.join(cwd, page_prefix + '.txt')
			soup = BeautifulSoup(req.content, 'html.parser')
			parse_tags = ['p', 'a', 'h1', 'h2', 'h3', 'h3', 'h4', 'h5', 'h6', 'h7', 'ul', 'ol', 'li']
			clean_data = "\n".join([line.get_text().strip() for tag in parse_tags for line in soup.find_all(tag)])
			print(clean_data)
			with open(fpath, 'w', encoding='UTF-8') as f:
				f.write(clean_data)
			saved_pages_set.add(page_prefix)
			stack.append(page_prefix)

		elif(url=='back'):
			if(not stack):
				pass
			elif(len(stack)==1):
				stack.pop()
			else:
				stack.pop()
				temp=stack.pop()
				fpath=os.path.join(cwd, temp + '.txt')
				with open(fpath, 'r', encoding='UTF-8') as f:
					print(f.read())

		else:
			print('Error: Incorrect URL')		
	except:
		print('Error: Incorrect URL')


def check_url(self,url):
	self.url=url
	if('https://' not in url):
		
