import colorgram
# This script extracts colors from an image using the colorgram library.

colors = colorgram.extract('images.jpg', 6)

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

# we goona use these colors to draw a random color from the list of colors
# [(243, 242, 242), (22, 149, 185), (234, 118, 46), (11, 59, 84), (228, 235, 239), (207, 66, 26)]

