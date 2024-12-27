import argparse

from mediatheory.ffmpeg import FFmpeg


def create_parser():
    parser = argparse.ArgumentParser(
        description="Process a path with an optional renderer."
    )

    parser.add_argument("path", type=str, help="The path to process")

    parser.add_argument(
        "--renderer",
        "-r",
        type=str,
        default="ffmpeg",
        help="Specify the renderer to use (default: %(default)s)",
    )

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.renderer == "ffmpeg":
        FFmpeg.reverse(args.path)


if __name__ == "__main__":
    main()
