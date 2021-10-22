from uGecko.uGecko import uGecko
from fuiHeader import fuiHeader
import struct

SupportedFuiFile = {
    'skinWiiU' : 0,
    'skinGraphics' : 1,
    'skinGraphicsHud' : 2,
    'skinGraphicsInGame' : 3,
    'skinGraphicsLabels' : 4,
    'skinLabels' : 5,
    'skinInGame' : 6,
    'skinHud' : 7,
    'skin' : 8,
    'ToolTips720' : 9,
    'WiiUDRC720' : 10,
    'PressStartToPlay720' : 12,
    'TutorialPopup720' : 14,
    'HUD720' : 15,
    'MenuBackground720' : 26
}

def getFuiFileIndex(swfName:str)->int:
    return SupportedFuiFile[swfName.replace(".swf", "")]

def replaceFuiFile(socket:uGecko, fui_data:bytes)->None:
    '''
    Takes data from an .fui file and replaces it with the currently used fui file
    '''
    address = 0x40000000 # unused MEM1 memory
    imgdata_ptr = address+8
    header = fuiHeader(fui_data[0:0x98])
    fuiFileIndex = getFuiFileIndex(header.swfname)
    print(f"File Index : {fuiFileIndex}")
    size:int = len(fui_data)
    if size != header.HeaderSize + header.size: raise BaseException("Detected File size is invalid")
    socket.poke32(address, imgdata_ptr)
    socket.poke32(address+4, size)
    socket.upload(imgdata_ptr, fui_data)
    fuiClassPtr = int.from_bytes(socket.read(0x109F75A8, 4),"big")
    fuifile = socket.call(0x02bababc, fuiClassPtr, fuiFileIndex)
    print("Calling fui::load")
    socket.call(0x02ba775c,fuifile,address,fuiFileIndex) # fuiFile::load
    print("reloading SkinThreadProc ...")
    socket.call(0x2da27a8,0x109F95E0) # ConsoleUIController::reloadSkinThreadProc(void)