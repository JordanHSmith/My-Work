'''kmeans.py
Performs K-Means clustering
YOUR NAME HERE
CS 251: Data Analysis Visualization
Spring 2023
'''
import numpy as np
import matplotlib.pyplot as plt
from palettable import cartocolors
import random


class KMeans:
    def __init__(self, data=None):
        '''KMeans constructor

        (Should not require any changes)

        Parameters:
        -----------
        data: ndarray. shape=(num_samps, num_features)
        '''

        # k: int. Number of clusters
        self.k = None
        # centroids: ndarray. shape=(k, self.num_features)
        #   k cluster centers
        self.centroids = None
        # data_centroid_labels: ndarray of ints. shape=(self.num_samps,)
        #   Holds index of the assigned cluster of each data sample
        self.data_centroid_labels = None

        # inertia: float.
        #   Mean squared distance between each data sample and its assigned (nearest) centroid
        self.inertia = None

        # data: ndarray. shape=(num_samps, num_features)
        self.data = data
        # num_samps: int. Number of samples in the dataset
        self.num_samps = None
        # num_features: int. Number of features (variables) in the dataset
        self.num_features = None
        if data is not None:
            self.num_samps, self.num_features = data.shape

    def set_data(self, data):
        self.data = data
        self.num_samps = data.shape[0]
        self.num_features = data.shape[1]

        '''Replaces data instance variable with `data`.

        Reminder: Make sure to update the number of data samples and features!

        Parameters:
        -----------
        data: ndarray. shape=(num_samps, num_features)
        '''
        pass

    def get_data(self):
        copy = np.copy(self.data)
        return copy

        '''Get a COPY of the data

        Returns:
        -----------
        ndarray. shape=(num_samps, num_features). COPY of the data
        '''
        pass

    def get_centroids(self):
        '''Get the K-means centroids

        (Should not require any changes)

        Returns:
        -----------
        ndarray. shape=(k, self.num_features).
        '''
        return self.centroids

    def get_data_centroid_labels(self):
        '''Get the data-to-cluster assignments

        (Should not require any changes)

        Returns:
        -----------
        ndarray of ints. shape=(self.num_samps,)
        '''
        return self.data_centroid_labels

    def dist_pt_to_pt(self, pt_1, pt_2):
        dist = np.sqrt(np.sum(np.square(pt_1-pt_2)))
        return dist

        '''Compute the Euclidean distance between data samples `pt_1` and `pt_2`

        Parameters:
        -----------
        pt_1: ndarray. shape=(num_features,)
        pt_2: ndarray. shape=(num_features,)

        Returns:
        -----------
        float. Euclidean distance between `pt_1` and `pt_2`.

        NOTE: Implement without any for loops (you will thank yourself later since you will wait
        only a small fraction of the time for your code to stop running)
        '''
        pass

    def dist_pt_to_centroids(self, pt, centroids):
        dists = np.linalg.norm(centroids - pt, axis=1)
        return dists
        '''Compute the Euclidean distance between data sample `pt` and and all the cluster centroids
        self.centroids

        Parameters:
        -----------
        pt: ndarray. shape=(num_features,)
        centroids: ndarray. shape=(C, num_features)
            C centroids, where C is an int.

        Returns:
        -----------
        ndarray. shape=(C,).
            distance between pt and each of the C centroids in `centroids`.

        NOTE: Implement without any for loops (you will thank yourself later since you will wait
        only a small fraction of the time for your code to stop running)
        '''
        pass

    def initialize(self, k):
        centroid_indices = np.random.choice(self.num_samps, k, replace=False)
        centroids = self.data[centroid_indices]
        self.k = k
        return centroids

        '''Initializes K-means by setting the initial centroids (means) to K unique randomly
        selected data samples

        Parameters:
        -----------
        k: int. Number of clusters

        Returns:
        -----------
        ndarray. shape=(k, self.num_features). Initial centroids for the k clusters.

        NOTE: Can be implemented without any for loops
        '''
        pass


    
    def cluster(self, k=2, tol=1e-2, max_iter=1000, verbose=False):
        self.k = k
        self.centroids = self.data[np.random.choice(self.data.shape[0], k, replace=False), :]
        
        prev_centroids = np.zeros_like(self.centroids)
        diff = np.abs(self.centroids - prev_centroids)

        
        iters = 0
        while (iters < max_iter) and (np.any(diff > tol)):
            dist = np.sqrt(((self.data[:, np.newaxis, :] - self.centroids) ** 2).sum(axis=2))
            self.data_centroid_labels = np.argmin(dist, axis=1)
            prev_centroids = self.centroids.copy()
            for i in range(k):
                self.centroids[i] = np.mean(self.data[self.data_centroid_labels == i], axis=0)
            
            diff = np.abs(self.centroids - prev_centroids)

            if verbose:
                print(f"Iteration {iters}: diff={diff}")
            
            iters += 1
 
        dist = np.sqrt(((self.data[:, np.newaxis, :] - self.centroids) ** 2).sum(axis=2))
        self.inertia = np.mean(dist[np.arange(self.data.shape[0]), self.data_centroid_labels] ** 2)
        
        print(f"K-means converged after {iters} iterations")
        return self.inertia, iters


        '''Performs K-means clustering on the data

        Parameters:
        -----------
        k: int. Number of clusters
        tol: float. Terminate K-means if the (absolute value of) the difference between all
        the centroid values from the previous and current time step < `tol`.
        max_iter: int. Make sure that K-means does not run more than `max_iter` iterations.
        verbose: boolean. Print out debug information if set to True.

        Returns:
        -----------
        self.inertia. float. Mean squared distance between each data sample and its cluster mean
        int. Number of iterations that K-means was run for

        TODO:
        - Initialize K-means variables
        - Do K-means as long as the max number of iterations is not met AND the absolute value of the
        difference between the previous and current centroid values is > `tol`
        - Set instance variables based on computed values.
        (All instance variables defined in constructor should be populated with meaningful values)
        - Print out total number of iterations K-means ran for
        '''
        pass


    def cluster_batch(self, k=2, n_iter=1, verbose=False):

        best_inertia = float('inf')
        best_centroids = None
        best_data_centroid_labels = None 
        
        for i in range(n_iter):
            self.cluster(k=k, tol=1e-2, max_iter=1000, verbose=verbose)
            
            if self.inertia < best_inertia:
                best_inertia = self.inertia
                best_centroids = self.centroids
                best_data_centroid_labels = self.data_centroid_labels
        
        self.centroids = best_centroids
        self.data_centroid_labels = best_data_centroid_labels
        self.inertia = best_inertia


        '''Run K-means multiple times, each time with different initial conditions.
        Keeps track of K-means instance that generates lowest inertia. Sets the following instance
        variables based on the best K-mean run:
        - self.centroids
        - self.data_centroid_labels
        - self.inertia

        Parameters:
        -----------
        k: int. Number of clusters
        n_iter: int. Number of times to run K-means with the designated `k` value.
        verbose: boolean. Print out debug information if set to True.
        '''
        pass


    def update_labels(self, centroids):
        cluster_indices = []

        for datum in self.data:
            dists = self.dist_pt_to_centroids(datum,centroids)
            min_dist = dists[0]
            min_i = len(dists)+1
            for i in range(self.centroids.shape[0]):
                if dists[i] <= min_dist:
                    min_dist = dists[i]
                    min_i = i
            cluster_indices.append(min_i)
        cluster_ind_arr = np.array(cluster_indices)
        return cluster_ind_arr



        '''Assigns each data sample to the nearest centroid

        Parameters:
        -----------
        centroids: ndarray. shape=(k, self.num_features). Current centroids for the k clusters.

        Returns:
        -----------
        ndarray of ints. shape=(self.num_samps,). Holds index of the assigned cluster of each data
            sample. These should be ints (pay attention to/cast your dtypes accordingly).

        Example: If we have 3 clusters and we compute distances to data sample i: [0.1, 0.5, 0.05]
        labels[i] is 2. The entire labels array may look something like this: [0, 2, 1, 1, 0, ...]
        '''
        pass

    def update_centroids(self, k, data_centroid_labels, prev_centroids):

        new_centroids = np.zeros((k, self.num_features))
        centroid_diff = np.zeros((k, self.num_features))
        for i in range(k):
            assigned_data = self.data[data_centroid_labels == i]
            if len(assigned_data) == 0:
                new_centroids[i] = self.data[np.random.randint(len(self.data))]
            else:
                new_centroids[i] = np.mean(assigned_data, axis=0)
            centroid_diff[i] = new_centroids[i] - prev_centroids[i]
        return new_centroids, centroid_diff

        '''Computes each of the K centroids (means) based on the data assigned to each cluster

        Parameters:
        -----------
        k: int. Number of clusters
        data_centroid_labels. ndarray of ints. shape=(self.num_samps,)
            Holds index of the assigned cluster of each data sample
        prev_centroids. ndarray. shape=(k, self.num_features)
            Holds centroids for each cluster computed on the PREVIOUS time step

        Returns:
        -----------
        new_centroids. ndarray. shape=(k, self.num_features).
            Centroids for each cluster computed on the CURRENT time step
        centroid_diff. ndarray. shape=(k, self.num_features).
            Difference between current and previous centroid values

        NOTE: Your implementation should handle the case when there are no samples assigned to a cluster —
        i.e. `data_centroid_labels` does not have a valid cluster index in it at all.
            For example, if `k`=3 and data_centroid_labels = [0, 1, 0, 0, 1], there are no samples assigned to cluster 2.
        In the case of each cluster without samples assigned to it, you should assign make its centroid a data sample
        randomly selected from the dataset.
        '''
        pass


    def compute_inertia(self):
        dists = np.zeros(len(self.data))
        for i in range(self.centroids.shape[0]):
            assigned_data = self.data[self.data_centroid_labels == i]
            centroid = self.centroids[i]
            dists[self.data_centroid_labels == i] = np.sum((assigned_data - centroid)**2, axis=1)
        inertia = np.mean(dists)
        return inertia

        '''Mean squared distance between every data sample and its assigned (nearest) centroid

        Returns:
        -----------
        float. The average squared distance between every data sample and its assigned cluster centroid.
        '''
        pass

    def plot_clusters(self):

        '''Creates a scatter plot of the data color-coded by cluster assignment.

        TODO:
        - Plot samples belonging to a cluster with the same color.
        - Plot the centroids in black with a different plot marker.
        - The default scatter plot color palette produces colors that may be difficult to discern
        (especially for those who are colorblind). Make sure you change your colors to be clearly
        differentiable.
            You should use a palette Colorbrewer2 palette. Pick one with a generous
            number of colors so that you don't run out if k is large (e.g. 10).
        '''
        pass


        labels = self.update_labels(self.centroids)
        # labels = self.predict(self.X)
        # Get the coordinates of the centroids
        centroids = self.centroids
        
        # Define a color palette using CartoColors
        colors = cartocolors.qualitative.Safe_10
        
        # Plot the samples, color-coded by cluster assignment
        for i, label in enumerate(set(labels)):
            plt.scatter(self.data[labels == label, 0], self.data[labels == label, 1],
                        cmap=colors.mpl_colormap, label=f'Cluster {label}')
        
        # Plot the centroids as black crosses
        plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=100, color='black',
                    label='Centroids')
        
        plt.legend(fontsize = 10,loc = 1)
        plt.show()


    def elbow_plot(self, max_k, n_iter=1):

        inertia = []
        ks = []
        for i in range(max_k):
            # inert, iter = self.cluster_batch(i+1,n_iter)
            self.cluster_batch(i+1,n_iter)
            inertia.append(self.inertia)
            ks.append(i+1)
        plt.plot(ks,inertia)
        plt.xlabel("K clusters")
        plt.ylabel("Inertia")

        '''Makes an elbow plot: cluster number (k) on x axis, inertia on y axis.

        Parameters:
        -----------
        max_k: int. Run k-means with k=1,2,...,max_k.
        n_iter: int. Number of iterations to run cluster function.

        TODO:
        - Run k-means with k=1,2,...,max_k, record the inertia.
        - Make the plot with appropriate x label, and y label, x tick marks.
        '''
        pass


    def replace_color_with_centroid(self):

        dist = []
        new_pix = []
        for i in range(self.data.shape[0]):
            dist = self.dist_pt_to_centroids(self.data[i],self.centroids)
            closest_cent_ind = np.argmin(dist)
            closest_cent = self.centroids[closest_cent_ind]
            new_pix.append(closest_cent)
            # self.data[i] = closest_cent
        
        new_pix_arr = np.array(new_pix)

        self.data = new_pix_arr

        '''Replace each RGB pixel in self.data (flattened image) with the closest centroid value.
        Used with image compression after K-means is run on the image vector.

        Parameters:
        -----------
        None

        Returns:
        -----------
        None
        '''
        pass