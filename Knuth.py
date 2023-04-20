# Knuth shuffle: This is a variation of the Fisher-Yates shuffle that is more efficient and produces a more uniform distribution
import random
import argparse
import os
from random import shuffle

parser = argparse.ArgumentParser()
parser.add_argument('--folder_path', default='./data', type=str,
                    help='The folder path')
parser.add_argument('--train_filename', default='./data/places2/train_shuffled.flist', type=str,
                    help='The output filename.')
parser.add_argument('--validation_filename', default='./data/places2/validation_shuffled.flist', type=str,
                    help='The output filename.')
parser.add_argument('--is_shuffled', default='1', type=int,
                    help='Needed to shuffle')


def knuth_shuffle(lst):
    for i in range(len(lst)):
        j = random.randint(i, len(lst) - 1)
        lst[i], lst[j] = lst[j], lst[i]


if __name__ == "__main__":

    args = parser.parse_args()

    # get the list of directories
    dirs = os.listdir(args.folder_path)
    dirs_name_list = []

    # make 2 lists to save file paths
    training_file_names = []
    validation_file_names = []

    # print all directory names
    for dir_item in dirs:
        # modify to full path -> directory
        dir_item = args.folder_path + "/" + dir_item
        # print(dir_item)

        training_folder = os.listdir(dir_item)
        for training_item in training_folder:
            training_item = dir_item + "/" + training_item
            training_file_names.append(training_item)

        validation_folder = os.listdir(dir_item)
        for validation_item in validation_folder:
            validation_item = dir_item + "/" + validation_item
            validation_file_names.append(validation_item)
    # print all file paths
    for i in training_file_names:
        print(i)
    for i in validation_file_names:
        print(i)

    # This would print all the files and directories

    # shuffle file names if set
    if args.is_shuffled == 1:
        knuth_shuffle(training_file_names)
        knuth_shuffle(validation_file_names)

    # make output file if not existed
    if not os.path.exists(args.train_filename):
        os.mknod(args.train_filename)

    if not os.path.exists(args.validation_filename):
        os.mknod(args.validation_filename)

    # write to file
    fo = open(args.train_filename, "w")
    fo.write("\n".join(training_file_names))
    fo.close()

    fo = open(args.validation_filename, "w")
    fo.write("\n".join(validation_file_names))
    fo.close()

    # print process
    print("Written file is: ", args.train_filename,
          ", is_shuffle: ", args.is_shuffled)
