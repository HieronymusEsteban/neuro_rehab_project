
import pandas as pd
#import numpy as np
import re


def identify_get_timestamps(file_name, data_item):

    """This function takes and transforms the timestamps variable
    that is stored as a numpy.array in a numpy.void object 
    (data_item['results'][0][0]), which is stored inside another
    numpy.array (data_item['results']), which is in turn stored
    inside a dictionary (data_item).
    The .dtype attribute of data_item['results'] contains the
    names of all the variables in the same order as the 
    numpy.arrays that contain the respective variable values.
    The time stamps should be used as identifiers as we 
    want to split the data into different parts based on 
    when data values were measured. The timestamps indicate
    the time span between the time the measuring device was switched on 
    and the measurement in seconds. Therefore, timestamps measured in hours are 
    also added. As a comparison between morning and afternoon
    is desired a categorical variable indicating whether a measurement
    took place in the morning or in the afternoon is also added."""

    # Get variable_names:
    num_elements = len(data_item['results'].dtype.descr)
    variable_names = []
    for index in range(0, num_elements):
        variable_name = data_item['results'].dtype.descr[index][0]
        variable_names.append(variable_name)
    # Get index of variable 'gait_timestamps': 
    variable_of_interest = 'gait_timestamps'
    variable_index = [i for i, expr in enumerate(variable_names) if re.search(variable_of_interest, expr)][0]


    # Get time stamps and categorize them into morning and afternoon: 
    # The actual data is stored as an numpy.array inside another
    # numpy.array data_item['results'][0][0][variable_index], which thereofore
    # you have to slice by adding another [0]. 
    time_stamps = data_item['results'][0][0][variable_index][0]
    time_stamps_hours = data_item['results'][0][0][variable_index][0]/3600
    morning = data_item['results'][0][0][variable_index][0]/3600 < 4
    morning_one_hot = [bools_to_one_hot(x) for x in morning]

    number_of_values = len(time_stamps)
    data_to_frame = {}
    #data_to_frame['subject'] = [file_name] * number_of_values

    #subject_name = file_name.split('.')[0]
    name_parts = file_name.split('_')[:2]
    subject_name = '_'.join(name_parts)
    subject_name_array = [subject_name] * number_of_values


    data_to_frame['file_name'] = [file_name] * number_of_values
    data_to_frame['subject'] = subject_name_array
    data_to_frame['time_stamps'] = time_stamps
    data_to_frame['time_stamps_hours'] = time_stamps_hours
    data_to_frame['morning_afternoon'] = morning_one_hot
    data_frame_to_add = pd.DataFrame(data_to_frame)

    return data_frame_to_add


def identify_get_variable(file_name, variable_name_of_interest, data_item, data_frame_to_add):
    
    """This function takes and transforms the variables stored as
    numpy.arrays in a numpy.void object 
    (data_item['results'][0][0]), which is stored inside a 
    numpy.array (data_item['results']), which is in turn stored
    inside a dictionary (data_item).
    The .dtype attribute of data_item['results'] contains the
    names of all the variables in the same order as the 
    numpy.arrays that contain the respective variable values.
    The function therefore matches the variable names from
    .dtype with the actual data by selected both of them in 
    the same order."""

    # Get variable_names:
    num_elements = len(data_item['results'].dtype.descr)
    variable_names = []
    for index in range(0, num_elements):
        variable_name = data_item['results'].dtype.descr[index][0]
        variable_names.append(variable_name)
    # Get index of variable: 
    variable_index = [i for i, expr in enumerate(variable_names) if re.search(variable_name_of_interest, expr)][0]

    # Get data corresponding to variable name: 
    # The actual data is stored as an numpy.array inside another
    # numpy.array data_item['results'][0][0][variable_index], which thereofore
    # you have to slice by adding another [0].
    variable = data_item['results'][0][0][variable_index][0]
    data_frame_to_add[variable_name_of_interest] = variable

    return data_frame_to_add



def bools_to_one_hot(x):
    """This function is used to make a categorical variable whose values correspond are 
    1 and 0 by converting the boolean value True to 1 and the boolean value False
    to 0."""
    if x:
        value = 1
    else:
        value = 0
    return value



def add_exp_phase_id(data_wide, col_after_which_insert):
    """This function extracts the T2 or T3 tags from the original file name
    to designate the pre-neuro-rehab and post-neuro-rehab phase data respectively."""
    exp_phase_id = []
    exp_phase_descr = []
    for index, row in data_wide.iterrows():
        #string_parts = row.subject.split('metrics_')
        string_parts = row.file_name.split('metrics_')
        if string_parts[1] == 'T2.mat':
            exp_phase_id.append('T2')
            exp_phase_descr.append('Control phase: before rehab training.')
        elif string_parts[1] == 'T3.mat':
            exp_phase_id.append('T3')
            exp_phase_descr.append('Test phase: after rehab training.')


    col_position = data_wide.columns.get_loc(col_after_which_insert)
    data_wide.insert(col_position + 1, 'exp_phase_id', exp_phase_id)
    data_wide.insert(col_position + 2, 'exp_phase_descr', exp_phase_descr)
    return data_wide