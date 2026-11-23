
from  ultralytics import YOLO


model = YOLO("/home/facebron/Model_YOLO/runs/detect/train-46/weights/last.pt")



results = model.val(data="/home/facebron/cross_val_gatos/itera_1.yaml",split="test",plots=True)
#results = model.val(data="/home/facebron/cross_val_gatos/itera_2.yaml",split="test",plots=True)
#results = model.val(data="/home/facebron/cross_val_gatos/itera_3.yaml",split="test",plots=True)

