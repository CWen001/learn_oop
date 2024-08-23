
from ast import Pass
import numpy as np
import pandas as pd
import csv

from data_entry import get_date, get_amount, get_category, get_description


class CSV:
    COLUMNS = ['date', 'amount', 'category', 'description']
    CSVFILE = r'notebooks\learn_ooptest_csvfile_3.csv'

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSVFILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSVFILE, index=False)
                
    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {'date': date,
                     'amount': amount,
                     'category': category,
                     'description': description}

        with open(cls.CSVFILE, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print('Entry added successfully')

    @classmethod
    def get_transactions(cls, start_time, end_time):
        
        df = pd.read_csv(cls.CSVFILE)
        df['date'] = pd.to_datetime(df['date'])
        
        start_time = pd.to_datetime(start_time)
        end_time = pd.to_datetime(end_time)

        mask = (df['date'] >= start_time) & (df['date'] <= end_time)
        filtered_df = df.loc[mask]
        
        # The total amount incomes between the given dates (category == 'income')
        total_incomes = filtered_df[filtered_df['category'] == 'income']['amount'].sum()
        print('Total incomes:', total_incomes)
    
        # The total amount expenses between the given dates (category == 'expense')
        total_expenses = filtered_df[filtered_df['category'] == 'expense']['amount'].sum()
        print('Total expenses:', total_expenses)
    
        # pretty print the filtered_df to console
        print(filtered_df)
       



# %%
# Example usage
CSV.initialize_csv()

def add():
    date = get_date()
    amount = get_amount()
    category = get_category()
    description = get_description()

    CSV.add_entry(date, amount, category, description)
    


def main():
    CSV.initialize_csv()
    # add()
    
    CSV.get_transactions(start_time='2016-01-01',
                         end_time=  '2018-12-31')

if __name__ == '__main__':
    main()



# %%


