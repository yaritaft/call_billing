import unittest
from classes import User,National_call,International_call,Phone_call,Regular_call,Late_night_call,Weekend_call,Rate_values

class Rate_values_TestCase(unittest.TestCase):
    def setUp(self):
        self.rate_values=Rate_values(0.05,0.02,0.01,1.0)
    def test_rate_national_values(self):
        """Test of a national call, this is the standar call that's why the multiplier keeps being 1."""
    def test_rate_international_values(self):
        self.assertEqual(self.rate_values.INTERNATIONAL_RATE,self.rate_values.NATIONAL_RATE*2)
    def test_weekend_rate_values(self):
      self.assertEqual(self.rate_values.WEEKEND_RATE,0.01)
    def test_regular_rate_values(self):
        self.assertEqual(self.rate_values.REGULAR_RATE,0.05)
    def test_night_rate_values(self):
        self.assertEqual(self.rate_values.LATE_NIGHT_RATE,0.02)
  

class Call_Rate_TestCase(unittest.TestCase):
    """In this class all the different rates are being tested and multipliers (National or International)."""
    def setUp(self):
        self.rate_values=Rate_values(0.05,0.02,0.01,1.0)
        self.national_call=National_call(self.rate_values)
        self.international_call=International_call(self.rate_values)
        self.yari=User('yari','taft','New')
        self.ivan=User('ivan','taft','Existing')
        self.national_call=National_call(self.rate_values)
        self.call_regular_nat=Regular_call(10,'20190404 19:00',self.rate_values)
        self.call_regular_nat.set_scope_call(self.national_call)
        self.call_late_night_nat=Late_night_call(7,'20190404 19:00',self.rate_values)
        self.call_late_night_nat.set_scope_call(self.national_call)
        self.call_weekend_nat=Weekend_call(2,'20190404 19:00',self.rate_values)
        self.call_weekend_nat.set_scope_call(self.national_call)
#These tests are only checking rates and multipliers(scope_rate).
    def test_national_call_rate(self):
        """Test of a national call, this is the standar call that's why the multiplier keeps being 1."""
        self.assertEqual(self.national_call.scope_rate(),1)
    def test_international_call_rate(self):
        """Tesf of International call, the multiplier in this case should be 2x more than national calls"""
        self.assertEqual(self.international_call.scope_rate(),2)

    def test_regular_call_rate_new_user(self):
        """Tesf of Regular call with a new user """
        self.assertEqual(self.call_regular_nat.rate(self.yari),0.02)
    def test_regular_call_rate_old_user(self):
        """ Tesf of Regular call with an old user"""
        self.assertEqual(self.call_regular_nat.rate(self.ivan),0.05)
    def test_late_night_call(self):
        """ Tesf of Late night call rate. In this test, it doesn't matter whether the call is from a new or existing user."""
        self.assertEqual(self.call_late_night_nat.rate(self.ivan),0.02)
    def test_weekend_call(self):
        """ Tesf of Weekend call. In this test, it doesn't matter whether the call is from a new or existing user."""
        self.assertEqual(self.call_weekend_nat.rate(self.ivan),0.01)

class Call_Calculation_TestCase(unittest.TestCase):
    """ Tesf call calculation, taking into account every variable."""
    def setUp(self):
        self.rate_values=Rate_values(0.05,0.02,0.01,1.0)
        self.yari=User('yari','taft','New')
        self.ivan=User('ivan','taft','Existing')        
        self.national_call=National_call(self.rate_values)
        self.international_call=International_call(self.rate_values)
        self.call_weekend_nat=Weekend_call(2,'20190404 19:00',self.rate_values)
        self.call_weekend_nat.set_scope_call(self.national_call)
        self.call_weekend_int=Weekend_call(1,'20190404 19:00',self.rate_values)
        self.call_weekend_int.set_scope_call(self.international_call)
        self.call_late_night_nat=Late_night_call(7,'20190404 19:00',self.rate_values)
        self.call_late_night_nat.set_scope_call(self.national_call)
        self.call_late_night_int=Late_night_call(9,'20190404 19:00',self.rate_values)
        self.call_late_night_int.set_scope_call(self.international_call)
        self.call_regular_nat=Regular_call(10,'20190404 19:00',self.rate_values)
        self.call_regular_nat.set_scope_call(self.national_call)
        self.call_regular_int=Regular_call(11,'20190404 19:00',self.rate_values)
        self.call_regular_int.set_scope_call(self.international_call)
        self.yari.set_calls([self.call_weekend_nat,self.call_late_night_int,self.call_regular_nat])
        self.ivan.set_calls([self.call_weekend_int,self.call_late_night_nat,self.call_regular_int])

    def test_call_weekend_nat(self):
        self.assertEqual(self.call_weekend_nat.calculate(self.yari),0.02)
    def test_call_weekend_int(self):
        self.assertEqual(self.call_weekend_int.calculate(self.yari),0.02)
    def test_call_late_night_nat(self):
        self.assertEqual(self.call_late_night_nat.calculate(self.yari),0.14)
    def test_call_late_night_int(self):
        self.assertEqual(self.call_late_night_int.calculate(self.yari),0.36)
    def test_call_regular_nat(self):
        self.assertEqual(self.call_regular_nat.calculate(self.yari),0.2)
    def test_call_regular_int(self):
        self.assertEqual(self.call_regular_int.calculate(self.yari),0.44)
    def test_call_regular_nat_existing_user(self):
        self.assertEqual(self.call_regular_nat.calculate(self.ivan),0.5)
    def test_call_regular_int_existing_user(self):
        self.assertEqual(self.call_regular_int.calculate(self.ivan),1.1)
    
class Total_User_Billing_Calculation_TestCase(unittest.TestCase):
    """Tesf of total billing calculations, one with an existing user and other with a new user. Each of
    them has different calls (Regular, National, International, Weekend Calls and Late Night Calls). """
    def setUp(self):
        #Weekend Rate 0.01, Late night Rate 0.02, Regular Rate 0.05, Multiplier National 1, Multiplier International 2
        self.rate_values=Rate_values(0.05,0.02,0.01,1.0)
        self.yari=User('yari','taft','New')
        self.ivan=User('ivan','taft','Existing')        
        self.national_call=National_call(self.rate_values)
        self.international_call=International_call(self.rate_values)
        self.call_weekend_nat=Weekend_call(2,'20190404 19:00',self.rate_values)
        self.call_weekend_nat.set_scope_call(self.national_call)
        self.call_weekend_int=Weekend_call(1,'20190404 19:00',self.rate_values)
        self.call_weekend_int.set_scope_call(self.international_call)
        self.call_late_night_nat=Late_night_call(7,'20190404 19:00',self.rate_values)
        self.call_late_night_nat.set_scope_call(self.national_call)
        self.call_late_night_int=Late_night_call(9,'20190404 19:00',self.rate_values)
        self.call_late_night_int.set_scope_call(self.international_call)
        self.call_regular_nat=Regular_call(10,'20190404 19:00',self.rate_values)
        self.call_regular_nat.set_scope_call(self.national_call)
        self.call_regular_int=Regular_call(11,'20190404 19:00',self.rate_values)
        self.call_regular_int.set_scope_call(self.international_call)
        self.yari.set_calls([self.call_weekend_nat,self.call_late_night_int,self.call_regular_nat])
        self.ivan.set_calls([self.call_weekend_int,self.call_late_night_nat,self.call_regular_int])

        self.yari.set_calls([self.call_weekend_nat,self.call_late_night_int,self.call_regular_nat])
        self.ivan.set_calls([self.call_weekend_int,self.call_late_night_nat,self.call_regular_int])
        self.julia=User('Julia','Mattone','New')
        self.julia.set_calls([self.call_weekend_int,self.call_late_night_nat,self.call_regular_int])   
        self.ryan=User('Ryan','Nasdaq','Existing')
        self.ryan.set_calls([self.call_weekend_nat,self.call_late_night_int,self.call_regular_nat])

    def test_yari_total_billing(self):
        """Tesf of the total billing calculation of a new user with:
        National weekend Call
        International late night Call
        National Regular Call """
        self.assertEqual(self.yari.calculate_billing(),0.58)

    def test_ryan_total_billing(self):
        """Tesf of the total calculation of an existing user with:
        National weekend Call
        International late night Call
        National Regular Call """
        self.assertEqual(self.ryan.calculate_billing(),0.88) 
    def test_ivan_total_billing(self):
        """Tesf of the total calculation of an existing user with:
        International weekend Call
        National late night Call
        International Regular Call """
        self.assertEqual(self.ivan.calculate_billing(),1.26) 

    def test_julia_total_billing(self):
        """Tesf of the total calculation of a new user with:
        International weekend Call
        National late night Call
        International Regular Call """
        self.assertEqual(self.julia.calculate_billing(),0.6) 


class Test_init_errors(unittest.TestCase):
    """Test of total billing calculations, one with an existing user and other with a new user. Each of
    them has different calls (Regular, National, International, Weekend Calls and Late Night Calls). """ 
    def setUp(self):
        self.valid_rates=Rate_values(1.0,2.0,3.0,4.0)

    def test_wrong_user_type(self):
        self.assertRaises(AttributeError, User,'yari','taft',5)
    def test_wrong_user_data(self):
        self.assertRaises(ValueError, User,'yari','taft','asd')

    def test_wrong_rate_values_type(self):
        self.assertRaises(AttributeError,Rate_values,1,2,3,'0')

    def test_wrong_national_call_type(self):
        self.assertRaises(AttributeError,National_call,[])

    def test_wrong_international_call_type(self):
        self.assertRaises(AttributeError,International_call,[])

    def test_wrong_generic_call_type_of_minutes(self):
        self.assertRaises(AttributeError,Phone_call,'ASD','19940404 19:00',self.valid_rates)

    def test_wrong_generic_call_type_of_date_time(self):
        self.assertRaises(AttributeError,Phone_call,44,99797,self.valid_rates)

    def test_wrong_rates_type_call(self):
        self.assertRaises(AttributeError,Phone_call,44,'19940404 19:00',[])

    def test_wrong_date_time_call_data(self):
        self.assertRaises(ValueError,Phone_call,44,'1949 949429 9429',self.valid_rates)

class Test_user_creation(unittest.TestCase):
    def setUp(self):
        self.yari=User('yari','taft','New')
    def test_user_surname(self):
        self.assertEqual(self.yari.surname,'taft')
    def test_user_name(self):
        self.assertEqual(self.yari.name,'yari')
    def test_user_calls(self):
        self.assertRaises(ValueError,self.yari.calls)

class Test_rate_call_errors(unittest.TestCase):
    """Test of call calculation errors with wrong user types. """
    def setUp(self):
        self.rate_values=Rate_values(0.05,0.02,0.01,1.0)
        self.national_call=National_call(self.rate_values)
        self.international_call=International_call(self.rate_values)
        self.yari=User('yari','taft','New')
        self.ivan=User('ivan','taft','Existing')
        self.national_call=National_call(self.rate_values)
        self.call_regular_nat=Regular_call(10,'20190404 19:00',self.rate_values)
        self.call_regular_nat.set_scope_call(self.national_call)
        self.call_late_night_nat=Late_night_call(7,'20190404 19:00',self.rate_values)
        self.call_late_night_nat.set_scope_call(self.national_call)
        self.call_weekend_nat=Weekend_call(2,'20190404 19:00',self.rate_values)
        self.call_weekend_nat.set_scope_call(self.national_call)
        self.rate_values2=Rate_values(0.05,0.02,0.01,1.0)
        self.rate_values2._NATIONAL_RATE=('A',)
        self.call_regular_nat2=Regular_call(10,'20190404 19:00',self.rate_values)
        self.call_regular_nat2._rate_values='A'
        self.call_late_night_nat2=Late_night_call(7,'20190404 19:00',self.rate_values)
        self.call_late_night_nat2._rate_values='A'
        self.call_weekend_nat2=Weekend_call(2,'20190404 19:00',self.rate_values)
        self.call_weekend_nat2._rate_values='A'
        self.call_weekend_nat3=Weekend_call(2,'20190404 19:00',self.rate_values)
        self.call_weekend_nat3._minutes=('A',)
        self.yari.set_calls([self.call_weekend_nat3])
 
    def test_total_billing_calculation_with_errors(self):
       self.assertRaises(ValueError,self.yari.calculate_billing)
 
    def test_call_calculation_without_minutes(self):
        self.assertRaises(AttributeError,self.call_weekend_nat3.calculate,self.yari)

    def test_weekend_call_without_rate_values(self):
        self.assertRaises(AttributeError,self.call_weekend_nat2.rate,self.yari)

    def test_night_call_without_rate_values(self):
        self.assertRaises(AttributeError,self.call_late_night_nat2.rate,self.yari)


    def test_regular_call_without_rate_values(self):
        self.assertRaises(AttributeError,self.call_regular_nat2.rate,self.yari)

    def test_call_without_user(self):
        self.assertRaises(AttributeError,self.call_regular_nat.calculate,'A')

    def test_late_night_call_calculation_wrong_user_type(self):
        self.assertRaises(AttributeError,self.call_late_night_nat.calculate,[])

    def test_weekend_call_calculation_wrong_user_type(self):
        self.assertRaises(AttributeError,self.call_weekend_nat.calculate,[])
        
    def test_regular_call_calculation_wrong_user_type(self):
        self.assertRaises(AttributeError,self.call_regular_nat.calculate,[])

    def test_international_call_rate_error(self):
        self.assertRaises(AttributeError,self.rate_values2.generate_international_rate)
   
    


if __name__ == '__main__':
    unittest.main()