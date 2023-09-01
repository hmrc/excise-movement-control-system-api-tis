def createTableHeader(html, tr, title):
    td = html.new_tag('th')
    td.string = title
    tr.append(td)

def createTableData(html, tr, data):
    td = html.new_tag('td')
    td.string = data
    tr.append(td)
