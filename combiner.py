#Combining CSV Files
#Interviewee: Suneth Tissera, tisserasuneth@gmail.com
#Company: PMG Digital Agency

#The files are first validated by checking if an input was given 
#If an input was given, existence of files are checked
#The list of files are then passed inside combine()
#The list is iterated through -> broken into chunks
#Each chunk is added into a dataframe using pd.concat()
#Dataframe is returned as a csv file

import os
import sys
import pandas as pd

class Combiner: 
    def validate():  #Validates input
        if (sys.argv == ['combiner.py']):
            print('No files entered! Please run the command with the path to each file')
            return
            
        del sys.argv[0]
        files = sys.argv

        for file in files:
            if (os.path.exists(file)==False):
                print('One or more files not found! Check input')
                return
        return files
    
    def combine(files): #Combines CSV Files
        df = pd.DataFrame()
        for file in files:
            for chunk in pd.read_csv(file,chunksize=10000, low_memory=False):
                chunk['filename']= os.path.basename(file)
                df = pd.concat([df,chunk])

        df = df.to_csv(index=False, chunksize=10000, line_terminator='\n')
        return df

def main():
    #Validates input
    validation = Combiner.validate()
    #if Validated -> Combine files
    if (validation):
        print(Combiner.combine(validation))

if __name__ == '__main__': 
    main()
