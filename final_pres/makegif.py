import imageio

images = []
filenames = []

for i in range(0,1001):
    filenames.append("for_gif/outcome{0:05d}.png".format(i))

with imageio.get_writer('demonstration/sznajd_anim.gif', mode='I', duration = 0.5) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

