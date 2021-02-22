# W3 - Image Histogram Comparisons

# Overview 

**Jakob Grøhn Damgaard, Feburary 2021** <br/>
This repository contains the W3 assigmnent for the course *Visual Analytics*

# Code
The code to execute the tasks can be found in the file *W3-Histogram-Comparison.py*<br/>

# Data
The raw data files are located in *data* > *jpg* <br/>
The script generates a *.csv* file on the bassis of a specified target image containing two columns:
<br>
- **filename:** The name of the given comparison images.
- **distance:** The chi-square distances between the histograms of the target image and the given comparison image. Small values reveal that two images are alike.

# Download and Execute
To locally download a compressed zip version of this repository, one can zip the entire repository from GitHub by navigating back to the home page of the repository and clicking the *Code* button and then *Download ZIP*. <br/>
<br>
Before executing the .py file, open the terminal, navigate the directory to the folder directory and run the following code to install the requirements list in the *requirements.txt* file:
<br>
```bash
pip install -r requirements.txt
```
<br>
It is highly recommended that one creates a virtual environment for the folder before installing the requirements and running the script.

# License
Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

