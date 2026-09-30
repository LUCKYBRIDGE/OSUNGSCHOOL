"""발표 대본 PDF와 검증 가능한 배포 ZIP. 사용법: python slides/build/package_materials.py"""
from pathlib import Path
import os, re, html, hashlib, zipfile
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Preformatted
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
ROOT=Path(__file__).resolve().parents[2]
def script_pdf():
    font=Path(os.environ.get('KOREAN_FONT','C:/Windows/Fonts/malgun.ttf'))
    bold=Path(os.environ.get('KOREAN_BOLD_FONT','C:/Windows/Fonts/malgunbd.ttf'))
    if not font.exists(): raise RuntimeError('Set KOREAN_FONT and KOREAN_BOLD_FONT to Korean TTF paths')
    pdfmetrics.registerFont(TTFont('Korean',str(font)))
    pdfmetrics.registerFont(TTFont('KoreanBold',str(bold if bold.exists() else font)))
    styles={
      'body':ParagraphStyle('body',fontName='Korean',fontSize=10,leading=16,spaceAfter=7,wordWrap='CJK'),
      'h1':ParagraphStyle('h1',fontName='KoreanBold',fontSize=19,leading=26,spaceAfter=16,keepWithNext=True,wordWrap='CJK'),
      'h2':ParagraphStyle('h2',fontName='KoreanBold',fontSize=15,leading=22,spaceBefore=13,spaceAfter=10,keepWithNext=True,wordWrap='CJK'),
      'h3':ParagraphStyle('h3',fontName='KoreanBold',fontSize=12,leading=19,spaceBefore=12,spaceAfter=8,keepWithNext=True,wordWrap='CJK'),
      'code':ParagraphStyle('code',fontName='Korean',fontSize=9,leading=13,spaceAfter=8,wordWrap='CJK',backColor='#F3F5F8',borderPadding=6),
    }
    def fmt(text):
      text=html.escape(text)
      text=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'\1 (\2)',text)
      text=re.sub(r'\*\*(.*?)\*\*',r'<font name="KoreanBold">\1</font>',text)
      return text.replace('`','')
    story=[]; paragraph=[]; in_code=False; code=[]
    def flush():
      if paragraph:
       story.append(Paragraph(fmt(' '.join(paragraph)),styles['body'])); paragraph.clear()
    text=(ROOT/'docs/03_speaker_script.md').read_text(encoding='utf-8')
    for line in text.splitlines():
      if line.startswith('```'):
        flush()
        if in_code:
          story.append(Paragraph('<br/>'.join(fmt(x) for x in code),styles['code'])); code=[]
        in_code=not in_code; continue
      if in_code: code.append(line); continue
      if not line.strip(): flush(); continue
      if line=='---': flush(); story.append(Spacer(1,5)); continue
      m=re.match(r'^(#{1,4}) (.+)',line)
      if m:
        flush(); level=len(m[1]); title=m[2]
        if level==2 and (title.startswith('1부.') or title.startswith('2부.') or '예상 질문' in title): story.append(PageBreak())
        story.append(Paragraph(fmt(title),styles['h1' if level==1 else 'h2' if level==2 else 'h3'])); continue
      if line.startswith('- '): flush(); story.append(Paragraph('• '+fmt(line[2:]),styles['body'])); continue
      paragraph.append(line)
    flush()
    out=ROOT/'docs/osung_speaker_script_v23_20260930.pdf'
    def footer(c,doc):
      c.setFont('Korean',8); c.setFillColorRGB(.35,.4,.45)
      c.drawString(42,25,'강릉오성학교 · 발표 대본 v23 · 2026. 9. 30.')
      c.drawRightString(A4[0]-42,25,str(doc.page))
    def korean_canvas(*args,**kwargs):
        kwargs['initialFontName']='Korean'
        return Canvas(*args,**kwargs)
    SimpleDocTemplate(str(out),pagesize=A4,rightMargin=42,leftMargin=42,topMargin=38,bottomMargin=42,title='OSUNGSCHOOL 발표 대본 v23',author='OSUNGSCHOOL').build(story,onFirstPage=footer,onLaterPages=footer,canvasmaker=korean_canvas)
    return out
def package():
    files=[ROOT/'slides/pdf/osung_ai_digital_problem_solving_part1_workspace_v23_20260930.pdf',ROOT/'slides/pdf/osung_ai_digital_problem_solving_part2_ux_implementation_v23_20260930.pdf',ROOT/'practice/osung_ai_digital_problem_solving_handout_a4_v23_20260930.pdf',ROOT/'docs/osung_speaker_script_v23_20260930.pdf',ROOT/'docs/03_speaker_script.md',ROOT/'practice/activity_guide.md',ROOT/'practice/README.md',ROOT/'docs/04_sources.md',ROOT/'docs/pdf_validation_v23.md']
    for p in files:
      if not p.exists(): raise FileNotFoundError(p)
    lines=['OSUNGSCHOOL 강의자료 v23 · 2026-09-30','','1부 42쪽 / 2부 35쪽 / 활동 안내 A4 양면 / 발표 대본 PDF·편집본','활동 안내: 자유 메모와 참고 질문. 미정은 만들면서 보완합니다.','현재 기준: https://github.com/LUCKYBRIDGE/OSUNGSCHOOL','','파일별 SHA-256:']
    lines += [hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(ROOT).as_posix() for p in files]
    out=ROOT/'practice/downloads/osung_course_materials_v23_20260930.zip'; out.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
      z.writestr('읽어주세요.txt','\n'.join(lines))
      for p in files: z.write(p,p.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(out) as z:
      assert z.testzip() is None
      for p in files: assert z.read(p.relative_to(ROOT).as_posix())==p.read_bytes()
    print(out)
if __name__=='__main__':
    import sys
    if '--script-only' in sys.argv: print(script_pdf())
    elif '--zip-only' in sys.argv: package()
    else: script_pdf(); package()
