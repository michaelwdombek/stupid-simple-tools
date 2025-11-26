import argparse
import sys
import os
from pypdf import PdfWriter

def main():
    # Initialize argument parser
    parser = argparse.ArgumentParser(description="Concatenate multiple PDFs.")

    # Add arguments
    # nargs='+' means it accepts a list of items (1 or more)
    parser.add_argument("--input", required=True, nargs='+', help="List of PDF files to merge")
    parser.add_argument("--output", required=True, help="Name of the output file")

    args = parser.parse_args()

    # Initialize the merger
    merger = PdfWriter()

    try:
        # Loop through the input list provided in the arguments
        for pdf in args.input:
            if not os.path.exists(pdf):
                print(f"Error: The file '{pdf}' does not exist.")
                sys.exit(1)
            
            print(f"Adding {pdf}...")
            merger.append(pdf)

        # Write the final file
        merger.write(args.output)
        merger.close()
        print(f"Successfully merged {len(args.input)} files into '{args.output}'")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
