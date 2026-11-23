from  ultralytics import YOLO

model = YOLO("runs/detect/train36/weights/last.pt")


results = model.val(data="coco.yaml",plots=True)

