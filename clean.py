# Run this file to unblock all the websites blocked using 'blocker' script
hosts_path= r"C:\Windows\System32\drivers\etc\hosts"

website_list = []
with open('website.txt', 'r') as file:
    websites = file.readlines()

for website in websites:
    website_list.append(website)
    website_list.append(website[4:])

with open(hosts_path, 'r+') as file:
    content = file.read()

    file.seek(0)
    for line in content:
        if not any(website in line for website in website_list):
            file.write(line)
    file.truncate()
