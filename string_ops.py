actor = "Chris Hemsworth"
print(len(actor))   # use a builtin (aka global) function
print(actor.upper())  # call a string method
print(actor.lower())
print(actor.count('h'))
print(actor.lower().count('h'))
print(actor.replace('Chris', 'Liam'))  # replace 'Chris' with 'Liam'
a2 = actor.replace('Chris', 'Liam')
print(a2)
print(actor.startswith("Chris"), actor.startswith("Liam"))
print("hem" in actor.lower())
print("haw" in actor.lower())
print(actor.index('Hem'), actor.find('Hem'))
print(actor.find('Liam'))

s = "      This is only a test     "
print('|' + s.lstrip() + '|')
print('|' + s.rstrip() + '|')
print('|' + s.strip() + '|')
print()

s = "ssseeeseseeeeeeeThis is only a testeeeeeeeeesesesesessssssss"
print('|' + s.lstrip('es') + '|')
print('|' + s.rstrip('es') + '|')
print('|' + s.strip('exs') + '|')

code_str = 'M365 I221 Z981 A456'
codes = code_str.split()
print(codes)

fields = 'alpha:beta:gamma'
print(fields.split(':'))
