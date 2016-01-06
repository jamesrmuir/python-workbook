#! python3
#Phone Number and Email Address Extractor 
import re, pyperclip

#phoneRegex = re.compile(r'''(
#    (\d{3}|\(\d{3}\))?                # area code
#    (\s|-|\.)?                        # separator
#    (\d{3})                           # first 3 digits
#    (\s|-|\.)                         # separator
#    (\d{4})                           # last 4 digits
#    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
#    )''', re.VERBOSE)

phoneRegex = re.compile(r'''(
    (\d{5}|\(\d{5}\))?
    (\s|-|\.)?
    (\d{6})  
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ 
    @ # @ symbol
    [a-zA-Z0-9.-]+ 
    (\.[a-zA-Z]{2,4}) 
)''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1]])
    if groups[3] != '':
        phoneNum += ' ' + groups[3]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

