'''rbf_net.py
Radial Basis Function Neural Network
YOUR NAME HERE
CS 251: Data Analysis Visualization
Spring 2023
'''
import numpy as np
import kmeans
import scipy


class RBF_Net:
    def __init__(self, num_hidden_units, num_classes):
        '''RBF network constructor

        Parameters:
        -----------
        num_hidden_units: int. Number of hidden units in network. NOTE: does NOT include bias unit
        num_classes: int. Number of output units in network. Equals number of possible classes in
            dataset

        TODO:
        - Define number of hidden units as an instance variable called `k` (as in k clusters)
            (You can think of each hidden unit as being positioned at a cluster center)
        - Define number of classes (number of output units in network) as an instance variable
        '''

        self.k = num_hidden_units
        self.num_classes = num_classes


        # prototypes: Hidden unit prototypes (i.e. center)
        #   shape=(num_hidden_units, num_features)
        self.prototypes = None
        # sigmas: Hidden unit sigmas: controls how active each hidden unit becomes to inputs that
        # are similar to the unit's prototype (i.e. center).
        #   shape=(num_hidden_units,)
        #   Larger sigma -> hidden unit becomes active to dissimilar inputs
        #   Smaller sigma -> hidden unit only becomes active to similar inputs
        self.sigmas = None
        # wts: Weights connecting hidden and output layer neurons.
        #   shape=(num_hidden_units+1, num_classes)
        #   The reason for the +1 is to account for the bias (a hidden unit whose activation is always
        #   set to 1).
        self.wts = None

    def get_prototypes(self):
        '''Returns the hidden layer prototypes (centers)

        (Should not require any changes)

        Returns:
        -----------
        ndarray. shape=(k, num_features).
        '''
        return self.prototypes

    def get_num_hidden_units(self):
        return self.k

        '''Returns the number of hidden layer prototypes (centers/"hidden units").

        Returns:
        -----------
        int. Number of hidden units.
        '''
        pass

    def get_num_output_units(self):
        return self.num_classes

        '''Returns the number of output layer units.

        Returns:
        -----------
        int. Number of output units
        '''
        pass

    def avg_cluster_dist(self, data, centroids, cluster_assignments, kmeans_obj):

        num_clusters = centroids.shape[0]
        avg_dists = np.zeros(num_clusters)

        for i in range(num_clusters):
            # Get the indices of the data points assigned to this cluster
            indices = np.where(cluster_assignments == i)[0]

            # Compute the distances between the data points and the cluster centroid
            dists = kmeans_obj.dist_pt_to_centroids(centroids[i], data[indices])

            # Compute the average distance
            avg_dists[i] = np.mean(dists)

        return avg_dists


        # num_clusters = centroids.shape[0]
        # avg_dists = np.zeros(num_clusters)

        # for i in range(num_clusters):
        #     # Get the indices of the data points assigned to this cluster
        #     indices = np.where(cluster_assignments == i)[0]

        #     # Compute the distances between the data points and the cluster centroid
        #     for index in indices:
        #         dists = kmeans_obj.dist_pt_to_centroids(data[indices],centroids)

        #     # Compute the average distance
        #     avg_dists[i] = np.mean(dists)

        # return avg_dists

        '''Compute the average distance between each cluster center and data points that are
        assigned to it.

        Parameters:
        -----------
        data: ndarray. shape=(num_samps, num_features). Data to learn / train on.
        centroids: ndarray. shape=(k, num_features). Centroids returned from K-means.
        cluster_assignments: ndarray. shape=(num_samps,). Data sample-to-cluster-number assignment from K-means.
        kmeans_obj: KMeans. Object created when performing K-means.

        Returns:
        -----------
        ndarray. shape=(k,). Average distance within each of the `k` clusters.

        Hint: A certain method in `kmeans_obj` could be very helpful here!
        '''
        pass

    def initialize(self, data):

        num_clusters = self.get_num_hidden_units()
        kmeans_obj = kmeans.KMeans(data)
        kmeans_obj.cluster_batch(k = self.get_num_hidden_units(), n_iter = 5) #Probably wrong

        self.prototypes = kmeans_obj.get_centroids()
        
        cluster_assignments = kmeans_obj.get_data_centroid_labels()
        self.sigmas = np.zeros(num_clusters)

        avg_dist = self.avg_cluster_dist(data,self.prototypes,cluster_assignments,kmeans_obj)
        self.sigmas = avg_dist

        '''Initialize hidden unit centers using K-means clustering and initialize sigmas using the
        average distance within each cluster

        Parameters:
        -----------
        data: ndarray. shape=(num_samps, num_features). Data to learn / train on.

        TODO:
        - Determine `self.prototypes` (see constructor for shape). Prototypes are the centroids
        returned by K-means. It is recommended to use the 'batch' version of K-means to reduce the
        chance of getting poor initial centroids.
            - To increase the chance that you pick good centroids, set the parameter controlling the
            number of iterations > 1 (e.g. 5)
        - Determine self.sigmas as the average distance between each cluster center and data points
        that are assigned to it. Hint: You implemented a method to do this!
        '''
        pass

    def linear_regression(self, A, y):

        # Add a column of ones to A to handle the intercept
        A = np.concatenate((A, np.ones((A.shape[0], 1))), axis=1)
        
        # Solve the linear system using least squares
        c, _, _, _ = scipy.linalg.lstsq(A, y)

        
        return c


        '''Performs linear regression
        Use SciPy lstsq.

        Parameters:
        -----------
        A: ndarray. shape=(num_data_samps, num_features).
            Data matrix for independent variables.
        y: ndarray. shape=(num_data_samps, 1).
            Data column for dependent variable.

        Returns
        -----------
        c: ndarray. shape=(num_features+1,)
            Linear regression slope coefficients for each independent var AND the intercept term

        NOTE: Remember to handle the intercept ("homogenous coordinate")
        '''
        pass


        '''Performs linear regression
        CS251: Adapt your SciPy lstsq code from the linear regression project.
        CS252: Adapt your QR-based linear regression solver

        Parameters:
        -----------
        A: ndarray. shape=(num_data_samps, num_features).
            Data matrix for independent variables.
        y: ndarray. shape=(num_data_samps, 1).
            Data column for dependent variable.

        Returns
        -----------
        c: ndarray. shape=(num_features+1,)
            Linear regression slope coefficients for each independent var AND the intercept term

        NOTE: Remember to handle the intercept ("homogenous coordinate")
        '''
        pass

    def hidden_act(self, data):

        num_samps = data.shape[0]
        num_clusters = self.prototypes.shape[0]
        activations = np.zeros((num_samps, num_clusters))

        for i in range(num_samps):
            for j in range(num_clusters):
                dist = np.linalg.norm(data[i] - self.prototypes[j])
                activations[i][j] = np.exp(-1 * (dist ** 2) / (2 * (self.sigmas[j] ** 2)+1e-8))

        return activations

        '''Compute the activation of the hidden layer units

        Parameters:
        -----------
        data: ndarray. shape=(num_samps, num_features). Data to learn / train on.

        Returns:
        -----------
        ndarray. shape=(num_samps, k).
            Activation of each unit in the hidden layer to each of the data samples.
            Do NOT include the bias unit activation.
            See notebook for refresher on the activation equation
        '''
        pass

    def output_act(self, hidden_acts):

        # Add bias unit to hidden layer activations
        ones = np.ones((hidden_acts.shape[0],1))
        hidden_acts_bias = np.hstack((hidden_acts,ones))
        
        # Compute activation of output layer using matrix multiplication
        output_acts = hidden_acts_bias @ self.wts
        
        return output_acts


        '''Compute the activation of the output layer units

        Parameters:
        -----------
        hidden_acts: ndarray. shape=(num_samps, k).
            Activation of the hidden units to each of the data samples.
            Does NOT include the bias unit activation.

        Returns:
        -----------
        ndarray. shape=(num_samps, num_output_units).
            Activation of each unit in the output layer to each of the data samples.

        NOTE:
        - Assumes that learning has already taken place
        - Can be done without any for loops.
        - Don't forget about the bias unit!
        '''
        pass

    def train(self, data, y):

        # Initialize the network
        self.initialize(data)
        
        # Recode the class vector to 1s and 0s for each output unit
        y_oh = np.zeros((len(y), self.num_classes))
        for c in range(self.num_classes):
            y_oh[:,c] = (y == c).astype(int)
        
        # Compute the activation of the hidden layer units
        hidden_acts = self.hidden_act(data)
        
        # Compute the weights between the hidden and output layer using linear regression
        A = np.hstack((hidden_acts, np.ones((len(data), 1))))  # Add bias column
        self.wts, _, _, _ = np.linalg.lstsq(A, y_oh, rcond=None)


        '''Train the radial basis function network

        Parameters:
        -----------
        data: ndarray. shape=(num_samps, num_features). Data to learn / train on.
        y: ndarray. shape=(num_samps,). Corresponding class of each data sample.

        Goal: Set the weights between the hidden and output layer weights (self.wts) using
        linear regression. The regression is between the hidden layer activation (to the data) and
        the correct classes of each training sample. To solve for the weights going FROM all of the
        hidden units TO output unit c, recode the class vector `y` to 1s and 0s:
            1 if the class of a data sample in `y` is c
            0 if the class of a data sample in `y` is not c

        Notes:
        - Remember to initialize the network (set hidden unit prototypes and sigmas based on data).
        - Pay attention to the shape of self.wts in the constructor above. Yours needs to match.
        - The linear regression method handles the bias unit.
        '''
        pass

    def predict(self, data):

        # Get the activations of the hidden layer
        hidden_acts = self.hidden_act(data)
        
        # Compute the activations of the output layer
        output_acts = self.output_act(hidden_acts)
        
        # Return the predicted classes
        return np.argmax(output_acts, axis=1)

        '''Classify each sample in `data`

        Parameters:
        -----------
        data: ndarray. shape=(num_samps, num_features). Data to predict classes for.
            Need not be the data used to train the network

        Returns:
        -----------
        ndarray of nonnegative ints. shape=(num_samps,). Predicted class of each data sample.

        TODO:
        - Pass the data thru the network (input layer -> hidden layer -> output layer).
        - For each data sample, the assigned class is the index of the output unit that produced the
        largest activation.
        '''
        pass

    def accuracy(self, y, y_pred):

        return np.mean(y == y_pred)

        '''Computes accuracy based on percent correct: Proportion of predicted class labels `y_pred`
        that match the true values `y`.

        Parameters:
        -----------
        y: ndarray. shape=(num_data_sams,)
            Ground-truth, known class labels for each data sample
        y_pred: ndarray. shape=(num_data_sams,)
            Predicted class labels by the model for each data sample

        Returns:
        -----------
        float. Between 0 and 1. Proportion correct classification.

        NOTE: Can be done without any loops
        '''
        pass