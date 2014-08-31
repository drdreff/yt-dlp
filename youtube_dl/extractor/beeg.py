from __future__ import unicode_literals

import re

from .common import InfoExtractor


class BeegIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?beeg\.com/(?P<id>\d+)'
    _TEST = {
        'url': 'http://beeg.com/5416503',
        'md5': '634526ae978711f6b748fe0dd6c11f57',
        'info_dict': {
            'id': '5416503',
            'ext': 'mp4',
            'title': 'Sultry Striptease',
            'description': 'md5:6db3c6177972822aaba18652ff59c773',
            'categories': list,  # NSFW
            'thumbnail': 're:https?://.*\.jpg$',
        }
    }

    def _real_extract(self, url):
        mobj = re.match(self._VALID_URL, url)
        video_id = mobj.group('id')

        webpage = self._download_webpage(url, video_id)

        video_url = self._html_search_regex(
            r"'480p'\s*:\s*'([^']+)'", webpage, 'video URL')

        title = self._html_search_regex(
            r'<title>([^<]+)\s*-\s*beeg\.?</title>', webpage, 'title')
        
        description = self._html_search_regex(
            r'<meta name="description" content="([^"]*)"',
            webpage, 'description', fatal=False)
        thumbnail = self._html_search_regex(
            r'\'previewer.url\'\s*:\s*"([^"]*)"',
            webpage, 'thumbnail', fatal=False)

        categories_str = self._html_search_regex(
            r'<meta name="keywords" content="([^"]+)"', webpage, 'categories', fatal=False)
        categories = categories_str.split(',')

        return {
            'id': video_id,
            'url': video_url,
            'title': title,
            'description': description,
            'thumbnail': thumbnail,
            'categories': categories,
        }
