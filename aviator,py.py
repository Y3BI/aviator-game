import random
import time

def aviator_simulation():
    """
    Simulates the Aviator game, demonstrating how the RNG determines the fly-away point.
    """
    print("Welcome to the Aviator Game Simulation!\n")

    # 1. Get User's Initial Bet
    while True:
        try:
            user_bet = float(input("Enter your bet amount: "))
            if user_bet > 0:
                break
            else:
                print("Please enter a positive bet amount.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # 2. Generate the Fly-Away Multiplier using RNG
    #    - This is the crucial part where the RNG determines the game's outcome.
    #    - We use a log-normal distribution to simulate a more realistic curve,
    #      where smaller multipliers are more common, but larger ones are possible.
    mean_log = 1.5  # Mean of the log of the distribution (adjust to change average multiplier)
    stdev_log = 0.7  # Standard deviation of the log (adjust to change volatility)
    fly_away_multiplier = random.lognormvariate(mean_log, stdev_log)

    # Ensure the multiplier is within a reasonable range
    fly_away_multiplier = max(1.0, fly_away_multiplier)  # Minimum multiplier
    fly_away_multiplier = min(100.0, fly_away_multiplier) # Maximum multiplier

    print(f"\nThe plane will fly away at a multiplier of approximately: {fly_away_multiplier:.2f}")
    time.sleep(2)  # Pause for suspense

    # 3. Simulate the Game Progression
    current_multiplier = 1.0
    print("\nStarting the flight...")

    while current_multiplier < fly_away_multiplier:
        # Increment the multiplier.  Use a smaller increment for smoother progression.
        increment = random.uniform(0.1, 0.3)
        current_multiplier += increment
        print(f"Current Multiplier: {current_multiplier:.2f}")
        time.sleep(0.2)  # Simulate time passing

        # 4. User Cash Out Logic
        cash_out = input("Cash out now? (y/n): ").lower()
        if cash_out == 'y':
            break # Exit the loop if user cashes out

    # 5. Determine the Outcome
    if current_multiplier >= fly_away_multiplier:
        print("\nOh no! The plane flew away before you cashed out.")
        print("You lose your bet.")
        winnings = 0
    else:
        winnings = user_bet * current_multiplier
        print(f"\nCongratulations! You cashed out at {current_multiplier:.2f}x.")
        print(f"You win: {winnings:.2f}")

    print("\nGame Over.")

aviator_simulation()
