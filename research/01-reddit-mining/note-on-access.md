# Note on Reddit Data Access

Direct Reddit access (both `reddit.com` and `old.reddit.com`) is blocked from this remote execution environment. WebFetch returns "unable to fetch."

## What we did instead

1. Used WebSearch to surface secondary sources (mom blogs, parenting magazines, Pinterest reports) that aggregate Reddit-style pain points.
2. Drew on Claude's training-knowledge of major parenting communities (Reddit baby subs, BabyCenter, What to Expect community) — this knowledge is real and substantial; these forums are heavily indexed in training data.

The synthesis lives in `research/05-customer-journey/pain-points.md`. Phrases there marked *"paraphrased from training-knowledge of forum discussions"* are reliable in *theme and pattern* but not verbatim. We never copy actual user posts.

## What this means for the final report

The pain-point themes, problem identification, and buyer segments in our research are reliable. What we DON'T have is:

- Exact viral-thread titles (e.g., "What's the one product that saved your 4th trimester?" threads)
- Live upvote counts to weight pain-frequency
- Current 2026-specific Reddit conversations (training data has a cutoff)

## Options to fill the gap (owner's call)

1. **Trust the synthesis** — themes are stable across years; the 2026-specific stuff comes from Pinterest report which is fresh.
2. **Owner paste-in** — owner manually copies 10–20 top Reddit threads from each target sub into `research/01-reddit-mining/raw-threads.md` and a future session re-synthesizes.
3. **Use eRank/Sale Samurai (paid)** — these tools include Reddit signal mining. ~$15/mo. Not in current budget.
4. **Skip live Reddit data entirely** — proceed with what we have. Risk: low. Reward: faster.

**Default recommendation: option 1** (trust the synthesis), revisit with option 2 if Day 3 review shows gaps.
