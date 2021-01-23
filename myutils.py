import numpy as np

def generate_random_colorlist(n):
    rgb = []
    for i in range(0, n):
        rgb.append(np.random.rand(3,))
    return rgb
    
    
def find_categories_w_missing_values(df):
    categories_w_mising_values = [] 
    for category in df.columns:
        if not df[category].isnull().values.any():
            print("No missing values in " + category)
        else:
            print("\033[1m" + "Missing values in " + category + "\033[0m")
            categories_w_mising_values.append(category)
    print("\033[1m" + "\nThere are", len(categories_w_mising_values), "categories with missing values" + "\033[0m")
    return categories_w_mising_values
    
    
# count missing values
def print_missing_values(df, categories):
    """ Args:
        df: 
        categories:
        
        return:
        none
    """
    for category in categories:
        print(df[category].isnull().value_counts(),"\n")