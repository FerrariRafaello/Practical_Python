# race_lap_tracker.py

# Track racers and their average lap times for a race

racers = []
MAX_PARTICIPANTS = 6
NUM_LAPS = 6

while True:
    start = input('Do you want to start a new race? Type [y] to continue or [n] to quit: ').strip().lower()
    if start != 'y':
        print("Exiting program.")
        break

    for participant in range(1, MAX_PARTICIPANTS + 1):
        name = input(f'Enter the name of participant {participant}: ').strip()
        lap_times = []
        for lap in range(1, NUM_LAPS + 1):
            while True:
                try:
                    time = float(input(f'Enter the result for lap {lap}: '))
                    lap_times.append(time)
                    break
                except ValueError:
                    print("Please enter a valid numeric value for the lap time.")

        avg = sum(lap_times) / NUM_LAPS
        racers.append({'name': name, 'lap_times': lap_times, 'average': avg})
        print(f"{name}'s lap times: {lap_times}")
        print(f"{name}'s average lap time: {avg:.2f}\n")

        # Optional: ask to continue before all participants
        if participant < MAX_PARTICIPANTS:
            cont = input("Add another participant? [y/n]: ").strip().lower()
            if cont != 'y':
                break

    # Show results after all participants
    print("\nRace results:")
    for racer in racers:
        print(f"Racer: {racer['name']} | Lap times: {racer['lap_times']} | Average: {racer['average']:.2f}")

    # Optionally rank by best average lap time
    racers_sorted = sorted(racers, key=lambda r: r['average'])
    print("\nRanking (Best Average Lap Time First):")
    for i, racer in enumerate(racers_sorted, 1):
        print(f"{i}. {racer['name']} - Avg Lap Time: {racer['average']:.2f}")

    # Ask if another race should be started
    again = input('\nDo you want to run another race? [y/n]: ').strip().lower()
    if again != 'y':
        print("Session ended. Thank you!")
        break
    else:
        racers.clear()  # Clear for the next race
