import cv2 as cv

class ImageProcessor:
    @staticmethod
    def annotate_image(image, shapes):

        for approx, shape_name, (x, y) in shapes:
            cv.drawContours(image, [approx], -1, (0, 255, 0), 2)
            cv.putText(image, shape_name, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        return image
