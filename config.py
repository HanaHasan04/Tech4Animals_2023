# import the necessary packages
import os

# initialize the path to the *original* input directory of images
ORIG_INPUT_DATASET = "C:/Users/USER/Documents/UniversityProjects/PythonProjects/FinalProject/Cropped_Resized"

# initialize the base path to the *new* directory that will contain
# our images after computing the training and testing split
BASE_PATH = "C:/Users/USER/Documents/UniversityProjects/PythonProjects/FinalProject/data_split"

# derive the training, validation, and testing directories
TRAIN_PATH = os.path.sep.join([BASE_PATH, "train"])
VAL_PATH = os.path.sep.join([BASE_PATH, "val"])
TEST_PATH = os.path.sep.join([BASE_PATH, "test"])

# define the amount of data that will be used training
TRAIN_SPLIT = 0.8

# the amount of validation data will be a percentage of the
# *training* data
VAL_SPLIT = 0.1

# define the names of the classes
CLASSES = ["Anticipation", "Baseline", "Disappointment", "Frustration"]

# initialize the initial learning rate, batch size, and number of
# epochs to train for
INIT_LR = 1e-4
BS = 32
NUM_EPOCHS = 20

# define the path to the serialized output model after training
MODEL_PATH = "C:/Users/USER/Documents/UniversityProjects/PythonProjects/FinalProject/horse_emotion_classifier.model"


