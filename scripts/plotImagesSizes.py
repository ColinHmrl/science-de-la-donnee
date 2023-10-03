import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from PIL import Image

def plot_image_sizes(image_paths):
    widths = []
    heights = []

    for image_path in image_paths:
        try:
            with Image.open(image_path) as img:
                width, height = img.size
                widths.append(width)
                heights.append(height)
        except Exception as e:
            print(f'Error processing {image_path}: {str(e)}')

    plt.figure(figsize=(10, 6))
    plt.scatter(widths, heights, alpha=0.5)
    plt.title('Image Sizes')
    plt.xlabel('Width')
    plt.ylabel('Height')

    plt.gca().set_aspect('equal', adjustable='box')

    plt.grid(True, linestyle='--', alpha=0.7)

    plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.show()
    
plot_image_sizes(df['image_path'])