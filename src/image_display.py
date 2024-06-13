import cv2 as cv

class ImageDisplay:
    @staticmethod
    def display_image(window_name, image):
  
        cv.imshow(window_name, image)
        cv.waitKey(0)
        cv.destroyAllWindows()
