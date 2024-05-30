
def Data01(data):
    results = []

    for feature in data['features']:
        project = feature['properties']['project']
        max_Temperature = feature['properties']['maxTemperature']
        hotspot_type = feature['properties']['hotspot_type']
        priority = feature['properties']['priority']
        string_tag = feature['properties']['tag']

        result = {
            "Project": project,
            "Max Temperature": max_Temperature,
            "hotspot_type": hotspot_type,
            "priority": priority,
            "string_tag": string_tag
        }

        results.append(result)

    return results

