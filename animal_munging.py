import pandas as pd
import numpy as np

# Validation
def qualified(num_intakes, num_outcomes):
    is_qualified = False
    
    if num_intakes == num_outcomes or num_intakes-1 == num_outcomes:
        is_qualified=True
    
    return is_qualified

def find_num_stays(df):
    stay_list=[]
    first_row = df.iloc[0, :]
    if first_row["is_intake"]:
        x_len = len(df)
        for i in range(0, x_len - 1):
            x1_row = df.iloc[i, :]
            x2_row = df.iloc[i + 1, :]
            if (x1_row["is_intake"]==True) & (x2_row["is_intake"]==False):
                if x1_row["is_intake"] != x2_row["is_intake"]:
                    stay = (x2_row['datetime']-x1_row["datetime"])/np.timedelta64(1, 'D')
                    stay_list.append(stay)
    num_stays=len(stay_list)
    return num_stays

def find_staymean(df):
#Finds the mean length of stay for a particular animal id if and only if
#the stay has followed by an adoption outcome.
    stay_list=[]
    first_row = df.iloc[0, :]
    if first_row["is_intake"]:
        x_len = len(df)
#The range has to be the length of the dataframe-1 because of the need to add 1 to the current row
#The for loop cannot use iterrows because the result has to refer to the current row and the next one.
        for i in range(0, x_len - 1):
#Sets variables equal to the first and second rows of the dataframe
            x1_row = df.iloc[i, :]
            x2_row = df.iloc[i + 1, :]
#First in pair has to be intake, the next has to be an outcome
            if (x1_row["is_intake"]==True) & (x2_row["is_intake"]==False):
#A pair of rows is valid if they are not both intakes or both outcomes.
                if x1_row["is_intake"] != x2_row["is_intake"]:
#Stay length is the number of days between intake and adoption outcome.
                    stay = (x2_row['datetime']-x1_row["datetime"])/np.timedelta64(1, "D")
                    stay_list.append(stay)
# Calculates and returns average
    try:
        average_stay = sum(stay_list)/len(stay_list)
    except ZeroDivisionError:
        average_stay = 0
        
    return average_stay

# Cleaning
def split_colors(color,*,primary=True):
    split_char = "/"
    
    color_list = color.split(split_char) if color.find(split_char) >=0 else color

    color_output = None
    if primary:
        color_output = color_list[0] if type(color_list) == list else color_list
    else:
        color_output = color_list[1] if type(color_list) == list else None
    
    return color_output

def convert_color(color, conversion_dict):
    converted_color = None
    for key, value in conversion_dict.items():
        if not color == None:
            if color in value:
                converted_color = key
        else:
            converted_color = None
    return converted_color


def total_color_set(color_series):
    
    primary_secondary = [
        split_colors(color)
        for color 
        in color_series.unique()
    ]

    primary = {pair[0] if type(pair) == list else pair for pair in primary_secondary}
    secondary = {pair[1] for pair in primary_secondary if type(pair) == list}

    return primary|secondary

def round_off(avg_stay_len):
    if avg_stay_len <1:
        avg_stay_len = 1
    
    return avg_stay_len

def convert_age_to_num(age_string):
    year=0
    if age_string.endswith("months"):
        year = 1
    else:
        year = int(age_string.split(" ")[0])
    return year