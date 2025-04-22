import re

def find_hrefs(fileName):
    with open(fileName, 'r', encoding='utf-8') as file:
        content = file.read()
        
    pattern = r'href="(.*?)"'
    matches = re.findall(pattern, content)
    people = set(matches)   
    print("number of people in " + fileName +": "+  str(len(people)))
    return people

followers = find_hrefs('followers.txt')
followings = find_hrefs('following.txt')
print()

difference = followings.difference(followers)
print("People you follow, but they don't follow you: ", difference)
# Fájl tartalmának kiíratása
