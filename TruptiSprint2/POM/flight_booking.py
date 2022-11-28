from DATA import reading_objects
flight_object = reading_objects.read_locators()
# # print(login_objects)
import time

class SearchFlight:
    def __init__(self,driver):
        self.driver= driver

    def click_login_popup(self):
        self.driver.find_element(*flight_object["login_pop"]).click()


    def enter_trip_type(self):
        self.driver.find_element(*flight_object["one_way"]).click()

        self.driver.find_element(*flight_object["round_way"]).click()

    def enter_Nooftravellers(self):
        self.driver.find_element(*flight_object["adult_economy"]).click()

        self.driver.find_element(*flight_object["adult_1"]).click()

        self.driver.find_element(*flight_object["children_1"]).click()

    def where_from(self,value1):
        self.value1 = value1
        departure = self.driver.find_element(*flight_object["where_from"])
        departure.click()
        dept=departure.send_keys(value1[0])
        time.sleep(2)

        city_dept = self.driver.find_elements(*flight_object["city_dept"])
        for city in city_dept:
            city.click()
            break

    def where_to(self,value1):
        self.value1 = value1
        arrival = self.driver.find_element(*flight_object["where_to"])
        arrival.click()
        time.sleep(2)
        arri=arrival.send_keys(value1[1])
        time.sleep(2)

        city_arri = self.driver.find_elements(*flight_object["city_arri"])
        for city in city_arri:
            city.click()
            break

    def return_trip(self):
        self.driver.find_element(*flight_object["round_way"]).click()

        self.driver.find_element(*flight_object["one_way"]).click()

    def enter_date(self):
        self.driver.find_element(*flight_object["date_1"]).click()
        self.driver.find_element(*flight_object["enter_date1"]).click()

        self.driver.find_element(*flight_object["return"]).click()
        self.driver.find_element(*flight_object["return_date"]).click()

    def click_arrrow(self):
        self.driver.find_element(*flight_object["click.arrow"]).click()

    def click_search(self):
        assert self.value1[0] != self.value1[1],"source and destination cannot be same"
        self.driver.find_element(*flight_object["click.search"]).click()


# sf=SearchFlight()
# sf.click_login_popup()
# sf.enter_trip_type()
# sf.enter_Nooftravellers()
# sf.where_from()
# sf.where_to()
# sf.return_trip()
# sf.enter_date()
# sf.click_arrrow()
# sf.click_search()










