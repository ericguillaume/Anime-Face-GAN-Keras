set -e

rm -rf ~/dev/data/images_lana+rhoades_2.txt_resized
rm -rf ~/dev/data/images_lana+rhoades_2.txt_resized.tar.gz

python3 generate_xh_dataset.py

cd ~/dev/data
tar -czvf images_lana+rhoades_2.txt_resized.tar.gz ./images_lana+rhoades_2.txt_resized
