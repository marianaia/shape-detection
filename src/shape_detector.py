import cv2 as cv

class ShapeDetector:
    @staticmethod
    def preprocess_image(image, blur_ksize=(5, 5), canny_thresh1=50, canny_thresh2=150):
        """Convert image to grayscale, blur it, and apply Canny edge detection."""
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        blurred = cv.GaussianBlur(gray, blur_ksize, 0)
        edged = cv.Canny(blurred, canny_thresh1, canny_thresh2)
        return edged

    @staticmethod
    def detect_shapes(image):
        """Detect shapes in an image."""
        edged = ShapeDetector.preprocess_image(image)
        contours, _ = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        shapes = []

        for contour in contours:
            epsilon = 0.04 * cv.arcLength(contour, True)
            approx = cv.approxPolyDP(contour, epsilon, True)
            x, y, w, h = cv.boundingRect(approx)
            
            if len(approx) == 3:
                shape_name = "Triangle"
            elif len(approx) == 4:
                aspect_ratio = w / float(h)
                shape_name = "Square" if 0.95 <= aspect_ratio <= 1.05 else "Rectangle"
            elif len(approx) == 5:
                shape_name = "Pentagon"
            else:
                shape_name = "Circle"
            
            shapes.append((approx, shape_name, (x, y)))
        
        return shapes
