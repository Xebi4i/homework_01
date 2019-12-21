import json
import pytest
import requests
import employee


class TestIntegration:
    employee = employee.Employee()

# Test verifies the request with no User Agent will be rejected.
    def test_get_request_with_no_user_agent(self):
        url = "http://dummy.restapiexample.com/api/v1/employee/1"
        response = requests.get(url)

        assert response.status_code == 406

# Test verifies the well decorated GET request will be handled by server with no errors
    def test_get_request_with_user_agent(self):
        url = "http://dummy.restapiexample.com/api/v1/employee/1"
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                     'Chrome/79.0.3945.88 Safari/537.36'
        headers = {'User-Agent': user_agent}
        response = requests.get(url, headers=headers)

        assert response.status_code == 200

# Test verifies POST request with good data in it is handled by server with no errors.
    def test_positive_post_request(self):
        url = "http://dummy.restapiexample.com/api/v1/create"
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                     'Chrome/79.0.3945.88 Safari/537.36'
        headers = {'User-Agent': user_agent, 'Content-Type': 'application/json'}
        name = self.employee.get_name()
        salary = self.employee.get_salary()
        age = self.employee.get_age()
        payload = {'name': name, 'salary': salary, 'age': age}

        response = requests.post(url, headers=headers, data=json.dumps(payload))
        results = response.json()
        employee_id = results["id"]
        self.employee.set_employee_id(employee_id)

        assert response.status_code == 200
        assert int(employee_id) > 0
        assert results["name"] == name
        assert results["salary"] == salary
        assert results["age"] == age

# Test verifies the data that was sent with POST is reachable via GET method
    def test_new_data_is_reachable_via_get(self):
        url = "http://dummy.restapiexample.com/api/v1/employee/"
        employee_id = self.employee.get_employee_id()
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                     'Chrome/79.0.3945.88 Safari/537.36'
        headers = {'User-Agent': user_agent}
        response = requests.get(url + employee_id, headers=headers)
        results = response.json()

        assert response.status_code == 200
        assert results["id"] == self.employee.get_employee_id()
        assert results["employee_name"] == self.employee.get_name()
        assert results["employee_salary"] == self.employee.get_salary()
        assert results["employee_age"] == self.employee.get_age()

# Test verifies POST request with not unique name parameter will be handled by server with error message in response
    def test_negative_post_request_with_not_unique_name_parameter(self):
        url = "http://dummy.restapiexample.com/api/v1/create"
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                     'Chrome/79.0.3945.88 Safari/537.36'
        headers = {'User-Agent': user_agent, 'Content-Type': 'application/json'}
        name = self.employee.get_name()
        salary = self.employee.get_salary()
        age = self.employee.get_age()
        payload = {'name': name, 'salary': salary, 'age': age}

        response = requests.post(url, headers=headers, data=json.dumps(payload))
        results = response.text
        error_text = "Integrity constraint violation: 1062 Duplicate entry '{}' for key 'employee_name_unique'"\
            .format(name)

        assert response.status_code == 200
        assert error_text in results

# Test verifies POST request with missed name parameter in data will be handled by server with error message in response
    def test_negative_post_request_with_missed_name_parameter(self):
        url = "http://dummy.restapiexample.com/api/v1/create"
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                     'Chrome/79.0.3945.88 Safari/537.36'
        headers = {'User-Agent': user_agent, 'Content-Type': 'application/json'}
        salary = self.employee.get_salary()
        age = self.employee.get_age()
        payload = {'salary': salary, 'age': age}

        response = requests.post(url, headers=headers, data=json.dumps(payload))
        results = response.text
        error_text = "Integrity constraint violation: 1048 Column 'employee_name' cannot be null"

        assert response.status_code == 200
        assert error_text in results
