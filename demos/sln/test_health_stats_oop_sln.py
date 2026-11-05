# ==========================================
# SOLUTION
# ==========================================

from datetime import date
import pytest

# Assuming your class is in a file named health_stats.py
from health_stats_oop_sln import DailyHealthStats


# ==========================================
# Pytest Fixtures (Setup Data)
# ==========================================
@pytest.fixture
def default_stats():
    """Provides a standard baseline object for basic feature testing."""
    return DailyHealthStats(
        height_m=1.80,
        weight_kg=82.5,
        steps=5000,  # Halfway towards the default 10,000 step goal
        calories_burned=2500,
        avg_heart_rate=72,
    )


# ==========================================
# Existing Test Cases (Maintained)
# ==========================================


def test_initialization_with_defaults(default_stats):
    """Test that all metrics initialize correctly and date defaults to today."""
    assert default_stats.height_m == 1.80
    assert default_stats.weight_kg == 82.5
    assert default_stats.steps == 5000
    assert default_stats.calories_burned == 2500
    assert default_stats.avg_heart_rate == 72
    assert default_stats.log_date == date.today()
    assert default_stats.step_goal == 10000  # Default goal check


def test_initialization_with_custom_date():
    """Test that a specific historic date can be explicitly recorded."""
    custom_date = date(2026, 5, 12)
    stats = DailyHealthStats(
        height_m=1.80,
        weight_kg=82.5,
        steps=5000,
        calories_burned=2000,
        avg_heart_rate=65,
        log_date=custom_date,
    )
    assert stats.log_date == custom_date


def test_bmi_calculation(default_stats):
    """Test standard BMI calculation: weight / height^2.

    For 82.5kg and 1.80m, BMI should equal 25.46.
    """
    assert default_stats.bmi == 25.46


def test_bmi_raises_value_error_for_invalid_height():
    """Test that an invalid height of 0 or below throws a ValueError."""
    stats = DailyHealthStats(
        height_m=0, weight_kg=70.0, steps=0, calories_burned=0, avg_heart_rate=60
    )
    with pytest.raises(ValueError, match="Height must be greater than zero."):
        _ = stats.bmi


def test_estimated_stride_length(default_stats):
    """Test that stride length defaults strictly to 0.414 * height.

    For 1.80m, stride should round to 0.75m.
    """
    assert default_stats.estimated_stride_m == 0.75


def test_km_walked_calculation(default_stats):
    """Test distance calculation: (steps * stride) / 1000.

    5,000 steps * 0.75m stride = 3,750m -> 3.75 km.
    """
    assert default_stats.km_walked == 3.75


def test_km_walked_with_zero_steps():
    """Test that distance is exactly 0.00 when zero steps are logged."""
    stats = DailyHealthStats(
        height_m=1.70, weight_kg=60.0, steps=0, calories_burned=1500, avg_heart_rate=60
    )
    assert stats.km_walked == 0.0


# ==========================================
# New Feature Test Cases (Added)
# ==========================================


def test_initialization_with_custom_step_goal():
    """Test that a non-default step goal can be successfully initialized."""
    stats = DailyHealthStats(
        height_m=1.80,
        weight_kg=82.5,
        steps=0,
        calories_burned=0,
        avg_heart_rate=70,
        step_goal=12000,
    )
    assert stats.step_goal == 12000


def test_add_steps_increments_total(default_stats):
    """Test that calling add_steps increases the steps attribute properly."""
    assert default_stats.steps == 5000
    default_stats.add_steps(1500)
    assert default_stats.steps == 6500


def test_add_steps_raises_error_for_negative_values(default_stats):
    """Test that passing a negative step count throws a ValueError."""
    with pytest.raises(ValueError, match="Steps to add cannot be negative."):
        default_stats.add_steps(-500)


def test_goal_progress_percentage(default_stats):
    """Test progress percentages under, at, and over the goal mark."""
    # 5,000 / 10,000 steps = 50.0%
    assert default_stats.goal_progress_percent == 50.0

    # Increment up to exact goal milestone
    default_stats.add_steps(5000)
    assert default_stats.goal_progress_percent == 100.0

    # Capped at 100.0% even when exceeding goals
    default_stats.add_steps(2000)
    assert default_stats.goal_progress_percent == 100.0


def test_goal_achieved_status(default_stats):
    """Test the boolean flag tracking if a goal milestone was crossed."""
    assert default_stats.goal_achieved is False

    default_stats.add_steps(5000)
    assert default_stats.goal_achieved is True


def test_goal_progress_raises_error_for_invalid_goal():
    """Test that a goal configuration of zero or lower causes a ValueError."""
    stats = DailyHealthStats(1.80, 80.0, 1000, 1000, 70, step_goal=0)
    with pytest.raises(ValueError, match="Step goal must be greater than zero."):
        _ = stats.goal_progress_percent
