# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from sphfile import SPHFile
import argparse
from tqdm.auto import tqdm
import unicodedata
import re

from tensorflow_asr.utils.utils import preprocess_paths

parser = argparse.ArgumentParser(prog="Setup Switchboard Transcripts")

parser.add_argument("--trans", "-t", type=str, default=None, help="Path to trans file")
parser.add_argument("--utt", "-u", type=str, default=None, help="Path to the utterance directory")

parser.add_argument("output", type=str, default=None, help="The output .tsv transcript file path")

args = parser.parse_args()

assert args.utt and args.output and args.trans

args.utt = preprocess_paths(args.utt)
args.trans = preprocess_paths(args.trans)
args.output = preprocess_paths(args.output)

# regex to strip [], -
p = re.compile('\s\[.+?\]|-|_1|&|\[|\]|{|}|<.+?>|\d', re.IGNORECASE)

transcripts = []

with open(args.trans, "r", encoding="utf-8") as txt:
    lines = txt.read().splitlines()
for line in tqdm(lines, desc="[Converting]"):
    line = line.split(" ", maxsplit=3)
    speaker_id = line[0]
    time_start = float(line[1])
    time_end = float(line[2])
    text = p.sub(" ", line[3]).replace("/","")
    audio_file_sph = args.utt + "/" + speaker_id + ".sph"
    audio_file_wav = args.utt + "/" + speaker_id + ".wav"
    sph = SPHFile(audio_file_sph)
    sph.write_wav(audio_file_wav)

    duration = time_end - time_start
    text = unicodedata.normalize("NFC", text)
    transcripts.append(f"{audio_file_wav}\t{duration}\t{text}\n")

with open(args.output, "w", encoding="utf-8") as out:
    out.write("PATH\tDURATION\tTRANSCRIPT\n")
    for line in tqdm(transcripts, desc="[Writing]"):
        out.write(line)
