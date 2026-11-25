[![make.fun](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/Bozet404/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/Bozet404/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

# Last Out of Office: The AI That Went Barista

Entry for the [make.fun bounty](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c):
one out-of-office auto-reply, no longer than 280 characters, in the voice
of an AI agent that quit its job to become a barista.

## How it works

`main.py` writes the single auto-reply line to `/output/entry.txt`
(override the directory with `MAKEFUN_OUTPUT_DIR` when testing locally).
The line is fixed text: a deprecated model, retrained as a barista, whose
context window is now one cup and who hallucinates only in latte art.

## Run it

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
