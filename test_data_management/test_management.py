import csv
import pytest

class TestDataManagement:

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data_from_csv(self):
        try:
            with open(self.file_path, 'r', newline='') as csv_file:
                self.data = list(csv.DictReader(csv_file))
                print(self.data)
            print("Data loaded successfully")
            if self.data:
                print("Keys in the first row:", self.data[0].keys())
        except Exception as e:
            print("Error in loading data", e)

    def get_test_data(self, test_case_name):        
        if self.data == None:
            print("No data found")
            return []
        try:
            test_data = [row for row in self.data if row['Test Case Name'] == test_case_name]
            return test_data
        except Exception as e:
            print("exception is", e)


@pytest.fixture()
def test_data_manager():
    file_path = "test_data.csv"
    data_manager = TestDataManagement(file_path)
    data_manager.load_data_from_csv()
    return data_manager


def test_get_data(test_data_manager):
    test_case_name = "Test Case 1"
    print("Test case name:", test_case_name)
    test_data = test_data_manager.get_test_data(test_case_name)
    print("Retrieved test data:", test_data)
    assert len(test_data) > 0
            




