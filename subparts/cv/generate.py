from pathlib import Path
import subprocess

RESUMATOR_PATH = Path.cwd().parent.joinpath('resumator')
RESUMATOR_RUN_PATH = RESUMATOR_PATH.joinpath('run.py')
RAW_CV_PATH = RESUMATOR_PATH.joinpath('content', 'cv.yaml')
CV_OUTPATH = Path.cwd().joinpath('templates', 'cv.html')


def regenerate_cv():
    command = [
        'python3',
        f'{RESUMATOR_RUN_PATH}',
        f'-s {RAW_CV_PATH}',
        f'-d {CV_OUTPATH}',
    ]

    subprocess.call(" ".join(command), shell=True)


if __name__ == '__main__':
    regenerate_cv()
