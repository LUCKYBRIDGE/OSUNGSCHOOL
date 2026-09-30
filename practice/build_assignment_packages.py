"""Build teacher starter ZIPs from the checked-in Markdown files."""
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

BASE = Path(__file__).resolve().parent
SOURCE = BASE / 'assignments'
OUTPUT = BASE / 'downloads'
PACKAGES = [
    ('01_idea', 'osung_task1_idea_20260930.zip'),
    ('02_kiosk', 'osung_task2_kiosk_20260930.zip'),
    ('03_safety', 'osung_task3_safety_20260930.zip'),
    ('04_free', 'osung_task4_free_20260930.zip'),
]


def add(archive, name, content):
    info = ZipInfo(name, date_time=(2026, 9, 30, 0, 0, 0))
    info.compress_type = ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    archive.writestr(info, content)


def main():
    OUTPUT.mkdir(exist_ok=True)
    common = (SOURCE / 'README.md').read_text(encoding='utf-8')
    common = re.sub(r'## 내려받기와 복사\n.*?(?=## 제출 방법)', '', common, flags=re.S)
    common = common.replace('(../ai_setup_and_install_20260930.md)', '(https://padlet.com/lucky20220528/260930-jhtj91ryy8mwbvog)')
    offline_common = re.sub(r'\[([^]]+)\]\((?!https?://)[^)]+\)', r'\1', common)
    submission = (SOURCE / 'submission.md').read_bytes()

    for folder, filename in PACKAGES:
        with ZipFile(OUTPUT / filename, 'w') as archive:
            for path in sorted((SOURCE / folder).glob('*.md')):
                add(archive, path.name, path.read_bytes())
            add(archive, 'submission.md', submission)
            add(archive, 'COMMON_GUIDE.md', offline_common.encode('utf-8'))

    with ZipFile(OUTPUT / 'osung_assignment_starters_20260930.zip', 'w') as archive:
        add(archive, 'README.md', common.encode('utf-8'))
        add(archive, 'submission.md', submission)
        for folder, _ in PACKAGES:
            for path in sorted((SOURCE / folder).glob('*.md')):
                add(archive, folder + '/' + path.name, path.read_bytes())

    for path in sorted(OUTPUT.glob('osung_*_20260930.zip')):
        with ZipFile(path) as archive:
            assert archive.testzip() is None
            assert all(not name.startswith('/') and '..' not in name.split('/') for name in archive.namelist())
            for name in archive.namelist():
                archive.read(name).decode('utf-8')
            print(f'{path.name}: {len(archive.namelist())} files, {path.stat().st_size} bytes, OK')


if __name__ == '__main__':
    main()
