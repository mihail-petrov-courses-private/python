def generate():
    # първо: вашата височина в сантиметри;
    height = float(input('Колко си висок в сантименти')) / 100
    
    # второ: вашето тегло в килограми.
    weight = float(input('Колко тежиш в килограми'))

    body_mass_index = weight / (height * height)

# под 16	под норма	генерираме цифра - 1
    if body_mass_index < 16:
        return 1
    
    if in_between(body_mass_index, 16, 16.99):
        return 2
    
    if body_mass_index >=17 and body_mass_index <= 18.49:
        return 3
    
    if body_mass_index >=18.5 and body_mass_index <= 24.99:
        return 4
    
    if body_mass_index >=25 and body_mass_index <= 29.99:
        return 5
    
    if body_mass_index >=30 and body_mass_index <= 34.99:
        return 6
    
    if body_mass_index >=35 and body_mass_index <= 39.99:
        return 7
    
    if body_mass_index >=40:
        return 8
    
def in_between(var, start, end):
    return var >= start and var <= end
