import argparse

from mediatheory.ffmpeg import FFmpeg


def create_parser():
    parser = argparse.ArgumentParser(
        description='Process a path with an optional renderer.'
    )

    parser.add_argument(
        'path',
        type=str,
        help='The path to process'
    )

    parser.add_argument(
        '--renderer',
        '-r',
        type=str,
        default='ffmpeg',
        help='Specify the renderer to use (default: %(default)s)'
    )

    parser.add_argument(
        "--width",
        "-w",
        type=str,
        default="-1",
        help="width scale",
    )

    parser.add_argument(
        "--height",
        "-l",
        type=str,
        default="-1",
        help="height scale",
    )

    parser.add_argument(
        "--fps",
        "-f",
        type=str,
        default="24",
        help="frames per second",
    )

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.renderer == "ffmpeg":
        FFmpeg.gif(args.path, args.width, args.height, args.fps)

if __name__ == '__main__':
    main()
