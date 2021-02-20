import pandas as pd
import cv2
class Recorder():
    def __init__(self):
        self.data = {}

    def record(self, object_id, class_name, img):
        # Save image if it is the first look
        if not (f'{class_name}-{object_id}' in self.data):
            cv2.imwrite(f'../cropped/{class_name}-{object_id}.jpg', img)

        # Record to dict
        self.data[f'{class_name}-{object_id}'] = [object_id, class_name]

    def export(self, fpath):
        df = pd.DataFrame(self.data)
        print(df.T.head())
        df.T.to_csv(fpath)