Creator - Gil zur

Test API
----------

Description:
-------------
This API lets you running your tests according to multiple filters:
	
	1. By file name - Running all of the tests on the specify file.
	2. By test name - Running only the selected test.
	3. By marker - Running only the tests with the relevant markers.
---------------------------------------------------------------------

General Structure:
------------------
The swagger api consist of one folder with the main following files:
	1. swagger.yml - define the structure of the swagger ui.
	2. app.py - Define the API's code - every request from the swagger ui getting to the suitable function.
	
Additionally there is "ExampleTests" folder with two tests:
	@pytest.mark.critical
	def test_subtraction():
		assert 2 == 4, "The subtraction operation was failed, Expected to 4-2=2"


	@pytest.mark.low
	def test_multiplication():
		assert (2 * 2) == 4, "The subtraction operation was failed, Expected to 2*2=4"


Operating Instructions
-----------------------

In order to start working with the API:
	1. Import to your project the "Swagger ex" folder.
	2. Install the Packages from Pipfile.
	3. Run "app.py" file.
	4. Swagger UI will be available on "http://localhost:8080/ui/#/"