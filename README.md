# Image Merge Tool

This Python script allows you to merge pairs of images from two directories, where one directory contains the original images, and the other contains edited versions of those images. The script matches images based on their filenames, ignoring a random numeric prefix on the edited images, and merges them side by side into new images.

## Features

- Automatically detects and matches original and edited images.
- Resizes images to have the same dimensions before merging.
- Saves merged images in an output directory.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed on your system.
- The Pillow library (PIL) installed. You can install it using pip: pip install pillow


## Usage

1. Clone this repository or download the script.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script by executing the following command: python image_merge.py


4. Follow the prompts to provide the paths to the original image directory, edited image directory, and output directory.

5. The script will process the images, merge them, and save the merged images in the output directory.

## Configuration

You can customize the script by adjusting the following parameters:

- `original_directory`: The path to the directory containing the original images.
- `edited_directory`: The path to the directory containing the edited images.
- `output_directory`: The path to the directory where the merged images will be saved.

## Contributing

Contributions to this project are welcome. Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
