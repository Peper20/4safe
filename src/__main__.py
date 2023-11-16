from colorama import init; init()


from app import create_app




app = create_app()


def main():
	from uvicorn import run
	run(app, host='0.0.0.0')

main()
