'''linear_regression.py
Subclass of Analysis that performs linear regression on data
YOUR NAME HERE
CS251 Data Analysis Visualization
Spring 2023
'''
import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt
import analysis


class LinearRegression(analysis.Analysis):
    '''
    Perform and store linear regression and related analyses
    '''

    def __init__(self, data):
        '''

        Parameters:
        -----------
        data: Data object. Contains all data samples and variables in a dataset.
        '''
        super().__init__(data)

        # ind_vars: Python list of strings.
        #   1+ Independent variables (predictors) entered in the regression.
        self.ind_vars = None
        # dep_var: string. Dependent variable predicted by the regression.
        self.dep_var = None

        # A: ndarray. shape=(num_data_samps, num_ind_vars)
        #   Matrix for independent (predictor) variables in linear regression
        self.A = None

        # y: ndarray. shape=(num_data_samps, 1)
        #   Vector for dependent variable predictions from linear regression
        self.y = None

        # R2: float. R^2 statistic
        self.R2 = None

        # Mean SEE. float. Measure of quality of fit
        self.mse = None

        # slope: ndarray. shape=(num_ind_vars, 1)
        #   Regression slope(s)
        self.slope = None
        # intercept: float. Regression intercept
        self.intercept = None
        # residuals: ndarray. shape=(num_data_samps, 1)
        #   Residuals from regression fit
        self.residuals = None

        # p: int. Polynomial degree of regression model (Week 2)
        self.p = 1

    def linear_regression(self, ind_vars, dep_var):

        x = self.data.select_data(ind_vars)
        y = self.data.select_data(dep_var)

        A = np.hstack( (x, np.ones( (x.shape[0],1) )) )

        c, _, _, _ = scipy.linalg.lstsq(A,y)
        

        self.slope = c[:-1]
        self.intercept = c[-1][0]
        self.ind_vars = ind_vars
        self.dep_var = dep_var
        self.A = A[:,:-1]
        self.y = y
        self.R2 = self.r_squared(self.predict())
        self.residuals = self.compute_residuals(self.predict())
        self.mse = self.compute_mse()


        '''Performs a linear regression on the independent (predictor) variable(s) `ind_vars`
        and dependent variable `dep_var.

        Parameters:
        -----------
        ind_vars: Python list of strings. 1+ independent variables (predictors) entered in the regression.
            Variable names must match those used in the `self.data` object.
        dep_var: str. 1 dependent variable entered into the regression.
            Variable name must match one of those used in the `self.data` object.

        TODO:
        - Use your data object to select the variable columns associated with the independent and
        dependent variable strings.
        - Perform linear regression by using Scipy to solve the least squares problem y = Ac
        for the vector c of regression fit coefficients. Don't forget to add the coefficient column
        for the intercept!
        - Compute R^2 on the fit and the residuals.
        - By the end of this method, all instance variables should be set (see constructor).

        NOTE: Use other methods in this class where ever possible (do not write the same code twice!)
        '''
        pass

    def predict(self, X=None):
        if(self.p > 1):
            if(X is not None):
                mat = self.make_polynomial_matrix(X, self.p)
            else:
                mat = self.make_polynomial_matrix(self.A[:,0], self.p)
            y_pred = mat@self.slope+self.intercept
        else:
            if X is not None:
                y_pred = X@self.slope + self.intercept
            else:
                print(self.A)
                y_pred = self.A@self.slope+self.intercept
        return y_pred.reshape(-1,1)

        '''Use fitted linear regression model to predict the values of data matrix self.A.
        Generates the predictions y_pred = mA + b, where (m, b) are the model fit slope and intercept,
        A is the data matrix.

        Parameters:
        -----------
        X: ndarray. shape=(num_data_samps, num_ind_vars).
            If None, use self.A for the "x values" when making predictions.
            If not None, use X as independent var data as "x values" used in making predictions.

        Returns
        -----------
        y_pred: ndarray. shape=(num_data_samps, 1)
            Predicted y (dependent variable) values

        NOTE: You can write this method without any loops!
        '''
        pass

    def r_squared(self, y_pred):
        E = np.sum((self.y-y_pred)**2)
        S = np.sum((self.y-np.mean(self.y))**2)
        r2 = 1 - (E/S)
        return r2
        '''Computes the R^2 quality of fit statistic

        Parameters:
        -----------
        y_pred: ndarray. shape=(num_data_samps,).
            Dependent variable values predicted by the linear regression model

        Returns:
        -----------
        R2: float.
            The R^2 statistic
        '''
        pass

    def compute_residuals(self, y_pred):
        return self.y-y_pred
        '''Determines the residual values from the linear regression model

        Parameters:
        -----------
        y_pred: ndarray. shape=(num_data_samps, 1).
            Data column for model predicted dependent variable values.

        Returns
        -----------
        residuals: ndarray. shape=(num_data_samps, 1)
            Difference between the y values and the ones predicted by the regression model at the
            data samples
        '''
        pass

    def compute_mse(self):
        y_pred = self.predict()
        residuals = self.compute_residuals(y_pred)
        mse = np.mean(residuals ** 2)
        return mse

        '''Computes the mean squared error in the predicted y compared the actual y values.
        See notebook for equation.

        Returns:
        -----------
        float. Mean squared error

        Hint: Make use of self.compute_residuals
        '''
        pass

    def scatter(self, ind_var, dep_var, title):
        an = analysis.Analysis(self.data)
        x,y = an.scatter(ind_var,dep_var,title + " R^2: " + str(round(self.R2,3)))

        if(self.p == 1):
            y = (self.slope[0][0] * x) + self.intercept
            plt.plot(x,y,color="red")
        else:
            x_fit = np.linspace(np.min(x), np.max(x), 100)
            x = self.make_polynomial_matrix(x_fit,self.p)
            y = (x @ self.slope) + self.intercept
            plt.plot(x_fit,y,color="red")


        '''Creates a scatter plot with a regression line to visualize the model fit.
        Assumes linear regression has been already run.

        Parameters:
        -----------
        ind_var: string. Independent variable name
        dep_var: string. Dependent variable name
        title: string. Title for the plot

        TODO:
        - Use your scatter() in Analysis to handle the plotting of points. Note that it returns
        the (x, y) coordinates of the points.
        - Sample evenly spaced x values for the regression line between the min and max x data values
        - Use your regression slope, intercept, and x sample points to solve for the y values on the
        regression line.
        - Plot the line on top of the scatterplot.
        - Make sure that your plot has a title (with R^2 value in it)
        '''
        pass

    def pair_plot(self, data_vars, fig_sz=(12, 12), hists_on_diag=True):
        an = analysis.Analysis(self.data)

        fig, ax = an.pair_plot(data_vars,fig_sz, "Data Lin Reg Comparison")\


        for i in range(len(data_vars)):
            for j in range(len(data_vars)):
                self.linear_regression([data_vars[i]],data_vars[j])
                data_copy = self.data.get_all_data()
                x,y = data_copy[:,self.data.get_mappings()[data_vars[i]]],data_copy[:,self.data.get_mappings()[data_vars[j]]]
                y = (self.slope[0][0] * x) + self.intercept
                ax[i][j].plot(x,y,color="red")
                ax[i][j].set_title("R^2: " + str(round(self.R2,3)))

                if(i==j):
                    numVars = len(data_vars)
                    ax[i, j].remove()
                    ax[i, j] = fig.add_subplot(numVars, numVars, i*numVars+j+1)
                    if j < numVars-1:
                        ax[i, j].set_xticks([])
                    else:
                        ax[i, j].set_xlabel(data_vars[i])
                    if i > 0:
                        ax[i, j].set_yticks([])
                    else:
                        ax[i, j].set_ylabel(data_vars[i])
                    ax[i][j].hist(x)

        '''Makes a pair plot with regression lines in each panel.
        There should be a len(data_vars) x len(data_vars) grid of plots, show all variable pairs
        on x and y axes.

        Parameters:
        -----------
        data_vars: Python list of strings. Variable names in self.data to include in the pair plot.
        fig_sz: tuple. len(fig_sz)=2. Width and height of the whole pair plot figure.
            This is useful to change if your pair plot looks enormous or tiny in your notebook!
        hists_on_diag: bool. If true, draw a histogram of the variable along main diagonal of
            pairplot.

        TODO:
        - Use your pair_plot() in Analysis to take care of making the grid of scatter plots.
        Note that this method returns the figure and axes array that you will need to superimpose
        the regression lines on each subplot panel.
        - In each subpanel, plot a regression line of the ind and dep variable. Follow the approach
        that you used for self.scatter. Note that here you will need to fit a new regression for
        every ind and dep variable pair.
        - Make sure that each plot has a title (with R^2 value in it)
        '''
        pass

    def make_polynomial_matrix(self, A, p):
        X = np.zeros((A.shape[0], p))
        for i in range(1, p+1):
            X[:,i-1] = np.power(A, i).flatten()
        return X

        '''Takes an independent variable data column vector `A and transforms it into a matrix appropriate
        for a polynomial regression model of degree `p`.

        (Week 2)

        Parameters:
        -----------
        A: ndarray. shape=(num_data_samps, 1)
            Independent variable data column vector x
        p: int. Degree of polynomial regression model.

        Returns:
        -----------
        ndarray. shape=(num_data_samps, p)
            Independent variable data transformed for polynomial model.
            Example: if p=10, then the model should have terms in your regression model for
            x^1, x^2, ..., x^9, x^10.

        NOTE: There should not be a intercept term ("x^0"), the linear regression solver method
        should take care of that.
        '''
        pass

    def poly_regression(self, ind_var, dep_var, p):

        x = self.data.select_data([ind_var])
        y = self.data.select_data([dep_var])

        A = np.hstack( (self.make_polynomial_matrix(x,p), np.ones( (x.shape[0],1) )) )

        c, _, _, _ = scipy.linalg.lstsq(A,y)
        
        self.slope = c[:-1]
        self.intercept = c[-1][0]
        self.ind_vars = [ind_var]
        self.dep_var = dep_var
        self.A = A[:,:-1]
        self.y = y
        self.R2 = self.r_squared(self.predict())
        self.residuals = self.compute_residuals(self.predict())
        self.p = p

        '''Perform polynomial regression — generalizes self.linear_regression to polynomial curves
        (Week 2)
        NOTE: For single linear regression only (one independent variable only)

        Parameters:
        -----------
        ind_var: str. Independent variable entered in the single regression.
            Variable names must match those used in the `self.data` object.
        dep_var: str. Dependent variable entered into the regression.
            Variable name must match one of those used in the `self.data` object.
        p: int. Degree of polynomial regression model.
             Example: if p=10, then the model should have terms in your regression model for
             x^1, x^2, ..., x^9, x^10, and a column of homogeneous coordinates (1s).

        TODO:
        - This method should mirror the structure of self.linear_regression (compute all the same things)
        - Differences are:
            - You create a matrix based on the independent variable data matrix (self.A) with columns
            appropriate for polynomial regresssion. Do this with self.make_polynomial_matrix.
            - You set the instance variable for the polynomial regression degree (self.p)
        '''
        pass

    def get_fitted_slope(self):
        return self.slope
        '''Returns the fitted regression slope.
        (Week 2)

        Returns:
        -----------
        ndarray. shape=(num_ind_vars, 1). The fitted regression slope(s).
        '''
        return self.slope

    def get_fitted_intercept(self):
        return self.intercept
        '''Returns the fitted regression intercept.
        (Week 2)

        Returns:
        -----------
        float. The fitted regression intercept(s).
        '''
        pass

    def initialize(self, ind_vars, dep_var, slope, intercept, p):

        self.slope = slope
        self.intercept = intercept
        if(p == 1):
            self.linear_regression(ind_vars,dep_var)
        else:
            self.poly_regression(ind_vars[0],dep_var,p)


        '''Sets fields based on parameter values.
        (Week 2)

        Parameters:
        -----------
        ind_vars: Python list of strings. 1+ independent variables (predictors) entered in the regression.
            Variable names must match those used in the `self.data` object.
        dep_var: str. Dependent variable entered into the regression.
            Variable name must match one of those used in the `self.data` object.
        slope: ndarray. shape=(num_ind_vars, 1)
            Slope coefficients for the linear regression fits for each independent var
        intercept: float.
            Intercept for the linear regression fit
        p: int. Degree of polynomial regression model.

        TODO:
        - Use parameters and call methods to set all instance variables defined in constructor. 
        '''
        pass