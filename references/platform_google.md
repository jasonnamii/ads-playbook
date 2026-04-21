# platform_google — Google Ads 운영 가이드

인하우스 마케터가 Google(Search/PMax/Shopping/Display/YouTube/Apps)을 운영할 때 핵심.

## 개요

2026년 Google Ads는 **AI 자동화 + 깨끗한 데이터** 패러다임으로 정착. 인하우스 역할은 Co-Pilot으로 전환: 추적 정합성(Conversion tracking integrity) + 고품질 크리에이티브 + 의도적 경계(Negative keywords, Brand exclusions). 강점: Search 고의도(최고 ROI), PMax 크로스채널, Shopping 정밀도. 약점: Consent Mode v2 데이터 손실, Customer Match API 마이그레이션 복잡도.

**언제 쓰나:** Search(의도 기반), 이커머스(Shopping), 신규 고객(Demand Gen), 앱설치(UAC). **언제 피하나:** 디스플레이만으로 구매 유도 금지, 배치 명확화 필수.

**계정 구조:** 계정 → 캠페인(타입별) → Ad Group(키워드) → 광고/확장.

## 캠페인 타입 8가지 & 각각의 2026년 역할

| 캠페인 타입 | 주요 목표 | 입찰 권장 | 최소 예산 | 신호 필수 |
|---|---|---|---|---|
| **Performance Max** | 멀티채널 전환 극대화 | tROAS/Max Conversions | $500–1000/월 | GA4 + Enhanced Conversions |
| **Search** | 고의도 키워드 전환 | tROAS (50+conv) → Cost Cap | $200–500/월 | Conversion tracking (정확도 중요) |
| **Shopping** | 이커머스 상품 판매 | tROAS/Max Conversion Value | $300–600/월 | 피드 품질, Enhanced Conversions |
| **Demand Gen** | 신규 고객 인식 창조 | tROAS/Target CPA | $200–400/월 | GA4, Website visitors |
| **YouTube (Reach)** | 브랜드 도달·회상 | CPM (자유) | $50–200/월 | 불릿 4: 자동 비디오 피하기 |
| **Display** | 리마케팅·재방문 | Manual CPC → Automated | $100–300/월 | 고객 리스트, 웹사이트 방문자 |
| **Local/PMax Local** | 오프라인 매장 방문 | 자동 입찰 | $100–300/월 | 로컬 피드, Google My Business |
| **Apps (UAC)** | 앱 설치·참여 최대화 | tCPA (초기) → tROAS | $200–500/월 | Firebase 4+ events, Signal engineering |

## 광고 목적별 실전 구현

### 앱 설치 (Universal App Campaigns)
- **자동화:** Smart Bidding (tCPA 초기, 30일 후 tROAS)
- **신호:** Firebase App Installation event + 첫 24–48h 플레이 행동 신호
- **최소 데이터:** 월 50+ 설치 (tROAS 활성화 조건)
- **크리에이티브:** 주간 3–5개 신규 테스트 (주기적 리프레시)
- **2026 신규:** Rewarded UA 플랫폼 82% 우수 성과

### 앱내 가입 (Firebase Custom Event)
- Firebase event → Google Ads 전환 연동
- tCPA로 목표 설정
- Enhanced Conversions로 hashed email 매칭
- Consent Mode v2: ad_user_data + ad_personalization 동의 확보 필수

### 리드 수집 (Lead Generation)
- **Google 도구:**
  - Lead Form Extension (Search 전용)
  - Discovery Lead Form (Gmail, Discover)
  - PMax + Lead conversion action
- **목표 CPA:** $5–20 (리드당)
- **최소 데이터:** 30–50 conversions/30d (tCPA 전환)
- **랜딩페이지 최적화:** SSL, 프라이버시 정책, 후기, 인증 (클릭율 2–3배)

### 이커머스 구매 (Shopping + PMax 하이브리드)
**Best Practice:**
- **80% 예산 → Shopping** (고의도, 기존 고객)
- **20% 예산 → PMax** (신규 고객, 크로스셀)

**피드 최적화:**
- 제목: 브랜드 + 상품유형 + 색상/사이즈 프로그래밍
- 이미지: 깔끔한 흰색 배경 우선 (라이프스타일 피하기)

**입찰:**
- tROAS (AOV 기반)
- Enhanced Conversions for Leads (전환 복구 5–15%)

**주의:** Content API for Shopping 2026년 8월 폐지 → Merchant Center 마이그레이션 필수

### 리타겟팅 (Display)
- **신호:** "Your Data Segments" (개편됨)
- **우선순위:** 푸시/이메일 오디언스 업로드 > 광범위 타게팅
- **구조:** 고온도(장바구니) → 중온도(30일 방문) → 저온도(180일 방문)

### 오프라인 방문 (PMax for Local)
- 로컬 피드: 주소, 영업시간, 전화, 매장별 특가
- 지역 타게팅: 5km 반경 + 근처 검색어
- 핵심 지표: Cost per Store Visit, Cost per Phone Call

## Smart Bidding 체계 & 선택 트리

### tCPA vs tROAS 결정

| | tCPA | tROAS |
|---|---|---|
| **적용 대상** | 초기 단계, 저전환량 | 성숙 계정, 50+ conv/30d |
| **목표** | 유닛당 비용 | 수익률 |
| **전환 값** | 불필수 | 필수 (정확도 중요) |
| **성능** | Q1 2026 기준치 | 38% 높은 ROAS vs 수동 |

**2026 권장 경로:** 론칭 → tCPA (30일, 30+conv) → tROAS로 전환 → Portfolio 전략

### Max Conversions vs Max Conversion Value

| 전략 | 언제 | 주의 |
|---|---|---|
| Max Conversions | 전환 수 극대화, 리드 목표 | 낮은 가치도 포함 |
| Max Conversion Value | 수익 극대화, AOV 편차 큼 | 전환 값 정확도 필수 |

### Portfolio Bid Strategy
- 다중 캠페인 공유 자동화 비딩 (tCPA, tROAS, Max Conversions 등)
- 중앙 집중식 목표 조정
- **제약:** PMax 미지원

## Performance Max (PMax) 심화

### Asset Groups 품질 = 성능의 핵심

**각 Asset Group:** 최대 15 제목 + 5 설명 + 20 이미지 + 5 비디오

**2026 Best Practice:**
| 항목 | 가이드 |
|---|---|
| 이미지 | 깔끔한 배경(흰색) 우선 > 라이프스타일 |
| 비디오 | 자동 생성 피하기 (25–40% 미달). 간단한 15초 브랜드 비디오 필수 |
| 헤드라인 | 15개 제공 (다양성 최대화) |
| 설명 | 5개, 구체적 가치명제 |
| 통일성 | 크리에이티브 + 랜딩페이지 + 오디언스 신호 동기화 필수 |

### Audience Signals 계층화

**신호의 역할:** 제약 아님 → 방향 힌트 (자동화는 신호 해석).

**2026년 최고 신호 (Priority):**
1. **Customer Match Lists** (최상): CRM 이메일/전화, Google 로그인
2. **Website Visitors:** 30–90일 활동 범위 (체크아웃 포기자 분리)
3. **High-Value Converters:** 다른 캠페인 전환자, LTV 상위
4. **In-Market Audiences:** Google 기성 세그먼트

**계층화 예시:**
```
Asset Group 1 (고의도):
  - Customer Match (기존 고객)
  - Checkout abandoners
  - High LTV converters

Asset Group 2 (상품 관심):
  - Category page visitors
  - In-market audiences
```

### Search Themes & Brand Exclusion (신규 2026)
- **Search Themes:** 키워드 없이 의도 기반 타게팅
- **Brand Exclusion:** 경쟁 브랜드 검색 제외 (비용 절감)

## Search 캠페인 2026년 권장

### Broad Match + Smart Bidding 표준화

**구조:**
- 광범위 매칭으로 자동화 신호 수집
- Smart Bidding (tROAS) 자동 최적화
- Negative keywords로 의도 제어

**정확 매칭 완전 제거 금지:**
- Exact Match (일부 30% 예산) 유지 → 브랜드, 고가 키워드
- Brand Protection 필수

**Negative Keywords 운영:**
- 성별/나이 필터 대신 Negative Keywords
- Category: 경쟁사 + 저품질 + 관련성 낮은 검색

## Consent Mode v2 & 데이터 손실 대응

### 현황 (April 2026)
- **위험:** 동의 미확보 시 데이터 30–50% 손실
- **대응:** Consent Mode v2 필수 구현
- **신호:** ad_user_data (리마케팅) + ad_personalization (개인화)

### 대응 전략
1. **Consent Banner 구현** (Google Consent Mode v2 SDK)
2. **First-Party Data 강화** (GA4 Event, Customer Match)
3. **Server-Side Tracking** (전환 정합성 복구)

## 크리에이티브 & 동영상 전략

### YouTube Reach Campaign (브랜드 인지)
- **포맷:** Bumper(6s, 스킵 불가) → TrueView + Efficient Reach 조합
- **자동 생성 피하기** (25–40% 미달)
- **간단한 15초 브랜드 비디오 필수**
- **자막 필수** (음소거 기본값)

### Demand Gen (신규 고객 창조)
- YouTube + Gmail + Maps + Discover 크로스채널
- 68% 신규 고객 획득 (Search 미노출)
- Discovery Ads + Video Action Campaigns 통합

## 2026년 4월 최신 변경

- **Consent Mode v2 강화:** 동의 미확보 시 추적 불가
- **Customer Match API 마이그레이션:** 구식 API 폐지
- **AI Mode 광고 확대:** Gemini 기반 자동 크리에이티브 생성
- **Content API 폐지:** Merchant Center 통합

## 인하우스 실전 노하우

### 1. 추적 정합성이 모든 것
CAPI/Server-Side Tracking 없이 스마트 비딩은 무의미. 정확도 = ROI.

### 2. Search + PMax + Shopping 역할 분담
- Search: 고의도 (최고 ROI)
- PMax: 신규 + 크로스셀
- Shopping: 이커머스 표준

### 3. Negative Keywords는 방어, Audience는 공격
- Negative: 경쟁사, 저품질 필터링
- Audience: 고온도 고객에 집중

### 4. Asset Group 품질 > 자동화 신뢰
구성요소가 좋으면 AI가 자동으로 성과 낸다.

### 5. First-Party Data 강화
쿠키 없는 시대 → GA4, Customer Match, CRM 통합 필수.

### 6. Consent Mode v2 필수
동의 미확보 = 30–50% 신호 손실. 초기 구현 필수.

## 주의 (Gotchas)

| 함정 | 대응 |
|---|---|
| Broad Match 신뢰 부족 | Smart Bidding + Negative Keywords 조합 |
| 추적 정합성 부실 | CAPI/Server-Side 구현 선행 |
| 자동 생성 비디오만 사용 | 간단한 브랜드 비디오 필수 |
| Consent Mode v2 미구현 | 30–50% 신호 손실 (즉시 대응) |
| Customer Match API 마이그레이션 지연 | 2026년 내 완료 필수 |
| PMax 신호 과다 제한 | Audience Signals는 힌트 (제약 아님) |
| Asset Group 부실 구성 | 15 headlines + 5 descriptions + 20 images 최소 |
| Negative Keywords 불충분 | 월 1–2회 리뷰 + 추가 |

