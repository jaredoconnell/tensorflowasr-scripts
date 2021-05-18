import argparse
from tqdm.auto import tqdm

parser = argparse.ArgumentParser(prog="Parse TSV Transcripts for sclite scoring")

parser.add_argument("--tsv", "-t", type=str, default=None, help="Path to tsv file")
parser.add_argument("output", type=str, default=None, help="The output .trans transcript file path, including file extension")
args = parser.parse_args()
assert args.tsv and args.output

#args.tsv = preprocess_paths(args.tsv)
#args.output = preprocess_paths(args.output)

transcripts = []

with open(args.tsv, "r", encoding="utf-8") as txt:
    lines = txt.read().splitlines()[1:] # skip first line
for line in lines:
    line = line.split(maxsplit=1)
    if len(line) == 2:
        text = line[1]
    else:
        text = ""
    file_path = line[0]
    speaker_id = file_path.split("/")[-1][:-4]
    transcripts.append(f"{text} ({speaker_id})\n")

with open(args.output, "w", encoding="utf-8") as out:
    for line in tqdm(transcripts, desc="[Writing]"):
        out.write(line)
