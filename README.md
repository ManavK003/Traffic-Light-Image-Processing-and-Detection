# Traffic-Light-Image-Processing-and-Detection

## Project Overview

The **Traffic Light Image Processing and Detection** project aims to create a robust traffic light detection system using image processing. This software is designed for integration into **autonomous vehicles (AVs)**, helping to enhance public safety and improve the driving capabilities of self-driving cars, particularly at intersections where traffic lights play a critical role.

As autonomous vehicles become more common, ensuring their safety, especially at high-risk locations like intersections, is vital. This project addresses this need by providing an efficient and reliable traffic light detection system that helps AVs recognize traffic signals in real-time.

## Problem Statement

With the increasing number of autonomous vehicles on the road, public safety has become a key priority. A large number of traffic-related injuries and fatalities occur near intersections. This project aims to solve the problem of detecting traffic lights in various conditions (e.g., different weather, day/night cycles) to improve the safety of autonomous vehicles at intersections.

## Goals and Objectives

- **Reliable Traffic Light Detection**: Develop an image processing algorithm that can consistently detect traffic lights under a range of conditions (e.g., day, night, varying weather).
- **Real-Time Processing**: The system should be able to process images and detect traffic lights in real-time so that autonomous vehicles can respond quickly.
- **Integration into AV Systems**: Ensure the software is compatible with autonomous vehicle control systems, helping to improve safety and performance at intersections.
- **Robust Functionality**: Handle edge cases like partial visibility, occlusions, or difficult lighting conditions with minimal errors.

## Key Features

- **Traffic Light Detection**: Identifies the presence and status (red, yellow, green) of traffic lights in images.
- **Spatial Image Processing**: Uses advanced techniques to differentiate between traffic lights and other objects in the scene.
- **Real-Time Operation**: Optimized for real-time processing to integrate seamlessly with AV systems.
- **Adaptability to Different Conditions**: The system can function effectively in various environmental conditions, such as low light, fog, or rain.

## Technologies Used

- **Python**: For image processing and detection logic.
- **OpenCV**: For real-time computer vision tasks.
- **TensorFlow** or **PyTorch (optional)**: For machine learning models to improve detection accuracy.
- **NumPy & Pandas**: For data handling and manipulation.
- **Matplotlib/Seaborn**: For visualizations (optional).
- **Git**: For version control.

## Installation Instructions

### Prerequisites

Make sure you have the following installed:

- **Python 3.x**
- **pip** (Python package installer)
- **Git** (for version control)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Traffic-Light-Image-Processing-and-Detection.git
   cd Traffic-Light-Image-Processing-and-Detection

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

3. Install the required dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

4. Run the Project:
    To test the project, run the detection script:
    ```bash
    pip install -r requirements.txt

## Usage

Once the project is set up, you can test the traffic light detection system. Here's how it works:

* **Webcam Input:** When you run the program, it connects to your webcam and starts processing the video feed.
* **Image or Video:** You can show the system an image or video containing traffic lights. The system will analyze the input and display the detected traffic light status (e.g., red, yellow, or green).

Example usage:

    ```bash
    python detect_traffic_lights.py --input images/test_image.jpg

This command will process the image located at images/test_image.jpg and display the detected traffic light status.

## Acknowledgements

* **Othman (2022):** For highlighting the importance of image processing in autonomous vehicle systems.
* **Cirincione (2023):** For their research on traffic-related fatalities and their correlation with intersections.

## References

1. Othman, S. (2022). *Image Processing for Autonomous Vehicles*. Journal of Computer Vision and Applications.
2. Cirincione, P. (2023). *Traffic Fatalities in the United States: The Role of Intersections*. Transportation Research Board.

