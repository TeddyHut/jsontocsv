import argparse

if __name__ == "__main__":
    DEFAULT_OUTPUT_FILENAME = "output.csv"
    parser = argparse.ArgumentParser(description="Convert json at http URL to CSV at intervals", prog="jsontocsv")
    parser.add_argument("-s", "--silent", action="store_true", help="only print output on error")
    parser.add_argument("-v", "--verbose", action="store_true", help="print on every request")
    parser.add_argument("-t", "--time-interval", metavar="time", type=float, help="polling interval in seconds")
    parser.add_argument("url", help="URL of json")
    parser.add_argument("output", help=f"CSV output file name [default: {DEFAULT_OUTPUT_FILENAME}]", nargs="?", default=DEFAULT_OUTPUT_FILENAME)

    args = parser.parse_args()
