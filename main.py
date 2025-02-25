import logging
import time

from distance_measuring import get_absurd_measurement, get_absurd_elevatino_gain, get_absurd_elevation_gain
from strava_api import StravaAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_latest_activity()->None:
    try:
        strava_api = StravaAPI()
        activities = strava_api.fetch_n_last_activities(3)
    except Exception as e:
        logger.error(f"Error fetching activity: {e}")
        return 
    for activity in activities:
            
        if activity['type'] == 'Run' and not activity.get("description"):
            description = ""

            distance = activity.get('distance', 0)
            distance_measuring_unit, absurd_distance = get_absurd_measurement(distance)
            distance_description = get_absurd_elevatino_gain(distance_measuring_unit,absurd_distance)

            total_elevation_gain = activity.get('total_elevation_gain', 0)
            elevation_gain_unit, absurd_elevation_gain = get_absurd_measurement(total_elevation_gain)
            elevation_description = get_absurd_elevation_gain(elevation_gain_unit,absurd_elevation_gain)
            
            description = "\n".join(["Équivaut à :",distance_description, elevation_description])
            logger.info(description)
            strava_api.update_activity_fields(activity['id'], [('description', description)])

        else:
            logger.warning("Latest activity is not a run or already has a description.")

if __name__ == "__main__":
    while True:
        fetch_latest_activity()
        time.sleep(30)