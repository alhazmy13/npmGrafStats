geoip = "yes"
bgeoip_bool =  False if str(geoip) == 'no' else True
print(bgeoip_bool)