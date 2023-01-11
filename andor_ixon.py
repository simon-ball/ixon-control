
import time
from tqdm import tqdm
from PIL import Image

import pylablib as pll
pll.par["devices/dlls/andor_sdk2"] = "C:/Program Files/Andor Driver Pack 2"
from pylablib.devices import Andor

"""
Pylablib Andor documentation:
pylablib.readthedocs.io/en/stable/.apidoc/pylablib.devices.Andor.html
"""


ixon = Andor.AndorSDK2Camera(fan_mode="low", amp_mode=None)
print("connecting to camera")


print("configuring imaging parameters")
ixon.set_exposure(80e-3)      # duration in seconds
#ixon.set_roi(0, 128, 0, 128)  # ROI in upper left

print("Configuring Shutter")
ixon.setup_shutter(mode="open")

print("Collecting images")
images = ixon.grab(2)         # take 2 images
ixon.setup_shutter(mode="closed")

print("Saving images")
for i, _ in enumerate(images):
    img = Image.fromarray(images[i])
    img.save(f"test_img_{i}.png")

print(images[0])

print("Closing connection")
ixon.set_cooler(on=False)
ixon.close()