import os

def createDirectory(directoryName):
    # check if required directory is a subdirectory & run appropriate code
    if ("/" in directoryName):    
        # create target directory & all intermediate directories if they don't exist
        if not os.path.exists(directoryName):
            os.makedirs(directoryName)
            print("Directory " + directoryName + " created ")
        else:    
            print("Directory " + directoryName + " already exists")
    else:
        # create target directory if it doesn't exist
        if not os.path.exists(directoryName):
            os.mkdir(directoryName)
            print("Directory " + directoryName + " created ")
        else:    
            print("Directory " + directoryName + " already exists")

createDirectory("rates/daily")
createDirectory("rates/weekly")
createDirectory("rates/monthly")