import os
import fnmatch

def list_all_files(directory, extensions=None):
    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            base, ext = os.path.splitext(filename)
            joined = os.path.join(root, filename)
            if extensions is None or ext.lower() in extensions:
                yield joined

def list_all_dirs(directory):
    return [x[0] for x in os.walk(directory)]

def list_all_files_within_subdirs(directory, extensions=None):
    alldirs = list_all_dirs(data_root)
    allfiles = list()
    for i in alldirs:
        addition = list(list_all_files(i, ".wav"))
        allfiles = allfiles + addition
    return allfiles

#data_root = "/Users/zebra/Developer/Python/AudioNotebooks/data/drums/samples/!llmind/!llmind BLAP-KIT 808s & STRING BREAKS/808s"
data_root = "/Users/zebra/Developer/Python/AudioNotebooks/data/drums/samples/"
print list_all_files_within_subdirs(data_root)
#x = list(list_all_files(data_root, ".wav"))
#print (x)
