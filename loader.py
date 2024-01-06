import cv2
import numpy as np
import torchvision.transforms as transforms
import base64

# fanks chatgpt
def load_from_data_url(data_url):
    header, encoded = data_url.split(",", 1)
    data = base64.b64decode(encoded)
    img_array = np.frombuffer(data, dtype=np.uint8)
    transf = transforms.ToTensor()
    image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) if image.ndim == 3 else image
    return transf(image_rgb).permute(1, 2, 0).unsqueeze(0)