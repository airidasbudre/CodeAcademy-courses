import re

# #1
# parašykite funkciją, kuri įvestą datą (formatas dd.mm.yyyy) keistų į yyyy mm dd. 
# Dėl datų logikos nesirūpinkite, dirbame grynai su tekstu.

# data = "1999.12.12"
# pattern = '\D'
# res = re.sub(pattern,' ', data)
# print(res)

# ---------------------------------------------------------

text = '''Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020'''

def dates(text2):
    pattern = re.compile(r'([A-Z]\w+)\s(\d{2}\,)\s(\d{4})')
    # pattern = re.compile(r'\d{4}')
    res = pattern.findall(text2)
    print(res)
dates(text)