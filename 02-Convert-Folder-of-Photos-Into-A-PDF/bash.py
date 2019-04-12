#!/usr/bin/env python3.5

# recreating bash tools in python so I don't have to use Bash for text processing

import os, sys ,pycurl, urllib.parse, urllib.request, urllib.error, zipfile, tarfile, glob
from io import BytesIO
import magic
import pip


class find():
    def files(path):
        filelist = []
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path, f)):
                filelist.append(os.path.abspath(os.path.join(path, f)))
        return filelist
    def dirs(path):
        dirlist = []
        for d in os.listdir(path):
            if os.path.isdir(os.path.join(path, d)):
               dirlist.append(d)
        return dirlist
    def mimetypes(path, mime=None):
        m = magic.Magic(mime=True)
        return [ item for item in find.files(path) if mime in m.from_file(item) ]
class pipInstall():
    def install(package):
        if hasattr(pip, 'main'):
            pip.main(['install', package])
        else:
            pip._internal.main(['install', package])
class text():
    # Resources
    # Line Number -> https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
    # Takes exactly one argument but two given ERROR -> https://stackoverflow.com/questions/4909585/interesting-takes-exactly-1-argument-2-given-python-error
    # Default constructor python 2.7 -> https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    # Explaining enumeratation -> https://www.geeksforgeeks.org/enumerate-in-python/
    # Word count -> https://stackoverflow.com/questions/19410018/how-to-count-the-number-of-words-in-a-sentence-ignoring-numbers-punctuation-an
    class WC:
        version = 1.0
        def __init__(self, string=None):
            if string == None:
                self.s = ""
            else:
                self.s = string
        def byte_count(self):
            # unknown
            return sys.getsizeof(self.s)
        def char_count(self):
            return len(self.s)
        @staticmethod
        def line_count(path):
            with open(path) as file:
                for i, l in enumerate(file):
                    pass
            return i + 1
        def word_count(self):
            return len(self.s.split())
    def sed(string):
        print("working on sed")
    def awkPrint(string, pattern):
        return string.split()[pattern-1]
    def findExtentsion(path=None, depth=None, extension=None):
        print(path)
        print(depth)
        print(extension)
        fileList = []
        for f in os.listdir(path):
            if f.endswith(extension):
                fileList.append(f)
        return fileList
    def printExtension(filePath):
        ext = os.path.splitext(filePath)[1:]
        return ext
    def cat(path):
        content = ''
        with open(path) as file:
            content = file.read()
        return content

class networking():
    def curl(link):
         buf = BytesIO()
         c = pycurl.Curl()
         c.setopt(c.URL, link)
         c.setopt(c.WRITEDATA, buf)
         c.perform()
         c.close()
         data = buf.getvalue()
         decoded_data = data.decode('iso-8859-1')
         return decoded_data
    def wget(link, path):
        urllib.request.urlretrieve(link, path)




def scp(localPath, remotePath):
    print("Working on scp")
    paramiko.util.log_to_file('/tmp/paramiko.log')
    paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
    host = 'root'
    port = 22
    username = 'jared'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=port, username=username)
    sftp = ssh.open_sftp()
    sftp.get(remotepath, localpath)
    sftp.close()
    ssh.close()



def tarExtract(tarPath, tarExtractDest):
    print("working on it")
    fileName = os.path.splitext(tarPath)[1]
    if not os.path.exists(fileName):
        os.makedirs(fileName)
        os.chdir(fileName)
    os.chdir(fileName)
    tar = tarfile.open(tarPath, "r:gz")
    tar.extractall()
    tar.close()
