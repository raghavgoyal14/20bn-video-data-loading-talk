import av  # noqa
import pynvvl  # order of av and pynvvl imports matters
import skvideo.io # noqa

from IPython import get_ipython
from torch.utils.dlpack import to_dlpack, from_dlpack

ipython = get_ipython()

# GPU id: 0
loader_nvvl = pynvvl.NVVLVideoLoader(device_id=0, log_level='error')

skvideo_alpha = "timeit v = skvideo.io.vread('{}')"
skvideo_beta = "timeit r = skvideo.io.vreader('{}') ; v= [i for i in r]"
pyav = "timeit r = av.open('{}') ; v = [i.to_rgb().to_nd_array() for i in r.decode(video=0)]"
nvvl = "timeit r = loader_nvvl.read_sequence('{}', normalized=True); v = from_dlpack(r.toDlpack())"

runners = [(skvideo_alpha, 'skvideo_alpha'),
           (skvideo_beta, 'skvideo_beta'),
           (pyav, 'pyav'),
           (nvvl, 'nvvl')
           ]


large_mp4_h264 = "video_large.mp4"
large_mp4_mpeg4 = "video_large_mpeg4.mp4"
large_webm = "video_large.webm"
small_webm = "smth-smth-1.webm"

files = [large_mp4_h264,
         large_mp4_mpeg4,
         large_webm,
         small_webm]

"""
Using runner: 'nvvl' on file: 'video_large_mpeg4.mp4'
terminate called after throwing an instance of 'std::runtime_error'
  what():  File video_large_mpeg4.mp4 is not the same size and codec as previous files. This is not yet supported. (640x480 instead of 640x480 or codec 13 != 28
"""

for fi, ru in ((fi, ru) for fi in files for ru in runners):
    print("Using runner: '{}' on file: '{}'".format(ru[1], fi))
    if ru[1] == "nvvl" and (fi.endswith('webm') or "mpeg4" in fi):
        print("Not valid for this file")
        continue
    ipython.magic(ru[0].format(fi))
