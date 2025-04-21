import click
import numpy as np
import soundcard as sc
from scipy.io.wavfile import write


@click.group()
def main():
    pass


@main.command()
@click.option("-l", "--include_loopback", type=click.BOOL, default=False,
              help="Include loopback")
def list_microphones(include_loopback=False):
    print("Microphones:")

    for it in sc.all_microphones(include_loopback):
        print(f"ID: [{it.id}] /{it.channels} -- {it.name}")


@main.command()
@click.argument("wav_path", type=click.Path(exists=False, dir_okay=False))
@click.argument("duration", type=click.FLOAT, default=10.0)
@click.option("-m", "--microphone_id", type=click.STRING, default=None,
              help="Microphone ID")
@click.option("-r", "--sample_rate", type=click.INT, default=48000,
              help="Sample rate")
@click.option("-q", "--quiet", type=click.BOOL, default=False,
              help="Disable output")
def record(wav_path: str, duration: float, microphone_id: str, sample_rate: int, quiet: bool):
    duration = abs(duration)

    if not quiet:
        print(f"Recording file: {wav_path}")

    microphone = sc.get_microphone(microphone_id) if microphone_id else sc.default_microphone()

    if not quiet:
        print(f"Input device: {microphone.name}")
        print(f"Sample rate: {sample_rate}Hz")
        print(f"Duration: {duration:.3f}s")

    with microphone.recorder(samplerate=sample_rate) as m:
        signal = m.record(numframes=round(sample_rate * duration))

    amplitude = np.iinfo(np.int16).max
    data = signal * amplitude

    write(wav_path, sample_rate, data.astype(np.int16))

    if not quiet:
        print("Done")


if __name__ == '__main__':
    main()
