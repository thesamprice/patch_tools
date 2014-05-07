import binascii
class s19():
    def __init__(self, filename):
        self.f = open(filename, 'r')
        self.loadImage()
        self.f.close()
    def readline(self):
        x = self.f.readline()
        type = x[0:2]
        address_bytes = 0
        if(type == 'S0'): #TODO....
            self.header = x[2:]
            return self.readline()
        elif(type == 'S1'):
            address_bytes = 2
        elif(type == 'S2'):
            address_bytes = 3
        elif(type == 'S3'):
            address_bytes = 4
        else:
            return None
        result = {}
        byte_count = int(x[2:4], 16) - address_bytes - 1
        start_add = 4
        end_add = address_bytes*2+ start_add
        address = x[start_add:end_add]
        data_end = end_add + byte_count*2
        data = x[end_add:data_end]
        result['bytes'] = byte_count
        result['data']  = data
        result['address'] = int(address, 16)
        return result
    def loadImage(self):

        data = ""
        a = self.readline()    
        start_address = a['address']

        while a != None:
            line_data = binascii.unhexlify(a['data'])
            #print a['bytes'], len(line_data)
            data += line_data
            old_address = a['address']
            a = self.readline() 
            
            if a != None:
                new_add = old_address + len(line_data)
                if(new_add != a['address']):
                    raise Exception('Address jump') 
        self.data = data
        self.start_address = start_address

if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    a = s19(filename)
    print a.data
