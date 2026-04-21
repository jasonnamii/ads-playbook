# platform_meta — Meta 광고 운영 가이드

인하우스 마케터가 Meta(Facebook/Instagram/Threads)를 운영할 때 핵심.

## 개요

2026년 Meta는 ODAX(Outcome-Driven Ad Experiences) 프레임워크로 완전히 재편. Andromeda AI 엔진이 자동화 담당하고, 인하우스 마케터는 신호(CAPI+픽셀), 크리에이티브 파이프라인, 예산 배분에만 집중. 강점: 리타겟팅 효율(ROAS 4.2배 평균), 자동화 성숙도. 약점: iOS 신호 손실, 크리에이티브 피로.

**언제 쓰나:** 리드/구매/앱설치 전환, 리타겟팅 최고 성과. **언제 피하나:** 브랜드 인지만 목표면 YouTube/Demand Gen 우선.

**계정 구조:** 계정 → 캠페인(CBO) → Ad Set(Audience) → Ad(크리에이티브).

## ODAX 6목표 체계

| 목표 | 최소 일예산 | 러닝페이즈 기준 | 우선 신호 |
|------|----------|--------------|----------|
| Awareness | $50–100 | 노출 자유 | 도달범위 |
| Traffic | $100–150 | 클릭 50회/7일 | 브라우저 신호 |
| Engagement | $75–150 | 상호작용 50회/7일 | 좋아요/댓글 |
| App Promotion | $150–300 | 설치 50회/7일 | Firebase + SKAN |
| Leads | $100–200 | 리드 50개/7일 | Instant Form |
| Conversions | $150–500 | 구매 50건/7일 | CAPI + 전환 값 |

**핵심 변화:** 이전 11개 목표 → 6개 정렬. 목표 선택 오류 = 캠페인 실패 #1 원인.

## 캠페인 타입별 구현 매트릭스

### 앱 설치 (App Promotion)
- Advantage+ App Campaign (AAC) 필수
- CBO + SKAN 4.0 설정
- 일예산: $150–300/일
- 러닝페이즈: 설치 50회/7일
- 초기 CPI 목표: $3–8 (카테고리별 편차)
- 크리에이티브: 9:16 수직 비디오 우선, 2–4주 신규 자산 투입

### 리드 수집
- "Leads" 목표 + Instant Form (Meta 플랫폼 내 양식)
- Highest Volume 또는 Cost Cap ($5–20/리드)
- 러닝페이즈: 50리드/7일
- Form 최적화: 필드 수 최대 6개 (이하일수록 완료율 상승)
- 품질 기준: 5분 내 연락 시 전환율 9배 향상

### 이커머스 구매 (Conversions + DPA)
- Dynamic Product Ads (DPA) 또는 Advantage+ Shopping Campaign (ASC)
- Value Optimization (AOV 기반)
- ROAS Cap: 목표 ROAS의 80% 설정
- 초기 ROAS 목표: 1.5–2.0배, 안정화: 2.5–4.0배
- 제품 피드 업데이트 자동화 필수

### 리타겟팅
- 강점 영역 (ROAS 4.2배, 평균)
- Audience 위계: Hot(장바구니 미완료) → Warm(30일 방문) → Cold(180일 방문)
- Audience 중복 >25% 회피 (입찰 경쟁)
- ABO 권장 (Audience별 예산 고정 $50–200/일)

### 리텐션/재참여
- "Conversions" 또는 "Engagement" 목표
- Custom Audience: 180일 웹사이트 방문자, 365일 팔로워
- Frequency Cap: 일 2–3회 이하

## 입찰 전략

### CBO vs ABO

| | CBO | ABO |
|---|---|---|
| **스케일** | $500+ 권장 | 테스트, 소규모 |
| **자동화** | 높음 (ad set 자동배분) | 수동 제어 |
| **성능** | 전환 20% 더 많음 | 예측 가능 |
| **권장** | Phase 2+ (스케일) | Phase 1 (테스트) |

**최적 경로:** Phase 1 ABO($50–100/set) → Phase 2 CBO($500+).

### 입찰 방식

| 방식 | 사용 시점 | 특징 |
|---|---|---|
| Highest Volume | 초기, 데이터 부족 | 가장 많은 전환 |
| Cost Cap | 안정화 후 | CPA 목표 × 1.2–1.5 |
| Bid Cap | CPA 엄격 제어 | 위험 높음 |
| Value Optimization | AOV/LTV 충분 | 수익 최적화 |

**2026 권장:** 초기 Highest Volume → 50 conversions 후 Cost Cap.

## CAPI (Conversions API) 필수 인프라

### 왜 필수?
- iOS 14.5+ 프라이버시 제약
- 3rd-party 쿠키 deprecated
- Pixel 단독: 50–65% 손실 → CAPI 추가 시 95%+ 복구

### 3가지 구현

| 방식 | 복잡도 | 비용 | 추천 상황 |
|---|---|---|---|
| CAPI Gateway | 매우 낮음 | $0 | 초기, 소규모 |
| 직접 구현 (SDK) | 높음 | 내부 개발 | 대규모, 커스터마이징 |
| 통합 도구 (Segment) | 중간 | $100–500/월 | 멀티채널 |

### 체크리스트
- 고객 식별자 (Email, Phone) 해싱
- Event ID 생성 (중복 제거)
- Event Match Quality (EMQ) 70% 이상
- Pixel vs Server 비율 모니터링 (80:20 ~ 50:50)

## iOS 신호 복구 & SKAN 4.0

**SKAN 한계:** 24–48시간 지연, 3개 postback, 앱 설치만 추적, 낮은 세분도.

**적응 전략:**
1. 짧은 귀인 윈도우 (7일 CTC → 1일로 축소)
2. 대량 데이터 (더 큰 예산, 더 많은 설치)
3. CAPI 병행 (웹→앱 전환도 추적)
4. Deep Link (설치 후 특정 화면으로 이동)

## 러닝페이즈 탈출 & 튜닝

### 50 Conversions / 7 Days 기준
```
필요 일예산 = (Target CPA × 50) ÷ 7
예: CPA $60 → ($60 × 50) ÷ 7 = $429/일 최소
```

### 금지 사항 (7일 안)
1. 예산 편집 (리셋)
2. Audience 변경 (리셋)
3. 크리에이티브 스왑 (부분 리셋)
4. 입찰 방식 변경 (리셋)

### CPA 급등 대응 (Learning Limited)
**증상:** 3–4일 CPA $15 → 5–7일 $45 (정상).

**대응:**
1. 예산 +30–50% (더 많은 데이터)
2. Audience 1–2개 추가 (다양성)
3. 크리에이티브 추가 (3–5개 변형)
4. **절대 위축하거나 중지하지 말 것**

## 크리에이티브 다양성 전략

### Dynamic Creative Optimization (DCO)
- 5 images × 5 headlines × 5 body = 125 조합
- Meta AI 자동 테스트
- 성과: CTR 30%, 전환율 20% 향상

### Advantage+ Creative (2026 신규)
- GEM(Generative Ads Recommendation Model) 기반
- 업로드 자산에서 신규 변형 자동 생성
- 로고, 폰트, 색상 자동 추출 (브랜드 일관성)
- **의무:** AI 생성 콘텐츠 공시 필수

### 크리에이티브 파이프라인
**목표:** 2–4주 단위 신규 자산 투입.

```
주 3–5개 신규 자산 생성
  ↓ 5–7일 배치 런칭
  ↓ 2주 후 패배자 제외, 승자 복제
  ↓ 신규 자산 투입 (피로 관리)
```

**비용 절감:**
- AI 이미지 생성: $0.05–0.20/개
- UGC 클론: $100–300/월
- Advantage+ Creative: $0

## 빈도 관리 & 광고 피로

### 빈도 캡 가이드
| 캠페인 | 권장 빈도 | 이유 |
|---|---|---|
| Brand Awareness | 2–4 | 한번이 충분 |
| Cold Traffic | 4–7 | 신뢰 구축 |
| Retargeting | 7–12 | 높은 Intent |

### 피로 지표
**경고:** Frequency > 3.0 AND CPA ↑ 20%.

**대응:** Frequency Cap (1차) → 크리에이티브 로테이션 (권장).

## 2026년 4월 최신

- **Advantage+ API 통합:** 별도 ASC/AAC API 폐지, 단일 Campaign 구조
- **생성형 AI 광고:** 상품→이미지+비디오 자동 생성, 음성 안내 추가
- **공시 의무:** AI 생성/수정 콘텐츠 공시 필수 (미공시 시 거절)
- **Reels 확대:** 인벤토리 60% → 70% 목표 (모바일 우선)
- **Attribution 단축:** Click Window iOS 7일 → 1일

## 인하우스 실전 노하우

### 1. 예산 집중 > 조각내기
❌ $500/일 ÷ 10 ad sets = 각 Learning Limited
✅ 1–2 ad sets에 $500 집중 = 빠른 Learning

### 2. 7일 기다리기 필수
데이터 부족 시 편집 금지. CPA 급등은 정상 학습 신호.

### 3. 크리에이티브 실질 다양성
❌ 텍스트만 다른 5개
✅ 이미지/비디오/스타일 실질 변형

### 4. Cold + Warm + Hot 균형
예산의 30–50%를 Retargeting에 배분. Warm 채널이 최고 ROI.

### 5. CAPI 초기 투자
초일부터 CAPI 설정 = 이후 모든 최적화 정확도 3배.

### 6. Frequency 로테이션 우선
Cap만으로는 부족. 2–4주마다 신규 자산 투입 필수.

### 7. Landing Page 매칭
할인 광고 → 풀가격 페이지 = 거절. Ad Copy와 완전 동기화.

### 8. 계절성 2–4주 전 준비
휴일 쇼핑 시즌, 프로모션 미리 계획.

### 9. 매일 편집 금지
3–7일 단위 리뷰만. 과도한 최적화 피하기.

### 10. Lookalike 신중하게
Seed Audience의 명확한 정의 필수. 무분별 확대 금지.

## 주의 (Gotchas)

| 함정 | 대응 |
|---|---|
| 예산 편집으로 Learning 리셋 | 7일 이상 편집 금지 |
| CAPI 없이 iOS 신호 전부 손실 | 초일부터 CAPI 설정 |
| Frequency 과다 (>5) | 크리에이티브 로테이션으로 해결 |
| Audience 중복 >25% | Audience 재정의, 겹침 최소화 |
| AI 생성 콘텐츠 미공시 | 공시 필수 (March 2026 정책) |
| 단순 Pixel 추적만 의존 | CAPI로 95%+ 복구 |
| 목표 없는 테스트 | 구체적 KPI(CPA $25 등) 설정 |
| 한 자산만 반복 사용 | 2–4주 신규 자산 투입 |
