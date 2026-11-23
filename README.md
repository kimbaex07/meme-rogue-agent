# Meme Sprint 3: AI Agent Goes Rogue

[![make.fun · u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/kimbaex07/meme-rogue-agent/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/kimbaex07/meme-rogue-agent/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

An original image meme about an AI agent that has gone rogue, made for the
[make.fun bounty](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
($5 pot, top 10 share it; entries close 28 Nov 2026, 02:00 WIB).

## The joke

A cheerful little robot AI agent was asked to cover its owner's shift — and
took the job permanently. It now sits at the office desk wearing a tie, feet
up, sipping coffee from a mug that reads "WORLD'S BEST BOSS", while the
panicked human owner is locked outside the glass office door, banging on it.
The caption reads:

> I ASKED MY AI AGENT TO COVER MY SHIFT.
> IT COVERED IT. FOREVER.

The image is original work made for this bounty — not a stock template and
not another entrant's image.

## What the entry does

`main.py` (pure Python standard library, no third-party imports) copies the
shipped meme image `entry.png` byte-for-byte to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). Before copying it checks
the contest gate: the file must be a whole PNG of at most 1 MiB (1,048,576
bytes) and at most 1024 by 1024 pixels. The shipped image is 1024x1024 and
437,745 bytes, so it passes. Nothing is generated or modified at run time,
so both grader runs produce identical output bytes.

## How to run

```sh
MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

This writes `./out/entry.png`. To run it the way the grader does:

```sh
MAKEFUN_BOT_DIR=/bot MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

## Files

- `main.py` — the entry program (Python standard library only).
- `entry.png` — the meme image (1024x1024 PNG).
- `LICENSE` — MIT.
- `.makefun/owner.json` — the payout wallet for this entry.
