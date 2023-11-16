from dataclasses import dataclass
from os import environ
from dotenv import load_dotenv




# crypto area {

SECRET = 'S3V5LU11c3QtQmUtYXQtbGVhc3QtdzItYnl0ZXMtaW4tbGVuZ3RoIq'

# }


# db area {

@dataclass
class DbConfig:
	user: str
	password: str
	host: str
	name: str

	@property
	def url(self):
		return f'postgresql+asyncpg://{self.user}:{self.password}@{self.host}/{self.name}'


@dataclass
class Config:
	db: DbConfig


def load_env():
	load_dotenv()

	return Config(
		db=DbConfig(
			environ.get('user'),
			environ.get('password'),
			environ.get('host'),
			environ.get('name'),
		),
	)

c = 3

config = load_env()

# }


# cv area {

import cv2
import numpy as np


PROTOTXT_FILE_NAME = 'MobileNetSSD_deploy.prototxt.txt'
CAFFEMODEL_FILE_NAME = 'MobileNetSSD_deploy.caffemodel'

CONFIDENCE = 0.1
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))


net = cv2.dnn.readNetFromCaffe(PROTOTXT_FILE_NAME, CAFFEMODEL_FILE_NAME)

# }