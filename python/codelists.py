import bs4 as bs
import json
import os
from os import path

filename='codelists.html'

# =============================================================================
# Main
# =============================================================================
soup = bs.BeautifulSoup(open(filename).read(), features="html.parser")

codelists = []
partial_dir = './partials'

if not os.path.exists(partial_dir):
    os.makedirs(partial_dir)

class Code():
	def __init__(self, tr):
		tds = tr.findChildren('td')
		self.value = tds[0].text.strip()
		self.description = tds[1].text.strip()
		self.remarks = tds[2].text.strip()

class CodeList():
	def __init__(self, h2):
		self.name = h2.text
		p = h2.find_next_sibling('p')
		self.format = p.text.removeprefix('Format ').strip()
		self.context = p.find_next_sibling('p').find_all('span')[1].text
		trs = p.find_next_sibling('table').findChildren('tr')[1:]
		self.codes = []
		for tr in trs:
			code = Code(tr)
			self.codes.append(code)

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
		td.string = self.format
		if self.context != '':
			tr = html.new_tag('tr')
			table.append(tr)
			td = html.new_tag('td',attrs={'colspan': '2'})
			tr.append(td)
			td.string = self.context
		table = html.new_tag('table')
		html.append(table)
		tr = html.new_tag('tr')
		table.append(tr)
		th = html.new_tag('th')
		tr.append(th)
		th.string = 'Value'
		th = html.new_tag('th')
		tr.append(th)
		th.string = 'Description'
		th = html.new_tag('th')
		tr.append(th)
		th.string = 'Remarks'
		for code in self.codes:
			tr = html.new_tag('tr')
			table.append(tr)
			td = html.new_tag('td')
			tr.append(td)
			td.string = code.value
			td = html.new_tag('td')
			tr.append(td)
			td.string = code.description
			td = html.new_tag('td')
			tr.append(td)
			td.string = code.remarks
			td = html.new_tag('td')
			tr.append(td)

		return html.prettify()

	def content(self, td):
		text = td.text.strip().replace('\u2022','-').replace('\u2018','"').replace('\u2019','"').replace('\u2013','-').replace('\u00a0',' ').replace('\\n','\n<br/>')
		return text

h2s = soup.find_all(lambda tag: tag.name == "h2")
for h2 in h2s:
	codelist = CodeList(h2)
	codelists.append(codelist)
	with open(f"{partial_dir}/_{codelist.name}.md", "w") as file:
		file.write(f"## {codelist.name.split(' ')[0]}\n{codelist.asHTML()}")

doc = f"---\ntitle: EMCS Technical Codelists\nweight: 5\ndescription: Software developers, designers, product owners or business analysts. Integrate your software with the EMCS service\n---\n"
doc = doc + f"#Technical Codelists\n"
for codelist in codelists:
    doc = doc + f"<%= partial 'documentation/partials/{codelist.name}' %>\n"

with open("technical-codelists.html.md.erb", "w") as file:
	file.write(doc)

