import imageio

images = []
filenames = []

for i in range(0,100):
    filenames.append("gol_frames/frame{0:05d}.png".format(i))

with imageio.get_writer('gol_movie.gif', mode='I', duration = 0.5) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

