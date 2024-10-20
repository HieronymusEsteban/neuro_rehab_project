import pandas as pd

def count_unique_subjects_per_hour(data_wide, time_bins):
    """This function counts the number of unique subjects per hour after
    start of recording. time_bins is a list containing the unique time bins."""
    time_bins.sort()
    subject_counts = []
    for time_bin in time_bins:
        selection_bools = (data_wide["time_stamps_bins"] == time_bin)
        data_time_bin = data_wide[selection_bools]
        unique_subjects = list(set(data_time_bin.subject))
        number_unique_subjects = len(unique_subjects)
        #print(time_bin)
        #print(number_unique_subjects)
        subject_counts.append(number_unique_subjects)
    subjects_per_hour = {'time_bin': time_bins, 'number_unique_subjects': subject_counts}
    subjects_per_hour = pd.DataFrame(subjects_per_hour)
    return subjects_per_hour



def test_monotony(time_stamp_list):
    indices = []
    test_values = []
    false_result_bools = []
    #tl = [0, 1, 3, 4]
    #time_stamps_l = tl
    for i in range(0,len(time_stamp_list) - 1):
        #print(i)
        indices.append(i)
        test_value = time_stamp_list[i] > time_stamp_list[i+1]
        test_values.append(test_value)
        #print(test_value)
    time_monotony_tests = pd.DataFrame({'index_column': indices, 
                                    'test_value': test_values}) 
    return time_monotony_tests  