# 01 — Reddit Pain-Phrase Mining

## Goal

Find the exact words new parents use when describing things they wish existed. These phrases become product titles, Etsy tags, blog post hooks, and Pinterest pin copy.

## Target subreddits

| Subreddit | Lens |
|---|---|
| r/Mommit | General mom community |
| r/BabyBumps | Pregnancy |
| r/beyondthebump | Postpartum + first year |
| r/NewParents | Mixed dad/mom new-parent |
| r/Postpartum_Depression | Mental health |
| r/ScienceBasedParenting | Evidence-seeking parents (premium buyer segment) |
| r/breastfeeding | Feeding |
| r/toddlers | Months 18–36 |
| r/SAHP | Stay-at-home parents |
| r/workingmoms | Working parents — high-income buyer segment |
| r/daddit | Dad community |
| r/Mommit, r/Parenting | Backup if others thin |

## What I'm extracting

For each subreddit:

- Top 25 highest-upvoted threads in last 12 months
- Threads matching: "I wish there was…", "Does anyone have…", "How do I keep track of…", "What do you use for…", "Is there a template/printable for…"
- For each thread: the *exact phrase* used, the underlying problem, the emotional intensity (sentiment), # of similar comments

## Output

- `phrases.md` — raw extracted phrases, grouped by theme
- `problems.md` — synthesized problem list with frequency counts
- `buyer-segments.md` — distinct buyer personas surfaced
- `quotes.md` — direct quotes I'll use in blog hooks and Etsy descriptions (paraphrased, never copied)

## Method note

Reddit data is public but quotes go in `quotes.md` as paraphrased pain-phrases, never verbatim, to respect contributor authorship.
