from mobilenet_v3_large import MobileNetV3_Large

model = MobileNetV3_Large(shape=(256,256,3), include_top=False).build(plot=True)