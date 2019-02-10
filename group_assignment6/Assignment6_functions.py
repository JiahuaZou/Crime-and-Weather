from cryptorandom.cryptorandom import SHA256
import random
import numpy as np
import pandas as pd


# get design matrix for temperature bins
def get_temp_features(TMAX_data):
    """
    Args:
        TMAX_data: dataframe that contains bins of TMAX of each YearMonth
    Return:
        a matrix with columns being bin categories of TMAX and rows being YearMonth
    """
    # create list of dataframes with each dataframe containing counts info for a bin category of all YearMonth
    bins_data = [TMAX_data[TMAX_data['temp_bins']==temp] for temp in TMAX_data['temp_bins'].unique()]
    # create an 0 matrix that is 8*359 to store the result
    values = np.zeros((8,359))

    # loop through each bin categories and get the sum of this month and previous month counts
    for i in range(8):
        a = list(bins_data[i].iloc[0:359,2])
        b = list(bins_data[i].iloc[1:,2])
        values[i] = [sum(x) for x in zip (a,b)]

    # transpose and rename the matrix
    temp_bins = pd.DataFrame(values.transpose())
    temp_bins = temp_bins.rename(columns={0:"30-39F", 1:"40-49F", 2:"50-59F",3:"60-69F",4:"70-79F",5:"80-89F",6:"90-99F",7:">100F"})
    return temp_bins

    # get design matrix for prcp bins
def get_prcp_features_whole(PRCP_data):
    """
    Args:
        PRCP_data: dataframe that contains bins of PRCP of each YearMonth of the whole Alameda
    Return:
        a matrix with columns being bin categories of PRCP and rows being YearMonth
    """
    # create list of 5 dataframes with each dataframe containing counts info for a bin category of all YearMonth
    prcp5= [PRCP_data[PRCP_data['prcp_bins'] == prcp] for prcp in PRCP_data['prcp_bins'].unique()]

    # loop through each bin categories and get the sum of this month and previous month counts
    values = np.zeros((5,359))
    for i in range(5):
        list1 = list(prcp5[i].iloc[0:359,2])
        list2 = list(prcp5[i].iloc[1:,2])
        values[i]=[sum(x) for x in zip(list1,list2)]

    # transpose and rename the matrix
    prcp_bins = pd.DataFrame(values.transpose())
    prcp_bins = prcp_bins.rename(columns={0:"0mm", 1:"1-4mm", 2:"5-14mm",3:"15-29mm",4:">30mm"})
    return prcp_bins


def get_prcp_features(PRCP_data):
    """
    Args:
        PRCP_data: dataframe that contains bins of PRCP of each YearMonth of part of the Alameda
    Return:
        a matrix with columns being bin categories of PRCP and rows being YearMonth
    """
    # create list of 3 dataframes with each dataframe containing counts info for a bin category of all YearMonth
    prcp5= [PRCP_data[PRCP_data['prcp_bins'] == prcp] for prcp in PRCP_data['prcp_bins'].unique()]

    # loop through each bin categories and get the sum of this month and previous month counts
    values = np.zeros((3,359))
    for i in range(3):
        list1 = list(prcp5[i].iloc[0:359,2])
        list2 = list(prcp5[i].iloc[1:,2])
        values[i]=[sum(x) for x in zip(list1,list2)]

    # transpose and rename the matrix
    prcp_bins = pd.DataFrame(values.transpose())
    prcp_bins = prcp_bins.rename(columns={0:"0mm", 1:"1-4mm", 2:"5-14mm"})
    return prcp_bins



    # get design matrix for dummy variables
def get_dummy_features(TMAX_data):
    """
    Args:
        TMAX_data: dataframe that contains bins of TMAX of each YearMonth
    Return:
        dataframe with dummfied Year and Month
    """
    theta = pd.get_dummies(TMAX_data['YearMonth'].unique()//100)
    phi = [np.identity(12) for i in range(30)]
    phi = pd.DataFrame(np.concatenate(phi))
    phi = phi.rename(columns={0:"Jan", 1:"Feb", 2:"Mar",3:"Apr",4:"May",5:"Jun",6:"Jul",7:"Aug",8:"Sep",9:"Oct",10:"Nov",11:"Dec"})
    # drop the first row of phi and theta to match the dimension of temp_bins and prcp_bins
    theta = theta.iloc[1:,:].reset_index(drop=True)
    phi = phi.iloc[1:,:].reset_index(drop=True)
    return theta,phi


def get_permute(k = 360, r = SHA256(seed=123456)):
    """
        Args:
        k: number of the Bernoulli trials.
        r: random seed.
        Return:
        a list of boolean that indicate whether the nth YearMonth need to be permute or not
        """
    # generate an integer with k random bits.
    p = r.getrandbits(k)
    # split into a list of binary string
    binary = list(bin(p))[2:]
   
    # change into list of integer first in order to change it into boolean
    integer_list = list(map(int, binary))
    # change into list of boolean
    boolean = list(map(bool,integer_list))
    # length check, if it is smaller than k, there are 0s in the beginning so we manually add 0s
    while len(boolean) < k:
        boolean = [False] + boolean   
    return boolean


def rms(y,y_hat):
    """
    Args:
        y: the response vector
        y_hat: the predicted response vector
    Return: 
        a number that shows the rms error
    """
    return (np.mean((y-y_hat)**2))**(1/2)
