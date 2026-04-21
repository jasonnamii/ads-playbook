---
name: ads-playbook
version: 1.1.0
description: |
  온라인 광고 인하우스 플레이북. 8플랫폼×10목적 진단·세팅·튜닝·용어. 시그널·러닝·크리에이티브·측정·안티패턴 처방.
  P1: 광고플레이북, ads playbook, 퍼포먼스마케팅, 메타광고, 구글광고, 틱톡광고, 네이버광고, 카카오광고, 카카오모먼트, 링크드인광고, PMax, ASA, Advantage+, ASC, UAC, Smart+, 비즈보드, 러닝페이즈, CAPI, SKAN, ROAS, CPA, 앱광고, 리타겟팅, 리드광고, 이커머스광고, 광고운영, 광고튜닝.
  P2: 세팅해줘, 진단해줘, 튜닝해줘, optimize.
  P3: paid social, paid search, tROAS, tCPA, incrementality.
  P5: .md로.
  NOT: IMC(→brand-campaign), 카피(→copywriting-engine), 사업전략(→biz-skill), 재무(→financial-model), KPI(→metric-tracker).
---

# ads-playbook

온라인 광고 인하우스 마케터를 위한 광고플레이북. 8플랫폼(메타광고·구글광고·구글애즈·틱톡광고·네이버광고·카카오광고·카카오모먼트·링크드인광고·ASA) × 10광고목적(앱광고·앱설치광고·앱가입·앱이벤트·앱내구매·리타겟팅·리드광고·이커머스광고·구독·브랜드광고·오프라인) 광고운영. 시그널·러닝·크리에이티브·측정·안티패턴 일관 처방. 퍼포먼스마케팅 인하우스 실전.

---

## §0 핵심 원칙 (절대 규칙 7개)

| # | 규칙 | 이유 |
|---|------|------|
| 1 | **목적 선정 먼저** — 10광고목적(앱광고·이커머스광고·리드광고·브랜드광고 등) 중 무엇인지 확정 후 플랫폼·크리에이티브·입찰 논의 | 목적 오선정 = 실패 1순위. ROAS 목표에 Reach 캠페인 = 실패 |
| 2 | **러닝페이즈 편집 금지** — Meta 50 conv/7d, Google PMax 50~100 conv, TikTok Smart+ 50 conv/7d 이전 편집 시 시그널 리셋 | 편집 = 7일 재학습 = 예산 낭비 |
| 3 | **시그널 복구 3축 동시** — CAPI(서버측) + Consent Mode v2(동의) + 1st party data(Customer Match·MMP). 한 축만 = 30~70% 유실 | iOS14·Chrome·DMA 이후 클라이언트 추적 불가 |
| 4 | **크리에이티브가 최대 레버** — CTR 변동의 56%가 크리에이티브 요인. 2~4주 주기 신규 자산 3~5개 투입 우선 | 타겟·입찰 최적화 < 크리에이티브 교체 |
| 5 | **자동화 Co-Pilot** — Advantage+·PMax·Smart+·Accelerate는 신뢰하되 가드레일(예산캡·CPA·브랜드 제외·시그널) 필수 | 가드레일 없는 자동화 = 카니발라이제이션 |
| 6 | **초보자용 용어 주석 필수** — 약어·기술용어 첫 등장 시 인라인 괄호 주석 (`CPA(전환당 비용)`·`CPI(설치당 비용)`) | 인하우스 신입·비마케터 임원 대상 |
| 7 | **한국 디폴트** — 플랫폼 미지정 시 네이버광고+카카오광고+메타광고+구글광고 4개 우선 검토. 카카오모먼트(비즈보드)·구글애즈 한국 디폴트 매트릭스 | 한국 인하우스 마케터 대상 |

---

## §1 4모드 라우터

| 모드 | 트리거 | 진입 | 산출 |
|------|--------|------|------|
| **M1 진단** | "왜 성과 떨어졌어", "CPA 급등", "광고진단", 러닝 미탈출 | §2 | 진단 리포트 |
| **M2 설계** | "광고세팅", "런칭", "신규 캠페인", "어떤 플랫폼?" | §3 | 세팅 가이드 |
| **M3 운영** | "광고튜닝", "광고최적화", "예산 조정", "빈도 관리", "시즈널" | §4 | 운영 플레이북 |
| **M4 용어** | "CPA가 뭐야", "SKAN 설명", "광고용어" | `→ references/glossary.md` | 용어 설명 |

복합 요청 → 순차 실행.

---

## §2 M1 진단 흐름

```
① 증상 수집 → ② 시그널·러닝 상태 → ③ 4축 진단 → ④ 처방
```

### ① 증상 수집 (핑퐁 필수)
플랫폼·캠페인 타입·광고목적(10종 중)·증상(CPA 급등·노출 급감·러닝 미탈출 등)·기간·최근 변경.

### ② 시그널·러닝 상태 (가장 흔한 근본원인)

| 체크 | 기준 | 실패 시 |
|------|------|---------|
| CAPI/EC 구현 | Meta 매칭율 ≥70%, Google EC 적용 | `→ references/measurement.md` |
| Consent Mode v2 | EU/KR 동의율 확인 | `→ references/measurement.md` |
| 러닝페이즈 | Meta 50 conv/7d, Google PMax 학습기간 | `→ references/tuning_playbook.md` |
| 픽셀 중복·iOS 도메인·AEM | 도메인 1개·이벤트 8개 | `→ references/measurement.md` |

### ③ 4축 진단 매트릭스

| 축 | 질문 | 참조 |
|----|------|------|
| 시그널 | 서버측·동의·1st party 중 빠진 게? | `→ references/measurement.md` |
| 러닝·입찰 | 편집 빈도·예산 급변·입찰전략 오선택? | `→ references/tuning_playbook.md` |
| 크리에이티브 | 동일 자산 14일+·Hook Rate <25%·UGC 0개? | `→ references/creative.md` |
| 타겟·구조 | 과도한 세그먼트·중복·PMax가 Search 잡아먹음? | `→ references/antipatterns.md` |

### ④ 처방 템플릿
증상 → 근본원인 → 즉시조치(≤7일) → 구조조치(≥2주) → 예상 회복 지표.

---

## §3 M2 설계 흐름

```
① 목적 확정 → ② 플랫폼 조합 → ③ 캠페인 타입·입찰 → ④ 시그널 세팅 → ⑤ 크리에이티브 → ⑥ 런칭 체크리스트
```

### ① 10목적 확정
`→ references/objective_matrix.md` — 라우터. 상세:
- 앱광고 5종(앱다운로드·앱설치광고·앱가입광고·앱내이벤트·앱내구매·리텐션·리타겟팅·리마케팅) → `→ references/objective_app.md`
- 이커머스광고·구독 → `→ references/objective_commerce.md`
- 리드광고(B2B·B2C) → `→ references/objective_lead.md`
- 브랜드광고·오프라인 → `→ references/objective_brand.md`

### ② 플랫폼 조합 룰 (한국 디폴트)

목적별 1순위·2순위·보조 플랫폼 매트릭스 → `→ references/objective_matrix.md`
플랫폼 상세: `→ references/platform_meta.md` · `platform_google.md` · `platform_tiktok_asa.md` · `platform_naver_kakao.md` · `platform_x_linkedin.md`

### ③ 캠페인 타입·입찰 핵심 (광고최적화 출발점)
- 학습 적음 (월 <50 conv) → Max Conv·CBO·Advantage+
- 충분 (월 ≥50) → tCPA
- 가치 추적 가능 → tROAS / Value Optimization
- 신규 진입 → Broad Match + Smart Bidding (구글애즈) / Advantage+ Audience (메타광고)

### ④ 시그널 세팅
`→ references/measurement.md` — Pixel+CAPI·GA4+EC·Consent v2·iOS 도메인·AEM·MMP·Customer Match.

### ⑤ 크리에이티브 브리프
`→ references/creative.md` — 3초훅·UGC·9:16·ABCD·자산개수.

### ⑥ 런칭 체크리스트
`→ references/launch_checklist.md` — 22항목.

---

## §4 M3 운영 흐름 (광고튜닝)

| 작업 | 주기 | 스포크 |
|------|------|--------|
| 러닝페이즈 탈출·CPA 모니터 | 일·주 | `→ references/tuning_playbook.md` |
| 예산 스텝업 | 3~5일 | `→ references/tuning_playbook.md` |
| 크리에이티브 로테이션 | 2~4주 | `→ references/creative.md` |
| A/B·Incrementality | 월 1+ | `→ references/tuning_playbook.md` |
| 주간·월간 리뷰·시즈널 | 정기 | `→ references/launch_checklist.md` |

---

## §4.5 조건부 로딩 매트릭스 (references 18개 과부하 방지)

허브는 분기만. 스포크는 **질문 맥락에 맞는 것만** 로드. 전량 로드 금지.

| 질문 맥락 | 로드 1차 | 로드 2차 (필요시) | 로드 금지 |
|-----------|----------|--------------------|-----------|
| 목적 불명 | `objective_matrix.md` | 해당 objective 파일 1개 | 플랫폼 파일 전량 |
| 플랫폼 1개 지정 | 해당 `platform_*.md` 1개 | `measurement.md` | 다른 플랫폼 파일 |
| 측정·CAPI·SKAN | `measurement.md` | `glossary.md` | objective/platform 파일 |
| 크리에이티브 | `creative.md` | `antipatterns.md` | 나머지 전량 |
| 러닝·입찰·튜닝 | `tuning_playbook.md` | `measurement.md` | objective 파일 전량 |
| 런칭 직전 | `launch_checklist.md` | `measurement.md` | — |
| 용어 질문 | `glossary.md` | — | 나머지 전량 |
| 최신 정책 확인 | `latest_2026q2.md` | — | — |

**원칙:** 1차 로드 후 부족할 때만 2차. 동시 3개+ 로드 = 토큰 폭식 → 허브 분기 재점검.

---

## §5 공통 참조

| 주제 | 포인터 |
|------|--------|
| 광고용어 사전 130+ | `→ references/glossary.md` |
| 측정·트래킹 | `→ references/measurement.md` |
| 안티패턴 24+ | `→ references/antipatterns.md` |
| 2026년 4월 최신 | `→ references/latest_2026q2.md` |

---

## Gotchas

| 함정 | 대응 |
|------|------|
| 용어 주석 누락 | 약어 첫 등장 시 괄호 주석 — `CPA(전환당 비용)`·`CPI(설치당 비용)` |
| 목적 없이 플랫폼부터 논의 | §3-①로 되돌아가 광고목적 확정 후 재진입 |
| 러닝 중 편집 제안 | 러닝상태 먼저 확인 → "편집 대신 신규 ad set" 제안 |
| PMax·Advantage+ 블랙박스 방치 | 가드레일(브랜드 제외·Audience Signal·예산 캡) 동반 제안 |
| iOS/앱광고 질문에 SKAN 누락 | 앱 캠페인 = SKAN 4 + MMP 자동 포함 |
| 한국 디폴트 누락 | 플랫폼 미지정 시 네이버광고·카카오광고 후보 제시 |
| B2B 리드광고에 LinkedIn 누락 | 링크드인광고 Lead Gen Form + Accelerate 최우선 |
| 리서치 인용시 인라인 URL | 본문은 포인터만, URL은 references 각 파일 |
| 최신 변경 미반영 | 2026-04 만료 시 `→ references/latest_2026q2.md` 업데이트 알림 |

---

## Self-Check

스킬 수정 후 검증:

```bash
python3 scripts/validate.py ./ads-playbook/
# grade: PASS → 통과. FAIL → errors 보고 후 skill-builder 재발동
```

검증 항목: SKILL.md 크기·필수 섹션·스포크 파일·evals 케이스·version 필드·한국 디폴트 보존.
evals: `evals/cases.json` — 5개 회귀 케이스 (진단·설계·운영·용어·B2B).
