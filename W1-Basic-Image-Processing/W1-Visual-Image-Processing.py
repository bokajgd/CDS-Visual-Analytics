# Importing packages
import os

from pathlib import Path
import numpy as np
import pandas as pd
import cv2

# Basic image processing using python
'''
Write a Python script which does the following:

- For each image, find the width, height, and number of channels
- For each image, split image into four equal-sized quadrants (i.e. top-left, top-right, bottom-left, bottom-right)
- Save each of the split images in JPG format
- Create and save a file containing the filename, width, height for all of the new image
''' 

# Defining main function
def main():
    ImageProcessing()

class ImageProcessing:
    def __init__(self):
        data_dir = self.setting_data_directory()
        out_dir = self.setting_output_directory()
        files = self.get_paths_from_data_directory(data_dir)
        org_images = self.get_images(files)  
        org_filenames = self.get_filenames(files)
        org_widths, org_heights, org_n_channels  = self.get_image_info(org_images)

        org_images_df = self.get_dataframe(filenames = org_filenames,
                                width = org_widths,
                                height = org_heights,
                                n_channels = org_n_channels)

        org_images_df.to_csv('org_data.csv') 

        new_images, new_file_names = self.split_image(files)
        new_widths, new_heights, new_n_channels  = self.get_image_info(new_images)

        new_images_df = self.get_dataframe(filenames = new_file_names,
                                width = new_widths,
                                height = new_heights,
                                n_channels = new_n_channels)

        new_images_df.to_csv('new_data.csv') 

    # Defining function for setting directory for the raw data
    def setting_data_directory(self):

        root_dir = Path.cwd()  # Setting root directory

        data_dir = root_dir / 'W1-Visual-Image-Processing' / 'data' / 'images' # Setting data directory

        return data_dir

    # Defining function for setting directory for the raw data
    def setting_output_directory(self):

        root_dir = Path.cwd()  # Setting root directory

        out_dir = root_dir / 'W1-Visual-Image-Processing' / 'data' / 'new_images' # Setting data directory

        return out_dir

    # Defining function for obtaining individual filepaths for data files
    def get_paths_from_data_directory(self, data_dir):
        '''
        Creates a list containing paths to filenames in a data directory
        Args:
            data_dir: Path to the data directory.
        Returns:
            files (list): List of individual image file paths
        '''
        files = [] # Creating empty list

        # Loop for iterating through all images in the directory and append individual file paths to the empty list files
        for file in data_dir.glob('*.png'): 
            files.append(file)

        return files


    # Defining function for obtaining filenames from the filepaths
    def get_filenames(self, files):
        '''
        Creates a list of filenames in a directory.
        Args:
            files (list): List of file paths
        Returns:
            filename: list of filenames
        '''

        filenames = []  # Creating empty list


        # Loop for iterating through the different files
        for file in files:

            individual_file_name = os.path.split(file)[-1]  # Extracting last chunk of the splitted filepath as the individual filenames

            filenames.append(individual_file_name)  # Append each filename to the list

        return filenames

    
        # Defining function for obtaining individual filepaths for data files
    def get_images(self, files):
        '''
        Creates a list containing images
        Args:
            data_dir: Path to the data directory.
        Returns:
            images (list): List of individual images
        '''

        images = []

        for file in files:
            image = cv2.imread(str(file))
            images.append(image)

        return images


    def split_image(self, files):
        
        new_images = []
        new_file_names = []

        for image in files:
            image = cv2.imread(str(image))
            image_file_name = os.path.split(image)[-1]
            width, height = image.shape[0], image.shape[1]

            top_right = image[0 : height // 2, width // 2 : width]
            new_images.append(top_right)
            cv2.imwrite(f"{out_dir}/{image_file_name}_top_right.jpg", top_right)
            new_file_names.append(f"{image_file_name}_top_right.jpg")

            top_left = image[0 : height // 2, 0 : width // 2]
            new_images.append(top_left)
            cv2.imwrite(f"{out_dir}/{image_file_name}_top_left.jpg", top_left)
            new_file_names.append(f"{image_file_name}_top_left.jpg")

            bot_right = image[height // 2 : height // 2, width // 2 : width]
            new_images.append(bot_right)
            cv2.imwrite(f"{out_dir}/{image_file_name}_bot_right.jpg", bot_right)
            new_file_names.append(f"{image_file_name}_bot_right.jpg")

            bot_left = image[height // 2 : height, 0: width // 2]
            new_images.append(bot_left)
            cv2.imwrite(f"{out_dir}/{image_file_name}_bot_left.jpg", bot_left)
            new_file_names.append(f"{image_file_name}_bot_left.jpg")
        
        return new_images, new_file_names


     
    def get_image_info(self, images):
        all_widths = []
        all_heights = []
        all_n_channels = []

        for image in images:
            width, height, n_channels = image.shape[0], image.shape[1], image.shape[2]
            all_widths.append(width)
            all_heights.append(height)
            all_n_channels.append(n_channels)
        
        return all_widths, all_heights, all_n_channels

              
    
        # Defining short function for creating a pd data frame 
    def get_dataframe(self, filenames, width, height, n_channels):
        '''
        Gets the total number of words from all the files
        Args:
            filenames (list): list of filenames
            total_words (list): List of total words per file in the input list
            unique_words (list): List of number of unique words per file in the input list

        Returns:
            df (pd data frame): pd data frame containing all the cleaned data
        '''

        # Initialising a pd data frame with the required columns and adding the data generated by former functions to these collumns 
        df = pd.DataFrame(data= {'filename': filenames, 'width': width, 'height': height, 'n_channels': n_channels})

        return df

# Executing main function when script is run
if __name__ == '__main__':
    main()