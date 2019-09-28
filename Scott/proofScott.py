from os import listdir
from os.path import isfile, join
def inputToList (mainPath):
        onlyFiles = [f for f in listdir(mainPath) if isfile(join(mainPath, f))]
        return onlyFiles;
        

