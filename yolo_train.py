import os
import json
import pandas as pd
import numpy as np
from PIL import Image
from tqdm import tqdm
from ultralytics import YOLO
import torch

# Load the model.
model = YOLO('config/yolo11m_biformer.yaml') 
model.load('ckpt/yolo11m.pt')

# Training.
results = model.train(
    data='data/yolo/dataset.yaml',  # .yaml file 
    imgsz=640, # image size
    epochs=100,  # epoch number
    batch=16, # batch size , I normally use 8 or 16 but my GPU gave memory errors, therefore I reduced it to 4 for this time.
    name='yolo11m_biformer', # output folder name, it contains model weights and all of the other things.
    plots=True, # Plots about metrics (precision, recall,f1 score)
    amp=False, # amp=True gives me an error, I don't know why , If it doesn't give you an error, set it to True
    close_mosaic=50,
    single_cls=True,
    cls=0.1,
    box=10,

)
