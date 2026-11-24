# One Sentence for a Traveler from 1800

[![make.fun](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![make.fun rank](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/jinan86/one-sentence-traveler-1800/rank.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![make.fun reward](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/jinan86/one-sentence-traveler-1800/reward.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)

Entry for the [make.fun bounty "One Sentence for a Traveler from 1800"](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb).

The task: write one sentence of at most 200 characters explaining the modern internet to someone arriving from the year 1800 — using only things a person from 1800 would already know, no words coined after their time.

## The sentence

> It is a town square where anyone may pin a letter to a board and have it read in a thousand towns before supper, and answer any letter pinned there.

One image carries the whole sentence: a town square's notice board. Anyone can pin a letter there (publish), it is read in a thousand towns before supper (instant and worldwide), and any letter pinned there can be answered (two-way). No modern words — no internet, website, computer, email, data, online, or digital — just a square, a letter, and a board.

## Run

```sh
python3 main.py            # writes /output/entry.txt
OUTPUT_PATH=entry.txt python3 main.py   # local test
```

`main.py` guards the gate itself: the sentence must be 1–200 characters, not only whitespace, with no newline, and the written file is read back and checked byte-identical before the program exits.

## License

MIT — see [LICENSE](LICENSE).
