# Traffic-Light-Image-Processing-and-Detection

## Project Overview

**Traffic-Light-Image-Processing-and-Detection** is a computer vision project that detects and identifies traffic light signals—red, yellow, and green—from images or real-time video streams using Python and OpenCV. Designed with **autonomous vehicles (AVs)** in mind, the goal of this system is to improve public safety by enabling AVs to correctly interpret traffic lights in various environments and conditions.

This project processes visual data from either a webcam or uploaded media and applies color segmentation and machine learning techniques to identify the status of traffic lights. It’s a lightweight, modular system that can be extended for integration into self-driving car simulation platforms, robotics systems, or traffic surveillance applications.

## Problem Statement

With the increasing number of autonomous vehicles on the road, public safety has become a key priority. A large number of traffic-related injuries and fatalities occur near intersections. This project aims to solve the problem of detecting traffic lights in various conditions (e.g., different weather, day/night cycles) to improve the safety of autonomous vehicles at intersections.

## Technologies Used

- **Python**: For image processing and detection logic.
- **OpenCV**: For real-time computer vision tasks.
- **TensorFlow** or **PyTorch**: For machine learning models to improve detection accuracy.
- **NumPy & Pandas**: For data handling and manipulation.
- **Matplotlib/Seaborn**: For visualizations.
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

2. Install the required dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

3. Run the Project:
    To test the project, run the detection script:
    ```bash
    pip install -r requirements.txt

## Usage

Once the project is set up, there's two ways you can test the traffic light detection system. Here's how it works:

* **Webcam Input:** When you run the program, it connects to your webcam and starts processing the video feed.
* **Image or Video:** You can show the system an image or video containing traffic lights. The system will analyze the input and display the detected traffic light status (e.g., red, yellow, or green).

Example usage:

    ```bash
    python detect_traffic_lights.py --input images/test_image.jpg

This command will process the image located at images/test_image.jpg and display the detected traffic light status.

## Acknowledgements and References

1. Othman, S. (2022). *Image Processing for Autonomous Vehicles*. Journal of Computer Vision and Applications.
2. Cirincione, P. (2023). *Traffic Fatalities in the United States: The Role of Intersections*. Transportation Research Board.

