import argparse
import requests
import datetime
import time

if __name__ == "__main__":
    DEFAULT_OUTPUT_FILENAME = "output.csv"
    parser = argparse.ArgumentParser(description="Convert an array of json objects at a http URL to CSV at regular intervals", prog="jsontocsv")
    parser.add_argument("-s", "--silent", action="store_true", help="only print output on error")
    parser.add_argument("-v", "--verbose", action="store_true", help="print on every request")
    parser.add_argument("-d", "--delay",type=float, help="delay between requests in seconds [default: 0]", default=0)
    parser.add_argument("url", help="URL of json")
    parser.add_argument("output", help=f"CSV output file name [default: {DEFAULT_OUTPUT_FILENAME}]", nargs="?", default=DEFAULT_OUTPUT_FILENAME)

    args = parser.parse_args()

    previous_hash = None
    while True:
        reqtime_str = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        if args.verbose:
            print(f"Request at: {reqtime_str}", end="", flush=True)

        r = requests.get(args.url)
        if args.verbose:
            print(f" Received {r.status_code}", end="")
        print("\n", end="")
        r.raise_for_status()

        current_hash = hash(r.text)
        if current_hash != previous_hash:
            previous_hash = current_hash
            if not args.silent:
                print(f"Update  at: {reqtime_str}")

            jsondata = r.json()

            with open(args.output, "w") as csvfile:
                # Write header row - assumes that jsondata[0] exists
                csvfile.write(",".join(f"\"{x}\"" for x in jsondata[0].keys()) + "\n")
                # Write data rows
                for row in jsondata:
                    csvfile.write(",".join(f"\"{x}\"" for x in row.values()) + "\n")

        time.sleep(args.delay)
