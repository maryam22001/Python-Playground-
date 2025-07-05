def calc_shipping_cost(weight, distance):
    """
    Calculate the shipping cost based on weight and distance.
    
    Parameters:
    weight (float): The weight of the package in kg.
    distance (float): The distance to ship in km.
    
    Returns:
    float: The calculated shipping cost.
    """
    base_cost = 5.0  # Base cost for shipping
    cost_per_kg = 2.0  # Cost per kg
    cost_per_km = 0.5  # Cost per km
    
    total_cost = base_cost + (cost_per_kg * weight) + (cost_per_km * distance)
    return total_cost