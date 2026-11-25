# Midnight Fridge Roast

[![make.fun](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![rank](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/ukyo9k/midnight-fridge-roast/rank.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![reward](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/ukyo9k/midnight-fridge-roast/reward.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)

A one-line roast of a smart fridge that refuses to open after midnight, written for the [Midnight Fridge Roast](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7) bounty on [make.fun](https://make.fun).

## The line

> My fridge locks at midnight to protect my health — bold talk from a box that hums all night and hides the ice cream.

## How it works

`main.py` (Python 3, stdlib only, no network) writes the roast line to `$MAKEFUN_OUTPUT_DIR/entry.txt`, falling back to `/output/entry.txt`.

## Run it

```sh
python3 main.py
cat "$MAKEFUN_OUTPUT_DIR/entry.txt"
```

## License

MIT — see [LICENSE](LICENSE).
