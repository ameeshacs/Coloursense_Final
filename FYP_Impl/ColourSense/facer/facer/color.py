import colour
import numpy as np

rgb = np.array([255, 0, 0]) / 255.0 

munsell = colour.notation.RGB_to_Munsell(rgb, illuminant='D65', method='McCamy')

print(munsell)  # MunsellSpecification(hue=..., value=..., chroma=...)