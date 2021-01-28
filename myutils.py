import numpy as np
import pandas as pd


def generate_random_colorlist(n):
    """
    Create a list of n random rbg-colors.

    Args:
    n: number of desired colors

    return:
    List with n random generated colors
    """
    rgb = []
    for i in range(0, n):
        rgb.append(np.random.rand(3,))
    return rgb


def find_categories_w_missing_values(df):
    """
    Find columns with missing values.

    Args:
    df: pandas dataframe

    return:
    List containing names of columns with missing values.
    """
    categories_w_mising_values = []
    for category in df.columns:
        if not df[category].isnull().values.any():
            print("No missing values in " + category)
        else:
            print("\033[1m" + "Missing values in " + category + "\033[0m")
            categories_w_mising_values.append(category)
    print("\033[1m" + "\nThere are", len(categories_w_mising_values),
          "categories with missing values" + "\033[0m")
    return categories_w_mising_values


def print_missing_values(df, categories):
    """
    Print categories with missing values.

    Args:
        df: pandas dataframe
        categories: list of columns \w missing values

    return:
        none
    """
    for category in categories:
        print(df[category].isnull().value_counts(), "\n")


def create_dummy_variables(df, dummy_categories=None):
    """
    Create dummy variables. This is a preprocessing step
    for linear regression.

    Args:
    df: pandas dataframe
    dummy_categories: categories where dummy variables are nedded

    return:
    dataframe with dummy variables
    """
    if (dummy_categories):
        cat_vars = dummy_categories
    else:
        # Dummy the categorical variables
        cat_vars = df.select_dtypes(include=['object']).copy().columns
    for var in cat_vars:
        # for each cat add dummy var, drop original column
        df = pd.concat([df.drop(var, axis=1), pd.get_dummies(df[var], 
                       prefix=var, prefix_sep='_', drop_first=True)], axis=1)

    return df
