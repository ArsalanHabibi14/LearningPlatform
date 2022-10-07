# sudo apt install mediainfo
# pip3 install pymediainfo
from pymediainfo import MediaInfo

media_info = MediaInfo.parse(
    'H:\ARSLAN\PracticeProjects\learning-web\learn_website\staticfiles\media_root\video\Test_Video.mp4')
for track in media_info.tracks:
    # for k in track.to_data().keys():
    #    print("{}.{}={}".format(track.track_type,k,track.to_data()[k]))
    if track.track_type == 'Video':
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("{} width                 {}".format(track.track_type, track.to_data()["width"]))
        print("{} height                {}".format(track.track_type, track.to_data()["height"]))
        print("{} duration              {}s".format(track.track_type, track.to_data()["duration"] / 1000.0))
        print("{} duration              {}".format(track.track_type, track.to_data()["other_duration"][3][0:8]))
        print("{} other_format          {}".format(track.track_type, track.to_data()["other_format"][0]))
        print("{} codec_id              {}".format(track.track_type, track.to_data()["codec_id"]))
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    elif track.track_type == 'Audio':
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("{} format                {}".format(track.track_type, track.to_data()["format"]))
        print("{} codec_id              {}".format(track.track_type, track.to_data()["codec_id"]))
        print("{} channel_s             {}".format(track.track_type, track.to_data()["channel_s"]))
        print("{} other_channel_s       {}".format(track.track_type, track.to_data()["other_channel_s"][0]))
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("********************************************************************")
