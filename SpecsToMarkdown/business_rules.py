import bs4 as bs
import json
import os
from os import path

filename='business-rules.html'

# =============================================================================
# Main
# =============================================================================
soup = bs.BeautifulSoup(open(filename).read(), features="html.parser")

rules = []
partial_dir = './partials'

if not os.path.exists(partial_dir):
    os.makedirs(partial_dir)

class Rule():
	def __init__(self, table):
		trs = table.findChildren('tr')
		headers = []
		for tr in trs:
		    headers.append(tr.findChildren('td')[0].text.strip())
		self.name = self.content(trs[headers.index("BR ID")])
		self.category = self.content(trs[headers.index("BR Category")])
		self.description = self.content(trs[headers.index("BR Description")])
		self.validation = self.content(trs[headers.index("FESS Validation Rule")])
		self.optionality = self.content(trs[headers.index("Optionality")])
		self.comments = self.content(trs[headers.index("Comments")])

	def toJSON(self):
		return json.dumps(self, default=vars, indent=4)

	def asHTML(self):
		html = bs.BeautifulSoup()

		table = html.new_tag('table')
		html.append(table)
		tr = html.new_tag('tr')
		table.append(tr)
		th = html.new_tag('th')
		tr.append(th)
		th.string = rule.name
		td = html.new_tag('td')
		tr.append(td)
		td.string = rule.optionality
		td = html.new_tag('td')
		tr.append(td)
		td.string = rule.category

		tr = html.new_tag('tr')
		table.append(tr)
		td = html.new_tag('td',attrs={'colspan': '3'})
		tr.append(td)
		td.string = rule.description

		tr = html.new_tag('tr')
		table.append(tr)
		td = html.new_tag('td',attrs={'colspan': '3'})
		tr.append(td)
		td.string = rule.validation

		return html.prettify()

	def content(self, tr):
		text = tr.findChildren('td')[1].get_text().strip().replace('\u2022','-').replace('\u2018','"').replace('\u2019','"').replace('\u2013','-').replace('\u00a0',' ').replace('•', '-').replace('\n - ', '\n\n - ').replace('\n- ', '\n\n - ').replace('\n', '  \n')
		return text


for h2 in soup.find_all('h2'):
	table = h2.find_next_sibling('table')
	rule = Rule(table)
	rules.append(rule)
	with open(f"{partial_dir}/_{rule.name}.md", "w") as file:
		file.write(f"## {rule.name}\n{rule.asHTML()}")

doc = f"---\ntitle: EMCS Business Rules\nweight: 5\ndescription: Software developers, designers, product owners or business analysts. Integrate your software with the EMCS service\n---\n"
doc = doc + f"#Business Rules\n"
for rule in rules:
    doc = doc + f"<%= partial 'documentation/partials/{rule.name}' %>\n"

with open("business-rules.html.md.erb", "w") as file:
	file.write(doc)

