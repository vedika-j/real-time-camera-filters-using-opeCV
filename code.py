import cv2
import numpy as np

def nothing(x):
    """A placeholder function for trackbar."""
    pass

# Initialize webcam
cap = cv2.VideoCapture(0)  # Use 0 for default camera
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Create a window and trackbars for filter parameters
cv2.namedWindow("Filters")
cv2.createTrackbar("Filter", "Filters", 0, 6, nothing)  # Switch between filters
cv2.createTrackbar("Blur Kernel Size", "Filters", 5, 30, nothing)  # Gaussian Blur
cv2.createTrackbar("Canny Lower", "Filters", 50, 255, nothing)  # Canny lower threshold
cv2.createTrackbar("Canny Upper", "Filters", 150, 255, nothing)  # Canny upper threshold
cv2.createTrackbar("Threshold", "Filters", 128, 255, nothing)  # Threshold for binary image

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Resize frame for better visualization
    frame = cv2.resize(frame, (800, 600))

    # Get the selected filter from the trackbar
    filter_type = cv2.getTrackbarPos("Filter", "Filters")
    blur_ksize = cv2.getTrackbarPos("Blur Kernel Size", "Filters")
    lower_thresh = cv2.getTrackbarPos("Canny Lower", "Filters")
    upper_thresh = cv2.getTrackbarPos("Canny Upper", "Filters")
    threshold_value = cv2.getTrackbarPos("Threshold", "Filters")

    # Ensure blur kernel size is odd and at least 1
    blur_ksize = max(1, blur_ksize)
    if blur_ksize % 2 == 0:
        blur_ksize += 1

    # Apply filters based on the selected option
    if filter_type == 0:  # Original Video
        output = frame

    elif filter_type == 1:  # Grayscale
        output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    elif filter_type == 2:  # Gaussian Blur
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        output = cv2.GaussianBlur(gray, (blur_ksize, blur_ksize), 0)

    elif filter_type == 3:  # Canny Edge Detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (blur_ksize, blur_ksize), 0)
        output = cv2.Canny(blurred, lower_thresh, upper_thresh)

    elif filter_type == 4:  # Sobel Edge Detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)  # Gradient in X
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)  # Gradient in Y
        output = cv2.magnitude(sobelx, sobely)  # Combine gradients
        output = cv2.convertScaleAbs(output)  # Convert to 8-bit

    elif filter_type == 5:  # Laplacian Edge Detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        laplacian = cv2.Laplacian(gray, cv2.CV_64F)
        output = cv2.convertScaleAbs(laplacian)

    elif filter_type == 6:  # Binary Thresholding
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, output = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

    # Display the selected filter
    if filter_type == 0:
        cv2.imshow("Filters", output)
    else:
        cv2.imshow("Filters", cv2.cvtColor(output, cv2.COLOR_GRAY2BGR))  # Convert to BGR for consistency

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
