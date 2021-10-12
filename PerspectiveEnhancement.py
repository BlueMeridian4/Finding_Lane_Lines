import cv2
import numpy as np

class PerspectiveEnhancement:
    """ This is class to hold functions that transform an image from front view to top-down view.
    
    Attributes:
      src (np.array): Coordinates of 4 source points
      dst (np.array): Coordinates of 4 source points
      M (np.array): Matrix to transform image from front to top-down view
      M_inv (np.array): Matrix to transform image from top-down to front view
    """
    
    def __init__(self):
        """Init PerspectiveEnhancement."""
        self.src = np.float32([(550, 460),  # top-left
                               (150, 720),  # bottom-left
                               (1200, 720), # bottom-right
                               (770, 460)]) # top-right
        self.dst = np.float32([(100, 0),
                               (100, 720),
                               (1100, 720),
                               (1100, 0)])
        self.M = cv2.getPerspectiveTransform(self.src, self.dst)
        self.M_inv = cv2.getPerspectiveTransform(self.dst, self.src)
        
    
    def top_down_view(self, img, img_size=(1280, 720), flags=cv2.INTER_LINEAR):
        """ Take a front view image and transform to top view
        Inputs:
            img (np.array): Image with front view perspective
            img_size (tuple): Size of the image (width, height)
            flags : flag to use in cv2.warpPerspective()
        Returns:
            img (np.array): Image with top-down view perspective
        """
        return cv2.warpPerspective(img, self.M, img_size, flags=flags)

    def front_view(self, img, img_size=(1280, 720), flags=cv2.INTER_LINEAR):
        """ Take a top view image and transform it to front view
        Inputs:
            img (np.array): Image with top-down view perspective
            img_size (tuple): Size of the image (width, height)
            flags (int): flag to use in cv2.warpPerspective()
        Returns:
            img (np.array): Image with front view perspective
        """
        return cv2.warpPerspective(img, self.M_inv, img_size, flags=flags)
