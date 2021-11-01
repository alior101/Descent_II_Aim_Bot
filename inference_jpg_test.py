import torch

# Model
#model = torch.hub.load('ultralytics/yolov5', 'best', pretrained=True)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='./best.pt')  # default

# Images
imgs = ['./d2.jpg']  # batch of images

# Inference
results = model(imgs)

# Results
results.print()
results.save()  # or .show()
results.show()

results.xyxy[0]  # img1 predictions (tensor)
results.pandas().xyxy[0]  # img1 predictions (pandas)
