#!/bin/zsh
# 사용법: ./build.sh part1 | part2 | handout
# HTML 원본을 Chrome으로 PDF로 만들고, 자동 검사 결과를 출력한다.
set -e
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
typeset -A OUT
OUT[part1]="../pdf/osung_ai_digital_problem_solving_part1_workspace_v22_20260930.pdf"
OUT[part2]="../pdf/osung_ai_digital_problem_solving_part2_ux_implementation_v22_20260930.pdf"
OUT[handout]="../../practice/osung_ai_digital_problem_solving_handout_a4_v22_20260930.pdf"
PART="${1:-}"
PDF=""
if [[ -n "$PART" ]]; then PDF="${OUT[$PART]:-}"; fi
if [[ -z "$PDF" ]]; then echo "사용법: ./build.sh part1 | part2 | handout"; exit 1; fi
mkdir -p "$(dirname "$PDF")" renders
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=15000 \
  --print-to-pdf="$PDF" "file://$PWD/$PART.html" >/dev/null 2>&1
"$CHROME" --headless=new --disable-gpu --virtual-time-budget=15000 \
  --dump-dom "file://$PWD/$PART.html" 2>/dev/null | perl -0ne 'print "$1\n" if /<pre id="qa">(.*?)<\/pre>/s'
pdfinfo "$PDF" | grep -E "Pages|Page size"
