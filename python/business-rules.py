import bs4 as bs
import json

filename='business-rules.html'

# =============================================================================
# Main
# =============================================================================
soup = bs.BeautifulSoup(open(filename).read(), features="html.parser")

rules = []

class Rule():
	def __init__(self, table):
		trs = table.findChildren('tr')
		self.name = self.content(trs[0])
		self.category = self.content(trs[1])
		self.description = self.content(trs[2])
		self.validation = self.content(trs[4])
		self.optionality = self.content(trs[7])
		self.comments = self.content(trs[8])

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
		text = tr.findChildren('td')[1].text.strip().replace('\u2022','-').replace('\u2018','"').replace('\u2019','"').replace('\u2013','-').replace('\u00a0',' ').replace('\\n','\n<br/>')
		return text


for h2 in soup.find_all('h2'):
	table = h2.find_next_sibling('table')
	rule = Rule(table)
	rules.append(rule)
	with open(f"_{rule.name}.md", "w") as file:
		file.write(f"## {rule.name}\n{rule.asHTML()}")

doc = f"---\ntitle: EMCS Business Rules\nweight: 5\ndescription: Software developers, designers, product owners or business analysts. Integrate your software with the EMCS service\n---\n"
doc = doc + f"#Business Rules\n"
for rule in rules:
    doc = doc + f"<%= partial 'documentation/partials/{rule.name}' %>\n"

with open("business-rules.html.md.erb", "w") as file:
	file.write(doc)

