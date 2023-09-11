import bs4 as bs
import json

filename='q2.html'

# =============================================================================
# Main
# =============================================================================
soup = bs.BeautifulSoup(open(filename).read(), features="html.parser")

rules = []

class Rule():
	def __init__(self, row):
		tds = row.findChildren('td')
		self.name = self.content(tds[0])
		self.description = self.content(tds[1])

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
		th.string = self.name
		td = html.new_tag('td')
		tr.append(td)
		td.string = self.description

		return html.prettify()

	def content(self, td):
		text = td.text.strip().replace('\u2022','-').replace('\u2018','"').replace('\u2019','"').replace('\u2013','-').replace('\u00a0',' ').replace('\\n','\n<br/>')
		return text

h1 = soup.find(lambda tag: tag.name == "h1" and 'Rules' in tag.text)
table = h1.find_next_sibling('table')
trs = table.findChildren('tr')
for tr in trs:
	rule = Rule(tr)
	rules.append(rule)
	with open(f"_{rule.name}.md", "w") as file:
		file.write(f"## {rule.name}\n{rule.asHTML()}")

doc = f"---\ntitle: EMCS Rules\nweight: 5\ndescription: Software developers, designers, product owners or business analysts. Integrate your software with the EMCS service\n---\n"
doc = doc + f"#Rules\n"
for rule in rules:
    doc = doc + f"<%= partial 'documentation/partials/{rule.name}' %>\n"

with open("rules.html.md.erb", "w") as file:
	file.write(doc)

