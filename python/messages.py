import bs4 as bs
import re
import copy
import itertools
import utils
import json

class MessageType():

    def __init__(self, messageTypeTag):
        self.name = messageTypeTag.text[:5]
        self.number = int(self.name[-3:])
        self.code = re.findall(r'\(.*?\)', messageTypeTag.text)[0].strip("()") 
        self.description = re.findall(r'\-.*?\(', messageTypeTag.text)[0].strip("-( ") 
        print(f"Processing message: {self.name}")

        self.headers = self.extractHeaders(messageTypeTag)

    def extractHeaders(self, messageTypeTag):
        headers = []
        headerTable = messageTypeTag.find_next('table')
        for row in headerTable.find_all('tr'):
            data = row.find_all('td')
            header = Header(data)
            headers.append(header)
            header.fields.extend(self.extractFields(headerTable, header.name))

            print(header.toJSON())
        return headers

    def extractFields(self, headerTable, name):
        h = headerTable.find_next_sibling(lambda tag: tag.name == 'p' and tag.text == name)
        fields = []
        if h is not None:
            p = h.find_next()
            spans = p.findChildren('span')
            while len(spans) > 0 and p.attrs['class'][0] in {'P9', 'P10'}:
                if p.attrs['class'][0] == 'P9':
                    fields.append(Field(spans))
                else:
                    fields[-1].addRule(spans)
                p = p.find_next_sibling()
                spans = p.findChildren('span')
        else:
            print(f"unable to extract details for {name}")
        return fields

    def asHTML(self):
        html = bs.BeautifulSoup()

        ## Titile table
        table = html.new_tag('table')
        html.append(table)
        tr = html.new_tag('tr')
        table.append(tr)
        createTableHeader(html, tr, "Message Type")
        createTableHeader(html, tr, "Name")
        createTableHeader(html, tr, "Code")
        tr = html.new_tag('tr')
        table.append(tr)
        createTableHeader(html, tr, self.name)
        createTableHeader(html, tr, self.description)
        createTableHeader(html, tr, self.code)

        ## Details table
        table = html.new_tag('table')
        html.append(table)
        tr = html.new_tag('tr')
        table.append(tr)
        createTableHeader(html, tr, "Field Name")
        createTableHeader(html, tr, "Priority")
        createTableHeader(html, tr, "Format / Max Repeat")
        createTableHeader(html, tr, "Rules")
        for header in self.headers:
            tr = html.new_tag('tr')
            table.append(tr)
            level = int(header.name.count('-')/3)
            createTableData(html, tr, header.name.replace('---','- '))
            createTableData(html, tr, header.mandatory)
            createTableData(html, tr, header.repeats)
            createRules(html, tr, header.rules.split(' '))
            for field in header.fields:
                tr = html.new_tag('tr')
                table.append(tr)
                createTableData(html, tr, ('- '*(level+1))+field.name)
                createTableData(html, tr, field.mandatory)
                createTableData(html, tr, field.format)
                createRules(html, tr, field.rules)

        return html.prettify()


class Header():
    def __init__(self, data):
        self.name = data[0].text.strip()
        self.repeats = data[1].text.strip()
        self.mandatory = data[2].text.strip()
        self.rules = data[3].text.strip()
        self.fields = []

    def toJSON(self):
        return json.dumps(self, default=vars, indent=4)

class Field():
    def __init__(self, data):
        self.name = data[0].text.strip()
        self.mandatory = data[1].text.strip()
        self.format = data[2].text.strip()
        self.rules = data[3].text.strip().split(' ')
        self.rules.extend(data[4].text.strip().split(' '))
        while('' in self.rules):
            self.rules.remove('')

    def addRule(self, data):
        self.rules.extend(data[0].text.strip().split(' '))

def createTableHeader(html, tr, title):
    td = html.new_tag('th')
    td.string = title
    tr.append(td)

def createTableData(html, tr, data):
    td = html.new_tag('td')
    td.string = data
    tr.append(td)

def createRules(html, tr, rules):
    td = html.new_tag('td')
    tr.append(td)
    data = ''
    for rule in rules:
        if rule.strip().startswith('BR'):
            a = html.new_tag('a', href=f"business-rules.html#{rule.lower()}")
            a.string = rule
            td.append(a)
        elif rule.strip().startswith('R') or rule.strip().startswith('TR'):
            a = html.new_tag('a', href=f"rules.html#{rule.lower()}")
            a.string = rule
            td.append(a)
        elif rule.strip().startswith('TC'):
            a = html.new_tag('a', href=f"technical-codelists.html#{rule.lower()}")
            a.string = rule
            td.append(a)
        else:
            span = html.new_tag('span')
            span.string = rule
            td.append(span)
