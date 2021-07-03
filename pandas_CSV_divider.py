
import pandas as pd
import numpy as np

# VARIABLES TO ASSIGN BY THE USER:

# This is the path where your big file actually is:
file_path = ''

# Insert the total of rows that you would like each file to have:
number_of_rows_per_file = 10000

# Asing the adress where you want your files to be:
personal_down_path = ''

file_number = 0

# AUTOMATIC VARIABLES:

# Create a Pandas DataFrame with it:
file_path = pd.read_csv(file_path)

# Insert the len of the file to the variable file_len:
file_len = file_path.id.count()



# FUNCTIONS:

#This is a calleable function to print each file.
def print_csv(table_to_csv, file_number):

    # Asing the adress where you want your files to be:
    down_path = personal_down_path + '{}'.format('part_num_' + str(file_number) + '.csv')

    # Save the csv part into the adress:
    table_to_csv.to_csv(down_path, index = False, sep = ',')


# This is a func to divide the files.
def divide(file_path, file_len, number_of_rows_per_file):

    # Create the counter and add the first number of rows per file.
    counter = 0
    counter = number_of_rows_per_file

    # Create the variable that will have the data to print into a csv file.
    file_path_x = file_path.iloc[0:counter,:]

    # print the file_path_x DataFrame:
    file_number = 1
    print_csv(file_path_x, file_number)

    # Create the print bucle:
    while counter < file_len & number_of_rows_per_file + counter + 1 < file_len:
        
        # Create last_counter to avoid duplicates.
        last_counter = counter
        counter = number_of_rows_per_file + counter

        # Create the variable that will have the data to print into a csv file.
        file_number = file_number + 1
        file_path_x = file_path.iloc[last_counter:counter,:]

        # print the file_path_x DataFrame:
        print_csv(file_path_x, file_number)

    # If the counter is no equal or greater than file_len print what is left:
    file_path_x = file_path.iloc[counter + 1:file_len,:]
    file_number = file_number + 1
    print_csv(file_path_x, file_number)




# START:

if __name__ == '__main__':
    divide(file_path, file_len, number_of_rows_per_file)
    print("All your files were printed in: " + personal_down_path)