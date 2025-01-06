# Write a program that extracts links from a given text. The text will come in the form of strings,
# each representing a sentence. You need to extract only the valid links from it. Example:

#                                         "www.internet.com"

#                              Sub-Domain     Domain name    Domain extension

# The Sub-Domain must always be "www". The Domain name can consist of English alphabet letters (uppercase and lowercase),
# digits, and dashes ("–"). The Domain extension consists of one or more domain blocks,
# a domain block consists of a dot followed by one or more lowercase English alphabet letters,
# a Domain extension must have at least one domain block in order to be valid.
# The Sub-Domain and Domain names must be separated by a single dot.
# Any link that does NOT follow the specified above rules should be treated as invalid.

# Example incorrect links:

#     · "ww.justASite.bg"
#     · "lel.awesome.com"
#     · "www.weird_site.hit.bg"
#     · "www.no-symb#^ols-allow%ed.com"
#     · "www.mark.12"
#     · "www.web-site."
#     · "www.example-site._*^#"

# Example of correct links:

#     · "Some textwww.softuni.bg"
#     · "Just a link in a www.sea-of-text.bg-swimming around"
#     · "Instruments www.Instruments.rom.com.trombone2000 Instrument here"
#     · "All your ice cream flavors-www.scream.for.ice.cream(We also have squirrels)"

# The output is all valid links you have found, printed – each on a new line.


#                             Examples

# Input                                                       Output

# Join WebStars now for free, at www.web-stars.com            www.web-stars.com
# You can also support our partners:                          www.internet.com
# Internet - www.internet.com                                 www.webspiders101.com
# WebSpiders - www.webspiders101.com
# Sentinel - www.sentinel.-ko

# Need information about cheap hotels in London?              www.london-hotels.co.uk
# You can check us at www.london-hotels.co.uk !               www.indigo.bloggers.com
# We provide the best services in London.                     www.rebel21.sedecrem.moc
# Here are some reviews in some blogs:
# London Hotels are awesome! - www.indigo.bloggers.com
# I am very satisfied with their services - ww.ivan.bg
# Best Hotel Services! - www.rebel21.sedecrem.moc


import re

data = input()

pattern = r"(www\.([A-Za-z0-9-]+)(\.[a-z]+)+)"

while data:
    result = re.search(pattern, data)
    if result:
        url = result.group(1)
        print(url)
    data = input()








