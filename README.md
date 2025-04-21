# Simple wav player/recorder

Easiest wav player/recorder with custom DAC/ADC access.

## Installation

### Pip

`pip install -r requirements.txt`

## Usage

### Player

Common usage:

```
Usage: play.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  list-speakers
  play
```

Play:

```
Usage: play.py play [OPTIONS] WAV_PATH

Options:
  -s, --speaker_id TEXT  Speaker ID
  -q, --quiet BOOLEAN    Disable output
  --help                 Show this message and exit.
```

List speakers:

```
Usage: play.py list-speakers [OPTIONS]

Options:
  --help  Show this message and exit.
```

### Recorder

Common usage:

```
Usage: record.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  list-microphones
  record
```

Record:

```
Usage: record.py record [OPTIONS] WAV_PATH [DURATION]

Options:
  -m, --microphone_id TEXT   Microphone ID
  -r, --sample_rate INTEGER  Sample rate
  -q, --quiet BOOLEAN        Disable output
  --help                     Show this message and exit.
```

List microphones:

```
Usage: record.py list-microphones [OPTIONS]

Options:
  -l, --include_loopback BOOLEAN  Include loopback
  --help                          Show this message and exit.
```
