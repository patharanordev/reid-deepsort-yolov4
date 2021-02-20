import pandas as pd

class Recorder():
    def __init__(self):
        self.data = {}

    def record(self, object_id, class_name, img):
        self.data[f'{class_name}-{object_id}'] = [object_id, class_name]

    def export(self, fpath):
        df = pd.DataFrame(self.data)
        print(df.T.head())
        df.T.to_csv(fpath)