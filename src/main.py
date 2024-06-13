import cv2 as cv
import os
from image_loader import ImageLoader
from shape_detector import ShapeDetector
from image_display import ImageDisplay
from image_processor import ImageProcessor


def main(image_path, save_path):
    
    """Main function to load image, detect shapes, classify and save the image."""
    try:
    
        image = ImageLoader.load_image(image_path)
        
        # Display the original image
        ImageDisplay.display_image("Original Image", image)
        
        # Detect shapes
        shapes = ShapeDetector.detect_shapes(image)
        
        # Classify with detected shapes
        annotated_image = ImageProcessor.annotate_image(image, shapes)
        
        ImageDisplay.display_image("Shapes Detected", annotated_image)
        
        ImageLoader.save_image(annotated_image, save_path)
    
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":

    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(os.path.dirname(current_dir), "images")
    image_path = os.path.join(image_dir, "test_image.png")
    save_path = os.path.join(image_dir, "modified_image.jpg")
    main(image_path, save_path)
