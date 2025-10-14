# Jonathon Szuba
# szuba@umich.edu
# ID: 5922 7325
# Working alone with the help of AI



### beginning code

import pandas as pd

def read_penguins_data():
    df = pd.read_csv('penguins.csv')
    return df

    

def df_clean(df):
    cols_needed = ['species', 'sex', 'body_mass_g', 'island', 'bill_length_mm', 'flipper_length_mm']
    df_cleaned = df.dropna(subset=cols_needed)
    for col in ['body_mass_g', 'bill_length_mm', 'flipper_length_mm']:
        df_cleaned.loc[:, col] = pd.to_numeric(df_cleaned[col], errors='coerce')
    df_cleaned = df_cleaned.dropna(subset=['body_mass_g', 'bill_length_mm', 'flipper_length_mm'])
    return df_cleaned



def average_body_mass_by_species_and_sex(df):
    result = df.groupby(['species', 'sex'])['body_mass_g'].mean().reset_index()
    result = result.rename(columns={'body_mass_g': 'average_body_mass_g'})
    # Ensure correct dtypes if result is empty
    if result.empty:
        result = pd.DataFrame({
            'species': pd.Series(dtype='object'),
            'sex': pd.Series(dtype='object'),
            'average_body_mass_g': pd.Series(dtype='float64')
        })
    return result
    





def correlation_bill_flipper_by_island(df):
    grouped_correlation = df.groupby('island')
    result = {}
    for island, group in grouped_correlation:
        if len(group) < 2:
            correlation = None
        else:
            correlation = group['bill_length_mm'].corr(group['flipper_length_mm'])
        result[island] = correlation
    return result

    






# generate report
def generate_report(correlation_by_island, avg_body_mass, filename="report.txt"):
    with open(filename, "w") as f:
        f.write("Correlation between Bill Length and Flipper Length by Island:\n")
        for island, corr in correlation_by_island.items():
            corr_str = f"{corr:.3f}" if corr is not None else "N/A"
            f.write(f"  {island}: {corr_str}\n")
        f.write("\nAverage Body Mass by Species and Sex:\n")
        f.write(avg_body_mass.to_string(index=False))
        f.write("\n")


### call main
def main():
    df = read_penguins_data()
    df_cleaned = df_clean(df)
    avg_body_mass = average_body_mass_by_species_and_sex(df_cleaned)
    correlation = correlation_bill_flipper_by_island(df_cleaned)
    generate_report(correlation, avg_body_mass)
    print("Report generated as report.txt")

if __name__ == "__main__":
    main()









# Test cases for average_body_mass_by_species_and_sex
def test_average_body_mass_by_species_and_sex():
    # General case 1: multiple species and sexes
    data1 = {
        'species': ['Adelie', 'Adelie', 'Chinstrap', 'Chinstrap', 'Gentoo'],
        'sex': ['Male', 'Female', 'Male', 'Female', 'Male'],
        'body_mass_g': [3700, 3450, 3800, 3700, 5000]
    }
    df1 = pd.DataFrame(data1)

    result1 = average_body_mass_by_species_and_sex(df1)
    expected1 = pd.DataFrame({
        'species': ['Adelie', 'Adelie', 'Chinstrap', 'Chinstrap', 'Gentoo'],
        'sex': ['Male', 'Female', 'Male', 'Female', 'Male'],
        'average_body_mass_g': [3700.0, 3450.0, 3800.0, 3700.0, 5000.0]
    })
    pd.testing.assert_frame_equal(
        result1.sort_values(['species', 'sex']).reset_index(drop=True),
        expected1.sort_values(['species', 'sex']).reset_index(drop=True)
    )

    # General case 2: multiple entries per group
    data2 = {
        'species': ['Adelie', 'Adelie', 'Adelie', 'Chinstrap'],
        'sex': ['Male', 'Male', 'Female', 'Female'],
        'body_mass_g': [3700, 3600, 3450, 3700]
    }
    df2 = pd.DataFrame(data2)

    result2 = average_body_mass_by_species_and_sex(df2)
    expected2 = pd.DataFrame({
        'species': ['Adelie', 'Adelie', 'Chinstrap'],
        'sex': ['Male', 'Female', 'Female'],
        'average_body_mass_g': [3650.0, 3450.0, 3700.0]
    })
    pd.testing.assert_frame_equal(
        result2.sort_values(['species', 'sex']).reset_index(drop=True),
        expected2.sort_values(['species', 'sex']).reset_index(drop=True)
    )

    # Edge case 1: empty DataFrame

    df3 = pd.DataFrame({'species': [], 'sex': [], 'body_mass_g': []})
    result3 = average_body_mass_by_species_and_sex(df3)
    expected3 = pd.DataFrame({
        'species': pd.Series(dtype='object'),
        'sex': pd.Series(dtype='object'),
        'average_body_mass_g': pd.Series(dtype='float64')
    })
    pd.testing.assert_frame_equal(result3, expected3)

    # Edge case 2: only one group

    data4 = {
        'species': ['Adelie', 'Adelie'],
        'sex': ['Male', 'Male'],
        'body_mass_g': [3700, 3800]
    }
    df4 = pd.DataFrame(data4)
    result4 = average_body_mass_by_species_and_sex(df4)
    expected4 = pd.DataFrame({
        'species': ['Adelie'],
        'sex': ['Male'],
        'average_body_mass_g': [3750.0]
    })
    pd.testing.assert_frame_equal(result4.reset_index(drop=True), expected4)

# Test cases for correlation_bill_flipper_by_island
def test_correlation_bill_flipper_by_island():
    # General case 1: two islands, two points each
    data1 = {
        'island': ['Torgersen', 'Torgersen', 'Biscoe', 'Biscoe'],
        'bill_length_mm': [39.1, 40.3, 46.5, 45.4],
        'flipper_length_mm': [181, 186, 211, 217]
    }
    df1 = pd.DataFrame(data1)
    result1 = correlation_bill_flipper_by_island(df1)
    expected1 = {'Torgersen': 1.0, 'Biscoe': -1.0}
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
    assert result3['Biscoe'] is None

    # Edge case 2: empty DataFrame
    df4 = pd.DataFrame({'island': [], 'bill_length_mm': [], 'flipper_length_mm': []})
    result4 = correlation_bill_flipper_by_island(df4)
    assert result4 == {}






if __name__ == "__main__":
    test_average_body_mass_by_species_and_sex()
    test_correlation_bill_flipper_by_island()
    print("All tests passed.")


