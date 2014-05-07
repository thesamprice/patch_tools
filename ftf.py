import binascii
#print h

adds = []
class ftf():
    def __init__(self,filename):
        f = open(filename)
        h  =  f.readline()
        h += f.readline()
        h +=f.readline()
        d = f.read()
        f.close()
        lines = d.split('\n')
        start_address = int(  lines[0].split(',')[0],16)
        data = ""
        for line in lines:
            if line == '':
                continue
            #print '-',line
            row = line.split(',')
            add = int(  row[0],16) - start_address
            le = int(row[1],16)
            adds.append(add)
            dd = binascii.unhexlify(row[2])
            data = data + dd[0:le]
        self.data = data
        self.start_address = start_address
#    if le != 200:
#        print add ,le, len(dd[0:le])


