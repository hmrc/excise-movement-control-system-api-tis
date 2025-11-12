## Message details

Message type details are as follows: 

- Characteristics of the data groups belonging to a message: sequence, number of repetitions, and a status value to indicate if a data group is: 
    - mandatory (R: Required), 
    - optional (O: Optional), or 
    - conditional (D: Dependent).
- Characteristics of the data items belonging to a data group: sequence, number of repetitions, type, length, and a value to indicate if a data item is: 
    - mandatory (R: Required), 
    - optional (O: Optional), or 
    - conditional (D: Dependent).
- Data group nesting is shown with dashes, which means that a data group may contain not only data items but also other groups of data. 
- Links to applicable rules and conditions. As the technical interface specification is still under development, some rules and conditions without links [may be found in the existing DDNEA documentation](https://www.gov.uk/government/publications/emcs-functional-stage-31-fs31-technical-specifications). 
- Header elements (XML fields that can contain other XML fields) are highlighted in **bold**.
- Further [information about data item formats](data-item-formats.html) is available.

## Accessing the XML schemas

You can [download the XML schemas on GitHub](https://github.com/hmrc/excise-movement-control-system-api/tree/main/app/xsd).

To view the XML schema for a specific message type, click the link under the **XML** heading in the table for the required message type listed below.

