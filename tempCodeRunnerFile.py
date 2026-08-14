import cv2, sqlite3, os
from datetime import datetime
import face_recognition

known_encodings=[]