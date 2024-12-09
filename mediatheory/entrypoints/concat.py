import argparse

from mediatheory.ffmpeg import FFmpeg


def create_parser():
    parser = argparse.ArgumentParser(
        description="Concatenate video files."
    )

    parser.add_argument(
        "input",
        nargs="+",
        type=str,
        help="space delimited input file paths",
    )

    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="output file path",
    )

    parser.add_argument(
        "--renderer",
        "-r",
        type=str,
        default="ffmpeg",
        help="Specify the renderer to use (default: %(default)s)"
    )

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.renderer == "ffmpeg":
        FFmpeg.concat(
            input_files=args.input,
            output_file=args.output,
        )

if __name__ == "__main__":
    main()
