import pandas as pd
import matplotlib.pyplot as plt
class MCA:
    def __init__(self, file_path):
        # Initialize the class with the DataFrame loaded from the specified file_path
        self.df = pd.read_csv(file_path)

    def display_data(self):
        # Display the DataFrame
        print(self.df.to_string())
        print('#' * 86)

    def replace_null_values(self, column, value):
        # Replace null values in a specified column with a given value
        self.df[column].fillna(value, inplace=True)

    def fill_null_values_with_median(self, column):
        # Fill null values in a specified column with the median
        median_value = self.df[column].median()
        self.df[column].fillna(median_value, inplace=True)
    def fill_null_values_with_mean(self, column):
        # Fill null values in a specified column with the median
        mean = self.df[column].mean()
        self.df[column].fillna(mean, inplace=True)
    def fill_null_values_with_mode(self, column):
        # Fill null values in a specified column with the mode
        modes = self.df[column].mode()
        if not modes.empty:
            self.df[column].fillna(modes.iloc[0], inplace=True)

    def drop_rows_with_null_values(self, column):
        # Drop rows with null values in a specified column
        self.df.dropna(subset=[column], inplace=True)

    def replace_wrong_data(self, column, threshold, replacement_value):
        # Replace values in a specified column that exceed a threshold with a replacement value
         self.df[column] = pd.to_numeric(self.df[column], errors='coerce')

        # Replace values exceeding the threshold
         self.df.loc[self.df[column] > threshold, column] = replacement_value

    def drop_wrong_data(self, column, threshold):
        self.df[column] = pd.to_numeric(self.df[column], errors='coerce')
        # Drop rows in the DataFrame where values in a specified column exceed a threshold
        self.df.drop(self.df[self.df[column] > threshold].index, inplace=True)

    def display_duplicated_data(self):
        # Display duplicated data indices
        print(self.df.duplicated())

    def remove_duplicates(self):
        # Remove duplicated rows from the DataFrame
        self.df.drop_duplicates(inplace=True)

    def save_to_excel(self, output_path):
        # Save the modified DataFrame to an Excel file
        self.df.to_excel(output_path, index=False)
    def data_integrity(self):
       self.df['Rep'] = self.df['Rep'].replace(r'[^a-zA-Z\s]', '', regex=True) #space
       self.df['Item'] = self.df['Item'].replace(r'[^a-zA-Z\s]', '', regex=True)
       self.df['Region'] = self.df['Region'].replace(r'[^a-zA-Z\s]', '', regex=True)
       self.df['Units'] = self.df['Units'].replace(r'[^0-9.]+', '', regex=True)
       self.df['UnitCost'] = self.df['UnitCost'].replace(r'[^0-9.]+', '', regex=True)
       self.df['Total'] = self.df['Total'].replace(r'[^0-9.]+', '', regex=True)
    def plot_units_distribution(self):
        # Plot a histogram of the 'Units' column
        self.df['Units'].astype(float).plot(kind='hist', bins=10, title='Units Distribution')
        plt.xlabel('Units')
        plt.ylabel('Frequency')
        plt.show()

    def plot_total_by_region(self):
        # Plot the total sales for each region
         self.df.groupby('Region')['Total'].sum().plot(kind='bar', title='Total Sales by Region')
         plt.xlabel('Region')
         plt.ylabel('Total Sales')
         plt.show()

# Example Usage:
file_path = r'C:\Users\hp\Desktop\GI\Second year\S3\UML\Projet\our_data.csv'
output_excel_path = r'C:\Users\hp\Desktop\GI\Second year\S3\UML\Projet\modified_dataGI.xlsx'

mca1 = MCA(file_path)                                         
mca1.display_data()
########################### Mainpulate emplty cells ####################
########## Replace null values ##################
####### Specify the value manually
#mca1.replace_null_values("OrderDate", '11/25/2023')
###### replace it based on ############
##### mean = sum of all values / number of the values
mca1.fill_null_values_with_mean('Total')
#### median = middle value
mca1.fill_null_values_with_median('Total')
#mode = the most used value
mca1.fill_null_values_with_mode('Total')
################## drop the rows with null values ##########################
mca1.drop_rows_with_null_values("OrderDate")
mca1.drop_rows_with_null_values("Total")
mca1.drop_rows_with_null_values("Rep")
############################## Data integrity ################################
mca1.data_integrity()
######################################Manipulate wrong data ###################
######## replace it
mca1.replace_wrong_data("Units", 100, 90)
######## delete it 
#mca1.drop_wrong_data("Units", 90)
################################Display dupliced data #####################
#### display duplicated data index
#mca1.display_duplicated_data()
## remove duplicated data
mca1.remove_duplicates()
#################################### Display and visualize ################
mca1.plot_total_by_region()
mca1.plot_units_distribution()
#### convert the results to exel file
mca1.save_to_excel(output_excel_path)
mca1.display_data()