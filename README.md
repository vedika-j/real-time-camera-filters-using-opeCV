# real-time-camera-filters-using-opeCV
Real-Time Webcam Filter Application 🎥✨

This project demonstrates a real-time webcam filter application using OpenCV. It allows users to apply various image processing filters dynamically via interactive trackbars.

Key Features 🌟

Dynamic Filters:
Original video feed
Grayscale
Gaussian Blur
Canny Edge Detection
Sobel Edge Detection
Laplacian Edge Detection
Binary Thresholding
Interactive Controls:
Filter Selection: Switch between filters using a trackbar.
Parameter Adjustment: Modify parameters (e.g., blur kernel size, thresholds) in real time.
Real-Time Processing:
Processes and displays the webcam feed with minimal latency.

How It Works ⚙️
The application uses the OpenCV VideoCapture feature to access the webcam.
Filters are selected via the "Filter" trackbar, and their parameters can be fine-tuned using additional trackbars:
Blur Kernel Size: Adjusts the Gaussian blur intensity.
Canny Thresholds: Fine-tunes the edge detection sensitivity.
Threshold Value: Controls binary thresholding output.
The processed frames are displayed live in an OpenCV window.



Trackbars:
Filter: Select the desired filter (0 for original, 1-6 for different filters).
Blur Kernel Size: Adjust the size of the kernel for Gaussian Blur.
Canny Lower/Upper: Define the thresholds for Canny Edge Detection.
Threshold: Adjust the binary threshold value.
Keyboard:
Press 'q' to quit the application.
Filters Explained 📸

Original Video: Displays the unprocessed webcam feed.
Grayscale: Converts the video feed to grayscale.
Gaussian Blur: Applies a blur effect to reduce noise.
Canny Edge Detection: Highlights edges using the Canny algorithm.
Sobel Edge Detection: Detects gradients in the X and Y directions.
Laplacian Edge Detection: Detects edges using the Laplacian operator.
Binary Thresholding: Converts the image to black and white based on intensity.
