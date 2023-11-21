import bs4 as bs

class Table():
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