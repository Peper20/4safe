from dataclasses import dataclass
from os import environ
from dotenv import load_dotenv




# crypto area {

SECRET = 'S3V5LU11c3QtQmUtYXQtbGVhc3QtdzItYnl0ZXMtaW4tbGVuZ3RoIq'

# }


# config area {

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



config = load_env()

# }