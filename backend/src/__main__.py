from colorama import init; init()
from argparse import ArgumentParser


from app import create_app




app = create_app()


def run_app():
	from uvicorn import run
	run(app, host='0.0.0.0')


def run_tests():
	from tests import run
	run(app)


def main():
	parser = ArgumentParser(prog='sirius')
	parser.add_argument('-t', '--run_tests', action='store_true', default=False)
	
	args = parser.parse_args()
	

	if args.run_tests:
		run_tests()
	else:
		run_app()


main()
