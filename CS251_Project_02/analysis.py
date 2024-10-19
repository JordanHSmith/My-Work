'''analysis.py
Run statistical analyses and plot Numpy ndarray data
YOUR NAME HERE
CS 251 Data Analysis Visualization
Spring 2023
'''
import numpy as np
import matplotlib.pyplot as plt


class Analysis:
    def __init__(self, data):
        '''

        Parameters:
        -----------
        data: Data object. Contains all data samples and variables in a dataset.
        '''
        self.data = data

        # Make plot font sizes legible
        plt.rcParams.update({'font.size': 18})

    def set_data(self, data):
        self.data = data

        '''Method that re-assigns the instance variable `data` with the parameter.
        Convenience method to change the data used in an analysis without having to create a new
        Analysis object.

        Parameters:
        -----------
        data: Data object. Contains all data samples and variables in a dataset.
        '''
        pass

    def min(self, headers, rows=[]):

        return np.amin(self.data.select_data(headers,rows),axis = 0)

       



        '''Computes the minimum of each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.
        (i.e. the minimum value in each of the selected columns)

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of min over, or over all indices
            if rows=[]

        Returns
        -----------
        mins: ndarray. shape=(len(headers),)
            Minimum values for each of the selected header variables

        NOTE: There should be no loops in this method!
        '''
        pass

    def max(self, headers, rows=[]):

        return np.amax(self.data.select_data(headers,rows),axis = 0)

        '''Computes the maximum of each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of max over, or over all indices
            if rows=[]

        Returns
        -----------
        maxs: ndarray. shape=(len(headers),)
            Maximum values for each of the selected header variables

        NOTE: There should be no loops in this method!
        '''
        pass

    def range(self, headers, rows=[]):

        return [np.amin(self.data.select_data(headers,rows),axis = 0), np.amax(self.data.select_data(headers,rows),axis = 0)]


        '''Computes the range [min, max] for each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of min/max over, or over all indices
            if rows=[]

        Returns
        -----------
        mins: ndarray. shape=(len(headers),)
            Minimum values for each of the selected header variables
        maxes: ndarray. shape=(len(headers),)
            Maximum values for each of the selected header variables

        NOTE: There should be no loops in this method!
        '''
        pass

    def mean(self, headers, rows=[]):

        if(rows == []):
            num_rows = self.data.get_num_samples()
        else:
            num_rows = len(rows)
        total = np.sum(self.data.select_data(headers,rows),axis = 0)

        mean = total / num_rows

        return mean

        '''Computes the mean for each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`).

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of mean over, or over all indices
            if rows=[]

        Returns
        -----------
        means: ndarray. shape=(len(headers),)
            Mean values for each of the selected header variables

        NOTE: You CANNOT use np.mean here!
        NOTE: There should be no loops in this method!
        '''
        pass

    def var(self, headers, rows=[]):

        numerator = np.sum(np.square(self.data.select_data(headers,rows) - self.mean(headers,rows)),axis = 0)
        
        if(rows == []):
            denominator = self.data.get_num_samples() - 1
        else:
            denominator = len(rows) - 1

        return numerator / denominator

        '''Computes the variance for each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of variance over, or over all indices
            if rows=[]

        Returns
        -----------
        vars: ndarray. shape=(len(headers),)
            Variance values for each of the selected header variables

        NOTE: You CANNOT use np.var or np.mean here!
        NOTE: There should be no loops in this method!
        '''
        pass

    def std(self, headers, rows=[]):

        return np.sqrt(self.var(headers,rows))

        '''Computes the standard deviation for each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of standard deviation over,
            or over all indices if rows=[]

        Returns
        -----------
        vars: ndarray. shape=(len(headers),)
            Standard deviation values for each of the selected header variables

        NOTE: You CANNOT use np.var, np.std, or np.mean here!
        NOTE: There should be no loops in this method!
        '''
        pass

    def show(self):
        '''Simple wrapper function for matplotlib's show function.

        (Does not require modification)
        '''
        plt.show()

    def scatter(self, ind_var, dep_var, title):

        data_copy = self.data.get_all_data()

        plt.title(title)
        plt.xlabel(ind_var)
        plt.ylabel(dep_var)
        plt.scatter(data_copy[:,self.data.get_mappings()[ind_var]],data_copy[:,self.data.get_mappings()[dep_var]])

        return data_copy[:,self.data.get_mappings()[ind_var]],data_copy[:,self.data.get_mappings()[dep_var]]

        # ax[0,0].set_title("Rows 0-10")
        # ax[0,0].set_ylabel("Y")
        # ax[0,0].set_xlabel("X")
        # ax[0,0].scatter(data_copy[:10,0],data_copy[:10,1])

        '''Creates a simple scatter plot with "x" variable in the dataset `ind_var` and
        "y" variable in the dataset `dep_var`. Both `ind_var` and `dep_var` should be strings
        in `self.headers`.

        Parameters:
        -----------
        ind_var: str.
            Name of variable that is plotted along the x axis
        dep_var: str.
            Name of variable that is plotted along the y axis
        title: str.
            Title of the scatter plot

        Returns:
        -----------
        x. ndarray. shape=(num_data_samps,)
            The x values that appear in the scatter plot
        y. ndarray. shape=(num_data_samps,)
            The y values that appear in the scatter plot

        NOTE: Do not call plt.show() here.
        '''
        pass

    def pair_plot(self, data_vars, fig_sz=(12, 12), title=''):

        data_copy = self.data.get_all_data()

        fig,ax = plt.subplots(nrows = len(data_vars), ncols = len(data_vars),figsize = fig_sz, sharex="col",sharey="row")

        fig.suptitle(title)

        # x_min = 1000
        # y_min = 1000
        # x_max = -1
        # y_max = -1
        y_min_list = []
        y_max_list = []

        for i in range(len(data_vars)):
            # if(i != 0):
            #     y_min_list.append(y_min)
            #     y_max_list.append(y_max)
            # y_min = 1000
            # y_max = -1
            # if(self.min([data_vars[i]])[0] < y_min):
            #     y_min = self.min([data_vars[i]])[0]
            #     y_mid = (y_min+y_max)/2
            # if(self.max([data_vars[i]])[0] > y_max):
            #     y_max = self.max([data_vars[i]])[0]
            #     y_mid = (y_min+y_max)/2
            # ax[i,0].set_yticks([round(y_min,1),round(y_mid,1),round(y_max,1)])
            ax[i,0].set_ylabel(data_vars[i])
            for j in range(len(data_vars)):
                # x_min = 1000
                # x_max = -1
                # if(self.min([data_vars[j]])[0] < x_min):
                #     x_min = self.min([data_vars[j]])[0]
                #     x_mid = (x_min+x_max)/2
                # if(self.max([data_vars[j]])[0] > x_max):
                #     x_max = self.max([data_vars[j]])[0]
                #     x_mid = (x_min+x_max)/2
                # ax[len(data_vars)-1,j].set_xticks([round(x_min,1),round(x_mid,1),round(x_max,1)])
                ax[len(data_vars)-1,j].set_xlabel(data_vars[j])
                ax[i,j].scatter(data_copy[:,self.data.get_mappings()[data_vars[j]]],data_copy[:,self.data.get_mappings()[data_vars[i]]])

        # y_min = 1000
        # y_max = -1
        # if(self.min([data_vars[i]])[0] < y_min):
        #     y_min = self.min([data_vars[i]])[0]
        #     y_mid = (y_min+y_max)/2
        # if(self.max([data_vars[i]])[0] > y_max):
        #     y_max = self.max([data_vars[i]])[0]
        #     y_mid = (y_min+y_max)/2

        return fig,ax

        '''Create a pair plot: grid of scatter plots showing all combinations of variables in
        `data_vars` in the x and y axes.

        Parameters:
        -----------
        data_vars: Python list of str.
            Variables to place on either the x or y axis of the scatter plots
        fig_sz: tuple of 2 ints.
            The width and height of the figure of subplots. Pass as a paramter to plt.subplots.
        title. str. Title for entire figure (not the individual subplots)

        Returns:
        -----------
        fig. The matplotlib figure.
            1st item returned by plt.subplots
        axes. ndarray of AxesSubplot objects. shape=(len(data_vars), len(data_vars))
            2nd item returned by plt.subplots

        TODO:
        - Make the len(data_vars) x len(data_vars) grid of scatterplots
        - The y axis of the first column should be labeled with the appropriate variable being
        plotted there.
        - The x axis of the last row should be labeled with the appropriate variable being plotted
        there.
        - There should be no other axis or tick labels (it looks too cluttered otherwise!)

        Tip: Check out the sharex and sharey keyword arguments of plt.subplots.
        Because variables may have different ranges, pair plot columns usually share the same
        x axis and rows usually share the same y axis.
        '''
        pass