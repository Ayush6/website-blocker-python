import time
from datetime import datetime as dt

hosts_path= r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

with open('website.txt', 'r') as file:
    websites = file.readlines()

website_list = []

for website in websites:
    website_list.append(website)
    website_list.append(website[4:])

# start and end time until which blocked website cannot be accessed
start_time, end_time = map(int, input("Enter the time e.g '9 5' for blocking website from 9AM to 5PM: ").split())

cur = dt.now()
while True:
    if dt(cur.year,cur.month,cur.day,start_time) < dt.now() < dt(cur.year,cur.month,cur.day, end_time):

        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n"redirect+" "+ website+"\n")

    else:

        with open(hosts_path,'r+') as file:

            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(10)
