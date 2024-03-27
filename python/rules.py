import bs4 as bs
import json
import os
from os import path

filename='q2.html'

# =============================================================================
# Main
# =============================================================================
soup = bs.BeautifulSoup(open(filename).read(), features="html.parser")

rules = []
partial_dir = './partials'

if not os.path.exists(partial_dir):
    os.makedirs(partial_dir)

class Rule():
	def __init__(self, row):
		tds = row.findChildren('td')
		self.name = self.content(tds[0])
		self.description = self.content(tds[1])

	def toJSON(self):
		return json.dumps(self, default=vars, indent=4)

	def asHTML(self):
		html = bs.BeautifulSoup()

		#table = html.new_tag('table')
		#html.append(table)
		#tr = html.new_tag('tr')
		#table.append(tr)
		#th = html.new_tag('th')
		#tr.append(th)
		#th.string = self.name
		#td = html.new_tag('td')
		#tr.append(td)
		#td.string = self.description

		html.append(self.description)

		return html.prettify()

	def content(self, td):
	    # Markdown whitespace:
	    # One new line just makes the output look nicer
	    # Two new lines \n\n creates a new paragraph tag in the html
	    # Two strings force a line break within the same paragraph
		text = td.get_text("\n").strip().replace('\u2022','-').replace('\u2018','"').replace('\u2019','"').replace('\u2013','-').replace('\u00a0',' ').replace('\n', '  \n')

		if (text.find("three digits number") != -1):
		    print("raw text: " + td.get_text())
		    print("raw text with new lines: " + td.get_text("\n"))
		    print("final text: " + text)

		return text

h1 = soup.find(lambda tag: tag.name == "h1" and 'Rules' in tag.text)
table = h1.find_next_sibling('table')
trs = table.findChildren('tr')

new_trs = []

for index in range(len(trs)-1):
    tds = trs[index].find_all('td')

    next_tr = trs[index+1]
    next_tds = next_tr.find_all('td')
    next_rule_code = next_tds[0].find('p').text.strip()

    # rules could be on two pages. If nect rule code is empty then the rule will be on two pages,
    # so append the next rules (paragraph) to the current rule code
    if not next_rule_code:
        paragraph_tags = next_tds[1].find_all('p')
        [tds[1].append(paragraph_tag) for paragraph_tag in paragraph_tags]

    rule_code = tds[0].find('p').text.strip()
    if rule_code:
         new_trs.append(trs[index])


for tr in trs:
	rule = Rule(tr)
	rules.append(rule)

	with open(f"{partial_dir}/_{rule.name}.md", "w") as file:
		file.write(f"## {rule.name}\n{rule.asHTML()}")

doc = f"---\ntitle: EMCS Rules\nweight: 5\ndescription: Software developers, designers, product owners or business analysts. Integrate your software with the EMCS service\n---\n"
doc = doc + f"#Rules\n"
for rule in rules:
    doc = doc + f"<%= partial 'documentation/partials/{rule.name}' %>\n"

with open("rules.html.md.erb", "w") as file:
	file.write(doc)

