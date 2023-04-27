import os
import argparse
from PIL import Image

def convert_png_to_jpg(input_dir, output_dir, quality=85):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file in os.listdir(input_dir):
        if file.lower().endswith(".png"):
            input_path = os.path.join(input_dir, file)
            output_path = os.path.join(output_dir, file[:-4] + ".jpg")

            img = Image.open(input_path)
            rgb_im = img.convert("RGB")
            rgb_im.save(output_path, "JPEG", quality=quality)

def main():
    parser = argparse.ArgumentParser(description="Batch convert PNG files to JPG files")
    parser.add_argument("input_dir", help="Path to the input directory containing PNG files")
    parser.add_argument("output_dir", help="Path to the output directory for saving JPG files")
    parser.add_argument("-q", "--quality", type=int, default=85, help="Quality of output JPG files (1-95, default: 85)")

    args = parser.parse_args()

    convert_png_to_jpg(args.input_dir, args.output_dir, args.quality)

if __name__ == "__main__":
    main()

