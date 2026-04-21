# objective_lead — 리드 수집 1목적 (B2B·B2C 분리)

영업 기회·문의·회원가입 등 리드(Lead) 정보 수집을 위한 광고.

## 목적 6: 리드 수집 (Lead Generation)

### 정의 및 KPI
- **정의**: 가입·상담·문의·데모 신청·화이트페이퍼 다운로드 등으로 리드 정보 획득
- **KPI 1순위**: CPL (Cost Per Lead) / Lead volume
- **KPI 2순위**: Lead quality score (영업전환율) / MQL→SQL 전환율
- **벤치마크 B2B**: CPL $10~100, MQL→SQL 20~40%
- **벤치마크 B2C**: CPL $0.5~5, Lead→Customer 10~30%

---

## B2B 리드 (LinkedIn 중심)

### LinkedIn Lead Gen Form (주력)

#### 폼 설계

**필수 필드 (3개)**:
```
1. 회사명 (Company)
2. 직급 (Job Title)
3. 업무 이메일 (Work Email)
```
→ 완료율 70% 이상 유지

**선택 필드 (추가 1~2개)**:
```
4. 회사 규모 (Company Size)
5. 관심사 (Interested in: Product A / Product B / Service)
```
→ 완료율이 50% 이상 유지하면 추가 가능

**금지 필드**:
```
❌ 개인 폰번 (거부 심함)
❌ 개인 휴대폰 (거부 심함)
❌ 급여 (개인정보 민감)
❌ 나이 (차별 우려)
```

#### 폼 전략

| 전략 | 설명 | 적합 |
|---|---|---|
| 자동채우기 | LinkedIn 프로필에서 자동 입력 | ○ 권장 (완료율 ↑60%) |
| 선택 동의 | "마케팅 이메일 수신 동의" 체크박스 | ○ 필수 (법규 준수) |
| 감사 페이지 | "리드 등록 완료! 24시간 내 연락하겠습니다" | ○ 권장 (기대치 관리) |
| 선물 유도 | "폼 완료 시 $50 할인쿠폰 제공" | ☒ 주의 (리드 질 저하) |

#### 플랫폼별 최적화

**LinkedIn Campaign Manager**:
- Campaign objective: Lead Generation Ads
- Audience: 직급 + 업계 + 회사 규모 (매우 정확한 타게팅 가능)
- 입찰: Manual CPC (클릭당 $0.5~3) 또는 Automatic
- 다음은 자체 할당 (Lead Gen Form → LinkedIn이 관리)

**Matched Audiences**:
```
Company list: 특정 회사 직원만 타게팅 (예: "Microsoft 직원")
Lookalike: 기존 리드와 유사한 사용자 추론
```

#### Revenue Attribution Report (2026신)

LinkedIn이 MQL→SQLClosed Won까지 추적:
```
Lead created → Sales team 영업 → Deal closed
→ LinkedIn이 광고 기여도 역산
```

**설정 필수**:
1. CRM(Salesforce·HubSpot) 연동
2. Lead Sync API 웹훅 자동화 (리드 자동 입력)
3. Deal stage 태깅 (MQL·SQL·Negotiation·Closed Won)

### LinkedIn Accelerate (신 기능)

- 자동화된 Lead Gen 캠페인
- Objective 선택 후 Audience·예산만 지정 → 나머지는 AI 자동
- 메타 Advantage+와 유사
- **조건**: 최소 100 leads/month 데이터 필요

---

## B2C 리드 (Meta·Google·Naver 분산)

### Meta Instant Form (ILG)

#### 폼 설계

**기본 (추천)**:
```
1. 이름 (First name)
2. 이메일 (Email)
3. 폰번 (Phone) — 필드 3개가 황금
```

**확장 (3개 초과 시 완료율 ↓)**:
```
4. 관심 상품 (Interested product: A / B / C)
5. 예산 범위 (Budget: <$100 / $100-500 / >$500)
```

#### 광고 창의

**헤드라인**: "무료 상담받기" / "가격 견적 받기"
**설명**: "30초 내 기본정보 입력 후 전문가 상담"
**CTA 버튼**: "상담 신청" / "견적 받기"

#### 입찰 전략

| 입찰 | CPL | 적합 상황 |
|---|---|---|
| CPC (Manual) | 낮음 ($0.3~0.8) | 리드 대량 수집 |
| Cost per result (Automatic) | 중간 ($2~10) | 균형 잡힌 수집 |
| CPC + Bid cap | 가변 | 매우 제한된 예산 |

### Google Lead Form Extension

#### 검색광고 + Lead Form

**세팅**:
1. Search campaign 생성
2. Ad group에서 "Lead Form extension" 추가
3. 폼: Google가 제공하는 기본 템플릿 (또는 자체 호스팅)

**장점**:
- 검색 사용자는 이미 intent 있음 → CPL 저렴 ($1~5)
- 자동화 높음 (Google AI 자동 최적화)

### Naver 파워컨텐츠 + GFA

**파워컨텐츠**:
- 네이버 블로그·포스트 형식의 광고
- 상담 신청 링크 포함

**GFA (Growth Feed Advertising)**:
- 타겟팅: 관심사·검색어·행동
- 형식: 네이티브 광고

### Kakao 비즈보드

**비즈보드 웹훅**:
```json
{
  "user_phone": "01012345678",
  "user_email": "user@example.com",
  "inquiry_type": "상담",
  "message": "상담 신청합니다"
}
```

---

## 리드 퀄리티 vs 볼륨: 트레이드오프

| 전략 | CPL | Lead quality | 적합 |
|---|---|---|---|
| Low barrier (간단한 폼) | 낮음 ($1) | 낮음 (50%) | 대량 확보 필요 |
| Medium (3 필드) | 중간 ($3) | 중간 (70%) | ◎ 권장 |
| High barrier (5필드+) | 높음 ($15) | 높음 (90%) | 소수 고품질 필요 |

**선택 팁**:
- 초기: Medium (3필드) → 데이터 축적
- 성숙화: 품질 필터 강화 (5~7필드)

---

## 리드 소유권 & 리드 라우팅

### 인하우스 관리 vs 마케팅 자동화

**인하우스 (초기)**:
```
Lead 생성 → Sales 팀이 수동으로 이메일·전화
→ 24시간 내 접촉 필수 (시간 지나면 전환율 ↓70%)
```

**마케팅 자동화 (HubSpot·Marketo)**:
```
Lead 생성 → 자동 확인 이메일
→ 영업 자격심사 (Qualification) 플로우
→ MQL (Marketing Qualified Lead) → Sales handoff
```

### SLA (Service Level Agreement) 수립

```
리드 생성 후:
- 0분: 자동 확인 이메일 발송
- 1시간: Sales에 알림
- 2시간: Sales 첫 연락
- 24시간: 첫 미팅 제안
```

**SLA 준수율 > 80% → 전환율 ↑ 40%**

---

## 리드 합격선 (Lead Scoring)

리드마다 점수 부여 → 영업 자격 판단:

| 신호 | 점수 | 누적 |
|---|---|---|
| 이메일 열기 | +5 | 5점 |
| 웹사이트 페이지 3개 이상 방문 | +10 | 15점 |
| 가격 페이지 방문 | +15 | 30점 |
| 데모 신청 | +20 | 50점 |
| 회의 예약 확인 | +30 | 80점 |

**규칙**: 50점 이상 = MQL (Sales 핸드오프) / 80점 이상 = SQL (즉시 영업)

---

## B2B vs B2C: 채널 선택

| 채널 | B2B 최강 | B2C 최강 | 공통 |
|---|---|---|---|
| LinkedIn | ○○○ 주력 | ◎ 보조 | Lead Gen Form |
| Meta | ◎ 보조 | ○○○ 주력 | Instant Form |
| Google | ◎ 보조 | ○○ 중간 | Lead Form ext. |
| Naver | ◎ 보조 | ○○ 중간 | GFA |

**조합 권장**:
- **B2B SaaS**: LinkedIn 80% + Meta 15% + Google 5%
- **B2C 서비스**: Meta 60% + Google 30% + Naver 10%
