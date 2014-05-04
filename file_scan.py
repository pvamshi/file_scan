from os import listdir,getcwd
from os.path import isfile,join, islink
import json

class File(object):

    def __init__(self):
        self.name =""
        self.path = ""
        self.isdir = False
        self.parent_file = 0
        self.children_files = []
        self.children_dirs = []

    def __str__(self):
        json_str  = '{'
        json_str += '"name":"%s", '%(self.name)
        json_str += '"path":"%s", '%(self.path)
        json_str += '"isdir":%s, '%(str(self.isdir).lower())
        json_str += '"parent_file":"%s", '%(self.parent_file)
        json_str += '"children_dirs":%s,'%(self.children_dirs)
        json_str += '"children_files":%s'%(self.children_files)
        json_str += '}'
        return json_str


files=[]

def scan_files(root_index):
    #print " root_index is %s"%root_index
    root_file = files[root_index]
    files_local = listdir(root_file.path)
    #print " files_local for %s is %s"%(root_file.name, files_local)
    for file in files_local:
        file_path = join(root_file.path, file)
        if file[0] == "." or  islink(file_path) :
            continue
        file_obj = File()
        #print "blank file is %s"%file_obj
        file_obj.name = file
        file_obj.path = file_path
        file_obj.isdir = not isfile(file_obj.path)
        file_obj.parent_file = root_index
        files.append(file_obj)
        file_index = len(files)-1
        if file_obj.isdir :
            root_file.children_dirs.append(file_index)
            scan_files(file_index)
        else:
            root_file.children_files.append(file_index)
        #print " newly created file %s"%file_obj

def get_file_scan(path=None):
    root = File()
    if path == None:
        path = getcwd()
    folders = path.split("/")
    root.name = folders[-1] if folders[-1] != "" else folders[-2]
    print root.name
    root.isdir = True
    root.path = path
    files.append(root)
    scan_files(len(files)-1)
    #print root
    """
    print "files finally is :"
    for index,fil in enumerate(files):
        print index
        print fil
        print ""
    """
    json_result = "[%s]"%",".join([ str(f) for f in files ])
    print "final json looks like %s"%json_result
    return json_result


if __name__=="__main__":
    filename = raw_input('Enter a file name: ')
    print filename
    #get_file_scan()
    if filename == "":
        filename = None
    get_file_scan(filename)

