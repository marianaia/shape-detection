import cv2 as cv

class ImageLoader:
    @staticmethod
    def load_image(image_path):
 
        image = cv.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Error: Unable to load image at path {image_path}.")
        return image

    @staticmethod
    def save_image(image, save_path):

        cv.imwrite(save_path, image)
        print(f"Image saved as {save_path}")
