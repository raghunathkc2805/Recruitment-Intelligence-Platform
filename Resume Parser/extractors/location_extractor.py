from utils.knowledge_base import INDIA_CITIES, INDIA_STATES


def extract_locations(text):
    """
    Extract cities and states from resume text.
    """

    text_lower = text.lower()

    cities = []
    states = []

    for city in INDIA_CITIES:
        if city.lower() in text_lower and city not in cities:
            cities.append(city)

    for state in INDIA_STATES:
        if state.lower() in text_lower and state not in states:
            states.append(state)

    return {
        "cities": cities,
        "states": states,
        "primary_city": cities[0] if cities else "",
        "primary_state": states[0] if states else ""
    }