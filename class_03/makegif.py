import imageio

images = []
filenames = []

for i in range(0,200):
    filenames.append("ant_colony_frames/frame{0:05d}.png".format(i))

with imageio.get_writer('ant_colony_s80_a100_fr200.gif', mode='I', duration = 0.05) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

