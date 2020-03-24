import os

RAW_CURLED_IMAGES_DIR = "/tmp/AnimeFaceGAN/RawCurledImages"
RAW_CURLED_IMAGES_GLOB = "{}/**/*.png".format(RAW_CURLED_IMAGES_DIR)
DATA_DIR = os.environ["ANIME_FACE_GAN_DATA_DIR"] if "ANIME_FACE_GAN_DATA_DIR" in os.environ else "/Users/eric/dev/data/AnimeFaceGAN"
DATA_GLOB = "{}/*.png".format(DATA_DIR)
GENERATED_IMAGES_DIR = "./generated"
