import re

w = open('CONDITIONS.txt', 'w')

with open('if.txt', 'r') as f:
    for line in f:
        #print(line.split("()|"))
        str_list = re.split(r'[`\-~!@#$%^&*()+\{};\'\\:"|,./?]', line)
        fuck = list(filter(None, str_list))

        hello = [x.strip(' ') for x in fuck]
        hello[-1] = hello[-1].strip()
        fuckMe = list(filter(None, hello))
        
        print(fuckMe)
        for i in fuckMe:
            w.write('s.add('+i+')\n')
