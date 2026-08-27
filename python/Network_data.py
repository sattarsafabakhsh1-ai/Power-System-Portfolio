# network_data.py
# Milestone 1: Basic data structure of distribution network
# Structure: Each station has its own dictionary of feeders

network = {
    "Main Station": {
        "5012": {"name": "Main 5012", "type": "Feeder"},
        "5022": {"name": "Main 5022", "type": "Feeder"},
        "5032": {"name": "Main 5032", "type": "Feeder"},
        "5042": {"name": "Main 5042", "type": "Feeder"},
        "5052": {"name": "Main 5052", "type": "Feeder"},
        "5062": {"name": "Main 5062", "type": "Feeder"},
        "5072": {"name": "Main 5072", "type": "Feeder"},
        "5082": {"name": "Main 5082", "type": "Feeder"},
        "5092": {"name": "Main 5092", "type": "Feeder"},
        "5102": {"name": "Main 5102", "type": "Feeder"},
    },
    "Sarv Station": {
        "5012": {"name": "Sarv 5012", "type": "Feeder"},
        "5022": {"name": "Sarv 5022", "type": "Feeder"},
        "5062": {"name": "Sarv 5062", "type": "Feeder"},
        "5102": {"name": "Sarv 5102", "type": "Feeder"},
    },
    "Hamidiyeh Substation": {
        "5012": {"name": "Hamidiyeh 5012", "type": "Feeder"},
        "5022": {"name": "Hamidiyeh 5022", "type": "Feeder"},
        "5032": {"name": "Hamidiyeh 5032", "type": "Feeder"},
    },
    "Sabhan Substation": {
        "5052": {"name": "Sabhan 5052", "type": "Feeder"},
        "5162": {"name": "Sabhan 5162", "type": "Feeder"},
        "5172": {"name": "Sabhan 5172", "type": "Feeder"},
    },
}


for station, feeders in network.items():
    print(f"\n=== {station} ===")
    # bus_id = Bus ID (second-level key)
    # info = Information about that bus (second-level value)
    for bus_id, info in feeders.items():
        print(f"  Bus {bus_id}: {info['name']} ({info['type']})")

# Total number of feeders identified in the entire network
total_feeders = sum(len(feeders) for feeders in network.values())
print(f"\n Total number of identified feeders:{total_feeders}")
print(f"Number of Stations: {len(network)}")