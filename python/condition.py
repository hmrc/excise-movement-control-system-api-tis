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

class Condition():
	def __init__(self, row):
		tds = row.findChildren('td')
		self.name = self.content(tds[0])
		self.description = self.content(tds[1])

	def toJSON(self):
		return json.dumps(self, default=vars, indent=4)

	def asHTML(self):
		html = bs.BeautifulSoup()

		html.append(self.description)

		return html.prettify()

	def content(self, td):
	    # Markdown whitespace:
	    # One new line \n just makes the output markdown look nicer
	    # Two new lines \n\n creates a new paragraph tag in the html
	    # Two spaces force a line break within the same paragraph (<br>)
		text = td.get_text("\n").strip().replace('\u2022','-').replace('\u2018','"').replace('\u2019','"').replace('\u2013','-').replace('\u00a0',' ').replace('•', '-').replace('\n - ', '\n\n - ').replace('\n- ', '\n\n - ').replace('\n', '  \n')

		return text



h1 = soup.find(lambda tag: tag.name == "h1" and 'Conditions' in tag.text)
table = h1.find_next_sibling('table')
trs = table.findChildren('tr')

new_trs = []

for index in range(len(trs)-1):
    tds = trs[index].find_all('td')

    next_tr = trs[index+1]
    next_tds = next_tr.find_all('td')
    next_condition_code = next_tds[0].find('p').text.strip()

    # conditions could be on two pages. If next condition code is empty then the rule will be on two pages,
    # so append the next condition (paragraph) to the current condition code
    if not next_condition_code:
        paragraph_tags = next_tds[1].find_all('p')
        [tds[1].append(paragraph_tag) for paragraph_tag in paragraph_tags]

    condition_code = tds[0].find('p').text.strip()
    if condition_code:
         new_trs.append(trs[index])


for tr in trs:
	condition = Condition(tr)
	print("condition: " + condition.asHTML())
	conditions.append(condition)
	with open(f"./{partial_dir}/_{condition.name}.md", "w") as file:
		file.write(f"## {condition.name}\n{condition.asHTML()}")

doc = f"---\ntitle: EMCS Conditions\nweight: 5\ndescription: Software developers, designers, product owners or business analysts. Integrate your software with the EMCS service\n---\n"
doc = doc + f"#Conditions\n"
for condition in conditions:
    doc = doc + f"<%= partial 'documentation/partials/{condition.name}' %>\n"

with open("conditions.html.md.erb", "w") as file:
	file.write(doc)

