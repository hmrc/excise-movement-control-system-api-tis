import bs4 as bs
import json
import os
from os import path
from table import Table

filename='q2.html'

# =============================================================================
# Main
# =============================================================================
soup = bs.BeautifulSoup(open(filename).read(), features="html.parser")

conditions = []
partial_dir = 'partials'

if not os.path.exists(partial_dir):
    os.makedirs(partial_dir)

h1 = soup.find(lambda tag: tag.name == "h1" and 'Conditions' in tag.text)
table = h1.find_next_sibling('table')
trs = table.findChildren('tr')
for tr in trs:
	condition = Table(tr)
	conditions.append(condition)
	with open(f"./{partial_dir}/_{condition.name}.md", "w") as file:
		file.write(f"## {condition.name}\n{condition.asHTML()}")

doc = f"---\ntitle: EMCS Conditions\nweight: 5\ndescription: Software developers, designers, product owners or business analysts. Integrate your software with the EMCS service\n---\n"
doc = doc + f"#Conditions\n"
for condition in conditions:
    doc = doc + f"<%= partial 'documentation/partials/{condition.name}' %>\n"

with open("conditions.html.md.erb", "w") as file:
	file.write(doc)

