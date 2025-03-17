from textwrap import dedent
import urllib.parse
import re

# 공유할 플랫폼 정보 (이름: URL)
SHARE_PLATFORMS = {
    "X": "https://x.com/intent/tweet?text={title}&url={url}",
    "Facebook": "https://www.facebook.com/sharer/sharer.php?u={url}"
}

# 특정 URL 패턴만 포함
include = re.compile(r"blog/[1-9].*")

def on_page_markdown(markdown, **kwargs):
    page = kwargs['page']
    config = kwargs['config']

    # 공유 대상 페이지인지 확인
    if not include.match(page.url):
        return markdown

    page_url = config.site_url + page.url
    page_title = urllib.parse.quote(page.title + '\n')

    # 공유 버튼 생성
    share_buttons = "\n".join(
        f"[:simple-{name.lower()}:에 공유하기]({url.format(title=page_title, url=page_url)}){{ .md-button }}"
        for name, url in SHARE_PLATFORMS.items()
    )

    return markdown + dedent(f"\n{share_buttons}\n")
