import re, pyperclip

msg = '''Chairman Secretariat 011-29581199 1199,1528 anju@aicte-india.org
Vice-Chairman
Secretariat
011-29581299 1299 vinaykumar@aicte-india.org
Member Secretary
Secretariat
011-29581399 1399 msaicte1@gmail.com'''


phoneNumRegex = re.compile(r'''
\d\d\d-
\d\d\d\d\d\d\d\d
''',re.VERBOSE | re.I | re.DOTALL)

text = pyperclip.paste()

email_regex = re.compile(r'''
[a-zA-Z0-9_.]+
@
[a-zA-z0-9_.-]+

''', re.VERBOSE)

m = phoneNumRegex.findall(text)
print(m)

e = email_regex.findall(text)
print(e)

for i in range(len(m)):
    print('{}\t{}'.format(m[i],e[i]))
        
