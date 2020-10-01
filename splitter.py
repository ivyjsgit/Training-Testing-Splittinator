import os

training_dir = "/Users/ivy/Desktop/Senior_Seminar/training"
testing_dir = "/Users/ivy/Desktop/Senior_Seminar/testing"
split_factor = 10

def listdirs(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

for dir in listdirs(training_dir):
    current_dir = f"{training_dir}/{dir}"
    current_testing_dir = f"{testing_dir}/{dir}"
    all_files = os.listdir(current_dir)

    num_files = len(all_files)
    #Get 10% of all files    
    num_test = round(num_files/split_factor)

    training_files = all_files[num_test:num_files]
    test_files =  all_files[0:num_test]

    test_files_dir_before_moves = list(map((lambda n:  f"{current_dir}/{n}"), test_files))
    test_files_dir_after_moves = list(map((lambda n: f"{current_testing_dir}/{n}"), test_files))

    map(lambda before_move, after_move: os.rename(before_move, after_move), test_files_dir_before_moves, test_files_dir_after_moves)

    
