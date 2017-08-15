from nptdms import TdmsFile

tdms_file = TdmsFile("path_to_file.tdms")
channel = tdms_file.object('Group', 'Channel1')
data = channel.data
time = channel.time_track()
# do stuff with data


https://nptdms.readthedocs.io/en/latest/
