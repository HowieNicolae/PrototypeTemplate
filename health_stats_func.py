# ==========================================
# STUDENT TEMPLATE
# ==========================================

from datetime import date

# ==========================================
# Functional Core Logic
# ==========================================


def create_daily_health_stats(
    height_m: float,
    weight_kg: float,
    steps: int,
    calories_burned: int,
    avg_heart_rate: int,
    step_goal: int = 10000,
    log_date: date = None,
) -> dict:
    """Creates and returns a dictionary tracking daily health metrics."""
    ...


def add_steps(stats: dict, steps_walked: int) -> None:
    """Increments the daily steps total in the stats dictionary by a given positive amount."""
    ...


def calculate_bmi(stats: dict) -> float:
    """Calculates and returns the Body Mass Index (BMI)."""
    ...


def estimate_stride_m(stats: dict) -> float:
    """Estimates stride length in meters based on height."""
    ...


def calculate_km_walked(stats: dict) -> float:
    """Calculates total estimated kilometers walked."""
    ...


def calculate_goal_progress_percent(stats: dict) -> float:
    """Calculates percentage of step goal achieved, capped at 100.0%."""
    ...


def is_goal_achieved(stats: dict) -> bool:
    """Returns True if the daily step goal has been met or exceeded."""
    ...


# ==========================================
# Example Usage
# ==========================================
if __name__ == "__main__":
    # Example 1: Creating stats for today tracking steps incrementally
    today_stats = create_daily_health_stats(
        height_m=1.80,
        weight_kg=82.5,
        steps=4500,  # Starting steps for the day
        calories_burned=1500,
        avg_heart_rate=72,
        step_goal=10000,  # Targeting 10k steps
    )

    print(f"--- Morning Health Summary for {today_stats['log_date']} ---")
    print(f"Steps Walked:      {today_stats['steps']:,} / {today_stats['step_goal']:,}")
    print(f"Goal Progress:     {calculate_goal_progress_percent(today_stats)}%")
    print(f"Goal Achieved?     {is_goal_achieved(today_stats)}")
    print(f"Distance Walked:   {calculate_km_walked(today_stats)} km")
    print(f"Calculated BMI:    {calculate_bmi(today_stats)}")

    # Simulating walking later in the afternoon
    print("\n...Logging an evening walk (adding 6,000 steps)...")
    add_steps(today_stats, 6000)

    print(f"\n--- End of Day Summary for {today_stats['log_date']} ---")
    print(f"Total Steps:       {today_stats['steps']:,} / {today_stats['step_goal']:,}")
    print(f"Goal Progress:     {calculate_goal_progress_percent(today_stats)}%")
    print(f"Goal Achieved?     {is_goal_achieved(today_stats)}")
    print(f"Final Distance:    {calculate_km_walked(today_stats)} km")

    # Example 2: Manually logging data for an intensive past workout day
    past_stats = create_daily_health_stats(
        height_m=1.80,
        weight_kg=83.0,
        steps=15500,
        calories_burned=3100,
        avg_heart_rate=84,
        step_goal=12000,
        log_date=date(2026, 10, 25),  # YYYY, MM, DD
    )

    print(f"\n--- Historic Health Summary for {past_stats['log_date']} ---")
    print(
        f"Steps Registered:  {past_stats['steps']:,} (Goal: {past_stats['step_goal']:,})"
    )
    print(f"Distance Covered:  {calculate_km_walked(past_stats)} km")
    print(
        f"Goal Achieved?     {is_goal_achieved(past_stats)} ({calculate_goal_progress_percent(past_stats)}%)"
    )
