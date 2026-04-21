# objective_commerce — 이커머스·구독 2목적

웹 기반 전자상거래와 정기 구독 모델을 위한 광고 목적.

## 목적 7: 이커머스 구매 (E-commerce Purchase)

### 정의 및 KPI
- **정의**: 웹·Shopify·자사 쇼핑몰에서 구매 완료
- **KPI 1순위**: ROAS (Return On Ad Spend) / AOV (Average Order Value)
- **KPI 2순위**: Conversion rate / CPA(purchase)
- **벤치마크**: 패션 ROAS 2:1~3:1, 전자제품 ROAS 1.5:1~2.5:1, 식품 ROAS 2:1~4:1

### 플랫폼별 구현

#### Meta ASC Shopping (App Store Campaign + Catalog)
- Campaign objective: "Conversions" (웹 기반)
- Optimization event: "Purchase" (웹픽셀 또는 CAPI)
- Product Catalog 필수: SKU·가격·재고·이미지
- Ad format: Dynamic Product Ads (DPA) → 사용자가 본 상품 자동 추천
- 타게팅: Lookalike (구매 사용자) + Broad (관심사)
- ROAS 목표: 설정 가능 (예: 2.5x → CPA 자동 조정)

**CAPI Purchase event (필수)**:
```json
{
  "event": "Purchase",
  "event_id": "uuid",
  "user_data": { "email": "hash", "phone": "hash" },
  "content": {
    "contents": [
      { "id": "sku_123", "quantity": 2, "title": "Blue T-Shirt" }
    ],
    "content_name": "Blue T-Shirt x2",
    "content_type": "product",
    "value": 59.98,
    "currency": "USD"
  }
}
```

#### Google PMax + Merchant Center
- Campaign objective: "Maximize conversion value" (ROAS 기반)
- Merchant Center: 제품 데이터 자동 동기화 (SKU·재고·배송)
- Asset: 텍스트·이미지·로고·영상 업로드 → Google이 자동 조합
- 도메인: Search·Display·YouTube·Gmail·Discover 자동 배치
- Bidding: Target ROAS 설정 (예: 3.0)
- **강점**: 멀티채널 자동화·재고 연동·전국 배송 최적화

#### Naver 쇼핑검색 + 성과형 광고
- 쇼핑검색: 자체 쇼핑몰 관리자 센터 > 상품 등록
- 광고: 클릭당 비용 (PC/모바일 따로)
- 타게팅: 키워드 또는 카테고리 (사용자 의도 기반)
- **강점**: 한국 검색 시장 장악·로컬 배송 신뢰도 높음
- **약점**: 국제 확장 약함·DB 동기화 복잡

#### Kakao 비즈보드
- 이미지·제품 카드 형식
- 비용: 클릭당 + 전환당 하이브리드
- **강점**: 카톡 광고 + 다음 쇼핑 통합
- **약점**: 재고 관리 API 미흡

### Catalog 설계 (Meta·Google)

**필수 피드 필드**:
```
id (SKU)
title (상품명 50자 이내)
description (상세 설명 5000자)
price (현재가)
currency
image_url (높은 해상도, 정사각형 또는 4:3)
category (대·중·소 분류)
inventory (재고 수)
url (구매 페이지 링크)
```

**추가 필드 (성능 ↑)**:
```
sale_price (할인가, 있으면 표시)
brand
stock_status (in stock / out of stock)
rating (상품 평점)
```

### 제품군별 예산 분배

| 우선순위 | 제품 | 전략 | 예산 배분 |
|---|---|---|---|
| 1순위 | 베스트셀러 | ROAS 높음·알려짐 | 50% |
| 2순위 | 신상품 | 낮은 ROAS 감수·인지 목표 | 30% |
| 3순위 | 롱테일 (낮은 판매량) | 디스커버리·틈새 노점 | 20% |

**조정 룰**:
- 베스트셀러 ROAS > 4.0 → 예산 +50%
- 신상품 ROAS < 1.5 → 2주 후 중단 또는 크리에이티브 교체

### BFCM·Q4 전략 (Black Friday / Cyber Monday / 연말)

**사전 3주 (Awareness)**:
- Google Reach·Meta Brand Awareness 캠페인
- 목표: Reach 100만+ (신규 고객 시장 조성)
- 예산: 총 Q4 예산의 20%

**1주전~당일 (Conversion)**:
- PMax·ASC Shopping 전환 집중
- ROAS 목표 완화 (일시적으로 1.5:1까지 허용)
- 재고 신호 강화 (Inventory feed 실시간 업데이트)
- 예산: 총 예산의 60%

**사후 1주 (Retention)**:
- 구매자 재타겟 (Up-sell·Cross-sell)
- Meta Custom Audience (구매 7일 이내)
- ROAS 목표 높음 (3.0 이상)
- 예산: 총 예산의 20%

### 실패 신호 & 탈출 기준

❌ **신호 1**: Catalog 이미지 품질 낮음
→ 클릭율 ↓ 50% · ROAS ↓ 1:1로 추락

❌ **신호 2**: 재고 업데이트 지연 (1주 이상)
→ 고객이 광고 클릭 후 "품절" → 신뢰도 ↓

❌ **신호 3**: 배송비·반품 정책 불명확
→ 장바구니 이탈율 ↑ 30%

---

## 목적 8: 구독·결제 전환 (Subscription & Recurring Payment)

### 정의 및 KPI
- **정의**: 정기 구독 또는 정기 결제 시작 (월간·연간)
- **KPI 1순위**: LTV/CAC ratio / Subscription conversion rate
- **KPI 2순위**: Churn rate (이탈율)
- **벤치마크**: SaaS 변환율 2~5%, 구독 앱 변환율 1~10%

### 플랫폼별 구현

#### Google PMax tROAS (최우선)
- Campaign objective: "Maximize conversion value"
- Optimization event: "Subscription purchase" (또는 custom)
- Bidding: target-ROAS 설정 (예: 2.0)
- 조건: 최소 50 subscription/30days 러닝 데이터 필수
- **강점**: Long-term value 학습 가능 (정기 매출 신호)

**수익 추적 (Multi-touch)**:
```
Month 1: $9.99 (첫 결제)
Month 2: $9.99 (갱신)
Month 3: $9.99 (갱신)
→ 3개월 LTV = $29.97 (모두 conversion value로 기록)
```

#### Meta Value Optimization (보조)
- Campaign objective: "Conversions"
- Optimization event: "Subscribe" (또는 "InitiateSubscription")
- Bidding: Bid Cap (최대 CPA) 또는 Dynamic
- 타게팅: Lookalike (기존 구독자) + Broad (관심사)
- **약점**: 정기 매출 신호 메타에 도달하기 어려움 (iOS 제약)

**CAPI Subscribe event**:
```json
{
  "event": "Subscribe",
  "event_id": "uuid",
  "user_data": { "email": "hash" },
  "value": 9.99,
  "currency": "USD",
  "custom_data": { "plan": "monthly", "duration": "annual" }
}
```

### 구독 모델 설계

#### 가격 계층화

| 플랜 | 가격 | 대상 사용자 | 특징 |
|---|---|---|---|
| Free | $0 | 모두 | 기본 기능만 |
| Starter | $4.99/month | 개인 | 1개월 무료 시험 |
| Pro | $9.99/month | 소규모팀 | 음성 지원 |
| Enterprise | $99/month+ | 대규모 조직 | 맞춤 SLA |

#### 트라이얼 전략

**7일 무료 트라이얼** → 전환율 ↑ 60%
```
Day 1: 즉시 기능 접근
Day 5: 리마인더 "3일 남음"
Day 7: 자동 결제 또는 취소 옵션
```

**구매 후 30일 환불** → 신뢰도 ↑
```
사용자가 구매 후 30일 이내 환불 신청 가능
→ 구매 장벽 ↓ 40%
```

### CAC & LTV 기반 입찰 설정

```
LTV 계산:
  Monthly subscription: $10
  Avg. subscription duration: 12개월
  LTV = $10 × 12 = $120

Acceptable CAC:
  CAC = LTV × 0.3 = $36 (30% 규칙)

PMax target-ROAS:
  ROAS = LTV / CAC = 120 / 36 = 3.3x
```

**매월 재검토**:
- Churn rate ↓ → LTV ↑ → ROAS 목표 상향
- Churn rate ↑ → LTV ↓ → 광고 예산 축소

### Churn 최소화 (마케팅 외 협력 필수)

| 주기 | 액션 | 효과 |
|---|---|---|
| Day 1 | 온보딩 이메일·비디오 튜토리얼 | Churn ↓ 10% |
| Day 7 | "이용 활황" 리포트 (최신 기능 강조) | Churn ↓ 5% |
| Day 30 | 갱신 전 리마인더 | Churn ↓ 15% |
| Day 45 | 초기 이탈자 대상 50% 할인 쿠폰 | Re-activate ↑ 20% |

### 실패 신호

❌ **신호 1**: 환불 요청 > 15%
→ 상품·가격·기대치 mismatch

❌ **신호 2**: Trial 종료 후 conversion < 1%
→ 온보딩 실패 또는 기능 불충분

❌ **신호 3**: 입찰 ROAS 2.0 이상으로 올려야 함
→ Churn rate 과도·LTV 낮음

---

## 이커머스 vs 구독: 선택 기준

| 요소 | 이커머스 (목적 7) | 구독 (목적 8) |
|---|---|---|
| **수익 흐름** | 일회성 | 정기 |
| **CAC 회수** | 첫 주문 내 | 3~6개월 내 |
| **광고 최적화** | ROAS (단기) | LTV/CAC (장기) |
| **예산 효율** | 즉시 (ROI 판단 빨름) | 느림 (3개월 필요) |
| **고객 관리** | 일시적 | 장기 관계 |

**선택 팁**:
- 초기 사업: 목적 7 (현금흐름 빨라야 함)
- 안정화 사업: 목적 8로 전환 (수익 예측 가능)
- 병렬: 목적 7 + 8 번들 (One-time + Subscription 동시 판매)
