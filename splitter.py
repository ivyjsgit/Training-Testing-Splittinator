import os
import sys

def listdirs(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

if len(sys.argv)>=3:

    training_dir = sys.argv[1]
    testing_dir = sys.argv[2]
    if len(sys.argv)==4:
        split_factor = sys.argv[3]
    else:
       split_factor = 10

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

        if not os.path.exists(current_testing_dir):
            os.makedirs(current_testing_dir)    

        for i in range(len(test_files_dir_before_moves)):
            before_move = test_files_dir_before_moves[i]
            after_move = test_files_dir_after_moves[i]
            print(f"Moving {before_move} {after_move}")
            os.rename(before_move, after_move)
else:
    print("Usage: python3 splitter.py training_dir testing_dir [split_factor] ")
