import os

RAW_CURLED_IMAGES_DIR = "/tmp/AnimeFaceGAN/RawCurledImages"
RAW_CURLED_IMAGES_GLOB = "{}/**/*.png".format(RAW_CURLED_IMAGES_DIR)
DATA_DIR = os.getenv("LANA_GAN_DATA_DIR", "/Users/eric/dev/data/images_lana+rhoades_2.txt_resized")
DATA_GLOB = "{}/*.jpg".format(DATA_DIR)
GENERATED_IMAGES_DIR = "./generated"
