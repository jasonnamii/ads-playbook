# objective_app — 앱 관련 5목적 심화

앱이 핵심 자산일 때의 5개 목적: 다운로드(목적1)·가입(목적2)·이벤트(목적3)·구매(목적4)·리텐션(목적5).

## 목적 1: 앱 다운로드 (App Install)

### 정의 및 KPI
- **정의**: 신규 사용자가 Apple App Store / Google Play Store에서 앱을 설치
- **KPI 1순위**: CPI (Cost Per Install) 또는 Install volume
- **KPI 2순위**: Installs / day, Quality (D1 retention)
- **벤치마크**: 게임 CPI $0.5~2, 유틸리티 $0.2~1, 소셜 $1~4

### 플랫폼별 구현

#### Meta ASC (App Store Campaign)
- 자동 입찰 기본
- Optimization event: "App Install" 또는 "Subscriptions" (구독 게임)
- 타게팅: Lookalike (기존 사용자·구매자) + Broad (관심사)
- 크리에이티브: 30s 영상 또는 9:16 이미지 (App Preview 우선)
- 비용: $5~20 초기 예산으로 50+ install/7days 목표
- **주의**: iOS 17 이상 Fingerprinting 제한·여러 앱 간 신호 경합 → 관계없는 사용자 섞임

#### Google UAC (Universal App Campaign)
- 자동 입찰·자동 크리에이티브 조합
- Optimization event: "Installs" 또는 "In-app conversions" (먼저 설치만 최적화)
- 입찰 설정: Target CPI 또는 Maximize installs
- Asset 제공: 텍스트(1~5줄)·이미지(4장)·영상(1~3장) → Google이 자동 조합
- 예산: $10~50 일일 (Global scale)
- **팁**: 초기 50 install 후 In-app event로 피벗 가능

#### Apple Search Ads (ASA)
- 유일한 "Intent 정상점" 앱 마케팅 채널
- 사용자가 App Store에서 직접 검색 → 광고
- 키워드: 앱명·경쟁사명·카테고리 (검색량 따라 노출 결정)
- 입찰 모드: Maximize conversions (CPI 최소화) 또는 Targe CPI
- CPP (Cost Per Tap): $0.1~1, CPI는 CTR에 따라 결정
- **강점**: 구글/메타보다 저렴·Intent 강함
- **약점**: iOS 사용자만·검색량 제한

#### TikTok Smart+
- 자동 최적화 (메타와 유사)
- Optimization event: "App Install"
- 타게팅: 광범위 (특별히 좁히지 않음)
- 크리에이티브: 9:16 영상 권장 (3~15초, Hook 중요)
- CPI 상대적 높음 ($1~3) 하지만 대량 install은 가능
- **팁**: 브랜드 안전성 낮음 → 게임·엔터 앱 적합

### 이벤트 설계

**SDK 이벤트 (필수)**:
```
Install: 플랫폼 자동 수집
Activate: 앱 첫 실행 (온보딩 단계)
FirstSession: 첫 세션 10초 이상 (활동 신호)
```

**서버 이벤트 (권장)**:
- CAPI(Meta)·Enhanced Conversions(Google) 통해 서버에서 install 재확인
- 신호 강화 + iOS 제약 우회

### 입찰전략 및 예산

| 전략 | CPI 예상 | 적합 상황 | 선택 기준 |
|---|---|---|---|
| Target CPI | ±10% 변동 | CPI 기준이 명확할 때 | 예산 안정성 중시 |
| Maximize Installs | CPI 상하 | 대량 수집 필요 (런처) | 빠른 러닝 데이터 |
| Bid Cap | 수동 상한 | 매우 제한된 예산 | 보수적 관리 |

**예산 최소치**:
- Meta: $5/day × 7days = $35 (50 install 도달)
- Google: $10/day × 7days = $70
- ASA: $5/day × 7days = $35 (Intent 높으므로 소액 효율 좋음)

**학습 조건**: 50 installs/7days 미달 → 러닝 단계 미진입

### 러닝 조건 및 탈출 기준

**러닝 중 수정 금지**:
- Optimization event 변경 금지
- 타게팅 좁히기 금지 (리셋)

**탈출 신호** (목적 2로 피벗):
- D1 retention < 20% → 앱 품질 문제
- CPI > LTV/3 (비용이 생애 가치의 1/3 초과) → ROI 불가
- CPI 5주 연속 상승 → 시장 포화·경쟁 심화

### 크리에이티브 가이드

- **포맷**: 30초 영상 또는 9:16 이미지 (모바일 우선)
- **훅**: 첫 3초 내에 "왜 설치해야 하나" 명확 (게임이면 게임플레이·기능이면 USE case)
- **Call-to-action**: "Get" / "Install" 명확
- **프레임 수**: 좌상단 5% 안전 마진 (다양한 기기에서 앱스토어 버튼 노출)
- **UGC 형식**: 유저가 직접 촬영한 영상 (게임 스트림, 실제 사용) → 신뢰도 ↑

### 측정 (SKAN 4 & MMP)

**SKAN 4 (Apple)**: 
- 최대 확인 가능 conversion value: 63,000 (앱 내 이벤트와 바인딩)
- 지연 시간: 0~72시간 (불규칙)
- 우회: Branch·AppsFlyer 등 MMP에서 확률 기반 매칭

**MMP (Adjust·Branch·AppsFlyer)**:
- iOS: 확률 기반 attribution (MMP unique ID로 추론)
- Android: 확정적 attribution (Google Play Referrer)
- 권장: SKAN v4 + MMP 병행 (신호 보강)

**주의**: SKAN 포함 시 사용자 동의 필수 (ATT Prompt)

### 인하우스 안티패턴

❌ **패턴 1**: 초기 10 installs만으로 CPI 계산 후 입찰 고정
→ 러닝이 덜 되어 음수·음수·음수 상승에 끌려다님

❌ **패턴 2**: "우리 CPI는 $1이어야 한다"고 고정 → 학습 단계에서 50% 손실
→ 처음 2주는 Learning flexibility 필요

❌ **패턴 3**: 일일 예산 $2 → 2주 학습 불가능
→ 최소 $5/day 7일

---

## 목적 2: 앱 가입 (App Sign-up)

### 정의 및 KPI
- **정의**: 앱 설치 후 회원가입 완료 (이메일·폰·소셜 로그인)
- **KPI 1순위**: CPA (Cost Per Sign-up) / Sign-up conversion rate (install → signup)
- **벤치마크**: B2C 앱 signup rate 15~40% (설치 기준)

### 플랫폼별 구현

#### Meta App Promo + Signup event
- Campaign objective: App Promotion
- Optimization event: "Signup" (또는 커스텀 이벤트명)
- 타게팅: 1st install pixel + Lookalike (기존 signup 사용자)
- 크리에이티브: "회원가입 10초 만에 끝내기" 등 인센티브 강조
- CPA: $0.5~3 (도메인·난이도에 따라)

**CAPI Signup event 매칭**:
```json
{
  "event": "Signup",
  "event_id": "uuid",
  "user_data": {
    "email": "hash",
    "phone": "hash",
    "first_name": "hash"
  },
  "server_timestamp": 1234567890
}
```
→ 메타가 웹상 signup 재확인 + 신호 강화

#### Google App Install 캠페인 (In-app event 피벗)
- 초기: Installs 목적으로 실행
- 7days 후: Optimization event를 "In-app event" (signup)로 변경
- tCPA signup 설정 (또는 Maximize conversions)
- 조건: 50+ signup/week 데이터 필요

### 이벤트 설계

```
"Signup" (또는 "CompleteRegistration"):
- 트리거: 회원가입 폼 제출 완료
- 필수 필드: user_id, email (해시)
- 타이밍: 서버 이벤트 (정확성 ↑)
```

### Signup rate 최적화

| 장벽 | 해결책 |
|---|---|
| 폼 필드 너무 많음 | 필수 3개로 축약 (이메일·비번·이름) → 나머지 뒤로 |
| 소셜 로그인 없음 | Google·Apple·카톡 빠른 로그인 추가 |
| 검증 메일 지연 | 비동기·재전송 옵션 |
| 인센티브 없음 | "가입 시 30일 프리미엄" 같은 명확한 보상 |

---

## 목적 3: 앱내 이벤트 (In-app Event Engagement)

### 정의 및 KPI
- **정의**: 특정 기능 사용·이벤트 참여 (레벨업·구매·라이브 참여 등)
- **KPI 1순위**: CPA(event) / Event conversion rate (signup → event)
- **벤치마크**: 게임 Level 5 도달율 40~70%

### 플랫폼별 구현

#### Meta App Engagement
- Optimization event: 커스텀 이벤트 ("Level_5", "Tournament_Join" 등)
- 리타겟: 앱 설치 사용자 (신규 포함, 기간 무제한)
- 크리에이티브: 이벤트의 FUN을 강조 ("1주일 토너먼트 우승 상금 $1000!")
- CPA: $0.2~1

#### TikTok Community Interaction
- Optimization event: "Community_Interaction" 또는 커스텀
- 특징: TikTok 고유의 "커뮤니티" (UGC·댓글·공유) 노출
- 브랜드 안전성 주의 필요

### 이벤트 설계 (SDK)

```
"LevelUp" / "TournamentJoin" / "VideoWatched":
- 타이밍: 기능 완료 시 즉시 서버 이벤트
- 파라미터: level_id, event_type, currency_spent
- 주기: 최소 주 1회 이상 이벤트 발생 필요
```

### 성공 시그널
- 신규 가입자 30%가 주 1회 이상 참여 → 스티키성 검증
- 참여 사용자의 retention ↑ → 마케팅 효과 확인

---

## 목적 4: 앱내 구매 (In-app Purchase)

### 정의 및 KPI
- **정의**: 앱 내에서 직접 결제 (IAP) 또는 광고 제거 구매
- **KPI 1순위**: ROAS (Revenue / Ad Spend) / CPA(purchase)
- **벤치마크**: 게임 ROAS 3:1~5:1, 구독 앱 ROAS 2:1~4:1

### 플랫폼별 구현

#### Meta Value Optimization (ASC)
- Optimization event: "Purchase" (IAP 이벤트)
- 입찰: Bid Cap (최대 CPA) 또는 Dynamic Bid Cap
- 타게팅: Custom Audience (구매 경험 있는 사용자) + Lookalike
- 크리에이티브: 구매 인센티브 강조 ("한정판 캐릭터 30% 할인!")

**CAPI Purchase event**:
```json
{
  "event": "Purchase",
  "event_id": "uuid",
  "user_data": { "email": "hash" },
  "value": 4.99,
  "currency": "USD"
}
```

#### Google tROAS (target Return On Ad Spend)
- Campaign objective: App promotion (또는 App engagement)
- Optimization event: "In-app purchase"
- Bidding: target-ROAS 설정 (예: 3.0 = 1달러 광고비당 3달러 수익)
- 조건: 최소 100 conversions/30days (높은 기준)

### 가격 전략
- **스타터 IAP**: $0.99~1.99 (낮은 진입장벽)
- **중단계**: $4.99~9.99 (구독 or 특별 아이템)
- **프리미엄**: $19.99+ (소수 고래 사용자)
- **구독**: $4.99/month~9.99/month (정기 매출)

### 결제 최적화

| 최적화 | 효과 |
|---|---|
| 첫 구매 가격 낮게 ($0.99) | Conversion rate ↑ 40% |
| 구매 완료 후 즉시 "다음 추천" | AOV ↑ 15% |
| 구독 7일 무료 트라이얼 | 전환율 ↑ 60% |

---

## 목적 5: 리텐션·재방문 (Retention & Re-engagement)

### 정의 및 KPI
- **정의**: 기존 사용자를 재활성화 (앱 재실행·재결제)
- **KPI 1순위**: D7/D30 return rate / Retention cost per active user
- **벤치마크**: 게임 D7 30~50%, 소셜 앱 D30 40~70%

### 플랫폼별 구현

#### Meta Custom Audience 리타겟
- Audience: 앱 설치 후 7~30일 비활동 사용자
- Optimization event: "App Opens" 또는 "Level_Complete"
- 크리에이티브: "돌아와 보세요! 신규 이벤트 추가됨"
- CPA: 신규보다 40% 저렴 (기존 사용자 이므로)

**Audience 세분화**:
```
유휴(7~14일 비활동) → 부드러운 메시지
휴면(30일 이상 비활동) → 강한 인센티브 + 별도 크리에이티브
```

#### Kakao 톡채널 메시지 (CRM)
- 1:1 메시지 (비광고, 고동의율)
- 개인화 가능 (사용자 레벨·마지막 구매·상태)
- 비용: 메시지당 5~50원 (광고비 대비 저렴)
- **제약**: 유저 동의 필수 (명시적 옵트인)

### 재방문 유도 전략

| 전략 | 효과 | 비용 |
|---|---|---|
| 푸시 알림 (앱 내) | 즉시 | 무료 |
| 이메일 | 지연 (1~2일) | 무료 |
| Kakao 톡채널 | 부드럽고 고동의율 | 매우 저렴 |
| Meta 광고 | 높은 도달 | 중간 |

### 탈출 기준
- D7 return < 15% → 앱 품질 문제 (마케팅 아님)
- Retention cost > LTV/10 → 마케팅 비용 초과

---

## 5목적 통합 퍼널

```
목적 1 (Install)
    ↓ [D1 retention 측정]
목적 2 (Signup) [20~40% 전환]
    ↓ [2~3일 후]
목적 3 (In-app event) [40~70% 참여]
    ↓ [1주일 후]
목적 4 (Purchase) [ARPU 측정, 5~20% 구매율]
    ↓ [1개월 후]
목적 5 (Retention) [D30 재방문 40~70%]
    ↓
LTV 계산 → CAC와 비교 → ROI 판단
```

### 성공 체크포인트

- [ ] Install CPI < Expected LTV/3
- [ ] D1 retention > 20%
- [ ] Signup conversion > 15%
- [ ] Active user D7 > 30%
- [ ] Purchase ARPU > CAC (순이익 양수)
- [ ] D30 retention > 40%
