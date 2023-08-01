import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]


# check if new/ exists, if not create one
print(os.path.exists(output_folder))



# loop through Pokedex,
# convert the images to png
# save it to the new folder.
