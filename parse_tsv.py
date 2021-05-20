import argparse
from tqdm.auto import tqdm

parser = argparse.ArgumentParser(prog="Parse TSV Transcripts for sclite scoring")

parser.add_argument("--tsv", "-t", type=str, default=None, help="Path to tsv file")
parser.add_argument("output", type=str, default=None, help="The output .trans transcript file path, including file extension")
args = parser.parse_args()
assert args.tsv and args.output

#args.tsv = preprocess_paths(args.tsv)
#args.output = preprocess_paths(args.output)

transcripts_greedy = []
transcripts_beamsearch = []

with open(args.tsv, "r", encoding="utf-8") as txt:
    lines = txt.read().splitlines() # skip first line
    header = lines[0].split('\t')
    lines = lines[1:]
    greedy_index = header.index("GREEDY")
    beamsearch_index = header.index("BEAMSEARCH")
for line in lines:
    line = line.split('\t')
    file_path = line[0]
    speaker_id = file_path.split("/")[-1][:-4]
    greedy_result = line[greedy_index]
    beamsearch_result = line[beamsearch_index]
    transcripts_greedy.append(f"{greedy_result} ({speaker_id})\n")
    transcripts_beamsearch.append(f"{beamsearch_result} ({speaker_id})\n")

with open("greedy_" + args.output, "w", encoding="utf-8") as out:
    for line in tqdm(transcripts_greedy, desc="[Writing]"):
        out.write(line)
with open("beamsearch_" + args.output, "w", encoding="utf-8") as out:
    for line in tqdm(transcripts_beamsearch, desc="[Writing]"):
        out.write(line)
