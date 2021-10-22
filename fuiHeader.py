import struct

def swap32(x , fmt:str):
    return struct.unpack(fmt.replace(">", "<"), struct.pack(fmt,x))[0]

class fuiHeader:
    def __init__(self,rawHeader:bytes):
        fmt = ">4s4xI64s60xffff"
        data = struct.unpack(fmt, rawHeader) # loaded : "FUI\x01" file : "\x01IUF"
        self.identifier:str = data[0]
        self.size:int = swap32(data[1],">I")
        self.swfname:str = data[2].decode("UTF-8").replace("\x00","")
        self.rect:dict = {
            "x" :swap32(data[3],">f"),
            "width" : swap32(data[4],">f"),
            "y" : swap32(data[5],">f"),
            "height" : swap32(data[6],">f")
           }
        self.HeaderSize:int = struct.calcsize(fmt)