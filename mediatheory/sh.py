from subprocess import STDOUT, CalledProcessError, check_output

from mediatheory.log import logging


def sh(*args, **kwargs):
    return bash(*args, **kwargs)


sh.brew = "/opt/homebrew/bin/brew"
sh.ffmpeg = "/opt/homebrew/bin/ffmpeg"
sh.which = "which"


def bash(*args, **kwargs):
    command = []

    for x in list(args):
        if isinstance(x, list):
            for y in x:
                command.append(y)
        else:
            command.append(x)

    logging.info(" ".join(command))

    try:
        output = check_output(command, stderr=STDOUT, **kwargs).decode().strip()
        if output:
            logging.info(output)
        return output
    except CalledProcessError as e:
        logging.error(f"{e.returncode}: {e.output.decode()}")
        raise e
