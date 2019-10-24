import keras
from mobilenet_v3_small import MobileNetV3_Small

input_tensor = keras.layers.Input(shape=(256, 256, 3))
print(input_tensor.shape)
model = MobileNetV3_Small(shape=(None,None,3), include_top=False).build(plot=True)