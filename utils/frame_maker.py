import cv2
import os
import uuid

from pathlib import Path
from datetime import datetime

from transliterate import translit

WORKDIR = Path(__file__).parent.parent.resolve()
PARENT_WORKDIR = os.path.split(os.path.abspath(WORKDIR))[0]

WIDTH = 250  # To feed images to a neural network
HEIGHT = 250  # To feed images to a neural network

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


def change_scale(image):
    return cv2.resize(image, (WIDTH, HEIGHT), interpolation=cv2.INTER_AREA)


def define_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, 1.1, 1, minSize=(130, 130), flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Найти центр картинки и от него уже изменять размер на 250х250
    # Without 250 x 250
    if len(faces) > 0:
        for _, (x, y, w, h) in enumerate(faces):
            if x <= 150 and y <= 150:
                continue

            face = frame[y : y + h, x : x + w]

            return change_scale(face)
    return []


def video_to_frames(path: str, user_data, uuid_value: str) -> list:
    video_capture = cv2.VideoCapture()
    video_capture.open(path)

    frames = video_capture.get(cv2.CAP_PROP_FRAME_COUNT)

    current_path = os.path.join(PARENT_WORKDIR, "ml-js", "labels")

    sub_folders = []
    for i in range(int(frames)):
        _, frame = video_capture.read()
        face = define_face(frame)

        original_first_name = user_data["first_name"]
        original_last_name = user_data["last_name"]

        first_name = translit(original_first_name, language_code="ru", reversed=True)
        last_name = translit(original_last_name, language_code="ru", reversed=True)

        user_path = os.path.join(
            current_path, f"{first_name}_{last_name}--{uuid_value}"
        )

        if not os.path.exists(user_path):
            os.mkdir(user_path)

        if len(face) > 0:
            cv2.imwrite(
                os.path.join(
                    user_path,
                    f"{i}",
                )
                + ".png",
                face,
            )

        sub_folders = [
            name
            for name in os.listdir(current_path)
            if os.path.isdir(os.path.join(current_path, name))
        ]

    return sub_folders


def start_make_frames(path: str, user_data, uuid_value: str) -> None:
    t1 = datetime.now()

    video_to_frames(path, user_data, uuid_value)

    t2 = datetime.now()

    print("Time cost = ", (t2 - t1))
