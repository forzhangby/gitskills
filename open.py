import json

with open('bing_paths.txt', 'r') as file:
    lines = file.readlines()

sites = []
for line_num, site in enumerate(lines, 1):
    site_obj = {
        'line': line_num,
        'site': site.strip()
    }
    sites.append(site_obj)

json_data = {'sites': sites}

with open('sites.json', 'w') as outfile:
    json.dump(json_data, outfile)
