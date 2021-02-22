# rocket.py

# https://www.stupid-projects.com/devops-for-embedded-part-1/

# https://blog.feabhas.com/2017/09/introduction-docker-embedded-developers-part-1-getting-started/

# https://blog.feabhas.com/2017/10/introduction-docker-embedded-developers-part-2-building-images/

def imperial_to_metric(altitude):
    # Convert feet to meters
    return 0.3048 * altitude


def metric_to_imperial(altitude):
    # Convert meters to feet
    return 3.28084 * altitude


def read_sensor():
    # Get value from sensor
    return 23.6


def rocket_name(name):
    # Capitalize rocket name
    if not isinstance(name, str):
        raise TypeError('Please provide a string argument.')
    return name.upper()


def tw_ratio(thrust, weight):
    # Calculate Thrust-to-Weight ratio
    return thrust / weight


if __name__ == "__main__":

    name = rocket_name('piccard')

    thrust = 8.0
    weight = 6.2

    twr = tw_ratio(thrust, weight)

    print(f"Rocket: {name}")
    print(f"Thrust-to-Weight Ratio: {twr:.2f}")
