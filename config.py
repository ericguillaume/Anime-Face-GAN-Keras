import os

RAW_CURLED_IMAGES_DIR = "/tmp/AnimeFaceGAN/RawCurledImages"
RAW_CURLED_IMAGES_GLOB = "{}/**/*.png".format(RAW_CURLED_IMAGES_DIR)
DATA_DIR = os.getenv("ANIME_FACE_GAN_DATA_DIR", "/Users/eric/dev/data/AnimeFaceGAN")
DATA_GLOB = "{}/*.png".format(DATA_DIR)
GENERATED_IMAGES_DIR = "./generated"
NUM_STEPS = int(os.getenv("ANIME_FACE_GAN_NUM_STEPS", 10000))
BATCH_SIZE = int(os.getenv("ANIME_FACE_GAN_BATCH_SIZE", 64))
