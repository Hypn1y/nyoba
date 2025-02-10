import streamlit as st
import pandas as pd
import cv2
import numpy as np
import os
from datetime import datetime
import base64

PHOTO_DIR = "photos"
os.makedirs(PHOTO_DIR,exist_ok=true)

DATA_FILE = "buku_tamu.csv"
