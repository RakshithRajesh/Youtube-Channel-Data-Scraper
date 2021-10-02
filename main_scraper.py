from requests_html import HTMLSession
import pandas as pd
from url_maker import url

url = url
s = HTMLSession()
r = s.get(url)
r.html.render(scrolldown=11000, timeout=20)
print(r.status_code)

channel_name = r.html.find("#text-container")[0].text
subscriber_count = r.html.find("#subscriber-count")[0].text

videos = r.html.find("#details")

video_name = r.html.find("#video-title")
video_views_and_time = r.html.find("#metadata-line")

print(f"""
Data Excrated From:
    1) Channel Name: {channel_name}
    2) Subscriber Count: {subscriber_count}
    3) Total Videos: {len(video_name)}
""")

video_view_list = []
video_upload_time_list = []
video_link_list = []
video_name_list = []

for i in range(len(video_name)):
    video_views = video_views_and_time[i].text.split("views")[0].strip()
    video_upload_time = video_views_and_time[i].text.split("views")[1].strip()

    video_view_list.append(f"{video_views}")
    video_upload_time_list.append(video_upload_time)

    video_link = video_name[i].attrs["href"]
    video_link_list.append(f'https://youtube.com' + str(video_link))

    video_actual_name = video_name[i].text
    video_name_list.append(video_actual_name)


df = pd.DataFrame({"Video Name: ": video_name_list, "Video Views: ": video_view_list,"Upload Time": video_upload_time_list, "Video Link: ": video_link_list})
df.to_csv(f"{channel_name}.csv")