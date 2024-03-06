import imageio

images = []
filenames = []

for i in range(0,200):
    filenames.append("spatialPD_frames/frame{0:05d}.PNG".format(i))

with imageio.get_writer('task_2_spatialPD_movie_b_208.gif', mode='I', duration = 0.5) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

