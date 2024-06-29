# SynScene: Synthetic Dataset for Natural Scene Text Recognition
Welcome to the SynScene Git repository! This project contains the Python code for generating a synthetic dataset designed for natural scene text recognition tasks. The SynScene dataset includes approximately 1.5 million synthetic images and 21477 natural images, that  all featuring text in the Persian language.

![سین](https://github.com/mmtalaie/SynScene/blob/main/SampleImage/23753.jpg?raw=true)
![سین](https://github.com/mmtalaie/SynScene/blob/main/SampleImage/23816.jpg?raw=true)
## Overview
Natural scene text recognition is a crucial task in the field of computer vision, with applications ranging from automated reading systems to enhancing accessibility. The SynScene dataset aims to provide a robust and diverse set of synthetic images to facilitate research and development in this area, particularly focusing on the Persian language.

## Dataset Details
* **Text Sources**: The text used in the dataset is derived from the Tabnak dataset, random Iranian phone numbers, and incremental numbers.

* **Backgrounds**: Images feature backgrounds from the [OpenImage dataset](https://storage.googleapis.com/openimages/web/index.html) or colored backgrounds, ensuring a variety of contexts and scenes.

* **Image Variations**: The dataset incorporates various random noise and transformations, including:
* Salt and Pepper noise
* Rotation
* Shearing
* Piecewise Affine transformation
* CLAHE (Contrast Limited Adaptive Histogram Equalization)
* Perspective Transform
* Blur

* **Color Format**: All images are stored in RGB format.

## Features
* **Persian Language Text**: All images in the SynScene dataset feature text in the Persian language, catering to specific linguistic research needs.
* **

## Repository Contents

* **Data Generation Scripts**: Python scripts used to generate the SynScene dataset, allowing for customization and further expansion.
* **Sample Images**: A subset of sample images from the SynScene dataset to provide an overview of the dataset's content and quality.
* **Documentation**: Comprehensive documentation detailing the data generation process, usage instructions, and dataset specifications.

## Download Links:
* You can download the 1.5 million dataset (except numbers an phone number) in image format from the following links:


    [Part 1](https://terabox.com/s/1-YI4uhS-ShS9i3H8sD8Y3w)

    [Part 2](https://terabox.com/s/1Iw0qlOU5xTmS2dv6dcNcUQ)

    [Part 3](https://terabox.com/s/1oy_oHwEyTLuTHAgUP9Q2GQ)

    [Part 4](https://terabox.com/s/1kezyFVGEUnKrJokcAlsNDQ)

    [Part 5](https://terabox.com/s/1gE6HYrI9eytKwP4ewtUOOA)

    
* You can download natuar dataset in LMDB database from the following list.

    [Natural Dataset](https://terabox.com/s/1ipPX0t9eP-RYSh1yvEE3aw)

    

## Contributing
We welcome contributions to enhance the SynScene dataset and its associated tools.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
We thank all contributors and collaborators who helped in the creation and validation of the SynScene dataset.

# Getting Started

To get started with the SynScene dataset and the associated data generation scripts, please refer to the Installation Guide and Usage Instructions.
## Read Dataset
To read lmdb dataset you can use ```ReadDAta.py``` to read lmdb dataset.

## Create Your Own Dataset

To create your own dataset you have prepare the requirements that discribe in bellow:

1. Put the tokenized text file inside ```text``` directory
2. Put background images [if needed] inside ```UnusedImage``` directory
3. Put fonts in the ```font``` directory
4. run the following command:
    
    ```python3 /home/mmt/myThesis/CreateDataSet/CreateDatasetMultiRunning.py --corpus_address ./text/textFile.txt --image_background --noise random```
    * You can run this command in multiple bash simultantly by different text file to speed up dataset creation by parallel generation.