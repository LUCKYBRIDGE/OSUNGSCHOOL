"""PDF를 페이지 이미지로 렌더링하고 여러 장씩 모은 검수용 시트를 만든다.
사용법: python3 contact.py <pdf> <이름> [한 장당 칸 수=6]
"""
import glob
import os
import subprocess
import sys

from PIL import Image, ImageDraw

pdf, name = sys.argv[1], sys.argv[2]
per = int(sys.argv[3]) if len(sys.argv) > 3 else 6
out_dir = os.path.join(os.path.dirname(__file__), "renders")
os.makedirs(out_dir, exist_ok=True)
for f in glob.glob(os.path.join(out_dir, f"{name}-*.png")):
    os.remove(f)
subprocess.run(["pdftoppm", "-r", "72", "-png", pdf, os.path.join(out_dir, f"{name}-p")], check=True)
pages = sorted(glob.glob(os.path.join(out_dir, f"{name}-p-*.png")))
cols = 2
w, h = 960, 540
for s in range(0, len(pages), per):
    chunk = pages[s:s + per]
    rows = (len(chunk) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * w + (cols + 1) * 12, rows * h + (rows + 1) * 12), "#9aa3ad")
    d = ImageDraw.Draw(sheet)
    for i, p in enumerate(chunk):
        im = Image.open(p).convert("RGB").resize((w, h))
        x = 12 + (i % cols) * (w + 12)
        y = 12 + (i // cols) * (h + 12)
        sheet.paste(im, (x, y))
        d.rectangle([x, y, x + 60, y + 26], fill="#d7263d")
        d.text((x + 8, y + 6), str(s + i + 1), fill="white")
    sheet.save(os.path.join(out_dir, f"{name}-sheet-{s // per + 1:02d}.png"))
print(len(pages), "pages")
