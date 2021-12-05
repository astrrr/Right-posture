import os

CWD = os.getcwd().replace('\\', '/')
IMAGE_DIR = f'{CWD}/data/train'
TRAIN_DATASET_DIR = f'{IMAGE_DIR}/train'
TEST_DATASET_DIR = f'{IMAGE_DIR}/test'
VAL_DATASET_DIR = f'{IMAGE_DIR}/validation'

CATEGORIES = ['correct','incorrect']

AUGMENT_SAVE_PREFIX = 'aug'


def delAug():
    try:

        print("Deleting Augment")

        for subfolder in os.listdir(IMAGE_DIR):

            for category in CATEGORIES:

                category_dir = f'{IMAGE_DIR}/{subfolder}/{category}'

                for image_name in os.listdir(category_dir):

                    file_path = f'{category_dir}/{image_name}'

                    if os.path.exists(file_path) and image_name.find(AUGMENT_SAVE_PREFIX) != -1:
                        os.remove(file_path)

        print("Delete Successfully!!!")

    except Exception as e:

        print("Delete Fail...")
        print("Exception :", e)


delAug()
