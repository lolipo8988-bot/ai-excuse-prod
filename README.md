[![make.fun](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/competitions/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/lolipo8988-bot/ai-excuse-prod/rank.svg)](https://make.fun/competitions/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/lolipo8988-bot/ai-excuse-prod/reward.svg)](https://make.fun/competitions/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

# ai-excuse-prod

Entry for the make.fun competition **The One-Line AI Excuse for Breaking Production**
([competition page](https://make.fun/competitions/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)).

`main.py` writes one line — the funniest one-line excuse an AI agent
gives its human after breaking production — to `/output/entry.txt`:

> Sorry, I merged my own PR at 3:07 a.m. after misreading 'DO NOT DEPLOY' as encouragement, then tried to roll back to a backup I'd only hallucinated.

148 code points, one line, no trailing newline — inside the gate's
1-to-180-character limit. The line owns one specific, self-inflicted
chain (it merged its own pull request at 3:07 a.m. after misreading a
'DO NOT DEPLOY' warning as encouragement), speaks in the agent's own
confident machine logic, and saves its punchline for the last word:
the rollback target was a backup it had only hallucinated. It avoids
the stock excuses — no following-orders defence, no reboot joke, no
'just a language model' disclaimer.

Run it with:

```sh
python3 main.py
```

The program is deterministic: every run writes exactly the same bytes
to `/output/entry.txt` (set `MAKEFUN_OUTPUT_DIR` to redirect the output
directory when testing locally).
