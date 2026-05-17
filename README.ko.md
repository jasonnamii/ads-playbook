# ads-playbook

> 🇺🇸 [English README](./README.md)

**온라인 광고 운영 플레이북. 목표·채널·측정·크리에이티브·튜닝을 연결해 캠페인 실행안을 만든다.**

## 사전 요구

- **Claude Cowork 또는 Claude Code** 환경

## 목표

대부분의 광고 캠페인이 실패하는 이유는 목표·채널·측정·크리에이티브가 따로 결정되기 때문이다. 이 스킬은 단일 경로 운영 순서를 강제한다 — 목표를 잠그고, 측정을 잠근 뒤, 예산·기간·타깃에 맞춰 채널 믹스와 크리에이티브를 라우팅한다. 결과는 빠진 조각을 사후에 채워넣을 필요 없이 바로 집행 가능한 캠페인 계획이다.

## 사용 시점 & 방법

"광고 짜줘", "튜닝해줘", "ROAS 점검", "매체믹스" 등 캠페인 수준 기획 요청 시 발동. 별도 지정이 없으면 한국 시장·원화·네이버·카카오·메타·구글 혼합이 디폴트. 매체 집행 디테일은 `media-buying`, 카피는 `copywriting-skill`, 브랜드 수준 캠페인 설계는 `brand-campaign`로 위임한다.

## 사용 사례

| 상황 | 프롬프트 | 동작 |
|---|---|---|
| 신제품 런칭 | `"신제품 런칭 광고 짜줘. 예산 월 3000만원"` | 목표 라우팅 → 채널 믹스 → 크리에이티브 브리프 → 측정 플랜 |
| ROAS 회복 | `"ROAS 떨어졌어. 튜닝해줘"` | 진단 → 입찰·예산·소재 레버 → 튜닝 플레이북 |
| 채널 비중 점검 | `"네이버·메타·구글 비중 점검"` | 채널별 목표 적합도 → 재배분 제안 |

## 주요 기능

- **목표 우선 라우팅** — 앱·리드·커머스·브랜드 라우팅 매트릭스가 나머지 계획을 잠근다
- **측정 게이트** — ROAS·CAC·CPA·LTV·리텐션 임계값을 채널 선택 전에 확정
- **플랫폼별 플레이북** — 네이버·카카오·메타·구글·틱톡·ASA·X·LinkedIn 레퍼런스
- **튜닝 플레이북** — 부진 캠페인 진단·레버 리스트
- **런칭 체크리스트** — 흔한 예산 누수 방지용 사전 점검
- **2026 Q2 플랫폼 변경** — 최신 플랫폼 업데이트 추적 레퍼런스

## 연동 스킬

- **[media-buying](https://github.com/jasonnamii/media-buying)** — 매체 집행·입찰·예산 배분 디테일
- **[copywriting-skill](https://github.com/jasonnamii/copywriting-skill)** — 광고 카피 생성
- **[brand-campaign](https://github.com/jasonnamii/brand-campaign)** — 브랜드 수준 IMC 캠페인 설계

## 설치

```bash
git clone https://github.com/jasonnamii/ads-playbook.git ~/.claude/skills/ads-playbook
```

## 업데이트

```bash
cd ~/.claude/skills/ads-playbook && git pull
```

`~/.claude/skills/`에 배치된 스킬은 Claude Code 및 Cowork 세션에서 자동으로 사용 가능합니다.

## Cowork Skills

25개 이상의 커스텀 스킬 중 하나입니다. 전체 카탈로그: [github.com/jasonnamii/cowork-skills](https://github.com/jasonnamii/cowork-skills)

## 라이선스

MIT License — 자유롭게 사용, 수정, 공유 가능합니다.
