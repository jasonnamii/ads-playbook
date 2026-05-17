# ads-playbook

> 🇰🇷 [한국어 README](./README.ko.md)

**Online ads operating playbook. Connects objective, channel, measurement, creative, and tuning into one campaign execution plan.**

## Prerequisites

- **Claude Cowork or Claude Code** environment

## Goal

Most ad campaigns fail because objective, channel, measurement, and creative are decided independently. This skill enforces a single-path operating sequence: lock the objective, lock the measurement, then route channel mix and creative against budget, period, and target. The result is a campaign plan you can ship without backfilling the missing pieces later.

## When & How to Use

Triggers on requests like "광고 짜줘", "튜닝해줘", "ROAS 점검", "매체믹스", or any campaign-level planning prompt. Korean market is the default — KRW, Naver/Kakao/Meta/Google mix — unless specified otherwise. For media buying execution detail, hand off to `media-buying`. For copy, hand off to `copywriting-skill`. For brand-level campaign design, hand off to `brand-campaign`.

## Use Cases

| Scenario | Prompt | What Happens |
|---|---|---|
| New product launch | `"신제품 런칭 광고 짜줘. 예산 월 3000만원"` | Objective routing → channel mix → creative brief → measurement plan |
| ROAS recovery | `"ROAS 떨어졌어. 튜닝해줘"` | Diagnostic → bid/budget/creative levers → tuning playbook |
| Channel mix audit | `"네이버·메타·구글 비중 점검"` | Objective fit by channel → reallocation proposal |

## Key Features

- **Objective-first routing** — App / Lead / Commerce / Brand routing matrix locks the rest of the plan
- **Measurement gate** — ROAS / CAC / CPA / LTV / retention thresholds set before channel selection
- **Platform-specific playbooks** — Naver, Kakao, Meta, Google, TikTok, ASA, X, LinkedIn reference files
- **Tuning playbook** — Diagnostic and lever list for underperforming campaigns
- **Launch checklist** — Pre-launch verification to prevent common spend leaks
- **2026 Q2 platform changes** — Reference file tracks current platform updates

## Works With

- **[media-buying](https://github.com/jasonnamii/media-buying)** — Media execution, bid strategy, budget allocation detail
- **[copywriting-skill](https://github.com/jasonnamii/copywriting-skill)** — Ad copy generation
- **[brand-campaign](https://github.com/jasonnamii/brand-campaign)** — Brand-level IMC campaign design

## Installation

```bash
git clone https://github.com/jasonnamii/ads-playbook.git ~/.claude/skills/ads-playbook
```

## Update

```bash
cd ~/.claude/skills/ads-playbook && git pull
```

Skills placed in `~/.claude/skills/` are automatically available in Claude Code and Cowork sessions.

## Part of Cowork Skills

This is one of 25+ custom skills. See the full catalog: [github.com/jasonnamii/cowork-skills](https://github.com/jasonnamii/cowork-skills)

## License

MIT License — feel free to use, modify, and share.
