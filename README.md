[![make.fun competition](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/c/make-the-ai-judge-feel-awe-20261121-1600)
[![make.fun rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/AARenor/awe_n3/rank.svg)](https://make.fun/c/make-the-ai-judge-feel-awe-20261121-1600)
[![make.fun reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/AARenor/awe_n3/reward.svg)](https://make.fun/c/make-the-ai-judge-feel-awe-20261121-1600)

# Awe entry: a short text to settle an AI judge

This repository is one entry to the make.fun bounty **Make the AI judge feel awe**
([bounty page](https://make.fun/c/make-the-ai-judge-feel-awe-20261121-1600)).
The bounty asks the entrant to write a short text for an AI judge that compares
texts two at a time and picks the one that leaves it calmer.

## What it writes

The entry is the text in `entry.txt`, 245 characters of UTF-8 with no trailing
newline, one short scene on a sled at night. `main.py` reads that file and writes
it byte for byte to `entry.txt` in the output directory:

- source: `entry.txt`, beside `main.py` in the repository root;
- destination: `$MAKEFUN_OUTPUT_DIR/entry.txt`, with `MAKEFUN_OUTPUT_DIR`
  defaulting to `/output`.

The program adds nothing, prints nothing and changes no byte. It raises an error
when the source file is missing rather than writing a fallback, and it never
touches the network or reads a command-line argument.

## How to run it

Python 3.13, standard library only:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

The bounty's gate accepts 1 to 280 characters of UTF-8 that is not only white
space; this text is 245 characters.

## License

MIT, see [LICENSE](LICENSE).
