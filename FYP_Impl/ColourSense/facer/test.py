import numpy as np
import unittest
from functions import get_rgb_codes, calc_dis
from skin_model import get_season
import functions as f
import skin_model as m

class TestFunctions(unittest.TestCase):
    def test_get_rgb_codes(self):
        # Define input image path for testing
        test_image_path = "C:/Users/ASUS/OneDrive/Desktop/FinalYear/FYP/FYP_Impl/ColourSense/facer/image.jpg"

        # Call the function under test
        rgb_codes = get_rgb_codes(test_image_path)

        # Print the result of get_rgb_codes
        print("Result of get_rgb_codes:", rgb_codes)

        # Assert that the output is of the expected type
        self.assertIsInstance(rgb_codes, np.ndarray)

        # Test the calc_dis function with the output of get_rgb_codes
        skin_types = calc_dis(rgb_codes)
        print("Result of colour type:", skin_types)

        # Test the get_season function with the input image
        f.save_skin_mask(test_image_path)
        ans = m.get_season("temp.jpg")
        if ans == 3:
            ans += 1
        elif ans == 0:
            ans = 3
        # Print the result of the season
        #If result is 1, then the season is Spring
        #If result is 2, then the season is Summer
        #If result is 3, then the season is Autumn
        #If result is 4, then the season is Winter
        if ans == 1:
            print("Result of season: Summer")
        elif ans == 2:
            print("Result of season: Autumn")
        elif ans == 3:
            print("Result of season: Spring")
        elif ans == 4:
            print("Result of season: Winter")


if __name__ == "__main__":
    unittest.main()

