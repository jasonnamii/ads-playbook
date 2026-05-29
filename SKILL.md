---
name: ads-playbook
description: |
  온라인 광고 운영 플레이북. 목표·채널·측정·크리에이티브·튜닝을 연결해 캠페인 실행안을 만든다. 트리거: 광고운영, 퍼포먼스광고, ads playbook, ROAS, CAC, 매체믹스, 광고 짜줘, 튜닝해줘, 점검해줘, optimize ads. NOT: 미디어 집행 실무(→media-buying), 카피(→copywriting-skill), 브랜드 캠페인(→brand-campaign).
---

# Ads Playbook

## §0 원칙


## Skill Boundaries

- **하는 것** — "온라인 광고 운영 플레이북.
- **안 하는 것** — 미디어 집행 실무(→media-buying), 카피(→copywriting-skill), 브랜드 캠페인(→brand-campaign)."

한국 디폴트: 별도 지정이 없으면 한국 시장, 원화, 네이버·카카오·메타·구글 혼합 집행을 기본으로 본다.

1. 목표를 먼저 고른다: 앱설치, 리드, 커머스, 브랜드.
2. 측정 기준을 먼저 잠근다: ROAS, CAC, CPA, LTV, 리텐션.
3. 채널 추천은 예산, 기간, 타깃, 소재 역량을 함께 본다.
4. 최신 플랫폼 변경은 `references/latest_2026q2.md`를 확인한다.

## When to Use

- 사용자가 "광고 짜줘", "튜닝해줘", "점검해줘", "optimize ads." 같은 표현으로 발동
- 도메인 작업이 필요한 시점
- **안 쓸 때** — 미디어 집행 실무(→media-buying), 카피(→copywriting-skill), 브랜드 캠페인(→brand-campaign)."


## Prerequisites

| # | 체크 | 미충족 시 |
|---|------|-----------|
| 1 | 대상·입력 명확 (스킬 발동 의도 확인) | 1줄 확인 후 진입 |
| 2 | references/ 폴더 접근 가능 | inline fallback |
| 3 | scripts/ 실행 권한 | 권한 보정 후 재시도 |


## §1 입력

| 항목 | 필요 내용 |
|---|---|
| Objective | 앱·커머스·리드·브랜드 |
| Budget | 일·월 예산 |
| Target | 지역·연령·관심사·고객 단계 |
| Creative | 영상·이미지·랜딩·카피 보유 여부 |
| Measurement | 전환 이벤트와 어트리뷰션 기준 |

## §2 라우팅

- 목표별 선택: `references/objective_matrix.md`
- 앱: `references/objective_app.md`
- 커머스: `references/objective_commerce.md`
- 리드: `references/objective_lead.md`
- 브랜드: `references/objective_brand.md`

## §3 채널

- Meta: `references/platform_meta.md`
- Google: `references/platform_google.md`
- TikTok/ASA: `references/platform_tiktok_asa.md`
- Naver/Kakao: `references/platform_naver_kakao.md`
- X/LinkedIn: `references/platform_x_linkedin.md`

## §4 실행

1. 캠페인 목표와 KPI를 확정한다.
2. 예산을 테스트, 확장, 방어로 나눈다.
3. 소재는 후킹, 증거, 전환 유도 버전으로 최소 3종 만든다.
4. 런칭 전 `references/launch_checklist.md`를 확인한다.

## §5 튜닝

- 측정: `references/measurement.md`
- 소재: `references/creative.md`
- 튜닝: `references/tuning_playbook.md`
- 금지 패턴: `references/antipatterns.md`
- 용어: `references/glossary.md`

## Output Path

| 산출물 | 경로 |
|---|---|
| 주 산출물 | `mnt/outputs/ads-playbook_{topic}_{YYYY-MM-DD}.md` |
| 형식 | 플레이북으로, .md로. |
| 리서치 결과 (해당 시) | `{VAULT}/_skills research/ads-playbook/{YYYY-MM-DD}_{topic}.md` |

## Reference Index

| 파일 | 내용 | 언제 |
|---|---|---|
| `references/antipatterns.md` | antipatterns | 해당 단계 진입 시 |
| `references/creative.md` | creative | 해당 단계 진입 시 |
| `references/glossary.md` | glossary | 해당 단계 진입 시 |
| `references/latest_2026q2.md` | latest 2026q2 | 해당 단계 진입 시 |
| `references/launch_checklist.md` | launch checklist | 해당 단계 진입 시 |
| `references/measurement.md` | measurement | 해당 단계 진입 시 |
| `references/objective_app.md` | objective app | 해당 단계 진입 시 |
| `references/objective_brand.md` | objective brand | 해당 단계 진입 시 |
| `references/objective_commerce.md` | objective commerce | 해당 단계 진입 시 |
| `references/objective_lead.md` | objective lead | 해당 단계 진입 시 |
| `references/objective_matrix.md` | objective matrix | 해당 단계 진입 시 |
| `references/platform_google.md` | platform google | 해당 단계 진입 시 |
| `references/platform_meta.md` | platform meta | 해당 단계 진입 시 |
| `references/platform_naver_kakao.md` | platform naver kakao | 해당 단계 진입 시 |
| `references/platform_tiktok_asa.md` | platform tiktok asa | 해당 단계 진입 시 |


## Next Phase

본 스킬 작업 후 자연스럽게 이어지는 흐름:

- 후속 작업 → `media-buying`
- 후속 작업 → `copywriting-skill`
- 후속 작업 → `brand-campaign`

## Failure Modes (Gotchas)

| 함정 | 대응 |
|---|---|
| ROAS만 보고 예산 증액 | CAC, 재구매, 마진을 같이 본다 |
| 채널을 너무 빨리 늘림 | 한 채널에서 학습량 확보 후 확장 |
| 소재 피로 무시 | 주 1회 빈도와 CTR 하락을 같이 본다 |
| ❌ 전환수만 보고 성공 판단 | ✅ 마진, CAC, 재구매 가능성을 같이 확인 |
