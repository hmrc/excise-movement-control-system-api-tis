
# Introduction

This SpecsToMarkdown directory contains all the files necessary to build a list of message types,
codes, rules, conditions and business rules.


# Option 1: do everything in one step

The `specs_to_markdown.py` Python script unarchives the DDNEA zip file and then uses LibreOffice to
convert each .docx file into HTML. These are then turned into Markdown and Ruby template (ERB)
files for use by Middleman (see top-level [README](https://github.com/hmrc/excise-movement-control-system-api-tis/blob/main/README.md)).
Comparing the generated files with what's in git shows us that changes were made to these files,
so the last step applies a patch to emulate this.

You should get the dependencies before trying to run it. You'll need the `soffice` command provided
by [LibreOffice](https://www.libreoffice.org/), as well as the [uv](https://docs.astral.sh/uv/)
Python package manager.

Then `cd` into this directory and run the following command:
```console
uv run specs_to_markdown.py
```


# Option 2: run each script individually

Alternatively, if you've already unarchived the DDNEA zip file and used LibreOffice to convert each
.docx file into HTML, you can run the following scripts individually. 

| python script                                    | DDNEA                                                     | HTML                |
|--------------------------------------------------|-----------------------------------------------------------| ------------------- |
| messagetypes.py <br> rules.py <br> conditions.py | SDEV-EMCS-P4-DDNEA_APP_D_TECHNICAL_MESSAGE_STRUCTURE.docx | q2.html             |
| codelists.py                                     | SDEV-EMCS-P4-DDNEA_APP_B_CODELISTS.docx                   | codelists.html      |
| business_rules.py                                | SDEV-EMCS-P4-DDNEA_APP_J_BUSINESS_RULES_CATALOGUE.docx    | business-rules.html |


## Build message type

Message types are built from the python scripts **messagetypes.py**. This script reads the **q2.html** file and extract the 
message types from it. It will put all the result message types into the **/SpecsToMarkdown/partials** directory. The directory 
will be created if it does not exist. 

To build the message type do the following:

1. Open the **messagetypes.py** file
2. Change the validMessageTypes array variable to list only the message types that you want to include
3. Open a terminal window
4. type the following command
    ```console
    uv run messagetypes.py
    ```
5. this will generate **_<message-type-name>.md** file in **/SpecsToMarkdown/partial** directory
6. this will also generate a **messagetypes.html.md.erb** file in the current directory


## Build business rules

The Business rules are built using the **business_rules.py** python script file. This script file reads the 
**business-rules.html** and extract each business rule into a file. It will put all the business rule file
into the **/SpecsToMarkdown/partials** directory. The directory will be created if it does not exist.

To build the business rules do the following:

1. Open a terminal window 
2. type the following command
    ```console
    uv run business_rules.py
    ```
3. this will generate **_BR<rule-number>.md** file in **/SpecsToMarkdown/partial** directory
4. this will also generate a **business-rules.html.md.erb** file in the current directory


## Build code list

The code list is built using the **codelists.py** python script file. This script file reads the
**codelists.html** file and extract each code into a file. It will put all the codes file
into the **/SpecsToMarkdown/partials** directory. The directory will be created if it does not exist.

To build the code list do the following:

1. Open a terminal window
2. type the following command
    ```console
    uv run codelists.py
    ```
3. this will generate **_TC<code-number>.md** file in **/SpecsToMarkdown/partial** directory
4. this will also generate a **technical-codelists.html.md.erb** file in the current directory


## Build condition list

The condition list is built using the **condition.py** python script file. This script file reads the
**q2.html** file and extract each condition into a file. It will put all the conditions file
into the **/SpecsToMarkdown/partials** directory. The directory will be created if it does not exist.

To build the code list do the following:

1. Open a terminal window
2. type the following command
    ```console
    uv run condition.py
    ```
3. this will generate **_C<condition-number>.md** file in **/SpecsToMarkdown/partial** directory
4. this will also generate a **conditions.html.md.erb** file in the current directory


## Build rules list

The rule list is built using the **rules.py** python script file. This script file read the
**q2.html** file and extract each rule into a file. It will put all the rules file
into the **/SpecsToMarkdown/partials** directory. The directory will be created if it does not exist.

To build the rule list do the following:

1. Open a terminal window
2. type the following command
    ```console
    uv run rules.py
    ```
3. this will generate **_R<rule-number>.md** file in **/SpecsToMarkdown/partial** directory
4. this will also generate a **rules.html.md.erb** file in the current directory


## Copy the files

To view the result in a browser:

1. Copy all the content in the **./SpecsToMarkdown/partial** directory into **./source/documentation/partials**
2. Copy the following files in **./SpecsToMarkdown** directory into the **./source/documentation** directory
    - business-rules.html.md.erb
    - conditions.html.md.erb
    - messagetypes.html.md.erb
    - rules.html.md.erb
    - technical-codelists.html.md.erb
 

# View the changes

Regardless of whether you generated the Markdown and Ruby templates in one step or ran each script
individually, you'll want to see how they look when Middleman renders them as HTML in a browser.
For instructions on how to do that, see the top-level [README](https://github.com/hmrc/excise-movement-control-system-api-tis/blob/main/README.md)
