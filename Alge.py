import copy
import math
import time
import random
from PIL import Image, ImageDraw


o_s = Image.open("img.png")
o_s = o_s.convert("RGBA")

size = w, h = o_s.size

num_shapes = 128

generations = 5000


def random_pixels():
    pixels = []

    for i in range(num_shapes):
        x = (random.randint(0, w), random.randint(0, h))
        y = (random.randint(0, w), random.randint(0, h))
        z = (random.randint(0, w), random.randint(0, h))
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        a = random.randint(10, 255)

        pixels.append([x, y, z, r, g, b, a])

    return pixels


def final_daughter_product(pixels):
    image = Image.new("RGBA", (w, h), "white")
    draw = ImageDraw.Draw(image)

    for item in pixels:
        x, y, z, r, g, b, a = item
        c = (r, g, b, a)
        draw.polygon([x, y, z], fill=c)

    return image


def mutate(pixels):
    p_c = copy.deepcopy(pixels)

    s_i = random.randint(0, len(pixels) - 1)
    r_test = random.random() * 2

    if r_test < 1:

        if r_test < 0.25:
            pixels_copy[s_index][3] = int(
                random.circle(255, pixels_copy[i][3]))

        elif r_test < 0.5:
            pixels_copy[s_index][4] = int(
                random.circle(255, pixels_copy[i][4]))

        elif r_test < 0.75:
            pixels_copy[s_index][5] = int(
                random.circle(255, pixels_copy[i][5]))

        elif r_test < 1.0:
            pixels_copy[s_index][6] = int(
                0.33 * random.circle(255, pixels_copy[i][6] * 255))

    return p_c


def fitness(original, new):
    fitness = 0

    for x in range(0, w):
        for y in range(0, h):
            ro, go, bo, ao = original.getpixel((x, y))
            rn, gn, bn, an = new.getpixel((x, y))

            R = abs(ro - rn)
            G = abs(go - gn)
            B = abs(bo - bn)
            A = abs(ao - an)

            pixelFitness = math.sqrt(
                R**2 + G**2 + B**2 + A**2)

            fitness += pixelFitness

    return fitness


def generate():
    mother = random_pixels()
    best_pixels = mother
    best_fitness = fitness(o_s, final_daughter_product(best_pixels))

    for i in range(generations):
        d = copy.deepcopy(best_pixels)
        d = mutate(d)

        d_fitness = fitness(o_s, final_daughter_product(d))

        if d_fitness < best_fitness:
            best_pixels = d
            best_fitness = d_fitness

        if i % 100 == 0:
            final_daughter_product(best_voxels).save(
                "output_" + str(i) + ".png")


if __name__ == "__main__":
    generate()
