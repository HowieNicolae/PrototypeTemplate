# ==========================================
# SOLUTION
# ==========================================

from datetime import date


class DailyHealthStats:
    """Tracks daily health metrics including dates, goal progress, and distance tracking."""

    def __init__(
        self,
        height_m: float,
        weight_kg: float,
        steps: int,
        calories_burned: int,
        avg_heart_rate: int,
        step_goal: int = 10000,  # Standard health milestone default
        log_date: date = None,  # Defaults to today if not provided
    ):
        # Static metric
        self.height_m = height_m

        # Daily variable metrics
        self.weight_kg = weight_kg
        self.steps = steps
        self.calories_burned = calories_burned
        self.avg_heart_rate = avg_heart_rate

        # Step goals
        self.step_goal = step_goal

        # Date tracking (uses provided date or defaults to today)
        self.log_date = log_date if log_date is not None else date.today()

    def add_steps(self, steps_walked: int) -> None:
        """Increments the daily steps total by a given positive amount."""
        if steps_walked < 0:
            raise ValueError("Steps to add cannot be negative.")
        self.steps += steps_walked

    @property
    def bmi(self) -> float:
        """Calculates and returns the Body Mass Index (BMI)."""
        if self.height_m <= 0:
            raise ValueError("Height must be greater than zero.")
        return round(self.weight_kg / (self.height_m**2), 2)

    @property
    def estimated_stride_m(self) -> float:
        """Estimates stride length in meters based on height.

        Uses the standard average multiplier of 0.414 * height.
        """
        return round(self.height_m * 0.414, 2)

    @property
    def km_walked(self) -> float:
        """Calculates total estimated kilometers walked.

        Formula: (steps * stride_length_in_meters) / 1000 meters in a km
        """
        total_meters = self.steps * self.estimated_stride_m
        return round(total_meters / 1000, 2)

    @property
    def goal_progress_percent(self) -> float:
        """Calculates percentage of step goal achieved, capped at 100.0%."""
        if self.step_goal <= 0:
            raise ValueError("Step goal must be greater than zero.")
        progress = (self.steps / self.step_goal) * 100
        return round(min(progress, 100.0), 1)

    @property
    def goal_achieved(self) -> bool:
        """Returns True if the daily step goal has been met or exceeded."""
        return self.steps >= self.step_goal


# ==========================================
# Example Usage
# ==========================================
if __name__ == "__main__":
    # Example 1: Creating a profile for today tracking steps incrementally
    today_stats = DailyHealthStats(
        height_m=1.80,
        weight_kg=82.5,
        steps=4500,  # Starting steps for the day
        calories_burned=1500,
        avg_heart_rate=72,
        step_goal=10000,  # Targeting 10k steps
    )

    print(f"--- Morning Health Summary for {today_stats.log_date} ---")
    print(f"Steps Walked:      {today_stats.steps:,} / {today_stats.step_goal:,}")
    print(f"Goal Progress:     {today_stats.goal_progress_percent}%")
    print(f"Goal Achieved?     {today_stats.goal_achieved}")
    print(f"Distance Walked:   {today_stats.km_walked} km")
    print(f"Calculated BMI:    {today_stats.bmi}")

    # Simulating walking later in the afternoon
    print("\n...Logging an evening walk (adding 6,000 steps)...")
    today_stats.add_steps(6000)

    print(f"\n--- End of Day Summary for {today_stats.log_date} ---")
    print(f"Total Steps:       {today_stats.steps:,} / {today_stats.step_goal:,}")
    print(f"Goal Progress:     {today_stats.goal_progress_percent}%")
    print(f"Goal Achieved?     {today_stats.goal_achieved}")
    print(f"Final Distance:    {today_stats.km_walked} km")

    # Example 2: Manually logging data for an intensive past workout day
    past_stats = DailyHealthStats(
        height_m=1.80,
        weight_kg=83.0,
        steps=15500,
        calories_burned=3100,
        avg_heart_rate=84,
        step_goal=12000,
        log_date=date(2026, 10, 25),  # YYYY, MM, DD
    )

    print(f"\n--- Historic Health Summary for {past_stats.log_date} ---")
    print(f"Steps Registered:  {past_stats.steps:,} (Goal: {past_stats.step_goal:,})")
    print(f"Distance Covered:  {past_stats.km_walked} km")
    print(
        f"Goal Achieved?     {past_stats.goal_achieved} ({past_stats.goal_progress_percent}%)"
    )
