# objective_brand — 브랜드·오프라인 2목적

직접적인 전환 목표 없이 인지도·기억도를 높거나 오프라인 방문을 유도하는 광고.

## 목적 9: 브랜드 인지 (Brand Awareness & Brand Lift)

### 정의 및 KPI
- **정의**: 타겟층의 브랜드 인지도·상기도·호의도 상승
- **KPI 1순위**: Brand lift (브랜드 인지 상승률, %) / Reach
- **KPI 2순위**: Frequency (사용자 노출 평균 회수) / Video completion rate
- **벤치마크**: 브랜드 lift 3~8% / Reach 효율 $0.5~2 per 1000 impressions (CPM)

### 플랫폼별 구현

#### YouTube (최강)

**YouTube Bumper Ads (6초)**:
- 포맷: 6초 이내 스킵 불가 영상
- 타게팅: 관심사·검색어·채널 (매우 정확)
- 가격: CPM $2~8 (높음)
- 적합: 짧고 임팩트 있는 메시지 (슬로건·로고·감정)

**YouTube TrueView for Reach (15~60초)**:
- 포맷: 처음 5초 후 스킵 가능
- 가격: CPM $1~3 (저렴)
- 타게팅: 매우 광범위 (Broad)
- 적합: 스토리텔링·제품 설명

**YouTube Video Actions**:
```
"Visit website" CTA → 웹사이트 클릭 유도 (인지 + 트래픽)
"Learn more" → 제품 페이지로
```

#### Meta (Facebook·Instagram)

**Campaign objective: Brand Awareness**:
- Optimization event: Impressions (노출 수)
- 타게팅: Broad (좁히지 않음, 최대한 많은 사람)
- 크리에이티브: 15~30초 영상 또는 고해상도 이미지
- 가격: CPM $0.5~2

**Meta Video Views 캠페인**:
- Objective: Video Views
- 입찰: CPV (Cost Per View) 설정
- 3초 이상 시청 = 1 view로 카운트
- 낮은 비용 + 높은 빈도 가능

**Meta Reach & Frequency**:
- 목표 reach: 100만 명
- 목표 frequency: 3회 (평균 노출 회수)
- 기간: 2~4주

#### TikTok

**TopView Ads**:
- 포맷: 60초 이내 영상
- 위치: 사용자가 TikTok 앱 열 때 첫 화면 (가장 프리미엄 위치)
- 가격: CPM $5~15 (매우 비쌈)
- 적합: 대형 캠페인·블록버스터 광고

**Brand Takeover**:
- 포맷: 60초 영상 또는 이미지
- 위치: For You feed 최상단
- 가격: CPM $3~8
- 기간: 1일 전담 가능

**Branded Effects**:
- AR 필터·렌즈 제공
- 사용자가 자발적으로 광고 콘텐츠 생성
- CPM $0.5~2 (저렴하지만 참여도 높음)

#### Naver (한국)

**Naver 브랜드검색**:
```
특정 브랜드명 검색 → 상단 배너·로고·소개 광고
예: "삼성" 검색 시 Samsung 광고 배너 노출
```
- 가격: 클릭당 고정액 (CPC)
- 적합: 이미 알려진 브랜드·신뢰도 강화

**Naver 브랜드검색+**:
- 기존 브랜드검색 + "관심사 기반 리타겟"
- 예: "삼성 검색" + "전자제품 관심 사용자" 조합

**GFA (Growth Feed Advertising)**:
- 네이버 피드·검색 결과에 자동 노출
- 다양한 관심사 사용자 도달 가능

### Brand Lift 측정 (Google·Meta·YouTube)

#### Google Brand Lift Study
- 캠페인 진행 중 특정 사용자에게 설문 (짧은 퀴즈)
- 노출 그룹 vs 미노출 그룹 비교
- 비용: 주 3~5만 원 (추가 비용)

```
질문 예:
1. "이 브랜드를 들어본 적 있나요?" (인지도)
2. "이 브랜드를 추천하시겠어요?" (호의도)
→ 노출 그룹이 미노출 그룹보다 "예" 답변 % 차이 = Brand lift
```

#### Meta Brand Lift
- A/B 테스트 자동 실행
- "Brand awareness" 또는 "Ad recall" 설정 시 자동 계산
- 비용: 무료 (캠페인 비용에 포함)

### 인지·기억도 극대화

| 전략 | 효과 | 비용 |
|---|---|---|
| 높은 빈도 (Frequency 5+) | 기억도 ↑ 60% | 중간 |
| 영상 형식 | 텍스트보다 3배 기억 | 중간 |
| 감정 자극 (웃음·감동) | 기억도 ↑ 40% | 낮음 |
| 유명인·인플루언서 | 신뢰도 ↑ 50% | 높음 |

---

## 목적 10: 오프라인 방문 (Store Visits & Local Traffic)

### 정의 및 KPI
- **정의**: 광고 노출 후 지역 오프라인 매장·장소 방문 유도
- **KPI 1순위**: Store visits (GPS 기반 방문 횟수) / 쿠폰 사용율
- **KPI 2순위**: Foot traffic / 오프라인 구매율
- **벤치마크**: Store visit conversion 0.5~3% (광고 노출 기준) / 쿠폰 사용율 5~20%

### 플랫폼별 구현

#### Google PMax Local & Local Campaigns

**PMax Local**:
```
캠페인 objective: "Store visits"
매장 주소: Google Business Profile 연동
반경: 광고 노출 반경 설정 (5km / 10km / 20km)
```
- 자동화 높음 (PMax는 자동 입찰)
- 타게팅: 위치 기반 + 검색어 (매장 카테고리)
- 가격: CPM $2~6

**Local Campaigns**:
```
여러 매장을 한 캠페인으로 관리
각 매장별 최적 예산 자동 분배
매장별 성과 보고 가능
```

#### Naver 플레이스 광고 (한국 강세)

**플레이스 광고**:
- Naver 지도·플레이스 검색 > 상단 광고 노출
- 예: "카페 강남" 검색 → 광고 카페 우선 노출
- 클릭당 비용 (CPC) 또는 전환당 비용

**플레이스 정보 관리**:
```
매장명·주소·전화·영업시간·사진·리뷰
↓
플레이스 광고 노출 시 함께 표시
→ 클릭 → 지도·방향 안내 → 방문
```

#### Meta Store Traffic / Location

**Campaign objective: Store Traffic**:
- Optimization event: "Store visits" (GPS 기반)
- 타게팅: 매장 반경 내 사용자 또는 이동 경로 사용자
- 크리에이티브: "지금 열어있나요?" / "30% 할인 오늘만"
- CPM $2~4

**위치 타게팅**:
```
현재 타겟 지역 바깥 → 매장으로 유도 (Discovery)
매장 근처 사용자 → 재확인·재방문 (리타겟)
```

### 오프라인 연결 (Offline Integration)

#### 쿠폰·바코드·QR 코드

**전략 1: 디지털 쿠폰**
```
광고 클릭 → "쿠폰 받기" → 카드 또는 휴대폰 저장
→ 매장에서 스캔 → 할인 적용
```
- 추적 가능 (누가 방문했는지 알 수 있음)
- 전환율 측정 가능

**전략 2: QR 코드**
```
광고에 QR 코드 포함 → 스캔 → 매장 할인 페이지 또는 예약
```

**전략 3: 프로모션 코드**
```
"VISIT20" → 20% 할인
광고에 코드 표시 → 매장에서 적용
```

#### Location Extensions (Google)

```
검색광고에 매장 주소·전화 추가 표시
사용자가 광고 클릭 → 지도 또는 전화 연결
→ Store visits 추적 가능
```

### 매장 방문 측정 (GPS)

**방법 1: Google Location Services**
- Google이 광고 노출 사용자의 GPS 추적
- 30일 내 매장 방문 여부 측정
- 개인정보 보호: 익명화 (집계 데이터만 리포팅)

**방법 2: MMP (AppsFlyer·Branch)**
- 앱 기반 방문 추적
- 더 정확하지만 앱 사용자만 가능

**방법 3: POS Integration**
- 매장 결제 시스템과 연동
- 영수증에서 고객 정보 수집 → 광고 노출 여부 매칭
- 한국: 쿠팡·배달앱 같은 결제 플랫폼 연동

### 비용 구조

| 채널 | 요금 | 추적 |
|---|---|---|
| Google PMax Local | CPM or CPC | 자동 (위치 기반) |
| Naver 플레이스 | CPC | 자동 (클릭) |
| Meta Store Traffic | CPM | 자동 (GPS) |
| 쿠폰·바코드 | 선택사항 | 수동 (스캔) |

---

## 브랜드 인지 vs 오프라인 방문: 통합 전략

```
Phase 1 (Weeks 1-2): 브랜드 인지
  YouTube Bumper + Meta Video Views
  목표: 50만 명 reach
  예산: 총의 50%

Phase 2 (Weeks 3-4): 오프라인 전환
  Google Local + Naver 플레이스
  목표: Store visits 5000명
  예산: 총의 50%
```

### 성공 체크포인트

- [ ] 브랜드 인지도 측정? (Brand Lift Study)
- [ ] 매장 위치 정보 최신인가? (Google Business Profile·Naver 플레이스)
- [ ] 오프라인 결제 시스템과 연동되었나?
- [ ] 쿠폰·프로모션 유효한가?
- [ ] Location extension 또는 store visits 추적 ON?
- [ ] 매장 직원이 광고 진행 사실을 아나?
