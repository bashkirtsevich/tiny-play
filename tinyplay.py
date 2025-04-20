import typing

import click
import numpy as np
import soundcard as sc
from scipy.io.wavfile import read


@click.group()
def main():
    pass


@main.command()
def list_speakers():
    print("Speakers:")

    for it in sc.all_speakers():
        print(f"ID: [{it.id}] /{it.channels} -- {it.name}")


@main.command()
@click.option("-l", "--include_loopback", type=click.BOOL, default=False,
              help="Include loopback")
def list_microphones(include_loopback=False):
    print("Microphones:")

    for it in sc.all_microphones(include_loopback):
        print(f"ID: [{it.id}] /{it.channels} -- {it.name}")


@main.command()
@click.argument("wav_path", type=click.Path(exists=False, dir_okay=False))
@click.option("-s", "--speaker_id", type=click.STRING, default=None,
              help="Speaker ID")
@click.option("-q", "--quiet", type=click.BOOL, default=False,
              help="Disable output")
def play(wav_path: str, speaker_id: typing.Optional[str] = None, quiet: bool = False):
    if not quiet:
        print(f"Playing file: {wav_path}")

    speaker = sc.get_speaker(speaker_id) if speaker_id else sc.default_speaker()

    sample_rate, signal = read(wav_path)

    if not quiet:
        print(f"Output device: {speaker.name}")
        print(f"Sample rate: {sample_rate}Hz")
        print(f"Duration: {len(signal) / sample_rate:.3f}s")

    with speaker.player(samplerate=sample_rate) as p:
        p.play(signal / np.max(np.abs(signal)))

    if not quiet:
        print("Done")


# TODO: Implement recorder


if __name__ == '__main__':
    main()
