import pandas as pd
import numpy as np

def get_stat(df1, df2):
    """function that calculates our test statistic: sum（Berkbins i-livbins i）^2 by vectorization
    Args:
        df1: pivot table of city1's grouped counts of days by temp_bins for each month. Ex: see Berkeley_grouped_counts
        df2: pivot table of city2's grouped counts of days by temp_bins for each month. Ex: see Livermore_grouped_counts
    Returns:
        A dataframe with one column of statistics, indexed by months.
    """
    diff_squared = df1.subtract(df2)**2
    stats_by_months = diff_squared.sum(0)
    return pd.DataFrame(stats_by_months)


def find_p_value(stats_df):
    """function that calculates p-value given a statistics table.
    Args:
        stats_df: a dataframe containing observed and test statistics from all permutations, indexed by months.
    Returns:
        A list of p-values, each p-value is for one unique month.
    """
    n = len(stats_df.columns)
    p_value = []
    for i in range(len(stats_df)):
        p = sum(np.array(stats_df.iloc[i, ]) >= stats_df.iloc[i, 0])/n
        p_value.append(p)
    
    return p_value



def fisher_comb(lambdas):
    """
        function that combines p-values for all months across strata using Fisher's combining function.
    Args:
        lambdas: a list of p-values, each p-value is for one unique month.
    Returns:
        A "p-value" combined from hypothesis tests on each month.
    """
    lamdas = np.array(lambdas)
    phi = -2*sum(np.log(lambdas))
    return phi

helper1 = {'a' : [1, 2, 3], 
            'b' : [2, 3, 4],
            'c' : [4, 6, 1]}
helper2 = {'a' : [2, 4, 1], 
            'b' : [9, 1, 6],
            'c' : [7, 4, 4]}
df1 = pd.DataFrame(data = helper1)
df2 = pd.DataFrame(data = helper2)

