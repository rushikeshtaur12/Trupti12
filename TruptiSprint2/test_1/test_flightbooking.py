from POM.flight_booking import SearchFlight
from DATA import reading_objects
import pytest
data_obj=reading_objects.read_data()
@pytest.mark.parametrize("value1",data_obj)
class TestSearchFlight:
    def test_searchFlight(self,_driver,value1):
        sf=sf=SearchFlight(_driver)
        sf.click_login_popup()
        sf.enter_trip_type()
        sf.enter_Nooftravellers()
        sf.where_from(value1)
        sf.where_to(value1)
        sf.return_trip()
        sf.enter_date()
        sf.click_arrrow()
        sf.click_search()

















