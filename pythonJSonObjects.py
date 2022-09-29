# JSon is a stand for Java Script Object Notation. JSon is a data exchange format similar to XML.
# Let's understand this by an address record:
JSon = {
    "name": "Ali",
    "Address": "Kabul",
    "Phone": "0784334545"
}

print(JSon["Address"])
for key in JSon:
    print("Key:", key, "\n", "Value:", JSon[key])

# XML
    """
    <name> Ali </name>
    <address> Kabul </address>
    <phone> phone </phone>
    """
# Here you can see in XML each of the keys are represented in opening and closing Tags, that's why XML takes of more
# volume of data, and it's not lightweight as JSon.
# So JSon is a lightweight format compared to XML. and this is the reason JSon is getting popular now-days.
"""
 Now let's write two simple examples, 1st create address book and write some records into it. 2nd read this address
 book. 
 
"""

