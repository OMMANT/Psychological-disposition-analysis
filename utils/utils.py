import os
import numpy as np
import pandas as pd
from pathlib import Path
from urllib.request import urlopen
from datetime import datetime


sample_submission_url = 'https://bit.ly/3lfysox'
test_x_url = 'https://bit.ly/3imZrMN'
train_url = 'https://bit.ly/2SlBPhh'

csvs = ['sample_submission.csv', 'test_x.csv', 'train.csv']
urls = [sample_submission_url, test_x_url, train_url]

cwd = Path(os.getcwd())
res_path = cwd / 'res'
csv_path = cwd / 'csvs'


def check_res():
    print('Checking data files')
    res_path = cwd / 'res'
    if not res_path.exists():
        os.mkdir(res_path)
        for idx, url in enumerate(urls):
            file = urlopen(url)
            file_data = file.read()
            with open(res_path / f'{csvs[idx]}', 'wb') as f:
                f.write(file_data)
    else:
        for i in range(3):
            csv_path = res_path / csvs[i]
            if not csv_path.exists():
                file = urlopen(urls[i])
                file_data = file.read()
                with open(csv_path, 'wb') as f:
                    f.write(file_data)
    print('Download Complete!')


def save_csv(dataframe: pd.DataFrame):
    now = datetime.now()

    year, month, day, hour, minute, second = now.year, now.month, now.day, now.hour, now.minute, now.second
    suffix = f'{year}_{month}_{day}__{hour}_{minute}_{second}'

    if not csv_path.exists():
        os.mkdir(csv_path)

    dataframe.to_csv(csv_path / f'submission_{suffix}.csv', index=True)