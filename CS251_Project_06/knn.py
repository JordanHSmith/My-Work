'''knn.py
K-Nearest Neighbors algorithm for classification
YOUR NAME HERE
CS 251 Data Analysis Visualization, Spring 2021
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from palettable import cartocolors


class KNN:
    '''K-Nearest Neighbors supervised learning algorithm'''
    def __init__(self, num_classes):
        '''KNN constructor

        TODO:
        - Add instance variable for `num_classes`
        '''
        # exemplars: ndarray. shape=(num_train_samps, num_features).
        #   Memorized training examples
        self.exemplars = None
        # classes: ndarray. shape=(num_train_samps,).
        #   Classes of memorized training examples
        self.classes = None

        self.num_classes = num_classes

    def train(self, data, y):   
        self.exemplars = data
        self.classes = y  

        '''Train the KNN classifier on the data `data`, where training samples have corresponding
        class labels in `y`.

        Parameters:
        -----------
        data: ndarray. shape=(num_train_samps, num_features). Data to learn / train on.
        y: ndarray. shape=(num_train_samps,). Corresponding class of each data sample.

        TODO:
        - Set the `exemplars` and `classes` instance variables such that the classifier memorizes
        the training data.
        '''
        pass

    def predict(self, data, k):

        num_test_samps = data.shape[0]  # Number of test samples
        num_train_samps = self.exemplars.shape[0]  # Number of training samples

        dists = np.empty((num_test_samps, num_train_samps))
        
        # Compute distances between test samples and training exemplars
        for i in range(num_test_samps):
            dists[i] = np.sqrt(np.sum(np.square(self.exemplars - data[i]), axis=1))

        # Find indices of k closest training exemplars for each test sample
        closest_indices = np.argpartition(dists, k)[:, :k]

        # Get the corresponding classes for the closest training exemplars
        closest_classes = self.classes[closest_indices]

        # Count the occurrences of each class in the k closest training exemplars for each test sample
        predicted_classes = np.array([np.bincount(classes.astype(int)).argmax() for classes in closest_classes])

        return predicted_classes

        '''Use the trained KNN classifier to predict the class label of each test sample in `data`.
        Determine class by voting: find the closest `k` training exemplars (training samples) and
        the class is the majority vote of the classes of these training exemplars.

        Parameters:
        -----------
        data: ndarray. shape=(num_test_samps, num_features). Data to predict the class of
            Need not be the data used to train the network.
        k: int. Determines the neighborhood size of training points around each test sample used to
            make class predictions. In other words, how many training samples vote to determine the
            predicted class of a nearby test sample.

        Returns:
        -----------
        ndarray of nonnegative ints. shape=(num_test_samps,). Predicted class of each test data
        sample.

        TODO:
        - Compute the distance from each test sample to all the training exemplars.
        - Among the closest `k` training exemplars to each test sample, count up how many belong
        to which class.
        - The predicted class of the test sample is the majority vote.
        '''
        pass

    def accuracy(self, y, y_pred):

        accuracy = (y == y_pred).mean()  # Compute accuracy as proportion of correct predictions
        return accuracy

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

    def plot_predictions(self, k, n_sample_pts):

        # Pick a discrete/qualitative color scheme
        color_palette = ListedColormap(['#e41a1c', '#377eb8', '#4daf4a', '#984ea3'])  # Example color palette

        # Generate sample points
        samp_vec = np.linspace(-40, 40, n_sample_pts)
        x, y = np.meshgrid(samp_vec, samp_vec)
        data = np.column_stack((x.ravel(), y.ravel()))

        # Make predictions for the sample points
        y_pred = self.predict(data, k)

        # Reshape predicted classes into a square grid format
        y_pred = y_pred.reshape(n_sample_pts, n_sample_pts)

        # Create plot
        plt.pcolormesh(x, y, y_pred, cmap=color_palette)
        plt.colorbar()
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('KNN Predictions')
        plt.show()



        '''Paints the data space in colors corresponding to which class the classifier would
         hypothetically assign to data samples appearing in each region.

        Parameters:
        -----------
        k: int. Determines the neighborhood size of training points around each test sample used to
            make class predictions. In other words, how many training samples vote to determine the
            predicted class of a nearby test sample.
        n_sample_pts: int.
            How many points to divide up the input data space into along the x and y axes to plug
            into KNN at which we are determining the predicted class. Think of this as regularly
            spaced 2D "fake data" that we generate and plug into KNN and get predictions at.

        TODO:
        - Pick a discrete/qualitative color scheme. We suggest, like in the clustering project, to
        use a ColorBrewer color palette. List of possible ones here:
        https://github.com/CartoDB/CartoColor/wiki/CARTOColor-Scheme-Names
            - An example: cartocolors.qualitative.Safe_4.mpl_colors
            - The 4 stands for the number of colors in the palette. For simplicity, you can assume
            that we're hard coding this at 4 for 4 classes.
        - Each ColorBrewer palette is a Python list. Wrap this in a `ListedColormap` object so that
        matplotlib can parse it (already imported above).
        - Make an ndarray of length `n_sample_pts` of regularly spaced points between -40 and +40.
        - Call `np.meshgrid` on your sampling vector to get the x and y coordinates of your 2D
        "fake data" sample points in the square region from [-40, 40] to [40, 40].
            - Example: x, y = np.meshgrid(samp_vec, samp_vec)
        - Combine your `x` and `y` sample coordinates into a single ndarray and reshape it so that
        you can plug it in as your `data` in self.predict.
            - Shape of `x` should be (n_sample_pts, n_sample_pts). You want to make your input to
            self.predict of shape=(n_sample_pts*n_sample_pts, 2).
        - Reshape the predicted classes (`y_pred`) in a square grid format for plotting in 2D.
        shape=(n_sample_pts, n_sample_pts).
        - Use the `plt.pcolormesh` function to create your plot. Use the `cmap` optional parameter
        to specify your discrete ColorBrewer color palette.
        - Add a colorbar to your plot
        '''
        pass


    def confusion_matrix(self, y, y_pred):

        confusion_mat = np.zeros((self.num_classes, self.num_classes), dtype=int)

        # Iterate over each sample and update the confusion matrix accordingly
        for i in range(len(y)):
            true_class = y[i]
            pred_class = y_pred[i]
            confusion_mat[true_class][pred_class] += 1

        return confusion_mat


    def predict_L1(self, data, k):
        num_test_samps = data.shape[0]  # Number of test samples
        num_train_samps = self.exemplars.shape[0]  # Number of training samples

        dists = np.empty((num_test_samps, num_train_samps))

        # Compute distances between test samples and training exemplars using L1 distance metric
        for i in range(num_test_samps):
            dists[i] = np.sum(np.abs(self.exemplars - data[i]), axis=1)

        # Find indices of k closest training exemplars for each test sample
        closest_indices = np.argpartition(dists, k)[:, :k]

        # Get the corresponding classes for the closest training exemplars
        closest_classes = self.classes[closest_indices]

        # Count the occurrences of each class in the k closest training exemplars for each test sample
        predicted_classes = np.array([np.bincount(classes.astype(int)).argmax() for classes in closest_classes])

        return predicted_classes