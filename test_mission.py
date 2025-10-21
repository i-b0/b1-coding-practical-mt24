
from uuv_mission.dynamic import Mission

# Load the CSV and create a Mission instance
mission = Mission.from_csv("data/mission.csv")

# Print some results to check
print("Reference (first 5):", mission.reference[:5])
print("Cave height (first 5):", mission.cave_height[:5])
print("Cave depth (first 5):", mission.cave_depth[:5])