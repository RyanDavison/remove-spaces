############################################################################################################################################################################################
##Remove_Spaces_From_Path.py
##
##Author: Ryan Davison
##
##
##Date: August 9, 2012
##
##Purpose: This script loops through a root directory and its sub directories and removes spaces from paths and file names
##
############################################################################################################################################################################################
import  os, sys


fixWhat = raw_input(r'Are you fixing the file path(enter 1) or just the actual file name(enter 2): ')
directorypath = raw_input("-->Enter path of top level folder: ")
directorypath = str(directorypath)

print

#Loop through all subfolders in your target directory. Find each map document and check to see if the mxd name has a space. The script then replaces the space with an underscore.
def fileFixer():
      for root, dirs, files in os.walk(directorypath):
            for di in dirs:
                  if ' ' in di and ' - ' not in di:
                        print di
                        newDi1 = di.replace(' ', '_')
                        try:
                              os.rename(os.path.join(root, di), os.path.join(root, newDi1))
                              fixedList.append(newDi1)
                              del newDi1
                        except:
                              pass


def mxdFixer():
      extension = raw_input(r'what type of file do you want to fix(input an extension): .')
      for root, dirs, files in os.walk(directorypath):
            for fi in files:
                  if fi.endswith(extension):
                        fileList = [fi]
                        for item in fileList:
                              if ' ' in item and ' - ' not in item:
                                    print item
                                    newFile = item.replace(' ', '_')
                                    try:
                                          os.rename(os.path.join(root, item), os.path.join(root, newFile))
                                          fixedList.append(newFile)
                                          del newFile
                                          del fileList
                                    except:
                                          pass



if fixWhat == '1':
      fileFixer()
else:
      mxdFixer()


class Repeat():
      y = raw_input("Do you want to run the tool again? (y/n): ")
      print
      if y == 'y':
            execfile(os.path.realpath(__file__))
      elif y != y:
            print "Done"





