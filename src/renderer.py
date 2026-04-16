from PIL import Image, ImageDraw, ImageFont

def print_grid(grid):
    for row in grid:
        print("".join(row))


def save_as_image(grid, filename="output/message.png"):
    cell_size = 20
    width = len(grid[0]) * cell_size
    height = len(grid) * cell_size

    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            draw.text((x * cell_size, y * cell_size), char, fill="black")

    image.save(filename)
