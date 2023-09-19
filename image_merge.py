import os
import re
from PIL import Image

def find_matching_images(original_dir, edited_dir, output_dir):
    try:
        # Verify that the original and edited directories exist
        if not os.path.exists(original_dir) or not os.path.exists(edited_dir):
            raise FileNotFoundError("One or both input directories do not exist.")

        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Get a list of files in each directory
        original_files = os.listdir(original_dir)
        edited_files = os.listdir(edited_dir)

        for original_file in original_files:
            # Ignore files that do not have the expected extension (e.g., .png)
            if not original_file.endswith('.png'):
                continue

            # Extract the filename without the extension
            original_filename = os.path.splitext(original_file)[0]

            # Use regular expression to find the corresponding edited file
            edited_pattern = re.compile(r'^\d{5}-' + re.escape(original_filename) + r'\.png$')
            matching_edited_files = [file for file in edited_files if edited_pattern.match(file)]

            if matching_edited_files:
                print(f"Processing: {original_file} and {matching_edited_files[0]}")

                # Load the original and edited images
                original_image = Image.open(os.path.join(original_dir, original_file))
                edited_image = Image.open(os.path.join(edited_dir, matching_edited_files[0]))

                # Get the dimensions of both images
                original_width, original_height = original_image.size
                edited_width, edited_height = edited_image.size

                # Determine the target width for the merged image
                target_width = max(original_width, edited_width)
                target_height = max(original_height, edited_height)

                # Resize images to match the target dimensions
                original_image = original_image.resize((target_width, target_height))
                edited_image = edited_image.resize((target_width, target_height))

                # Create a new image by merging the original and edited images side by side
                merged_image = Image.new('RGB', (2 * target_width, target_height))
                merged_image.paste(original_image, (0, 0))
                merged_image.paste(edited_image, (target_width, 0))

                # Save the merged image to the output directory
                # Save the merged image to the output directory with specified quality
                output_file = os.path.join(output_dir,
                                           f'merged_{original_filename}.jpg')  # Change file format to JPEG for better compression
                merged_image.save(output_file, format='JPEG',
                                  quality=90)  # Adjust quality as needed (90 is just an example)
                print(f"Merged image saved as: {output_file}")

        print("Images have been merged and saved in the output directory.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    original_directory = "/Users/miti/Desktop/AI/epic/test"
    edited_directory = "/Users/miti/Desktop/AI/epic/batch"
    output_directory = "/Users/miti/Desktop/AI/epic/together"

    find_matching_images(original_directory, edited_directory, output_directory)
