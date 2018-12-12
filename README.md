# 20bn-video-data-loading-talk
- Originally written [Valentin Haenel](http://haenel.co/)
- I forked it to include some more benchmark results


It is based on this thread: https://github.com/TwentyBN/GulpIO/issues/81


## Video files
Files that were already present:
```
- smth-smth-1.webm
- video_large.mp4
- video_large.webm
```

#### Additions
I added `video_large_mpeg4.mp4` (mp4 container with mpeg4 codec), using:

`ffmpeg -i video_large.mp4 -vcodec mpeg4 -strict experimental video_large_mpeg4.mp4`

#### Status

Using `ffprobe`
```
smth-smth-1.webm
Duration: 00:00:03.92, start: 0.000000, bitrate: 161 kb/s
    Stream #0:0: Video: vp9 (Profile 0), yuv420p(tv), 427x240, SAR 1:1 DAR 427:240, 12 fps, 12 tbr, 1k tbn, 1k tbc (default)



video_large.mp4
Duration: 00:00:04.88, start: 0.023220, bitrate: 2122 kb/s
    Stream #0:0(und): Video: h264 (High) (avc1 / 0x31637661), yuv420p, 640x480 [SAR 1:1 DAR 4:3], 2006 kb/s, 29.97 fps, 29.97 tbr, 30k tbn, 59.94 tbc (default)



video_large.webm
Duration: 00:00:04.83, start: 0.000000, bitrate: 677 kb/s
    Stream #0:0: Video: vp9 (Profile 0), yuv420p(tv), 640x480, SAR 1:1 DAR 4:3, 24 fps, 24 tbr, 1k tbn, 1k tbc (default)



video_large_mpeg4.mp4
Duration: 00:00:04.90, start: 0.023220, bitrate: 994 kb/s
    Stream #0:0(und): Video: mpeg4 (Simple Profile) (mp4v / 0x7634706D), yuv420p, 640x480 [SAR 1:1 DAR 4:3], 865 kb/s, 29.97 fps, 29.97 tbr, 30k tbn, 30k tbc (default)
```

File space on disk
```
80K	smth-smth-1.webm
1,3M	video_large.mp4 (h264 codec)
596K	video_large_mpeg4.mp4
400K	video_large.webm

```

## Benchmark results

Using `nocache` and deleting video files from fs cache using `cachedel`

```
Using runner: 'skvideo_alpha' on file: 'video_large.mp4'
385 ms ± 5.62 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
Using runner: 'skvideo_beta' on file: 'video_large.mp4'
399 ms ± 11.1 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
Using runner: 'pyav' on file: 'video_large.mp4'
333 ms ± 4.77 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

Using runner: 'skvideo_alpha' on file: 'video_large_mpeg4.mp4'
357 ms ± 4.65 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
Using runner: 'skvideo_beta' on file: 'video_large_mpeg4.mp4'
388 ms ± 6.95 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
Using runner: 'pyav' on file: 'video_large_mpeg4.mp4'
133 ms ± 1.47 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

Using runner: 'skvideo_alpha' on file: 'video_large.webm'
576 ms ± 9.96 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
Using runner: 'skvideo_beta' on file: 'video_large.webm'
588 ms ± 4.57 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
Using runner: 'pyav' on file: 'video_large.webm'
229 ms ± 4.85 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

Using runner: 'skvideo_alpha' on file: 'smth-smth-1.webm'
287 ms ± 5.69 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
Using runner: 'skvideo_beta' on file: 'smth-smth-1.webm'
288 ms ± 6.41 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
Using runner: 'pyav' on file: 'smth-smth-1.webm'
42.6 ms ± 522 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
```
