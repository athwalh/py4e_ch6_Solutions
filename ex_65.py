str = 'X-DSPAM-Confidence:0.8475'

atpos = str.find(':')
#print(atpos)

sspos = str.find('5', atpos)
#print(sspos)

id1 = str[atpos+1:sspos +1]

id = float(id1)
print(id)
