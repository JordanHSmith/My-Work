'''naive_bayes_multinomial.py
Naive Bayes classifier with Multinomial likelihood for discrete features
YOUR NAME HERE
CS 251/2: Data Analysis Visualization
Spring 2023
'''
import numpy as np


class NaiveBayes:
    '''Naive Bayes classifier using Multinomial likeilihoods (discrete data belonging to any
     number of classes)'''
    def __init__(self, num_classes):

        self.num_classes = num_classes
        self.class_priors = None
        self.class_likelihoods = None
        '''Naive Bayes constructor

        TODO:
        - Add instance variable for `num_classes`.
        - Add placeholder instance variables the class prior probabilities and class likelihoods (assigned to None).
        You may store the priors and likelihoods themselves or the logs of them. Be sure to use variable names that make
        clear your choice of which version you are maintaining.
        '''
        pass

        # class_priors: ndarray. shape=(num_classes,).
        #   Probability that a training example belongs to each of the classes
        #   For spam filter: prob training example is spam or ham

        # class_likelihoods: ndarray. shape=(num_classes, num_features).
        #   Probability that each word appears within class c

    def get_priors(self):
        return self.class_priors
        '''Returns the class priors (or log of class priors if storing that)'''
        pass

    def get_likelihoods(self):
        return self.class_likelihoods
        '''Returns the class likelihoods (or log of class likelihoods if storing that)'''
        pass

    def train(self, data, y):
        '''
        Train the Naive Bayes classifier so that it records the "statistics" of the training set:
        class priors (i.e. how likely an email is in the training set to be spam or ham?) and the
        class likelihoods (the probability of a word appearing in each class — spam or ham)

        Parameters:
        -----------
        data: ndarray. shape=(num_samps, num_features). Data to learn / train on.
        y: ndarray. shape=(num_samps,). Corresponding class of each data sample.
        '''
        

        num_samples, num_features = data.shape
        classes = np.unique(y)
        # Compute class priors
        class_counts = np.bincount(y)
        self.class_priors = class_counts / num_samples

        # Compute class likelihoods
        self.class_likelihoods = np.zeros((self.num_classes, num_features))
        for i, c in enumerate(classes):
            class_data = data[y == c]
            class_word_counts = np.sum(class_data, axis=0)
            total_word_counts = np.sum(class_word_counts)
            self.class_likelihoods[i] = (class_word_counts + 1) / (total_word_counts + num_features)

        # Convert likelihoods to probabilities by adding small epsilon to avoid division by zero
        epsilon = 1e-9
        self.class_likelihoods = np.clip(self.class_likelihoods, epsilon, 1 - epsilon)


        '''Train the Naive Bayes classifier so that it records the "statistics" of the training set:
        class priors (i.e. how likely an email is in the training set to be spam or ham?) and the
        class likelihoods (the probability of a word appearing in each class — spam or ham)

        Parameters:
        -----------
        data: ndarray. shape=(num_samps, num_features). Data to learn / train on.
        y: ndarray. shape=(num_samps,). Corresponding class of each data sample.

        TODO:
        - Compute the class priors and class likelihoods (i.e. your instance variables) that are needed for
        Bayes Rule. See equations in notebook.
        '''
        pass

    def predict(self, data):
        '''Combine the class likelihoods and priors to compute the posterior distribution. The
        predicted class for a test sample from `data` is the class that yields the highest posterior
        probability.

        Parameters:
        -----------
        data: ndarray. shape=(num_test_samps, num_features). Data to predict the class of
            Need not be the data used to train the network

        Returns:
        -----------
        ndarray of nonnegative ints. shape=(num_samps,). Predicted class of each test data sample.

        TODO:
        - For the test samples, we want to compute the log of the posterior by evaluating
        the the log of the right-hand side of Bayes Rule without the denominator (see notebook for
        equation). This can be done without loops.
        - Predict the class of each test sample according to the class that produces the largest
        log(posterior) probability (hint: this can also be done without loops).

        NOTE: Remember that you are computing the LOG of the posterior (see notebook for equation).
        NOTE: The argmax function could be useful here.
        '''



        log_posteriors = np.zeros((data.shape[0], self.num_classes))
        for i in range(self.num_classes):
            log_posteriors[:, i] = np.sum(np.log(self.class_likelihoods[i]) * data, axis=1) + np.log(self.class_priors[i])
        
        # Make predictions based on the class with the highest log posterior
        predictions = np.argmax(log_posteriors, axis=1)
        
        return predictions


        # # Compute log posteriors for each class
        # log_likelihoods = np.zeros((data.shape[0], self.num_classes))


        # class_data = data[y == c]
        # class_word_counts = np.sum(class_data, axis=0)

        # for i, c in enumerate(self.num_classes):
        #     log_likelihoods[:, i] = np.sum(data * np.log(self.feature_counts[i]), axis=1)
            
        # log_posteriors = log_likelihoods + np.log(self.priors)
        
        # # Make predictions based on the class with the highest log posterior
        # predictions = np.argmax(log_posteriors, axis=1)
        
        # return predictions


        # Compute log of the posterior without the denominator
        # log_posterior = np.zeros((data.shape[0], self.num_classes))
        # for i in range(self.num_classes):
        #     log_posterior[:, i] = np.sum(np.log(self.class_likelihoods[i]) * data, axis=1) + np.log(self.class_priors[i])
        
        # # Predict class with highest log posterior probability
        # predicted_classes = np.argmax(log_posterior, axis=1)
        
        # return predicted_classes



    
        # # Compute the log of the posterior without the denominator (log likelihood + log prior)
        # log_likelihoods = np.log(self.class_likelihoods)
        # log_priors = np.log(self.class_priors)
        # log_posteriors = np.dot(data, log_likelihoods.T) + log_priors

        # # Predict the class with the highest log posterior probability
        # predicted_classes = np.argmax(log_posteriors, axis=1)

        # return predicted_classes

        

    def accuracy(self, y, y_pred):
        return np.mean(y==y_pred)


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

    def confusion_matrix(self, y, y_pred):

        confusion_mat = np.zeros((self.num_classes, self.num_classes), dtype=int)

        # Iterate over each sample and update the confusion matrix accordingly
        for i in range(len(y)):
            true_class = y[i]
            pred_class = y_pred[i]
            confusion_mat[true_class][pred_class] += 1

        return confusion_mat

        # num_classes = self.num_classes  # Assumes class labels start from 0 and are consecutive integers
        # confusion_matrix = np.zeros((num_classes, num_classes), dtype=np.int32)

        # for i in range(len(y)):
        #     confusion_matrix[y[i], y_pred[i]] += 1

        # return confusion_matrix

        '''Create a confusion matrix based on the ground truth class labels (`y`) and those predicted
        by the classifier (`y_pred`).

        Recall: the rows represent the "actual" ground truth labels, the columns represent the
        predicted labels.

        Parameters:
        -----------
        y: ndarray. shape=(num_data_samps,)
            Ground-truth, known class labels for each data sample
        y_pred: ndarray. shape=(num_data_samps,)
            Predicted class labels by the model for each data sample

        Returns:
        -----------
        ndarray. shape=(num_classes, num_classes).
            Confusion matrix
        '''
        pass