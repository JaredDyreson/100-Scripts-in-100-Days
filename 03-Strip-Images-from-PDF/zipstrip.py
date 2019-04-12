#!/usr/bin/env python3.5
# tries to extract images from a pdf, not all file types to be supported
# this article specifically targets jpgs -> https://nedbatchelder.com/blog/200712/extracting_jpgs_from_pdfs.html
import os
import sys

# image_headers = {"jpg": ["\xff\xd8", "\xff\xd9"]}
# for image_type in image_headers.items():
#     print(image_type[0])
if len(sys.argv) < 2:
    print("Usage: zipstrip <pdf file>")
    quit()
elif not os.path.isfile(sys.argv[1]):
    print("[-] File not found at {}".format(sys.argv[1]))
    quit()
file = sys.argv[1]
content = open(file, "rb").read()
for b in content:
    print(b)
    if(b == "\xff\xd8"):
        print("Header found")
# print(content)
