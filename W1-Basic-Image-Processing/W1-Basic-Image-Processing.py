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

# Setting class 'CountFunctions'
class ImageProcessing:
    def __init__(self):
        data_dir, root_dir = self.setting_data_directory() # Setting data directory and root directory 
        out_dir = self.setting_output_directory() # Setting output directory for the generated images
        files = self.get_paths_from_data_directory(data_dir) # Getting list of filepaths for the images
        
        org_images = self.get_images(files) # Reading images and geeting list of all the images 
        org_filenames = self.get_filenames(files) # Getting list of filepaths
        org_widths, org_heights, org_n_channels  = self.get_image_info(org_images) # Getting lists of image information

        # Generating .csv file the original images
        org_images_df = self.get_dataframe(filenames = org_filenames,
                                width = org_widths,
                                height = org_heights,
                                n_channels = org_n_channels)

        # Writing csv file to folder
        org_images_df.to_csv(f'{root_dir}/org_data.csv') 

        new_images, new_file_names = self.split_image(files, out_dir) # Splitting images and saving them as .jpg files in 'new_images' folder
        new_widths, new_heights, new_n_channels  = self.get_image_info(new_images) # Getting information on the split images

        # Generating .csv file the original images
        new_images_df = self.get_dataframe(filenames = new_file_names,
                                width = new_widths,
                                height = new_heights,
                                n_channels = new_n_channels)

        # Writing csv file to folder
        new_images_df.to_csv(f'{root_dir}/new_data.csv') 
        
        print(Path.cwd())

    # Defining function for setting directory for the raw data
    def setting_data_directory(self):

        root_dir = Path.cwd()  # Setting root directory

        data_dir = root_dir / 'data' / 'images' # Setting data directory

        return data_dir, root_dir

    # Defining function for setting directory for the raw data
    def setting_output_directory(self):

        root_dir = Path.cwd()  # Setting root directory

        out_dir = root_dir / 'data' / 'new_images' # Setting data directory

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
            filenames: list of filenames
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
            files (list): List of file paths
        Returns:
            images (list): List of individual images
        '''
        
        # Empty list
        images = []

        # Looping through paths, reading images and appending to list
        for file in files:
            image = cv2.imread(str(file))
            images.append(image)

        return images


    # Defining function for splitting images and saving them as .jpg files
    def split_image(self, files, out_dir):
        '''
        Creates new split images with new file names and saves them as .jpg files
        Args:
            files (list): List of file paths
        Returns:
            new_images (list): List of split images
            new_file_names (list): List of file names for new split images

        '''

        # Creating empty lists
        new_images = []
        new_file_names = []
            
        # Loops throug paths
        for file in files:
            image = cv2.imread(str(file)) # Reads image
            image_file_name = str(os.path.split(file)[-1]).replace('.png', '') # Gets filename 
            width, height = image.shape[0], image.shape[1] # Gets dimensions

            top_right = image[0 : height // 2, width // 2 : width] # Subsets one quarter of images
            new_images.append(top_right) # Appends to list of new images 
            cv2.imwrite(f"{out_dir}/{image_file_name}_top_right.jpg", top_right) # Writes as .jpg files
            new_file_names.append(f"{image_file_name}_top_right.jpg") # Adds new filename to list

            top_left = image[0 : height // 2, 0 : width // 2]
            new_images.append(top_left)
            cv2.imwrite(f"{out_dir}/{image_file_name}_top_left.jpg", top_left)
            new_file_names.append(f"{image_file_name}_top_left.jpg")

            bot_right = image[height // 2 : height, width // 2 : width]
            new_images.append(bot_right)
            cv2.imwrite(f"{out_dir}/{image_file_name}_bot_right.jpg", bot_right)
            new_file_names.append(f"{image_file_name}_bot_right.jpg")

            bot_left = image[height // 2 : height, 0: width // 2]
            new_images.append(bot_left)
            cv2.imwrite(f"{out_dir}/{image_file_name}_bot_left.jpg", bot_left)
            new_file_names.append(f"{image_file_name}_bot_left.jpg")
        
        return new_images, new_file_names


    # Defining function for getting information on a list of images        '
    def get_image_info(self, images):    
        '''
        Creates a lists of relevant information 
        Args:
            images (list): List of read, individual images
        Returns:
            all_widths (list): List of image widhts
            all_heights (list): List of image heights
            all_n_channels (list): List of image n_channels
        '''
        all_widths = []
        all_heights = []
        all_n_channels = []

        # Loops through all iamges
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
            all_widths (list): List of image widhts
            all_heights (list): List of image heights
            all_n_channels (list): List of image n_channels

        Returns:
            df (pd data frame): pd data frame containing all the cleaned data
        '''

        # Initialising a pd data frame with the required columns and adding the data generated by former functions to these collumns 
        df = pd.DataFrame(data= {'filename': filenames, 'width': width, 'height': height, 'n_channels': n_channels})

        return df

# Executing main function when script is run
if __name__ == '__main__':
    main()