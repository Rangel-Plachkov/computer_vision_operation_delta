import os
import numpy as np
from PIL import Image
from pathlib import Path
from tqdm import tqdm


INPUT_DIR = "val"
OUTPUT_DIR = "val_png"

# Define target colors thresholds -> set lower to avoid black pixels in the middle
RED_TH = np.array([160, 0, 0])
BLUE_TH = np.array([0, 0, 160])

# Define target colors
BLACK = np.array([0, 0, 0])
RED = np.array([255, 0, 0])
BLUE = np.array([0, 0, 255])


def clean_jpg_to_png(input_path, output_path):
    """
    Convert JPG mask with artifacts to clean 3-color PNG (red, blue, and black background).
    Uses color distance to classify pixels.
    """
    # Load image
    img = Image.open(input_path).convert('RGB')
    arr = np.array(img, dtype=np.float32)

    # Reshape for vectorized operations
    h, w = arr.shape[:2]
    pixels = arr.reshape(-1, 3)

    # Calculate distance to each target color
    dist_to_red = np.linalg.norm(pixels - RED_TH, axis=1)
    dist_to_blue = np.linalg.norm(pixels - BLUE_TH, axis=1)
    dist_to_black = np.linalg.norm(pixels - BLACK, axis=1)

    # Stack distances and find minimum
    distances = np.stack([dist_to_red, dist_to_blue, dist_to_black], axis=1)
    labels = np.argmin(distances, axis=1)

    # Create output array
    result = np.zeros((h * w, 3), dtype=np.uint8)
    result[labels == 0] = RED
    result[labels == 1] = BLUE
    result[labels == 2] = BLACK

    # Reshape back to image
    result = result.reshape(h, w, 3)

    # Save as PNG
    Image.fromarray(result).save(output_path, 'PNG')

def process_directory():
    """Process all JPG files in INPUT_DIR and save to OUTPUT_DIR"""

    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Find all jpg files
    input_path = Path(INPUT_DIR)
    jpg_files = list(input_path.glob('*.jpg')) + list(input_path.glob('*.jpeg')) + list(input_path.glob('*.JPG'))

    if not jpg_files:
        print(f"No JPG files found in {INPUT_DIR}")
        return

    print(f"Found {len(jpg_files)} JPG files to process")

    # Process each file
    for jpg_file in tqdm(jpg_files, desc="Converting JPG to PNG"):
        # Create output filename (same name but .png extension)
        output_filename = jpg_file.stem + '.png'
        output_path = Path(OUTPUT_DIR) / output_filename

        try:
            clean_jpg_to_png(str(jpg_file), str(output_path))
        except Exception as e:
            print(f"\nError processing {jpg_file.name}: {e}")

    print(f"\nCompleted! Cleaned PNG files saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    process_directory()