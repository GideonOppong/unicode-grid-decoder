import requests

def fetch_data(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.splitlines()
    except Exception as e:
        raise RuntimeError(f"Failed to fetch data: {e}")


def parse_points(lines):
    points = []
    max_x, max_y = 0, 0

    for line in lines:
        parts = line.strip().split()
        if len(parts) == 3:
            char, x, y = parts[0], int(parts[1]), int(parts[2])
            points.append((char, x, y))
            max_x = max(max_x, x)
            max_y = max(max_y, y)

    return points, max_x, max_y
