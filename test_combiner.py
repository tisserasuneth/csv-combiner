#Unit Tests
#Interviewee: Suneth Tissera, tisserasuneth@gmail.com
#Company: PMG Digital Agency

import unittest
import unittest.mock
import sys
import os
import pandas as pd
from io import StringIO as strIO
from combiner import Combiner
import generate_forTest

class TestCombiner(unittest.TestCase):

    accessoriesPath = ''
    clothingPath = ''
    createdOutput = ''
    
    @classmethod
    def setUpClass(cls):
        #Creating necessary files and paths
        if (os.path.exists('./test_csv'))==False:
            os.mkdir('./test_csv')
        
        cls.accessoriesPath = './test_csv/test_accessories.csv'
        cls.clothingPath = './test_csv/test_clothing.csv'
        cls.createdOutput = './test_csv/test_output.csv'

        #Generating Smaller CSV files for testing purposes
        generate_forTest.main()
    
    @classmethod
    def tearDownClass(cls):
        #Removing files and directories at the end of testing process
        os.remove(cls.accessoriesPath)
        os.remove(cls.clothingPath)
        os.remove(cls.createdOutput)
        os.rmdir('./test_csv')


#---Tests for validate() method

    def test_validate_no_files(self):  
        # Test case where no files are passed into stdin
        sys.argv = ['combiner.py']
        with unittest.mock.patch('sys.stdout', new=strIO()) as stdout:
            Combiner.validate()
            self.assertIn('No files entered! Please run the command with the path to each file', stdout.getvalue())
    
    def test_validate_valid_files(self):
        # Test case where valid files are passed into stdin
        sys.argv = ['combiner.py', 'accessories.csv', 'clothing.csv']
        os.path.exists = lambda path: True
        self.assertEqual(Combiner.validate(),['accessories.csv', 'clothing.csv'])

    def test_validate_invalid_files(self):
        # Test case where invalid files are passed into stdin
        sys.argv = ['combiner.py', 'accessories.csv', 'clothing.csv']
        os.path.exists = lambda path: path != 'clothing.csv'
        with unittest.mock.patch('sys.stdout', new=strIO()) as stdout:
            Combiner.validate()
            self.assertIn('One or more files not found! Check input', stdout.getvalue())

#---Tests for combine() method
    
    def test_combine_filenameCol(self):
        #Test case to confirm the 'filename' column is added to dataframe
        files = [self.accessoriesPath,self.clothingPath]
        output = open(self.createdOutput, 'w+')
        output.write(Combiner.combine(files))
        output.close()
        df = pd.read_csv('./test_csv/test_output.csv')
        self.assertTrue('filename' in df.columns)

    def test_combine_csv_match(self):
        #Test case to confirm that the csv files combine as required
        output = open(self.createdOutput, 'w+')
        files = [self.accessoriesPath,self.clothingPath]
        output.write(Combiner.combine(files))
        output.close()
        testDataFrame = pd.read_csv(self.createdOutput,index_col=False)

        with open(self.accessoriesPath) as f:
            a = pd.read_csv(f)
            a['filename']= os.path.basename(self.accessoriesPath)
        with open(self.clothingPath) as f:
            b = pd.read_csv(f)
            b['filename']= os.path.basename(self.clothingPath)
        trueDataFrame = pd.concat([a,b],ignore_index=True)
        result = testDataFrame.equals(trueDataFrame)
        self.assertEqual(result,True)
   
if __name__ == '__main__':
    unittest.main()