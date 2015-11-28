import argparse

from app import app


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5000)

    args = parser.parse_args()

    app.run(host='0.0.0.0', port=args.port, threaded=True)

if __name__ == '__main__':
    main()
