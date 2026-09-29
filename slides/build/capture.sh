#!/bin/zsh
# 사용법: ./capture.sh
# knollab-001 네 실험 사이트의 첫 화면을 1280×800으로 캡처해 assets/knollab-001/에 JPG로 저장한다.
# D 사이트가 완성되면 다시 실행하고 ./build.sh part2로 PDF를 다시 만든다.
set -e
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
mkdir -p renders assets/knollab-001
for x in a:knollab-001-a-ai-only b:knollab-001-b-design-md c:knollab-001-c-design-figma-mcp d:knollab-001-d-design-figma-mcp-actively; do
  k=${x%%:*}; r=${x#*:}
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --window-size=1280,800 --virtual-time-budget=10000 \
    --screenshot="$PWD/renders/knollab-$k.png" "https://luckybridge.github.io/$r/" >/dev/null 2>&1
  python3 -c "from PIL import Image; Image.open('renders/knollab-$k.png').convert('RGB').resize((960, 600), Image.Resampling.LANCZOS).save('assets/knollab-001/$k.jpg', quality=85)"
  echo "saved assets/knollab-001/$k.jpg"
done
