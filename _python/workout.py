# importing modules
import pathlib
import helper
import random
import yaml

def getRandomItemsFromList(workouts: list, items: int) -> str:
    string = "AMRAP for 45 seconds, 15 second rest, 3 rounds\n\n"
    for item in random.sample(workouts, items):
            string += f"-  {item['name']}\n"
    return string

# processing
if __name__ == "__main__":
    try:
        root = pathlib.Path(__file__).parent.parent.resolve()
        yaml_file = root / "_data/workouts.yaml"
        print(yaml_file)
        with open(yaml_file, 'r') as stream:
            workouts = yaml.safe_load(stream)
        string = getRandomItemsFromList(workouts, 3)

        try:
            f = root / "_pages/morning.md"
            print(f)
            m = f.open().read()
            c = helper.replace_chunk(m, "workout_marker", string)
            f.open("w").write(c)
            print("Workout completed")
        except FileNotFoundError:
            print('Output File does not exist, unable to proceed')

    except FileNotFoundError:
        print('yaml_file does not exist, unable to proceed')