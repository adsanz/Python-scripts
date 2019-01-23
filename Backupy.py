import os
import distutils.core
import time
import zipfile

#copy files to a target folder - creates a logfile which contains the date of the last backup.
def docopy(source, target_folder):
    distutils.dir_util.copy_tree(source, target_folder,update=1)
    #Delete "update=1" if you want a complete backup

def logfile():
    #This def creates a logfile saving the date and time
    source_logfile = '' #route with the logfile ej: D:\Datos\ASIR\ASIRx\ASIR2-xx\COPIA\logfile.txt
    date = time.strftime("Last backup made in: %d of %b, %Y at %H:%M:%S")
    if os.path.exists(source_logfile) == False:
        print("Creating a logfile with actual date")
        f = open(source_logfile, "w+")
        f.write(date)
        f.close()
        print("done")
    else:
        print("Logfile exist, deleting it")
        os.remove(source_logfile)
        print("Creating a new logfile with actual date")
        f = open(source_logfile, "w+")
        f.write(date)
        f.close()
        print("done")

def compress(source_dir, target_zip):
    #This def saves all files of the backup and save it in a zip
    zipf = zipfile.ZipFile(target_zip, "w")
    for subdir, dirs, files in os.walk(source):
        for file in files:
            print(os.path.join(subdir, file))
            zipf.write(os.path.join(subdir, file))
    print("Created", target_zip)

timestr = time.strftime("%Y%m%d-%H%M%S")

if __name__ =='__main__':
    print("Starting execution")
    #back up
    source = '' #source of the copy ej D:\Datos\ASIR\ASIRx\ASIR2-xx\CAMBIOS
    target_folder = '' #target where the files are gonna be coppied D:\Datos\ASIR\ASIRx\ASIR2-xx\COPIA
    try:
        docopy(source, target_folder)
        print("Done backing up!")
        logfile()
    except:
        print("Something went wrong!")
    external_disk = input("Do you want to save to external disk?: ")
    if external_disk == "Yes" or "Si" or "Y":
        try:
            print("Starting to compress to disk!")
            source_dir = '' #source where the files are gonna be compressed ej D:\Datos\ASIR\ASIRx\ASIR2-xx\COPIA
            target_zip = '{}.zip'.format(timestr) #where the file is gonna be saved as a zip ej E:\ASIRx\compressed_backup\
            compress(source_dir, target_zip)
            print("Compress is done!")
        except:
            print("Media not connected!")
    else:
        print("Okey, backup done! exiting now")
else:
    print("Something went terribly wrong!")
