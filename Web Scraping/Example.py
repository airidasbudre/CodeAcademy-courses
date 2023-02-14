from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# print(type(soup))
# print(soup.body.div)
# print(soup.find('div'))
# print(soup.find_all(class_='special'))
# print(soup.find_all(attrs={'data-example': 'yes'}))

# print(soup.select('#first'))

# element = soup.select('.special')[0]
# print(element.get_text())

# elements = soup.select('meta')
# print(elements[0].attrs)

print(soup.div.contents)