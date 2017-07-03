"# pubg

Goal: To build a utility to help guide player decision making using location and
      map data.

Need to finish filling out all of this stuff in txt files or some documentation:

  general project direction,
  to do list,
  building out infrastructure

Have done already:

  simple tool for grabbing screenshots. req: pillow

To Do List:

  --begin logging function runtime

  --get tool for getting image directly from GPU for processing

  --build cpu equivalent for runtime comparisons

  --build tool for getting image of map from game screen

  --build tool to automatically gather location data from game
  (keylogger/robot reference: https://stackoverflow.com/questions/13207678/whats-the-simplest-way-of-detecting-keyboard-input-in-python-from-the-terminal )

  --build library for map image processing:
    -determine building clusters (num buildings and location),
    -predict circles (possibly use this to determine player location),
    -terrain data (for player movement and loot path mapping)

  --analyze image of map from game screen to determine quadrants, buildings, etc.

  --ingest data from data images relevant to location data.
  
  --build out dictionaries using information mined from maps (data amortization)

  --build functions for:
    -determining plane line (and distance to "good" drop zones),
    -distance measurement (point to point, quadrant measurement),
    -circle calculations (center and radius)

  --have tool suggest next destination in looting path:
    -include variable of player input,
    -create some sort of DAG structure for path algorithm (make path algorithm),


determine if additional resources needed."
