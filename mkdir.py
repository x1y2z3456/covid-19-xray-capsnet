import os
home_directory = os.path.expanduser('~')
base_dir = os.path.abspath(
    f'{home_directory}/Efficient-CapsNet/covid-chestxray-dataset')

to_create = {
    'root': base_dir,
    'train_dir': os.path.join(base_dir, 'train'),
    'test_dir': os.path.join(base_dir, 'test'),
}
sub_dirs = ['bacteria', 'healthy', 'viral_covid-19', 'viral_other']

for directory in to_create.values():
    try:
        os.mkdir(directory) if not os.path.exists(
            directory) else print(directory, ' already exists!')
        # iterating through dictionary to make new dirs
        if 'train' in directory or 'test' in directory:
            for sub_directory in sub_dirs:
                sub_dir = os.path.join(directory, sub_directory)
                os.mkdir(sub_dir) if not os.path.exists(
                    sub_dir) else print(sub_dir, ' already exists!')
        # print(directory, 'created')
    except:
        print(directory, 'failed')

