import imageio.v3 as iio
from PIL import Image

filenames = ['happy.png', 'sad.png']
images = [ ]

for filename in filenames:
  img = Image.open(filename).convert('RGB')
  img = img.resize((500, 500))  # force same size
  images.append(img)

iio.imwrite('team.gif', images, duration = 500, loop = 0)