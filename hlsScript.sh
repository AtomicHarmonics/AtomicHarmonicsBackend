mkdir -p ./staticContent/static/audio
cd ./staticContent/static/audio/ 
ffmpeg -i rtsp://localhost:8554/mystream -fflags flush_packets -max_delay 2 -flags -global_header -hls_time 2 -hls_list_size 5 -hls_wrap 6 -hls_playlist_type event -vcodec copy -y ./index.m3u8