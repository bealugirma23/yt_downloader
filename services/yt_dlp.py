
import yt_dlp
import os
import re
async def get_metadata(url):
   # Configure yt-dlp options
    ydl_opts = {
        'quiet': True,  # Suppress output
        'no_warnings': True,
        'extract_flat': 'in_playlist',  # Don't download any videos
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            return info
        except Exception as e:
            print(f"Error: {e}")
            return None


async def sending_audio(url):
    output_folder = os.path.abspath("uploads")  # Use an absolute path
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    def sanitize_title(title):
        # Remove or replace invalid characters
        return re.sub(r'[<>:"/\\|?*]', '_', title)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'quiet': False,
        'noplaylist': True,
        'sanitize-filename': True,  # Ensure yt-dlp sanitizes the filename
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            sanitized_title = info['title']
            final_filename = f"{info['title']}.mp3"
            final_path = os.path.join(output_folder, final_filename)

            # Log the paths for debugging
            print("Sanitized Title:", sanitized_title)
            print("Final Path:", final_path)

            if os.path.exists(final_path):
                return final_path
            else:
                raise FileNotFoundError(f"File not found: {final_path}")

    except Exception as e:
        print("Error in sending_audio:", e)
        return None
# async def sending_audio(url):
#    output_folder = "uploads"
#    if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
    
#     # yt-dlp options for downloading the best audio
#    ydl_opts = {
#         'format': 'worstaudio/worst',  # Select the best audio
#         'postprocessors': [{  # Optional: Convert to mp3
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',  # Adjust quality (128, 192, 320 kbps)
#         }],
#         'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),  # Output template
#         'quiet': False,  # Show progress
#         'noplaylist':True
#          }
#    try:
#       with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#           song = ydl.download([url])
#       return song
#    except Exception as e: 
#       print(e)