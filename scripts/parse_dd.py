import sys

dddata = open(sys.argv[1],"rb").read()
vdata = dddata[2:1002]
bdata = dddata[1026:]

fh = open("logo-b.c64", "wb")
fh.write("\x00\x60" + bdata)
fh.close()

fh = open("logo-v.c64", "wb")
fh.write("\x00\x40" + vdata)
fh.close()



