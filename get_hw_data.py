def get_data():
    value = 0
    with open('/sys/class/thermal/thermal_zone0/temp') as p:
        value = p.readline()

    return int(value)

def get_cpu_tmpl():
    value = get_data()
    return round(value/1000, 2)
    
