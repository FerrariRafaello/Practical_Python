from typing import List

# Lists to store pilot info
pilots: List[dict] = []

def clear_screen():
    print('\n' * 50)

def menu() -> int:
    print('[1] - Add pilot\n'
          '[2] - Remove pilot\n'
          '[3] - List pilots\n'
          '[4] - Show ranking\n'
          '[5] - Exit')
    try:
        return int(input(': '))
    except ValueError:
        return 0  # Invalid input

def create_pilot() -> dict:
    clear_screen()
    name = input('Enter pilot name: ')
    laps = []
    for i in range(1, 7):  # 6 laps
        while True:
            try:
                lap = float(input(f'Enter time for lap {i}: '))
                laps.append(lap)
                break
            except ValueError:
                print("Invalid time, please enter a numeric value.")
    avg_score = sum(laps) / len(laps)
    return {'name': name, 'laps': laps, 'average': avg_score}

def find_pilot_index(name: str) -> int:
    for i, pilot in enumerate(pilots):
        if pilot['name'].lower() == name.lower():
            return i
    return -1

def add_pilot():
    pilot = create_pilot()
    pilots.append(pilot)
    print('Pilot added! Press <Enter> to continue.')
    input()

def remove_pilot():
    name = input('Enter the name of the pilot to remove: ')
    index = find_pilot_index(name)
    clear_screen()
    if index != -1:
        removed = pilots.pop(index)
        print(f'Removed pilot: {removed["name"]}')
    else:
        print('Pilot not found.')
    input('Press <Enter> to continue.')

def list_pilots():
    clear_screen()
    if not pilots:
        print('No pilots in the list.')
    else:
        print('Pilots:')
        for pilot in pilots:
            print(f"- {pilot['name']} | Laps: {pilot['laps']} | Average: {pilot['average']:.2f}")
    input('Press <Enter> to continue.')

def show_ranking():
    clear_screen()
    if not pilots:
        print('No pilots to rank.')
    else:
        # Rank by average (lower average = better)
        ranked = sorted(pilots, key=lambda x: x['average'])
        print('Ranking (Best Avg Lap Time First):')
        for i, pilot in enumerate(ranked, 1):
            print(f"{i}. {pilot['name']} - Avg: {pilot['average']:.2f}")
    input('Press <Enter> to continue.')

# Main menu loop
option = 0
while option != 5:
    clear_screen()
    option = menu()
    if option == 1:
        add_pilot()
    elif option == 2:
        remove_pilot()
    elif option == 3:
        list_pilots()
    elif option == 4:
        show_ranking()
    elif option == 5:
        break
    else:
        print('Invalid option!')
        input('Press <Enter> to continue.')
print('Session ended by user.')
