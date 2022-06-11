from raw_to_dataframe import create_df
import pandas as pd

def test_create_df():
    id_list = [1, 2, 3, 4,]
    name    = ["Salman", "Numair", "Uzair", "Ammar"]
    age     = [30, 10, 3, 6]
    marks   = [45, 56, 86, 96]
    column_names = ["Id", "Name", "Age", "Marks"]

    df_observed = create_df(id_list, name, age, marks, column_names)

    df_expected = pd.DataFrame([[1, 'Salman', 30, 45], [2, 'Numair', 10, 56], 
                                [3, 'Uzair', 3, 86], [4, 'Ammar', 6, 96]], columns =["Id", "Name", "Age", "Marks"])

    assert df_expected.equals(df_observed)

