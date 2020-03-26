import glob
from pathlib import Path

from PIL import Image
from tqdm import tqdm


NEW_SIZE = 64
RAW_CURLED_IMAGES_GLOB = "/Users/eric/dev/data/images_lana+rhoades_2.txt/**/**/**/*.jpg"
OUTPUT_DIR = "/Users/eric/dev/data/images_lana+rhoades_2.txt_resized"

images_filenames = list(glob.glob(RAW_CURLED_IMAGES_GLOB))
if not images_filenames:
    raise ValueError("{} contains no images".format(RAW_CURLED_IMAGES_GLOB))
print("len(images_filenames) = {}".format(len(images_filenames)))

MAX_WIDTH_HEIGHT_RATIO = 1.4

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
count = 0
print("Resizing images to size {}".format(NEW_SIZE))
for image_filepath in tqdm(images_filenames):
    im = Image.open(image_filepath)

    width, height = im.size
    width_height_ratio = max(height/width, width/height)
    if width_height_ratio > MAX_WIDTH_HEIGHT_RATIO:
        continue

    im = im.resize((NEW_SIZE, NEW_SIZE), Image.ANTIALIAS)  # todo(eric) best adapt sizep
    im.save("{}/{}.jpg".format(OUTPUT_DIR, count))
    count += 1
