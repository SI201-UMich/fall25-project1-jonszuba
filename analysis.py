# Jonathon Szuba
# szuba@umich.edu
# ID: 5922 7325
# Working alone with the help of AI



### beginning code

import pandas as pd

def read_penguins_data():
    df = pd.read_csv('penguins.csv')
    return df

def main():
    filename = "penguins.csv"
    data = read_penguins_data(filename)





def average_body_mass_by_species_and_sex(df):

    pass
















def correlation_bill_flipper_by_island(df):
   
    pass












def calculate_average(values):
  
    pass







def calculate_correlation(x_list, y_list):

    pass















import pandas as pd

def test_average_body_mass_by_species_and_sex():
    data = {
        'species': ['Adelie', 'Adelie', 'Chinstrap', 'Chinstrap', 'Gentoo'],
        'sex': ['Male', 'Female', 'Male', 'Female', 'Male'],
        'body_mass_g': [3700, 3450, 3800, 3700, 5000]
    }
    df = pd.DataFrame(data)
    # General case 1: multiple species and sexes
    data1 = {
        'species': ['Adelie', 'Adelie', 'Chinstrap', 'Chinstrap', 'Gentoo'],
        'sex': ['Male', 'Female', 'Male', 'Female', 'Male'],
        'body_mass_g': [3700, 3450, 3800, 3700, 5000]
    }
    df1 = pd.DataFrame(data1)
    result1 = average_body_mass_by_species_and_sex(df1)
    expected1 = {
        'Adelie': {'Male': 3700, 'Female': 3450},
        'Chinstrap': {'Male': 3800, 'Female': 3700},
        'Gentoo': {'Male': 5000}
    }
    assert result1 == expected1, f"Expected {expected1}, got {result1}"

    # General case 2: multiple entries per group
    data2 = {
        'species': ['Adelie', 'Adelie', 'Adelie', 'Chinstrap'],
        'sex': ['Male', 'Male', 'Female', 'Female'],
        'body_mass_g': [3700, 3600, 3450, 3700]
    }
    df2 = pd.DataFrame(data2)
    result2 = average_body_mass_by_species_and_sex(df2)
    expected2 = {
        'Adelie': {'Male': 3650, 'Female': 3450},
        'Chinstrap': {'Female': 3700}
    }
    assert result2 == expected2, f"Expected {expected2}, got {result2}"

    # Edge case 1: empty DataFrame
    df3 = pd.DataFrame({'species': [], 'sex': [], 'body_mass_g': []})
    result3 = average_body_mass_by_species_and_sex(df3)
    expected3 = {}
    assert result3 == expected3, f"Expected {expected3}, got {result3}"

    # Edge case 2: only one group
    data4 = {
        'species': ['Adelie', 'Adelie'],
        'sex': ['Male', 'Male'],
        'body_mass_g': [3700, 3800]
    }
    df4 = pd.DataFrame(data4)
    result4 = average_body_mass_by_species_and_sex(df4)
    expected4 = {'Adelie': {'Male': 3750}}
    assert result4 == expected4, f"Expected {expected4}, got {result4}"

def test_correlation_bill_flipper_by_island():
    data = {
        'island': ['Torgersen', 'Torgersen', 'Biscoe', 'Biscoe'],
        'bill_length_mm': [39.1, 40.3, 46.5, 45.4],
        'flipper_length_mm': [181, 186, 211, 217]
    }
    df = pd.DataFrame(data)
    # General case 1: two islands, two points each
    data1 = {
        'island': ['Torgersen', 'Torgersen', 'Biscoe', 'Biscoe'],
        'bill_length_mm': [39.1, 40.3, 46.5, 45.4],
        'flipper_length_mm': [181, 186, 211, 217]
    }
    df1 = pd.DataFrame(data1)
    result1 = correlation_bill_flipper_by_island(df1)
    expected1 = {'Torgersen': 1.0, 'Biscoe': 1.0}
    assert all(abs(result1[k] - expected1[k]) < 1e-6 for k in expected1), f"Expected {expected1}, got {result1}"

    # General case 2: three points, positive correlation
    data2 = {
        'island': ['Dream', 'Dream', 'Dream'],
        'bill_length_mm': [40, 42, 44],
        'flipper_length_mm': [190, 200, 210]
    }
    df2 = pd.DataFrame(data2)
    result2 = correlation_bill_flipper_by_island(df2)
    assert 'Dream' in result2 and abs(result2['Dream'] - 1.0) < 1e-6

    # Edge case 1: only one data point for an island
    data3 = {
        'island': ['Biscoe'],
        'bill_length_mm': [46.5],
        'flipper_length_mm': [211]
    }
    df3 = pd.DataFrame(data3)
    result3 = correlation_bill_flipper_by_island(df3)
    # Correlation undefined for one point, expect None or similar
    assert result3['Biscoe'] is None

    # Edge case 2: empty DataFrame
    df4 = pd.DataFrame({'island': [], 'bill_length_mm': [], 'flipper_length_mm': []})
    result4 = correlation_bill_flipper_by_island(df4)
    assert result4 == {}



if __name__ == "__main__":
    test_average_body_mass_by_species_and_sex()
    test_correlation_bill_flipper_by_island()
    test_calculate_average()
    test_calculate_correlation()
    print("All tests passed.")


