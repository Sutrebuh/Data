from nptdms import TdmsFile

tdms_file = TdmsFile("data1.tdms")
print tdms_file.groups()
print tdms_file.object()
#channel = tdms_file.object('Group', 'Channel1')
#data = channel.data
#time = channel.time_track()
# do stuff with data

test = tdms_file.as_dataframe()
print test

data = tdms_file.channel_data('U-Remote','dt')
print data

channel = tdms_file.group_channels('U-Remote')
#print channel
#https://nptdms.readthedocs.io/en/latest/
