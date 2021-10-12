import cv2
import numpy as np
import matplotlib.image as mpimg

def hist(img):
    bottom_half = img[img.shape[0]//2:,:]
     return np.sum(bottom_half, axis=0)
   
class LaneLinePixels:
  """ Class containing information about detected lane lines.
  Attributes:
      left_fit (np.array): Coefficients of a polynomial that fit left lane line
      right_fit (np.array): Coefficients of a polynomial that fit right lane line
      parameters (dict): Dictionary containing all parameters needed for the pipeline
      debug (boolean): Flag for debug/normal mode
  """
  def __init__(self):
      self.left_fit = None
      self.right_fit = None
      self.binary = None
      self.nonzero = None
      self.nonzerox = None
      self.nonzeroy = None
      self.clear_visibility = True
      self.dir = []

       # HYPERPARAMETERS
      # Number of sliding windows
      self.nwindows = 9
      # Width of the the windows +/- margin
      self.margin = 100
      # Mininum number of pixels found to recenter window
      self.minpix = 50
      
  def lane_lines(self, img):
      """ Take an image and detect lane lines.
      """
