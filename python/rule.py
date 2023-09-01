import bs4 as bs
import json

class Rule():
	def __init__(self, table):
		trs = table.findChildren('tr')
		self.name = trs[0].findChildren('td')[1]

	def toJSON(self):	
		return json.dumps(self, default=vars, indent=4)