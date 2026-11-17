import re


def domain_name(url):
    search = re.search(r"h?t?t?p?s?:?/?/?w?w?w?\.?(.*)\.", url)
    return search.group(1)


print(domain_name("http://google.co.jp"))

# didnt get this one right tho
# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python
