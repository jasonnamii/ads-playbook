# objective_matrix — 10광고목적 × 8플랫폼 라우터

광고목적(Objective) 선정이 모든 캠페인의 출발점이자 기초. 잘못 선택하면 플랫폼·크리에이티브·입찰 전략을 아무리 최적화해도 실패.

## 10목적 일람

| # | 목적 | 한 줄 정의 | KPI 1순위 | 플랫폼 1순위 | 상세 섹션 |
|---|---|---|---|---|---|
| 1 | 앱 다운로드 | 신규 사용자 앱 설치 | CPI / Install volume | Meta ASC App / Google UAC / Apple ASA | → objective_app.md §1 |
| 2 | 앱 가입 | 앱 설치 후 회원가입 완료 | CPA(signup) / Signup conversion rate | Meta App Promo + Signup event | → objective_app.md §2 |
| 3 | 앱내 이벤트 | 특정 기능 사용·이벤트 참여 | CPA(event) / Event participation rate | Meta App Engagement / TikTok Community Interaction | → objective_app.md §3 |
| 4 | 앱내 구매 | 앱내 결제 완료 (IAP) | ROAS / CPA(purchase) | Meta Value Optimization / Google tROAS App | → objective_app.md §4 |
| 5 | 리텐션·재방문 | 기존 사용자 재활성·방문 | D7/D30 return rate / Retention cost | Meta Custom Audience 리타겟 / Kakao 톡채널 메시지 | → objective_app.md §5 |
| 6 | 리드 수집 | 가입·상담·문의·영업기회 정보 획득 | CPL / Lead quality score | LinkedIn Lead Gen Form (B2B) / Meta Instant Form (B2C) | → objective_lead.md |
| 7 | 이커머스 구매 | 웹·쇼핑몰 구매 완료 | ROAS / AOV / Conversion rate | Meta ASC Shopping + DPA / Google PMax + Merchant Center | → objective_commerce.md §1 |
| 8 | 구독·결제 전환 | 정기결제·구독 시작 | LTV/CAC ratio / Subscription rate | Google PMax tROAS / Meta Value Optimization | → objective_commerce.md §2 |
| 9 | 브랜드 인지 | 타겟층 인지도·기억도 상승 | Reach / Brand lift score | YouTube Reach·Bumper / Meta Reach·Brand Awareness | → objective_brand.md §1 |
| 10 | 오프라인 방문 | 지역 매장·오프라인 장소 방문 | Store visit count / 쿠폰 사용율 | Google PMax Local / Naver 플레이스광고 | → objective_brand.md §2 |

## 의사결정 트리: 내 캠페인의 목적은?

```
├─ 핵심 자산이 앱인가?
│  ├─ Yes → 1~5 검토 (앱 다운로드·가입·이벤트·구매·리텐션)
│  └─ No → 다음 단계로
│
├─ 웹 이커머스·온라인 판매인가?
│  ├─ Yes & 일회성 → 7 (이커머스 구매)
│  ├─ Yes & 구독·정기결제 → 8 (구독·결제 전환)
│  └─ No → 다음 단계로
│
├─ B2B 영업 기회인가?
│  ├─ Yes → 6 with LinkedIn Lead Gen Form
│  └─ No → 다음 단계로
│
├─ 브랜드 자체를 알리려는가? (TOFU stage, 인지도 목표)
│  ├─ Yes & 영상 공급 충분 → 9 (브랜드 인지)
│  ├─ Yes & 예산 제한 → 1·7과 번들 (Discovery 채널에서 인지 확보)
│  └─ No → 다음 단계로
│
├─ 지역 기반 오프라인 매장 방문인가?
│  ├─ Yes → 10 (오프라인 방문)
│  └─ No → 다시 확인
│
└─ B2C 리드 수집 (전시·컨설팅·무료체험)?
   └─ Yes → 6 with Meta Instant Form or Google Lead Form ext.
```

## 플랫폼별 목적 강세도 요약

### Meta (Facebook·Instagram·Threads)
**주력**: 1,2,4,5,6,7,9 (7개)
- 강점: 오디언스 타게팅·1st party 데이터·자동화·DPA·CRM
- 약점: 10 (오프라인), 리드 B2B는 LinkedIn이 낫다

### Google (Search·Display·YouTube·Shopping)
**주력**: 1,4,7,8,9,10 (6개)
- 강점: Intent 포착·PMax·tROAS·Local campaigns·Brand lift 측정
- 약점: 2 (앱 가입), 6 B2B는 LinkedIn이 강함

### TikTok
**주력**: 1,3,7,9 (4개, Discovery 편향)
- 강점: 3초 UGC·Spark·전환도 가능하지만 의도 포착 약함
- 약점: 브랜드 안전성·리드 B2B 없음

### Apple Search Ads (ASA)
**주력**: 1 (앱 다운로드 전담)
- 강점: Intent 정상점 (iOS 사용자 검색)·CPI 경쟁력
- 약점: 1개 목적만 지원

### Naver (파워링크·쇼핑검색·GFA·플레이스)
**주력**: 7,9,10 (3개, 한국 특화)
- 강점: 한국 검색 시장 장악·로컬 검색·쇼핑
- 약점: 앱 마케팅 약함·국제 확장 어려움

### Kakao (비즈보드·카톡채널)
**주력**: 5,6,7 (3개, CRM 채널)
- 강점: 카톡 채널 메시지 (재타게팅)·1st party 데이터·한국 특화
- 약점: 신규 트래픽 창조 약함

### X (Twitter)
**주력**: 1,9 (보조)
- 강점: 실시간 트렌드·브랜드 세이프티 높은 채널 (특정 분야)
- 약점: 정책 불안정성·ROI 예측 어려움·앱 마케팅 약함

### LinkedIn
**주력**: 6 (B2B 리드)
- 강점: B2B 리드 전담·ABM·구직자 타겟·고품질 리드
- 약점: 다른 목적에는 매우 약함

## 실패 사례: 목적 잘못 선택

| 상황 | 실패 선택 | 정답 | 이유 |
|---|---|---|---|
| 캐주얼 게임 앱 | Meta Reach 목적 (브랜드 인지) | Meta App Install (목적 1) | 인지만으로는 설치로 안 이어짐; 직접 IAP 최적화 |
| SaaS B2B 영업 | Google PMax (이커머스) | LinkedIn Lead Gen Form (목적 6) | PMax는 구매 최적화; LinkedIn은 영업 기회/MQL 최적화 |
| 로컬 카페 | Meta Video Views (목적 9) | Google PMax Local / Naver 플레이스 (목적 10) | Video View는 인지; Local은 store visit signal |
| 이커머스 신제품 | Meta App Install (목적 1) | Meta ASC Shopping (목적 7) | 앱은 없음; 웹 쇼핑몰이 자산이므로 DPA/Catalog 우선 |

## 목적별 성공 임계값 (Learning Phase 탈출)

모든 플랫폼이 목적별로 **충분한 전환 데이터** 요구:

- **Meta**: 50 conversions / 7days / ad set
- **Google PMax**: 50~100 conversions / campaign, 2~3주
- **TikTok Smart+**: 50 conversions / 7days
- **Google UAC**: 50 installs / 7days
- **LinkedIn Lead Gen**: 15 conversions / week
- **Naver GFA**: 20 conversions / 7days

**주의**: 러닝 중 목적 변경 = 데이터 리셋 = 다시 러닝. 목적은 캠페인 시작 전에 확정할 것.

## 목적별 핵심 체크리스트

- [ ] 목적 선정 이유를 1줄로 쓸 수 있나?
- [ ] 해당 목적의 KPI 1순위를 알고 있나? (CPI? ROAS? Reach?)
- [ ] 목적에 최강 플랫폼이 비용 범위 내인가?
- [ ] 전환 데이터를 충분히 (50+ per 7days) 수집할 자신이 있나?
- [ ] 크리에이티브가 목적에 맞나? (앱 설치면 AppStore 링크·클릭 유도, 리드면 폼 클릭 유도 등)
