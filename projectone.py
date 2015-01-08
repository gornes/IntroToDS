__author__ = 'itoledo'

import pandas as pd
import numpy as np

from ggplot import *


def normalize_features(array):
    """
    Normalize the features in the data set.
    """
    array_normalized = (array-array.mean())/array.std()
    mu = array.mean()
    sigma = array.std()

    return array_normalized, mu, sigma


def compute_cost(features, values, theta):
    """
    Compute the cost function given a set of features / values,
    and the values for our thetas.

    This can be the same code as the compute_cost function in the lesson #3
    exercises, but feel free to implement your own.
    """

    m = len(values)
    # noinspection PyUnresolvedReferences
    sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost


def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of
    features.

    This can be the same gradient descent code as in the lesson #3 exercises,
    but feel free to implement your own.
    """

    m = len(values)
    cost_history = []
    for i in range(num_iterations):
        theta_n = theta + (alpha/m) * np.dot(
            (values - np.dot(features, theta)), features)
        cost_history.append(compute_cost(features, values, theta_n))
        theta = theta_n
    return theta, pd.Series(cost_history)


def predictions(dataframe, features_list=['Hour', 'weekday', 'rain']):
    """
    The NYC turnstile data is stored in a pandas dataframe called
    weather_turnstile.
    Using the information stored in the dataframe, let's predict the
    ridership of
    the NYC subway using linear regression with gradient descent.

    You can download the complete turnstile weather dataframe here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk
    /turnstile_data_master_with_weather.csv

    Your prediction should have a R^2 value of 0.20 or better.
    You need to experiment using various input features contained in the
    dataframe.
    We recommend that you don't use the EXITSn_hourly feature as an input to
    the
    linear model because we cannot use it as a predictor: we cannot use exits
    counts as a way to predict entry counts.

    Note: Due to the memory and CPU limitation of our Amazon EC2 instance,
    we will
    give you a random subet (~15%) of the data contained in
    turnstile_data_master_with_weather.csv. You are encouraged to experiment
    with
    this computer on your own computer, locally.


    If you'd like to view a plot of your cost history, uncomment the call to
    plot_cost_history below. The slowdown from plotting is significant,
    so if you
    are timing out, the first thing to do is to comment out the plot command
    again.

    If you receive a "server has encountered an error" message, that means
    you are
    hitting the 30-second limit that's placed on running your program. Try
    using a
    smaller number for num_iterations if that's the case.

    If you are using your own algorithm/models, see if you can optimize your
    code so
    that it runs faster.
    """
    # Select Features (try different features!)
    features = dataframe.reset_index(drop=True)[features_list]

    # Add UNIT to features using dummy variables
    dummy_units = pd.get_dummies(dataframe.reset_index(drop=True)['UNIT'], prefix='unit')
    features = features.join(dummy_units)
    # d_u2 = pd.get_dummies(dataframe['Hour'], prefix='hour')
    # features = features.join(d_u2)
    # d_u3 = pd.get_dummies(dataframe['weekday'], prefix='day')
    # features = features.join(d_u3)

    # Values
    values = dataframe.reset_index(drop=True)[['ENTRIESn_hourly']]
    m = len(values)

    features, mu, sigma = normalize_features(features)
    features['ones'] = np.ones(m)  # Add a column of 1s (y intercept)

    # Convert features and values to numpy arrays
    features_array = np.array(features)
    values_array = np.array(values).flatten()

    # Set values for alpha, number of iterations.
    alpha = 0.1  # please feel free to change this value
    num_iterations = 75  # please feel free to change this value

    # Initialize theta, perform gradient descent
    theta_gradient_descent = np.zeros(len(features.columns))
    theta_gradient_descent, cost_history = gradient_descent(
        features_array, values_array, theta_gradient_descent, alpha,
        num_iterations)

    # -------------------------------------------------
    # Uncomment the next line to see your cost history
    # -------------------------------------------------
    plot = plot_cost_history(alpha, cost_history)
    #
    # Please note, there is a possibility that plotting
    # this in addition to your calculation will exceed
    # the 30 second limit on the compute servers.

    prediction = np.dot(features_array, theta_gradient_descent)
    return prediction, plot


def plot_cost_history(alpha, cost_history):
    """This function is for viewing the plot of your cost history.
    You can run it by uncomment this

        plot_cost_history(alpha, cost_history)

    call in predictions.

    If you want to run this locally, you should print the return value
    from this function.
    """
    cost_df = pd.DataFrame({
        'Cost_History': cost_history,
        'Iteration': range(len(cost_history))
    })
    return ggplot(cost_df, aes('Iteration', 'Cost_History')) + \
        geom_point() + ggtitle('Cost History for alpha = %.3f' % alpha)


def compute_r_squared(data, prediction):
    """
    In exercise 5, we calculated the R^2 value for you. But why don't you try
    and
    and calculate the R^2 value yourself.

    Given a list of original data points, and also a list of predicted data
    points,
    write a function that will compute and return the coefficient of
    determination (R^2)
    for this data.  numpy.mean() and numpy.sum() might both be useful here, but
    not necessary.

    Documentation about numpy.mean() and numpy.sum() below:
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html
    """

    r_squared = 1 - np.sum((data - prediction)**2) / np.sum(
        (data - data.mean())**2)

    return r_squared


def predictions_system(dataframe, features_list=['hour', 'day_week', 'rain_day'],
                       dummies=None, intercept=True):
    """
    The NYC turnstile data is stored in a pandas dataframe called
    weather_turnstile.
    Using the information stored in the dataframe, let's predict the
    ridership of
    the NYC subway using linear regression with gradient descent.

    You can download the complete turnstile weather dataframe here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk
    /turnstile_data_master_with_weather.csv

    Your prediction should have a R^2 value of 0.20 or better.
    You need to experiment using various input features contained in the
    dataframe.
    We recommend that you don't use the EXITSn_hourly feature as an input to
    the
    linear model because we cannot use it as a predictor: we cannot use exits
    counts as a way to predict entry counts.

    Note: Due to the memory and CPU limitation of our Amazon EC2 instance,
    we will
    give you a random subet (~15%) of the data contained in
    turnstile_data_master_with_weather.csv. You are encouraged to experiment
    with
    this computer on your own computer, locally.


    If you'd like to view a plot of your cost history, uncomment the call to
    plot_cost_history below. The slowdown from plotting is significant,
    so if you
    are timing out, the first thing to do is to comment out the plot command
    again.

    If you receive a "server has encountered an error" message, that means
    you are
    hitting the 30-second limit that's placed on running your program. Try
    using a
    smaller number for num_iterations if that's the case.

    If you are using your own algorithm/models, see if you can optimize your
    code so
    that it runs faster.
    """
    # Select Features (try different features!)
    features = dataframe.reset_index(drop=True)[features_list]

    if dummies is not None:
        for d in dummies:
            dummy_units = pd.get_dummies(dataframe.reset_index(drop=True)[d], prefix=d)
            features = features.join(dummy_units)
    # Add UNIT to features using dummy variables
    #dummy_units = pd.get_dummies(dataframe.reset_index(drop=True)['UNIT'], prefix='unit')
    #features = features.join(dummy_units)
    # d_u2 = pd.get_dummies(dataframe['Hour'], prefix='hour')
    # features = features.join(d_u2)
    # d_u3 = pd.get_dummies(dataframe['weekday'], prefix='day')
    # features = features.join(d_u3)

    # Values
    values = dataframe.reset_index(drop=True)[['ENTRIESn_hourly']]
    m = len(values)

    features, mu, sigma = normalize_features(features)
    if intercept:
        features['ones'] = np.ones(m)  # Add a column of 1s (y intercept)

    # Convert features and values to numpy arrays
    features_array = np.array(features)
    values_array = np.array(values).flatten()

    # Set values for alpha, number of iterations.
    alpha = 0.1  # please feel free to change this value
    num_iterations = 75  # please feel free to change this value

    # Initialize theta, perform gradient descent
    theta_gradient_descent = np.zeros(len(features.columns))
    theta_gradient_descent, cost_history = gradient_descent(
        features_array, values_array, theta_gradient_descent, alpha,
        num_iterations)

    # -------------------------------------------------
    # Uncomment the next line to see your cost history
    # -------------------------------------------------
    plot = plot_cost_history(alpha, cost_history)
    #
    # Please note, there is a possibility that plotting
    # this in addition to your calculation will exceed
    # the 30 second limit on the compute servers.

    prediction = np.dot(features_array, theta_gradient_descent)
    return prediction, plot
