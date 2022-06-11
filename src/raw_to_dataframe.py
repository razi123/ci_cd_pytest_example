import pandas as pd


def create_df(id_list, name_list, age_list, marks_list, column_names):
    data = []
    for i in range(len(id_list)):
        data.append([id_list[i], name_list[i], age_list[i], marks_list[i]])
        df = pd.DataFrame(data, columns = column_names)
    
    return df


if __name__ == "__main__":

    df_students = create_df([1, 2, 3, 4], 
		    ["Salman", "Numair", "Uzair", "Ammar"], 
                    [30, 10, 3, 6], [45, 56, 86, 96],
                    ["Id", "Name", "Age", "Marks"])



