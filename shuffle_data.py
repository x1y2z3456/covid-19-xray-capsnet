from shutil import copyfile
import random
import os

home_directory = os.path.expanduser('~')
base_dir = os.path.abspath(
    f'{home_directory}/Efficient-CapsNet/covid-chestxray-dataset')
src_base_dir = os.path.abspath(
    f'{home_directory}/Efficient-CapsNet/covid-chestxray-dataset/images_ok')
to_create = {
    'root': base_dir,
    'bacteria_train_dir': os.path.join(base_dir, 'train', 'bacteria'),
    'healthy_train_dir': os.path.join(base_dir, 'train', 'healthy'),
    'covid-19_train_dir': os.path.join(base_dir, 'train', 'viral_covid-19'),
    'other_train_dir': os.path.join(base_dir, 'train', 'viral_other'),
    'bacteria_test_dir': os.path.join(base_dir, 'test', 'bacteria'),
    'healthy_test_dir': os.path.join(base_dir, 'test', 'healthy'),
    'covid-19_test_dir': os.path.join(base_dir, 'test', 'viral_covid-19'),
    'other_test_dir': os.path.join(base_dir, 'test', 'viral_other'),
}


def split_data(SOURCE, Train_path, Test_path, split_size):
    all_files = []
    # os.listdir lists all the files/folders in a directory
    for image in os.listdir(SOURCE):
        # joining the root dir with the image name to get the path to the image
        image_path = os.path.join(image, SOURCE)
        # os.path.getsize returns the size of a file in bytes, here it is being used to check if file has size greater than 0 or not
        if os.path.getsize(image_path):
            all_files.append(image)
        else:
            print('{} has zero size, skipping'.format(image))

    total_files = len(all_files)
    split_point = int(total_files * split_size)
    # sample n number of files randomly from the given list of files
    shuffled = random.sample(all_files, total_files)
    train = shuffled[:split_point]  # slicing from start to split point
    test = shuffled[split_point:]
    for image in train:  # copy files from one path to another
        copyfile(os.path.join(SOURCE, image), os.path.join(Train_path, image))
    for image in test:
        copyfile(os.path.join(SOURCE, image), os.path.join(Test_path, image))


split_data(os.path.join(src_base_dir, 'bacteria'), to_create.get('bacteria_train_dir'),
           to_create.get('bacteria_test_dir'), 0.8)
split_data(os.path.join(src_base_dir, 'healthy'), to_create.get('healthy_train_dir'),
           to_create.get('healthy_test_dir'), 0.8)
split_data(os.path.join(src_base_dir, 'viral', 'covid-19'), to_create.get('covid-19_train_dir'),
           to_create.get('covid-19_test_dir'), 0.8)
split_data(os.path.join(src_base_dir, 'viral', 'other'), to_create.get('other_train_dir'),
           to_create.get('other_test_dir'), 0.8)

