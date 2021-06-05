import youtube_dl
# from youtube_dl import YoutubeDL
# ydl = YoutubeDL({'ignoreerrors': True, 'quiet': True})

# # 'DonCharismaTV' channel UCzKlrCD9iN4XYWoTBSmBNsA
# # playlist_url can be channel or playlist        
# playlist_url = 'https://www.youtube.com/playlist?list=PLMvaT-Nb9FtSA0CgE60n-gBaINbCSz6ht'

# playd = ydl.extract_info(playlist_url, download=False)

# print(playd)

# ydl_opts = {
#     'ignoreerrors': True,
#     'quiet': True
# }

# # input_file = open("https://www.youtube.com/playlist?list=PLMvaT-Nb9FtSA0CgE60n-gBaINbCSz6ht")

# # for playlist in input_file:

# playlist = 'https://www.youtube.com/playlist?list=PLMvaT-Nb9FtSA0CgE60n-gBaINbCSz6ht'

# with youtube_dl.YoutubeDL(ydl_opts) as ydl:

#     playlist_dict = ydl.extract_info(playlist, download=False)

#     for video in playlist_dict['entries']:

#         print()

#         if not video:
#             print('ERROR: Unable to get info. Continuing...')
#             continue

#         for property in ['thumbnail', 'id', 'title', 'description', 'duration']:
#             print(property, '--', video.get(property))

download = False 
ydl_opts = {
    'writesubtitles': True,
    'format': 'mp4',
    'writethumbnail': True
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ie_result = ydl.extract_info('https://www.youtube.com/playlist?list=PLMvaT-Nb9FtSA0CgE60n-gBaINbCSz6ht', download=False)

    print(ie_result)