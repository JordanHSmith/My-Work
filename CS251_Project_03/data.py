'''data.py
Reads CSV files, stores data, access/filter data by variable name
YOUR NAME HERE
CS 251 Data Analysis and Visualization
Spring 2023
'''

import numpy as np
import csv


class Data:
    def __init__(self, filepath=None, headers=None, data=None, header2col=None):
        
        self.headers = headers
        self.filepath = filepath
        self.data = data
        self.header2col = header2col
        if(filepath != None):
            self.read(self.filepath)


        pass

        '''Data object constructor

        Parameters:
        -----------
        filepath: str or None. Path to data .csv file
        headers: Python list of strings or None. List of strings that explain the name of each
            column of data.
        data: ndarray or None. shape=(N, M).
            N is the number of data samples (rows) in the dataset and M is the number of variables
            (cols) in the dataset.
            2D numpy array of the dataset’s values, all formatted as floats.
            NOTE: In Week 1, don't worry working with ndarrays yet. Assume it will be passed in
                  as None for now.
        header2col: Python dictionary or None.
                Maps header (var str name) to column index (int).
                Example: "sepal_length" -> 0

        TODO:
        - Declare/initialize the following instance variables:
            - filepath
            - headers
            - data
            - header2col
            - Any others you find helpful in your implementation
        - If `filepath` isn't None, call the `read` method.
        '''

    def read(self, filepath):

        self.headers = []
        self.filepath = filepath
        self.data = []
        self.header2col = {}

        file = open(filepath, "r")
        data = list(csv.reader(file, skipinitialspace = True, delimiter = ","))
        file.close()

        for i in range(len(data[0])):
            if(data[1][i] == "numeric"):
                if(data[0][i][-1] == " "):
                    self.headers.append(data[0][i][:-1])
                else:
                    self.headers.append(data[0][i])


        if(self.headers == []):
            print("You need to have headers stating the type of data in your second row")
            return

        for i in range(len(self.headers)):
            self.header2col[self.headers[i]] = i


        line = []
        for i in range(2,len(data)):
            for j in range(len(data[0])):
                if(data[1][j] == "numeric"):
                    line.append(float(data[i][j]))
            self.data.append(line)
            line = []

        self.data = np.array(self.data)
        

        pass

        '''Read in the .csv file `filepath` in 2D tabular format. Convert to numpy ndarray called
        `self.data` at the end (think of this as 2D array or table).

        Format of `self.data`:
            Rows should correspond to i-th data sample.
            Cols should correspond to j-th variable / feature.

        Parameters:
        -----------
        filepath: str or None. Path to data .csv file

        Returns:
        -----------
        None. (No return value).
            NOTE: In the future, the Returns section will be omitted from docstrings if
            there should be nothing returned

        TODO:
        - Read in the .csv file `filepath` to set `self.data`. Parse the file to only store
        numeric columns of data in a 2D tabular format (ignore non-numeric ones). Make sure
        everything that you add is a float.
        - Represent `self.data` (after parsing your CSV file) as an numpy ndarray. To do this:
            - At the top of this file write: import numpy as np
            - Add this code before this method ends: self.data = np.array(self.data)
        - Be sure to fill in the fields: `self.headers`, `self.data`, `self.header2col`.

        NOTE: You may wish to leverage Python's built-in csv module. Check out the documentation here:
        https://docs.python.org/3/library/csv.html

        NOTE: In any CS251 project, you are welcome to create as many helper methods as you'd like.
        The crucial thing is to make sure that the provided method signatures work as advertised.

        NOTE: You should only use the basic Python library to do your parsing.
        (i.e. no Numpy or imports other than csv).
        Points will be taken off otherwise.

        TIPS:
        - If you're unsure of the data format, open up one of the provided CSV files in a text editor
        or check the project website for some guidelines.
        - Check out the test scripts for the desired outputs.
        '''

    def __str__(self):

        string = ""

        shape_str = "(" + str(self.data.shape[0]) + "x" + str(self.data.shape[1]) + ")\n"
        string += self.filepath + " " + shape_str + "\n"
        string += "Headers:\n"
        string += "    "
        for header in self.headers:
            string += header + "   "

        num_lines = 0
        if(len(self.data) > 5):
            num_lines = 5
        else:
            num_lines = len(self.data)

        if(num_lines == 5):
            string += "\nShowing first 5/" + str(self.data.shape[0]) + " rows.\n"
        else:
            string += "\n"

        
        for i in range(num_lines):
            for j in range(len(self.data[0])):
                string += str(self.data[i][j]) + "   "
            string += "\n"

        return string

        '''toString method

        (For those who don't know, __str__ works like toString in Java...In this case, it's what's
        called to determine what gets shown when a `Data` object is printed.)

        Returns:
        -----------
        str. A nicely formatted string representation of the data in this Data object.
            Only show, at most, the 1st 5 rows of data
            See the test code for an example output.
        '''

    def get_headers(self):
        
        return self.headers
        
        '''Get method for headers

        Returns:
        -----------
        Python list of str.
        '''
        pass

    def get_mappings(self):

        return self.header2col

        '''Get method for mapping between variable name and column index

        Returns:
        -----------
        Python dictionary. str -> int
        '''
        pass

    def get_num_dims(self):
        
        return len(self.headers)

        '''Get method for number of dimensions in each data sample

        Returns:
        -----------
        int. Number of dimensions in each data sample. Same thing as number of variables.
        '''
        pass

    def get_num_samples(self):
        return len(self.data)

        '''Get method for number of data points (samples) in the dataset

        Returns:
        -----------
        int. Number of data samples in dataset.
        '''
        pass

    def get_sample(self, rowInd):

        return self.data[rowInd]

        '''Gets the data sample at index `rowInd` (the `rowInd`-th sample)

        Returns:
        -----------
        ndarray. shape=(num_vars,) The data sample at index `rowInd`
        '''
        pass

    def get_header_indices(self, headers):

        indices = []
        for header in headers:
            indices.append(self.header2col[header])

        return indices
        '''Gets the variable (column) indices of the str variable names in `headers`.

        Parameters:
        -----------
        headers: Python list of str. Header names to take from self.data

        Returns:
        -----------
        Python list of nonnegative ints. shape=len(headers). The indices of the headers in `headers`
            list.
        '''
        pass

    def get_all_data(self):
        return np.copy(self.data)
        '''Gets a copy of the entire dataset

        (Week 2)

        Returns:
        -----------
        ndarray. shape=(num_data_samps, num_vars). A copy of the entire dataset.
            NOTE: This should be a COPY, not the data stored here itself.
            This can be accomplished with numpy's copy function.
        '''
        pass

    def head(self):
        short_data = []
        line = []

        num_lines = 0
        if(len(self.data) > 5):
            num_lines = 5
        else:
            num_lines = len(self.data)


        for i in range(num_lines):
            line = []
            for j in range(len(self.data[0])):
                line.append(self.data[i][j])
            short_data.append(line)
        short_data = np.array(short_data)
        return short_data


        '''Return the 1st five data samples (all variables)

        (Week 2)

        Returns:
        -----------
        ndarray. shape=(5, num_vars). 1st five data samples.
        '''
        pass

    def tail(self):
        short_data = []
        line = []

        num_lines = 0
        start_index = 0
        if(len(self.data) > 5):
            num_lines = 5
            start_index = len(self.data)-5
        else:
            num_lines = len(self.data)
            start_index = 0

        for i in range(start_index,start_index+num_lines):
            line = []
            for j in range(len(self.data[0])):
                line.append(self.data[i][j])
            short_data.append(line)
        short_data = np.array(short_data)
        return short_data
        '''Return the last five data samples (all variables)

        (Week 2)

        Returns:
        -----------
        ndarray. shape=(5, num_vars). Last five data samples.
        '''
        pass

    def limit_samples(self, start_row, end_row):
        short_data = []
        line = []


        for i in range(start_row,end_row):
            line = []
            for j in range(len(self.data[0])):
                line.append(self.data[i][j])
            short_data.append(line)
        self.data = np.array(short_data)


        '''Update the data so that this `Data` object only stores samples in the contiguous range:
            `start_row` (inclusive), end_row (exclusive)
        Samples outside the specified range are no longer stored.

        (Week 2)

        '''
        pass

    def select_data(self, headers, rows=[]):
        short_data = []
        line = []
        for i in range(len(self.data)):
            line = []
            for j in range(len(self.headers)):
                for header in headers:
                    if(header == self.headers[j]):
                        if rows != []:
                            for row in rows:
                                if row == i:
                                    line.append(self.data[i,j])
                        else:
                            line.append(self.data[i,j])
            if([] in short_data):
                short_data.remove([])
            short_data.append(line)
        if([] in short_data):
            short_data.remove([])
        short_data = np.array(short_data)
        return short_data
            


        '''Return data samples corresponding to the variable names in `headers`.
        If `rows` is empty, return all samples, otherwise return samples at the indices specified
        by the `rows` list.

        (Week 2)

        For example, if self.headers = ['a', 'b', 'c'] and we pass in header = 'b', we return
        column #2 of self.data. If rows is not [] (say =[0, 2, 5]), then we do the same thing,
        but only return rows 0, 2, and 5 of column #2.

        Parameters:
        -----------
            headers: Python list of str. Header names to take from self.data
            rows: Python list of int. Indices of subset of data samples to select.
                Empty list [] means take all rows

        Returns:
        -----------
        ndarray. shape=(num_data_samps, len(headers)) if rows=[]
                 shape=(len(rows), len(headers)) otherwise
            Subset of data from the variables `headers` that have row indices `rows`.

        Hint: For selecting a subset of rows from the data ndarray, check out np.ix_
        '''
        pass