
## Introduction

The python directory contains all the files necessary to build a list of message type, code, rules, condition and
business rule.

Python script files are used to read and extract information from HTML files. These HTML files are .docx document that come from the DDNEA which are converted to HTML using OpenOffice Writer program.

| python script   | DDNEA       | HTML            |
| --------------- | ----------- | --------------- |
| messagetypes.py <br> rules.py <br> conditions.py| SDEV-EMCS-P4-DDNEA_APP_D_TECHNICAL_MESSAGE_STRUCTURE.docx | q2.html |
| codelists.py | SDEV-EMCS-P4-DDNEA_APP_B_CODELISTS | codelists.html |
| business-rules.py  | SDEV-EMCS-P4-DDNEA_APP_J_BUSINESS_RULES_CATALOGUE | business-rules.html |



## Python version

Python v3.9.0.

## Build message type

Message types are built from the python scripts **messagetypes.py**. This script reads the **q2.html** file and extract the 
message types from it. It will put all the result message types into the **/python/partials** directory. The directory 
will be created if it does not exist. 

To build the message type do the following:

1. Open the **messagetypes.py** file
2. Change the validMessageTypes array variable to list only the message types that you want to include
3. Open a terminal window
4. type the following command
    
```aidl
    python messagetypes.py
```
5. this will generate **_<message-type-name>.md** file in **/python/partial** directory
6. this will also generate a **messagetypes.html.md.erb** file in the current directory


## Build business rules

The Business rules are built using the **business-rules.py** python script file. This script file reads the 
**business-rules.html** and extract each business rule into a file. It will put all the business rule file
into the **/python/partials** directory. The directory will be created if it does not exist.

To build the business rules do the following:

1. Open a terminal window 
2. type the following command

```aidl
    python business-rules.py

```
3. this will generate **_BR<rule-number>.md** file in **/python/partial** directory
4. this will also generate a **business-rules.html.md.erb** file in the current directory

## Build code list

The code list is built using the **codelists.py** python script file. This script file reads the
**codelists.html** file and extract each code into a file. It will put all the codes file
into the **/python/partials** directory. The directory will be created if it does not exist.

To build the code list do the following:

1. Open a terminal window
2. type the following command

```aidl
    python codelists.py
```
3. this will generate **_TC<code-number>.md** file in **/python/partial** directory
4. this will also generate a **technical-codelists.html.md.erb** file in the current directory

## Build condition list

The condition list is built using the **condition.py** python script file. This script file reads the
**q2.html** file and extract each condition into a file. It will put all the conditions file
into the **/python/partials** directory. The directory will be created if it does not exist.

To build the code list do the following:

1. Open a terminal window
2. type the following command

```aidl
    python condition.py
```
3. this will generate **_C<condition-number>.md** file in **/python/partial** directory
4. this will also generate a **conditions.html.md.erb** file in the current directory


## Build rules list

The rule list is built using the **rules.py** python script file. This script file read the
**q2.html** file and extract each rule into a file. It will put all the rules file
into the **/python/partials** directory. The directory will be created if it does not exist.

To build the rule list do the following:

1. Open a terminal window
2. type the following command

```aidl
    python rules.py
```
3. this will generate **_R<rule-number>.md** file in **/python/partial** directory
4. this will also generate a **rules.html.md.erb** file in the current directory


### View the changes

To view the result in a browser:

1. Copy all the content in the **./python/partial** directory into **./source/documentation/partials**
2. Copy the following file in **./python** directory into the **./source/documentation** directory

```aidl
messagetypes.html.md.erb
business-codelists.html.md.erb
business-rules.html.md.erb
conditions.html.md.erb
rules.html.md.erb
```

3. then to view in the browser see the top level [README.md](https://github.com/hmrc/excise-movement-control-system-api-tis/blob/main/README.md)
