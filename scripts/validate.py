#!/usr/bin/env python3
"""
ads-playbook self-check validator.

검증 항목:
  1. SKILL.md 크기 (목표 ≤10KB)
  2. 필수 섹션 존재 (§0~§5, Gotchas)
  3. references/ 스포크 파일 모두 존재 (허브에서 참조된 것들)
  4. evals/cases.json 유효성 + 최소 3개 케이스
  5. frontmatter version 필드 존재
  6. 한국 디폴트 문구 보존 (§0 규칙 7)

사용:
  python3 scripts/validate.py ./ads-playbook/
"""
import json
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = ["## §0", "## §1", "## §2", "## §3", "## §4", "## §5", "## Gotchas"]
REQUIRED_SPOKES = [
    "glossary.md", "measurement.md", "creative.md", "tuning_playbook.md",
    "antipatterns.md", "objective_matrix.md", "objective_app.md",
    "objective_commerce.md", "objective_lead.md", "objective_brand.md",
    "platform_meta.md", "platform_google.md", "platform_tiktok_asa.md",
    "platform_naver_kakao.md", "platform_x_linkedin.md",
    "launch_checklist.md", "latest_2026q2.md",
]
KOREAN_DEFAULT_MARKER = "한국 디폴트"


def check(target_dir: Path) -> dict:
    errors = []
    warnings = []

    skill_md = target_dir / "SKILL.md"
    if not skill_md.exists():
        return {"errors": ["SKILL.md 없음"], "warnings": [], "grade": "FAIL"}

    content = skill_md.read_text()
    size = len(content.encode("utf-8"))

    # 1. 크기
    if size > 10_240:
        errors.append(f"SKILL.md 크기 {size}B > 10KB 한계")
    elif size > 5_120:
        warnings.append(f"SKILL.md 크기 {size}B > 5KB 목표 (허용)")

    # 2. 섹션
    for sec in REQUIRED_SECTIONS:
        if sec not in content:
            errors.append(f"필수 섹션 누락: {sec}")

    # 3. 스포크 파일
    refs_dir = target_dir / "references"
    if not refs_dir.exists():
        errors.append("references/ 디렉토리 없음")
    else:
        for spoke in REQUIRED_SPOKES:
            if not (refs_dir / spoke).exists():
                errors.append(f"스포크 누락: references/{spoke}")

    # 4. evals
    evals_file = target_dir / "evals" / "cases.json"
    if not evals_file.exists():
        errors.append("evals/cases.json 없음")
    else:
        try:
            data = json.loads(evals_file.read_text())
            case_count = len(data.get("cases", []))
            if case_count < 3:
                errors.append(f"evals 케이스 {case_count}개 < 3개 최소")
        except json.JSONDecodeError as e:
            errors.append(f"evals/cases.json JSON 오류: {e}")

    # 5. version
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if fm_match:
        fm = fm_match.group(1)
        if "version:" not in fm:
            warnings.append("frontmatter version 필드 없음")
    else:
        errors.append("frontmatter 없음")

    # 6. 한국 디폴트
    if KOREAN_DEFAULT_MARKER not in content:
        errors.append("한국 디폴트 문구 소실 (본질 유실)")

    grade = "PASS" if not errors else "FAIL"
    return {
        "size_bytes": size,
        "errors": errors,
        "warnings": warnings,
        "grade": grade,
    }


def main():
    if len(sys.argv) < 2:
        print("usage: validate.py <target_dir>")
        sys.exit(2)
    target = Path(sys.argv[1]).resolve()
    result = check(target)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result["grade"] == "PASS" else 1)


if __name__ == "__main__":
    main()
