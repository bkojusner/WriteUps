import re

w = open('CONDITIONS.txt', 'w')

with open('if.txt', 'r') as f:
    for line in f:
        str_list = re.split(r'[`\-~!@#$%^&*()+\{};\'\\:"|,./?]', line)
        funk = list(filter(None, str_list))

        hello = [x.strip(' ') for x in funk]
        hello[-1] = hello[-1].strip()
        funkMe = list(filter(None, hello))
        
        print(funkMe)
        for i in funkMe:
            w.write('s.add('+i+')\n')
