import unittest

storage = {}


def add(date: str, amount: float) -> bool:
    if not date.isdigit() or len(date) != 8:
        raise ValueError("Invalid date format")

    storage[date] = storage.get(date, 0.0) + amount
    return True


def calculate_total() -> float:
    total = sum(storage.values())
    return total


def calculate_within_range(start_date: str, end_date: str) -> float:
    total = 0.0
    for date, amount in storage.items():
        if start_date <= date <= end_date:
            total += amount
    return total


class FinanceTrackerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        storage.update({"20220101": 100.0, "20220102": 200.0, "20220103": 300.0})

    def test_add_endpoint(self):
        add("20220104", 400.0)
        self.assertEqual(storage["20220104"], 400.0)

    def test_calculate_total_endpoint(self):
        total = calculate_total()
        self.assertEqual(total, 1000.0)

    def test_calculate_within_range_endpoint(self):
        total = calculate_within_range("20220101", "20220102")
        self.assertEqual(total, 300.0)

    def test_add_endpoint_invalid_date_format(self):
        with self.assertRaises(ValueError):
            add("2022-01-04", 400.0)

    def test_calculate_total_endpoint_no_data(self):
        storage.clear()
        total = calculate_total()
        self.assertEqual(total, 0.0)

    def test_calculate_within_range_endpoint_no_data(self):
        storage.clear()
        total = calculate_within_range("20220101", "20220102")
        self.assertEqual(total, 0.0)


if __name__ == "__main__":
    unittest.main()
