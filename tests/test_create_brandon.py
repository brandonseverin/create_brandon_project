import pytest
from datetime import datetime, timezone
from create_brandon.scripts.helper_functions import create_parent_name, wpm_to_cps
import os


# Nightmate to test as it is a CLI application
# def test_directory_name():
#     # Arrange
#     create_brandon.main()

#     now = datetime.now(timezone.utc)
#     date_today = now.strftime("%Y%m%d")
#     # Act - Search through current working directory
#     directories = [f for f in os.listdir(".") if not os.path.isfile(f)]
#     result = [word for word in directories if date_today in word]
#     # Assert
#     assert date_today == result[: len(date_today)]


def test_create_parent_name():
    # Arrange
    now = datetime.now(timezone.utc)
    date_today = now.strftime("%Y%m%d")
    # Act
    parent_name = create_parent_name(date_today=date_today)
    # Assert
    assert date_today == parent_name[: len(date_today)]


def test_wps_to_cps():
    # Arrange
    typing_speed = 1
    # Act
    cps = wpm_to_cps(typing_speed=typing_speed)
    # Assert
    assert typing_speed * 5 / 60 == cps

