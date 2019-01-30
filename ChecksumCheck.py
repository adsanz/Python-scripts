import os
import hashlib
import sys
import json

version = "0.0.1"
author = "@AdSanz_IT"

#dictionaries that will hold the file with his checksum
dict_hashes = {}
dict_hashes1 = {}
#file where the hashes will be saved
filename = 'hash.txt'
#source admits a list of dicrectories, remember if the path has "\" it must be specified like C:\\System\\... Because in python backslash is an escape character ej -> "source = ['E:\\ASIR2\\ACTUALIZADO\\ASOE104','E:\\ASIR2\\ACTUALIZADO\\ASOE103']"
source = []
#source = ''


def help_s():
    print("This script is intended to check the integrity of files located in the \"source\" recursively. It saves the checksums on {}, and later on you can compare them overtime, it also checks whether a new file was created.\n\nThe tool itself is to check whether a file has been modified by any means.\n\n Usage = \n ChecksumChecker.py 1/2 \n\n Options: \n--> 1 = Get checksums on source and save it on {} \n--> 2 = Compare the checksums on source with checksums saved on {} \n\nRemember: whenever you change the source variable, you should use (1) to save the checksum of those files before checking!!!".format(filename,filename,filename))

def get_checksums_list():
    # Use this def if "source" is a list of dicrectories
    for items in source:
        for subdirs,dirs,files in os.walk(items):
            for name in files:
                filename1 = os.path.join(subdirs,name)
                with open(filename1, 'rb') as f:
                    hasher = hashlib.md5()
                    while True:
                        data = f.read(65536)
                        if not data:
                            break
                        hasher.update(data)
                    hex_val = hasher.hexdigest()
                    dict_hashes.update({filename1:hex_val})

def get_checksums():
    # Use this def is "source" is only a directory and not a list
    for subdirs,dirs,files in os.walk(source):
        for name in files:
            filename1 = os.path.join(subdirs,name)
            with open(filename1, 'rb') as f:
                hasher = hashlib.md5()
                while True:
                    data = f.read(65536)
                    if not data:
                        break
                    hasher.update(data)
                hex_val = hasher.hexdigest()
                dict_hashes.update({filename1:hex_val})

def get_checksums1():
    # This def get the checksums of the file and saves it on a dictionary
    with open(filename, 'r+') as output:
        dict_hashes1.update(json.load(output))


def create():
    # Save checksums (from get_checksums / get_checksums_list) on the file
    with open(filename, 'w+') as checksums:
        checksums.write(json.dumps(dict_hashes))

def compare_checksums():

    for key,value in zip(dict_hashes.keys(),dict_hashes.values()):
        if key in dict_hashes1.keys():
            if value in dict_hashes1.values():
                print("Checked: {}".format(key))
                print("Integrity OK")
            elif value not in dict_hashes1.values():
                print("Checked: {}".format(key))
                print("New checksum -> \"{}\"  |  checksum on {} -> \"{}\"".format(value,filename,dict_hashes1[key]))
                print("Integrity not OK")
        elif key not in dict_hashes1.keys():
            print("The file {} is not on {}, not checking".format(key,filename))
            pass

if len(sys.argv) < 2:
    help_s()
elif len(sys.argv) == 2 and len(sys.argv) < 3:
    print(" Script made by {}: https://github.com/adsanz/Python-scripts \n Version: {}\n\n".format(author,version))
    if sys.argv[1] == "1":
        try:
            get_checksums()
        except:
            get_checksums_list()
        create()
        if os.path.isfile(filename):
            print("Saved checksums on {}".format(filename))
        else:
            print("Created file {} and saved checksums".format(filename))
    elif sys.argv[1] == "2":
        try:
            get_checksums()
        except:
            get_checksums_list()
        get_checksums1()
        compare_checksums()
        print("Done...")
    else:
        print("Choose a value between 1 and 2\n")
        help_s()
else:
    print("This script only takes 1 argument between 1 and 2\n")
    help_s()
