# Shape detection and classification

The Shape detection and classification project is using image processing techniques to identify and label shapes ( triangles, rectangles and circles). The result is the modified image with shape classification. The Canny edge detection algorithm is used to identify edges in the image. Classification is made based on the number of vertices and aspect ratio between squares and rectangles.

## Requirements

- Python 3.x
- OpenCV

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/marianaia/shape-detection
   cd shape-detection/src
   ```

2. **Install the required packages:**
   ```sh
   pip install opencv-python
   ```

## Usage

1. **Prepare your image:**

   - Place the image you want to process in a images directory.

2. **Modify paths in `main.py`:**

   - Update `image_path` and `save_path` with the appropriate paths for your input and output images.

3. **Run the script:**

   ```sh
   python main.py
   ```

   This will:

   - Load the specified image.
   - Display the original image.
   - Detect shapes within the image.
   - Annotate the image with the detected shapes and their names.
   - Display the annotated image.
   - Save the annotated image to the specified path.
