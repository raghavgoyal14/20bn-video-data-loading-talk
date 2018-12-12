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
382 ms ± 4.46 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
Using runner: 'skvideo_beta' on file: 'video_large.mp4'
388 ms ± 4.13 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
Using runner: 'pyav' on file: 'video_large.mp4'
332 ms ± 1.75 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
Using runner: 'nvvl' on file: 'video_large.mp4'
55.7 ms ± 5.68 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

Using runner: 'skvideo_alpha' on file: 'video_large_mpeg4.mp4'
569 ms ± 8.51 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
Using runner: 'skvideo_beta' on file: 'video_large_mpeg4.mp4'
584 ms ± 5.41 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
Using runner: 'pyav' on file: 'video_large_mpeg4.mp4'
132 ms ± 663 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
Using runner: 'nvvl' on file: 'video_large_mpeg4.mp4'
Not valid for this file

Using runner: 'skvideo_alpha' on file: 'video_large.webm'
883 ms ± 9.89 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
Using runner: 'skvideo_beta' on file: 'video_large.webm'
908 ms ± 12.4 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
Using runner: 'pyav' on file: 'video_large.webm'
227 ms ± 1.72 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
Using runner: 'nvvl' on file: 'video_large.webm'
Not valid for this file

Using runner: 'skvideo_alpha' on file: 'smth-smth-1.webm'
612 ms ± 3.51 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
Using runner: 'skvideo_beta' on file: 'smth-smth-1.webm'
617 ms ± 5.72 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
Using runner: 'pyav' on file: 'smth-smth-1.webm'
42.5 ms ± 944 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
Using runner: 'nvvl' on file: 'smth-smth-1.webm'
Not valid for this file

```

```

```
