import folium


def mark_circles_on_map(base_map, locations, data, value_multiplier, color):
    '''
    
    '''
    for k in data:
        _value = data[k]
        _radius = _value * value_multiplier
        _popup = str(_value) + " | " + k
        folium.CircleMarker(
            location=locations[k],
            radius=_radius,
            popup=_popup,
            color=color,
            fill_opacity=0.5
        ).add_to(base_map)
