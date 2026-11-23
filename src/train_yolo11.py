from  ultralytics import YOLO


model = YOLO("yolo11n.pt")


results = model.train(data="/home/facebron/cross_val_gatos/itera_1.yaml",epochs=5,plots=True)
#results = model.train(data="/home/facebron/cross_val_gatos/itera_2.yaml",epochs=5,plots=True)
#results = model.train(data="/home/facebron/cross_val_gatos/itera_3.yaml",epochs=5,plots=True)

