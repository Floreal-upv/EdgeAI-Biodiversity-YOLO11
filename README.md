
The dataset has been prepared using images and videos obtained from camera traps. Since the images extracted from each video are very similar, they are all placed into the same fold, where applicable, into the test folder. A directory structure and a set of YAML files have been created to facilitate the training and validation of YOLO11n, employing a 3-fold cross-validation approach.


The `weights` directory contains the weights after training for 5 epochs.

`/itera_1` contains the `last.pt` file obtained using `itera_1.yaml`.

`/itera_2` contains the `last.pt` file obtained using `itera_2.yaml`.
`/itera_3` contains the `last.pt` file obtained using `itera_3.yaml`.

For weight freezing, only iteration 1 was used, with training performed for 5 epochs:

`/freeze11` contains the `last.pt` file obtained using `itera_1.yaml`, with the first 11 layers of the model frozen.

`/freeze23` contains the `last.pt` file obtained using `itera_1.yaml`, with the first 23 layers of the model frozen.

"/relay10 contains the `last.pt` file obtained using `/raplay10/dataset.yaml`, wint the 10 % of COCO 2017 classes cat, dog, bear, cow




