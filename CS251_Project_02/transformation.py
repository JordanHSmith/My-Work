'''transformation.py
Perform projections, translations, rotations, and scaling operations on Numpy ndarray data.
YOUR NAME HERE
CS 251 Data Analysis Visualization
Spring 2023
'''
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
import palettable
import analysis
import data
import scipy.stats


class Transformation(analysis.Analysis):

    def __init__(self, orig_dataset, data=None):

        if(np.any(data) != None):
            super().__init__(data)
        self.orig_dataset = orig_dataset

        '''Constructor for a Transformation object

        Parameters:
        -----------
        orig_dataset: Data object. shape=(N, num_vars).
            Contains the original dataset (only containing all the numeric variables,
            `num_vars` in total).
        data: Data object (or None). shape=(N, num_proj_vars).
            Contains all the data samples as the original, but ONLY A SUBSET of the variables.
            (`num_proj_vars` in total). `num_proj_vars` <= `num_vars`

        TODO:
        - Pass `data` to the superclass constructor.
        - Create an instance variable for `orig_dataset`.
        '''
        pass

    def project(self, headers):

        # def __init__(self, filepath=None, headers=None, data=None, header2col=None):
        
        temp_data = self.orig_dataset.select_data(headers)
        dict = {}
        for i in range(len(headers)):
            dict[headers[i]] = i
        self.data = data.Data(headers = headers,data = temp_data,header2col = dict)

        '''Project the original dataset onto the list of data variables specified by `headers`,
        i.e. select a subset of the variables from the original dataset.
        In other words, your goal is to populate the instance variable `self.data`.

        Parameters:
        -----------
        headers: Python list of str. len(headers) = `num_proj_vars`, usually 1-3 (inclusive), but
            there could be more.
            A list of headers (strings) specifying the feature to be projected onto each axis.
            For example: if headers = ['hi', 'there', 'cs251'], then the data variables
                'hi' becomes the 'x' variable,
                'there' becomes the 'y' variable,
                'cs251' becomes the 'z' variable.
            The length of the list matches the number of dimensions onto which the dataset is
            projected — having 'y' and 'z' variables is optional.

        TODO:
        - Create a new `Data` object that you assign to `self.data` (project data onto the `headers`
        variables). Determine and fill in 'valid' values for all the `Data` constructor
        keyword arguments (except you dont need `filepath` because it is not relevant here).
        '''
        pass

    def get_data_homogeneous(self):
        return np.hstack( (self.data.select_data(self.data.get_headers()),np.ones((self.data.get_all_data().shape[0] ,1))))
        '''Helper method to get a version of the projected data array with an added homogeneous
        coordinate. Useful for homogeneous transformations.

        Returns:
        -----------
        ndarray. shape=(N, num_proj_vars+1). The projected data array with an added 'fake variable'
        column of ones on the right-hand side.
            For example: If we have the data SAMPLE (just one row) in the projected data array:
            [3.3, 5.0, 2.0], this sample would become [3.3, 5.0, 2.0, 1] in the returned array.

        NOTE:
        - Do NOT update self.data with the homogenous coordinate.
        '''
        pass

    def translation_matrix(self, magnitudes):

        t_matrix = np.eye(len(magnitudes)+1)
        t_matrix[:-1,len(magnitudes)] = magnitudes
        t_matrix[-1,len(magnitudes)] = 1
        return t_matrix

        ''' Make an M-dimensional homogeneous transformation matrix for translation,
        where M is the number of features in the projected dataset.

        Parameters:
        -----------
        magnitudes: Python list of float.
            Translate corresponding variables in `headers` (in the projected dataset) by these
            amounts.

        Returns:
        -----------
        ndarray. shape=(num_proj_vars+1, num_proj_vars+1). The transformation matrix.

        NOTE: This method just creates the translation matrix. It does NOT actually PERFORM the
        translation!
        '''
        pass

    def scale_matrix(self, magnitudes):
        magnitudes.append(1)
        return np.diag(magnitudes)


        '''Make an M-dimensional homogeneous scaling matrix for scaling, where M is the number of
        variables in the projected dataset.

        Parameters:
        -----------
        magnitudes: Python list of float.
            Scale corresponding variables in `headers` (in the projected dataset) by these amounts.

        Returns:
        -----------
        ndarray. shape=(num_proj_vars+1, num_proj_vars+1). The scaling matrix.

        NOTE: This method just creates the scaling matrix. It does NOT actually PERFORM the scaling!
        '''
        pass

    def translate(self, magnitudes):
        Mh = np.hstack( (self.data.select_data(self.data.get_headers()),np.ones((self.data.get_all_data().shape[0] ,1))))
        translated_matrix = (self.translation_matrix(magnitudes) @ Mh.T).T
        translated_matrix = translated_matrix[:,:-1]
        self.data = data.Data(headers=self.data.get_headers(),header2col=self.data.get_mappings(),data = translated_matrix)
        return self.data.get_all_data()
        '''Translates the variables `headers` in projected dataset in corresponding amounts specified
        by `magnitudes`.

        Parameters:
        -----------
        magnitudes: Python list of float.
            Translate corresponding variables in `headers` (in the projected dataset) by these amounts.

        Returns:
        -----------
        ndarray. shape=(N, num_proj_vars). The translated data (with all variables in the projected).
            dataset. NOTE: There should be NO homogenous coordinate!

        TODO:
        - Use matrix multiplication to translate the projected dataset, as advertised above.
        - Update `self.data` with a NEW Data object with the SAME `headers` and `header2col`
        dictionary as the current `self.data`, but DIFFERENT data (set to the data you
        transformed in this method). NOTE: The updated `self.data` SHOULD NOT have a homogenous
        coordinate!
        '''
        pass

    def scale(self, magnitudes):
        Mh = np.hstack( (self.data.select_data(self.data.get_headers()),np.ones((self.data.get_all_data().shape[0] ,1))))
        scaled_matrix = (self.scale_matrix(magnitudes) @ Mh.T).T
        scaled_matrix = scaled_matrix[:,:-1]
        self.data = data.Data(headers=self.data.get_headers(),header2col=self.data.get_mappings(),data = scaled_matrix)
        return self.data.get_all_data()

        '''Scales the variables `headers` in projected dataset in corresponding amounts specified
        by `magnitudes`.

        Parameters:
        -----------
        magnitudes: Python list of float.
            Scale corresponding variables in `headers` (in the projected dataset) by these amounts.

        Returns:
        -----------
        ndarray. shape=(N, num_proj_vars). The scaled data (with all variables in the projected).
            dataset. NOTE: There should be NO homogenous coordinate!

        TODO:
        - Use matrix multiplication to scale the projected dataset, as advertised above.
        - Update `self.data` with a NEW Data object with the SAME `headers` and `header2col`
        dictionary as the current `self.data`, but DIFFERENT data (set to the data you
        transformed in this method). NOTE: The updated `self.data` SHOULD NOT have a
        homogenous coordinate!
        '''
        pass

    def transform(self, C):
        self.project(self.data.get_headers())
        h_data = np.hstack( (self.data.select_data(self.data.get_headers()),np.ones((self.data.get_all_data().shape[0] ,1))))
        new = (C@h_data.T).T
        new = new[:,:-1]
        self.data = data.Data(headers=self.data.get_headers(),header2col=self.data.get_mappings(),data = new)
        return self.data.get_all_data()
        '''Transforms the PROJECTED dataset by applying the homogeneous transformation matrix `C`.

        Parameters:
        -----------
        C: ndarray. shape=(num_proj_vars+1, num_proj_vars+1).
            A homogeneous transformation matrix.

        Returns:
        -----------
        ndarray. shape=(N, num_proj_vars). The projected dataset after it has been transformed by `C`

        TODO:
        - Use matrix multiplication to apply the compound transformation matix `C` to the projected
        dataset.
        - Update `self.data` with a NEW Data object with the SAME `headers` and `header2col`
        dictionary as the current `self.data`, but DIFFERENT data (set to the data you
        transformed in this method). NOTE: The updated `self.data` SHOULD NOT have a homogenous
        coordinate!
        '''
        pass

    def normalize_together(self):
        temp_tran_in = np.min(self.data.get_all_data())
        tran_in = []
        for i in range(self.data.get_all_data().shape[1]):
            tran_in.append(temp_tran_in)
        min = np.min(self.data.get_all_data())
        max = np.max(self.data.get_all_data())
        scale_in = []
        for i in range(self.data.get_all_data().shape[1]):
            scale_in.append(1/(max-min))
        norm = self.translate(tran_in) @ self.scale(scale_in).T @ self.data.select_data(self.data.get_headers())
        return norm

        '''Normalize all variables in the projected dataset together by translating the global minimum
        (across all variables) to zero and scaling the global range (across all variables) to one.

        You should normalize (update) the data stored in `self.data`.

        Returns:
        -----------
        ndarray. shape=(N, num_proj_vars). The normalized version of the projected dataset.

        NOTE: Given the goal of this project, for full credit you should implement the normalization
        using matrix multiplications (matrix transformations).
        '''
        pass

    def normalize_separately(self):

        tran_in = self.min(self.data.get_headers())
        tran_in[:-1] = -tran_in[:-1]
        min = self.min(self.data.get_headers())
        max = self.max(self.data.get_headers())
        scale_in = list(1/(max-min))
        norm = self.translate(tran_in) @ self.scale(scale_in).T @ self.data.select_data(self.data.get_headers())
        return norm

        '''Normalize each variable separately by translating its local minimum to zero and scaling
        its local range to one.

        You should normalize (update) the data stored in `self.data`.

        Returns:
        -----------
        ndarray. shape=(N, num_proj_vars). The normalized version of the projected dataset.

        NOTE: Given the goal of this project, for full credit you should implement the normalization
        using matrix multiplications (matrix transformations).
        '''
        pass

    def rotation_matrix_3d(self, header, degrees):

        axis = self.data.get_header_indices([header])

        rot = np.eye(4)

        rad = np.radians(degrees)
        print(rad)

        if(axis[0] == 0):
            rot[1,:] = [0,np.cos(rad),-np.sin(rad),0]
            rot[2,:] = [0,np.sin(rad),np.cos(rad),0]
        elif(axis[0] == 1):
            rot[0,:] = [np.cos(rad),0,np.sin(rad),0]
            rot[2,:] = [-np.sin(rad),0,np.cos(rad),0]
        elif(axis[0] == 2):
            rot[0,:] = [np.cos(rad),-np.sin(rad),0,0]
            rot[1,:] = [np.sin(rad),np.cos(rad),0,0]

        return rot

        '''Make an 3-D homogeneous rotation matrix for rotating the projected data
        about the ONE axis/variable `header`.

        Parameters:
        -----------
        header: str. Specifies the variable about which the projected dataset should be rotated.
        degrees: float. Angle (in degrees) by which the projected dataset should be rotated.

        Returns:
        -----------
        ndarray. shape=(4, 4). The 3D rotation matrix with homogenous coordinate.

        NOTE: This method just creates the rotation matrix. It does NOT actually PERFORM the rotation!
        '''
        pass

    def rotate_3d(self, header, degrees):

        h_data = np.hstack( (self.data.select_data(self.data.get_headers()),np.ones((self.data.get_all_data().shape[0] ,1))))
        rot = self.rotation_matrix_3d(header,degrees)
        new = (rot@h_data.T).T
        new = new[:,:-1]
        self.data = data.Data(headers=self.data.get_headers(),header2col=self.data.get_mappings(),data = new)
        return self.data.get_all_data()

        '''Rotates the projected data about the variable `header` by the angle (in degrees)
        `degrees`.

        Parameters:
        -----------
        header: str. Specifies the variable about which the projected dataset should be rotated.
        degrees: float. Angle (in degrees) by which the projected dataset should be rotated.

        Returns:
        -----------
        ndarray. shape=(N, num_proj_vars). The rotated data (with all variables in the projected).
            dataset. NOTE: There should be NO homogenous coordinate!

        TODO:
        - Use matrix multiplication to rotate the projected dataset, as advertised above.
        - Update `self.data` with a NEW Data object with the SAME `headers` and `header2col`
        dictionary as the current `self.data`, but DIFFERENT data (set to the data you
        transformed in this method). NOTE: The updated `self.data` SHOULD NOT have a
        homogenous coordinate!
        '''
        pass

    def scatter_color(self, ind_var, dep_var, c_var, title=None):
        # self.scatter(ind_var,dep_var,title)

        data_copy = self.orig_dataset.get_all_data()
        fig,ax = plt.subplots(1,1,sharex=True, sharey=True)

        ax.set_title(title)
        ax.set_xlabel(ind_var)
        ax.yaxis.set_label_position("left")
        ax.set_ylabel(dep_var)
        # ax2 = ax.twinx()
        # ax2.yaxis.set_label_position("right")
        # ax2.set_ylabel(c_var)
        color_map = palettable.colorbrewer.sequential.Greys_9
        # cmap = plt.cm.hot

        norm = colors.Normalize(vmin=self.min([c_var]), vmax=self.max([c_var]))

        sm = plt.cm.ScalarMappable(norm = norm)
        # sm.set_label('colorbar label')
        # fig.colorbar(sm)
        cb = plt.colorbar(sm)
        # plt.clim(self.orig_dataset., maximal_value)
        cb.set_label(c_var)

        plt.scatter(data_copy[:,self.orig_dataset.get_mappings()[ind_var]],data_copy[:,self.orig_dataset.get_mappings()[dep_var]],c=data_copy[:,self.orig_dataset.get_mappings()[c_var]],cmap=color_map.mpl_colormap, edgecolor='black')
        # plt.scatter(x, y, s=75, c=z, cmap=color_map.mpl_colormap, edgecolor='black')
        # plt.scatter(X, Y, c=Z, s=75, cmap=color_map.mpl_colormap, edgecolor='black')
        # plt.scatter(data_copy[:,self.orig_dataset.get_mappings()[ind_var]],data_copy[:,self.orig_dataset.get_mappings()[dep_var]],cmap=color_map.mpl_colormap, edgecolor = "black")

        # return data_copy[:,self.data.get_mappings()[ind_var]],data_copy[:,self.data.get_mappings()[dep_var]]

        '''Creates a 2D scatter plot with a color scale representing the 3rd dimension.

        Parameters:
        -----------
        ind_var: str. Header of the variable that will be plotted along the X axis.
        dep_var: Header of the variable that will be plotted along the Y axis.
        c_var: Header of the variable that will be plotted along the color axis.
            NOTE: Use a ColorBrewer color palette (e.g. from the `palettable` library).
        title: str or None. Optional title that will appear at the top of the figure.
        '''
        pass

    def rotation_matrix_2d(self, header, degrees):

        # axis = self.data.get_header_indices([header])

        rad = np.radians(degrees)

        rot = np.eye(3)

        rot[0,:] = [np.cos(rad),-np.sin(rad),0]
        rot[1,:] = [np.sin(rad),np.cos(rad),0]

        return rot

    def rotate_2d(self, header, degrees):
        h_data = np.hstack( (self.data.select_data(self.data.get_headers()),np.ones((self.data.get_all_data().shape[0] ,1))))
        rot = self.rotation_matrix_2d(header,degrees)
        new = (rot@h_data.T).T
        new = new[:,:-1]
        self.data = data.Data(headers=self.data.get_headers(),header2col=self.data.get_mappings(),data = new)
        return self.data.get_all_data()

    def normalize_z(self):
        norm = scipy.stats.zscore(self.data.get_all_data())
        return norm