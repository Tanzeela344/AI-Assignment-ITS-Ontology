def calculate_area(shape, **kwargs):
    if shape == "Triangle":
        return 0.5 * kwargs["base"] * kwargs["height"]
    elif shape == "Square":
        return kwargs["side"] ** 2
    elif shape == "Rectangle":
        return kwargs["length"] * kwargs["width"]
    elif shape == "Circle":
        import math
        return math.pi * (kwargs["radius"] ** 2)
    elif shape == "Trapezium":
        return 0.5 * (kwargs["base1"] + kwargs["base2"]) * kwargs["height"]
    elif shape == "Rhombus":
        return 0.5 * kwargs["diagonal1"] * kwargs["diagonal2"]
    elif shape == "Hexagon":
        import math
        return 1.5 * math.sqrt(3) * (kwargs["side"] ** 2)
    elif shape == "Pentagon":
        import math
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (kwargs["side"] ** 2)
    elif shape == "Octagon":
        import math
        return 2 * (1 + math.sqrt(2)) * (kwargs["side"] ** 2)
    else:
        return None
