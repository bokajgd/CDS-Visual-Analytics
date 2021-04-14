# W11 - Classifying Paintings with a CNN

# Overview 

**Jakob Grøhn Damgaard, March 2021** <br/>
This repository contains the W11 assigmnent for the course *Visual Analytics*

# Code
The code to execute the task can be found in the file *cnn_artists.py*<br/>

# Data
The data files are too large to push to github and should dowloaded locally for Kaggle. Please place the downloaded data in a folder called *data* located in the project home directory  <br/>
The script generates a classification report and an *.png* image of the fully conected part of the network. These are located in the output folder (I've included outputs from  a test run).
<br>

# Download and Execute
To locally download a compressed zip version of this repository, one can zip the entire repository from GitHub by navigating back to the home page of the repository and clicking the *Code* button and then *Download ZIP*. <br/>
<br>
Before executing the .py file, open the terminal, navigate the directory to the folder directory and run the following code to install the requirements list in the *requirements.txt* file in a virtual environment:
<br>
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
deactivate
```

You can then proceed to run the script in the terminal by running the following line: 

```bash
python cnn_artists.py 
```
I hope everything works! 

# License
Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

