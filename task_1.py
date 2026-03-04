time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0

# Разделяем по запятым (это отдельные интервалы или группы)
for interval in time_string.split(','):
    # Внутри интервала могут быть значения через пробел
    for item in interval.split():
        if 'h' in item:
            hours = int(item[:-1])  # убираем последний символ 'h'
            total_minutes += hours * 60
        elif 'm' in item:
            minutes = int(item[:-1])
            total_minutes += minutes
        elif 's' in item:
            seconds = int(item[:-1])
            total_minutes += seconds // 60

print("Общее количество минут:", total_minutes)
