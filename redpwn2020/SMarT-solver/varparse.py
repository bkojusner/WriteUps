f = open('VARIABLES.txt', 'w')

with open('var.txt', 'r') as funk:
    for line in funk:
        name = line.split(' ')[3]
        moi = name[:-2]
        f.write(moi + " = Int('" + moi + "')" + '\n')
        f.write("s.add(97 <=" + moi + ")\n")
        f.write("s.add(" + moi + " <= 124)\n")
