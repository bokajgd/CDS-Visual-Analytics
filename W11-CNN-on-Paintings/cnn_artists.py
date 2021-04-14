# Classifying impressionist paintings by painter

# Import packages
import numpy as np # Matrix maths
import tensorflow as tf # NN functions
import matplotlib.pyplot as plt # For drawing graph
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import classification_report
import keras

from pathlib import Path

# Import utility functions definied in utils.py
from utils.utils import draw_neural_net

# Defining main function
def main():
    
    # Instantiate class
    cnn = CNNonPaintings()

    cnn.preprocess_data()  # Preproces data
    cnn.build_model(n_layers = 2, n_nodes = [32,16]) # Build model  
    cnn.train_and_evaluate() # Train and evaluate model
    cnn.visualise_network(n_layers = 2, n_nodes = [32,16]) # Create visualisation

# Defining class
class CNNonPaintings:
    def __init__(self):
        return


    def preprocess_data(self):
        # Setting model output directory 
        self.model_out_dir = Path.cwd() / 'W11-CNN-on-Paintings' / 'output' 

        # Setting model data directory 
        self.model_data_dir = Path.cwd() / 'W11-CNN-on-Paintings' / 'data' 


        self.train_data = tf.keras.preprocessing.image_dataset_from_directory(self.model_data_dir / 'training',
                                                                            image_size=(64, 64),
                                                                            batch_size=32)

        self.val_data = tf.keras.preprocessing.image_dataset_from_directory(self.model_data_dir / 'validation',
                                                                          image_size=(64, 64),
                                                                          batch_size=32)

        # Preprocessing data for evaluation and classification report
        self.val_images = np.concatenate([images for images, labels in self.val_data], axis=0)

        self.val_labels = np.concatenate([labels for images, labels in self.val_data], axis=0)

        self.train_class_names = self.train_data.class_names

        self.val_class_names = self.val_data.class_names

        self.num_classes = len(self.train_class_names)


    # Defining cnn in a single function
    def build_model(self,n_layers, n_nodes):

        input_shape = (64, 64, 3)

        # Build the model
        self.model = keras.models.Sequential()
        self.model.add(keras.layers.experimental.preprocessing.Rescaling(1. / 255, input_shape=input_shape))
        self.model.add(keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu'))
        self.model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
        self.model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
        self.model.add(keras.layers.Dropout(0.25))
        self.model.add(keras.layers.Flatten())
        # Add dense layers with the dimensions according to input
        for layer in range(n_layers):
            self.model.add(keras.layers.Dense(n_nodes[layer], activation='relu'))
        self.model.add(keras.layers.Dense(self.num_classes, activation='softmax'))

        # Compile the layers into one model
        # Loss function and optimizer needed
        self.model.compile(
            optimizer = 'adam',
            loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), # This allows more than two classes
            metrics = ['accuracy']
        )

        print(self.model.summary())


    def train_and_evaluate(self):
        # Train the model
        self.model.fit(
            self.train_data,
            validation_data=self.val_data, 
            epochs = 4, # Number of iterations over the entire training dataset
        )

        # Saving evaluation metrics
        class_report_path = self.model_out_dir / "classification_report.txt"

        predictions = self.model.predict(self.val_images, batch_size=512)
        eval_report = classification_report(self.val_labels,
                                            predictions.argmax(axis=1),
                                            target_names=self.val_class_names)

        print(eval_report)
        class_report_path.write_text(eval_report)


    def visualise_network(self, n_layers, n_nodes):
        # Visualising network
        # Styling title
        title = {'family': 'serif',
                'color': '#4A5B65',
                'weight': 'normal',
                'size': 24,
                }

        network_structure = n_nodes + [10] # Creating full network structure by adding the dimension of the output layer
        fig = plt.figure(figsize=(7, 7)) # Creating figure
        ax = fig.gca()
        ax.axis('off')
        draw_neural_net(ax, .1, .9, .1, .9, network_structure) # Running visualisation function
        ax.set_title(f"{n_layers}-dense-{n_nodes}-nodes-CNN", fontdict = title, y = 0.9) # Setting unique titlie
        plt.savefig(self.model_out_dir / f"{n_layers}-dense-{n_nodes}-nodes-CNN-viz.png") # Saving figure
        plt.show()


# Executing main function when script is run
if __name__ == '__main__':   
    main()