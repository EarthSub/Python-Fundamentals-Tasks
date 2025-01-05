# Write a program that receives a single string and extracts all email addresses from it.
# Print the extracted email addresses on separate lines. Emails are in the format "{user}@{host}", where:

#     · {user} could consist only of letters and digits; the symbols ".", "-" and "_" can appear between them.
#         o Examples of valid users: "stephan", "mike03", "s.johnson", "st_steward", "softuni-bulgaria", "12345"
#         o Examples of invalid users: ''--123", ".....", "nakov_-", "_steve", ".info"

#     · {host} is a sequence of at least two words, each couple of words must be separated by a single dot ".".
#       Each word consists of letters. There can be hyphens "-" between the letters, except for the last word.
#         o Examples of valid hosts: "softuni.bg", "software-university.com", "intoprogramming.info", "mail.softuni.org"
#         o Examples of invalid hosts: "helloworld", ".unknown.soft." , "invalid-host-", "invalid-"

# Examples of valid emails: info@softuni-bulgaria.org, (kiki@hotmail.co.uk, no-reply@github.com, s.peterson@mail.uu.net,
# info-bg@software-university.software.academy)

# Examples of invalid emails: --123@gmail.com, …@mail.bg, .info@info.info, _steve@yahoo.cn, mike@helloworld,
# mike@.unknown.soft., s.johnson@invalid-


#                                     Examples

# Input                                                                       Output

# Please contact us at: support@github.com.                                   support@github.com

# Just send email to s.miller@mit.edu and j.hopking@york.ac.uk                s.miller@mit.edu
# for more information.                                                       j.hopking@york.ac.uk

# Many users @ SoftUni confuse email addresses.We @                           steve.parker@softuni.de
# Softuni.BG provide high-quality training @ home or @ class.
# –- steve.parker @ softuni.de.


import re

data = input()


pattern = r"\s((([a-z0-9]+)[a-z0-9\.\-\_]*)@([a-z0-9\-]+)(\.[a-z]+)+)\b"

extracted_emails = re.findall(pattern, data)


for emails in extracted_emails:
    print(emails[0])