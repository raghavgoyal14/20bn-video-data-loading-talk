from IPython import get_ipython
import av  # noqa
import skvideo.io # noqa

ipython = get_ipython()

skvideo_alpha = "timeit v = skvideo.io.vread('{}')"
skvideo_beta = "timeit r = skvideo.io.vreader('{}') ; v= [i for i in r]"
pyav = "timeit r = av.open('{}') ; v = [i.to_rgb().to_nd_array() for i in r.decode(video=0)]"

runners = [(skvideo_alpha, 'skvideo_alpha'),
           (skvideo_beta, 'skvideo_beta'),
           (pyav, 'pyav')
           ]


large_mp4_h264 = "video_large.mp4"
large_mp4_mpeg4 = "video_large_mpeg4.mp4"
large_webm = "video_large.webm"
small_webm = "smth-smth-1.webm"

files = [large_mp4_h264,
         large_mp4_mpeg4,
         large_webm,
         small_webm]

for fi, ru in ((fi, ru) for fi in files for ru in runners):
    print("Using runner: '{}' on file: '{}'".format(ru[1], fi))
    ipython.magic(ru[0].format(fi))
