# -*- coding: UTF-8 -*-
from lxml.html import parse, HTMLParser
import re, datetime


def scrape(cat):
	iso_parser = HTMLParser(encoding='utf-8')

	soup = parse("http://camarasp.flashserverbr.com/search.php?id_categoria=" + str(cat[0]), iso_parser).getroot()

	VIDEOS = []

	genre = cat[1]

	for video in soup.xpath("//img"):
		video_path = video.get("src").split("/")[3].split(".")[0]
		video_desc = video.xpath("../../..//span")[1].text
		try:
			video_data = re.search("Data:(.*)h", video_desc).group(1).strip()
			video_datetime = datetime.datetime.strptime(video_data, "%d/%m/%Y - %H:%M")
			video_order = str(cat[0])+video_datetime.strftime('%s')
		except:
			video_data = ""
			video_order = '0'

		v = {
			"name" : video.xpath("../../..//strong")[0].text,
			"thumb" : "http://camarasp.flashserverbr.com/images/thumbs/" + video_path + ".jpg",
			"genre" : genre,
			"video" : "rtsp://camarasp.flashserverbr.com:1935/camarasp_vod/mp4:" + video_path + ".mp4",
			"tagline" : video_desc,
			"order" : video_order
		}

		VIDEOS.append(v)
	return VIDEOS