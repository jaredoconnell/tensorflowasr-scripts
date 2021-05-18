# tensorflowasr-scripts
### This repository stores useful scripts for translating between transcript types with sclite and the switchboard corpus for TensorFlowASR.

## Setup

This repository is for Python 3, tested on 3.7.3

`python3 -m pip install -r requirements.txt`
or
`pip3 install -r requirements.txt`

The switchboard corpus contains sph (sphere) files instead of WAV files, so `sphfile` is used to convert them.

## Scripts
### create_switchboard_trans.py
This script is used for creating a `.tsv` file from the switchboard's `.trans` file for use in TensorFlowASR.

There is a chance that your transcript will be different, and you would then need to change the split value and index accessed. Feel free to create an issue if you run into that issue.

Arguments:
- `--utt` Used to specify the directory that contains the `.sph` files.
- `--trans` Used to specify the `.trans` transcript file to be converted.
- Unnamed argument: The output `.tsv` file

Example:
```
python3 ~/capstone/repos/tensorflowasr-scripts/create_switchboard_trans.py --utt ../audio/utt/ --trans train.trans train.tsv`
```

### parse_tsv.py
This script is used to convert the `.tsv` to a `.trans` file for decoding with sclite.

Arguments:
- `--tsv` Used to specify the `.tsv` transcript file to be converted.
- Unnamed argument: The output `.trans` file


Example:
```
python3 ~/capstone/repos/tensorflowasr-scripts/parse_tsv.py --tsv test.tsv hyp.trans
```
