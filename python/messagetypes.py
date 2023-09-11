import bs4 as bs
import re
import messages
from datetime import datetime

filename='q2.html'
validMessageTypes = [
'IE810','IE813','IE818','IE819','IE825','IE837','IE871',
'IE704','IE801','IE802','IE803','IE807','IE829','IE839','IE840','IE881','IE905'
]

def getIssueDate(soup):
    field_title = soup.find('span', string=re.compile("Date:(.*)"))
    field_value = field_title.find_parent('tr').find_all('td')[1]
    return datetime.strptime(field_value.text.strip(), "%d/%m/%Y")

def getVersion(soup):
    field_title = soup.find('span', string=re.compile("Version:(.*)"))
    field_value = field_title.find_parent('tr').find_all('td')[1]
    return field_value.text.strip()

# =============================================================================
# Main
# =============================================================================
soup = bs.BeautifulSoup(open(filename).read(), features="html.parser")

messageTypes = []

# Iterate round each message type
for messageTypeTag in soup.find_all('h2'):

    if messageTypeTag.text[:5] in validMessageTypes:
        messageType = messages.MessageType(messageTypeTag)
        messageTypes.append(messageType)
        with open(f"_{messageType.name}.md", "w") as file:
            file.write(f"## {messageType.name} {messageType.description}\n{messageType.asHTML()}")
    else:
        print(f"Ignoring message type: {messageTypeTag.text[:5]}")


issueDate = getIssueDate(soup)
documentVersion = getVersion(soup)

doc = f"---\ntitle: EMCS Technical Interface Specification\nweight: 4\ndescription: Software developers, designers, product owners or business analysts. Integrate your software with the EMCS service\n---\n"
doc = doc + f"#Message types\n"
doc = doc + f"Based on document version {documentVersion} and issue date {issueDate.strftime('%b %d, %Y')}\n"
doc = doc + f"<%= partial 'documentation/partials/messagetypeintro' %>\n"
for messageType in messageTypes:
    doc = doc + f"<%= partial 'documentation/partials/{messageType.name}' %>\n"

with open("messagetypes.html.md.erb", "w") as file:
    file.write(doc)
