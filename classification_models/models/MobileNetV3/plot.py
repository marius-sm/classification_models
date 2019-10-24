from mobilenet_v3_small import MobileNetV3_Small

model = MobileNetV3_Small(shape=(256,256,3), include_top=False).build(plot=True)