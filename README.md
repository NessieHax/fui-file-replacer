# Fui File Replacer
Simple script that allows dynamic replacment of `.fui` files for Minecraft Wii U

## Requirements
- [Python 3.7(.12)](https://www.python.org/downloads/release/python-3712/) or newer (only tested on python 3.7.8)
- [TCPGecko](https://github.com/BullyWiiPlaza/tcpgecko/blob/master/tcpgecko.elf) running on the Wii U.
- [uGecko](https://github.com/NessieHax/uGecko) for TCPGecko communication.

## Setup
```
git clone https://github.com/NessieHax/fui-file-replacer --recursive --recurse-submodules
cd fui-file-replacer
git submodule update --init --recursive
```

## Example
Example code can be found [here](./example.py).\
or run the command below to excute the example
```
python3 ./example.py <*.fui> <WiiUIP>
```

## Details
- fui file's can have any name ( `*.fui` ) however it needs to have the right header format to detect the specific fui file to replcae

## Known Issue
- [#1 Game Frezzing when trying to replace texturepack loaded fui file](https://github.com/NessieHax/fui-file-replacer/issues/1)

## Credits
[NessieHax](https://github.com/NessieHax) aka Miku-666.