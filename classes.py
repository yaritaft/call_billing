from datetime import datetime

class Rate_values:
    """ This class purpose is to have the rates of each type of call.
    
    Each call will be related to one object from this class, if prices change, then another instance of this 
    class may be created and the following calls will be related to that new object. Different rates may be 
    established for different users too, by creating multiple instances of this class.
    
    Attributes:
        REGULAR_RATE (float): Regular rate value per minute (pences),
        LATE_NIGHT_RATE (float): Late Night rate value per minute (pences),
        WEEKEND_RATE (float):  Weekend rate value per minute (pences),
        NATIONAL_RATE (float): National multiplier
        INTERNATIONAL_RATE (float): International multiplier
    """
    def __init__(self,REGULAR_RATE,LATE_NIGHT_RATE,WEEKEND_RATE,NATIONAL_RATE):
        """Create Rate_Values objects, set values and validate those values.
            Args:
                REGULAR_RATE (float): Regular rate value per minute (pences),
                LATE_NIGHT_RATE (float): Late Night rate value per minute (pences),
                WEEKEND_RATE (float):  Weekend rate value per minute (pences),
                NATIONAL_RATE (float): National multiplier
            Returns:
                None
        """
        self._REGULAR_RATE=REGULAR_RATE
        self._LATE_NIGHT_RATE=LATE_NIGHT_RATE
        self._WEEKEND_RATE=WEEKEND_RATE
        self._NATIONAL_RATE=NATIONAL_RATE
        self.generate_international_rate()
        self.validate_rates_type()
    
    def validate_rates_type(self):
        """Validate rate values by checking if they are float or not.
            Args:
                None
            Raises:
                AttributeError: When at least one rate is not a float value.
            Returns:
                None
        """
        if not (isinstance(self._REGULAR_RATE,float) & isinstance(self._LATE_NIGHT_RATE,float) & isinstance(self._WEEKEND_RATE,float) & isinstance(self._NATIONAL_RATE,float) & isinstance(self._INTERNATIONAL_RATE,float)):
            raise AttributeError("One of the rates is not set or it is not a float value.")
    #TODO, RESEARCH IF RATES MAY BE 0, IF NOT ANOTHER EXCEPTION SHOULD BE ADDED TO MITIGATE THAT POSSIBLE RISK
    def generate_international_rate(self):
        """Assign international rate by doubling the national rate also check if the National Rate is float.
            Args:
                None
            Raises:
                AttributeError: When the national set was not set or it is not valid.
            Returns:
                None
        """
        try:
            self._INTERNATIONAL_RATE=float(2*self._NATIONAL_RATE)
        except:
            raise AttributeError("The national rate was not set or the value is not valid because it is not a float number.")

    @property
    def REGULAR_RATE(self):
        """Get the REGULAR_RATE."""
        return self._REGULAR_RATE
    @property
    def LATE_NIGHT_RATE(self):
        """Get the current LATE_NIGHT_RATE."""
        return self._LATE_NIGHT_RATE
    @property
    def WEEKEND_RATE(self):
        """Get the current WEEKEND_RATE."""
        return self._WEEKEND_RATE
    @property
    def NATIONAL_RATE(self):
        """Get the current NATIONAL_RATE."""
        return self._NATIONAL_RATE
    @property
    def INTERNATIONAL_RATE(self):
        """Get the current INTERNATIONAL_RATE."""
        return self._INTERNATIONAL_RATE

class User:
    """This is a user, it has a name, a surname and a type of user. 
    
    Assuming that a user only can have one line, when this method is called "User.calls()" the program will gather 
    all the calls from that user. The user will also perform it's own billing by asking each call to be calculated.

    Attributes:
        name (string): User's name,
        surname (string): User's surname,
        type_of_user (string):  The type of user (for example: New or Existing)
    """
    def __init__(self,name,surname,type_of_user):
        """Create User instance, set values and validate those values.
            Args:
                name (string): User's name,
                surname (string): User's surname,
                type_of_user (string):  The type of user (for example: New or Existing)
            Returns:
                None
        """
        self._name=name
        self._surname=surname
        self._type_of_user=type_of_user
        self.validate_type_of_user()

    def validate_type_of_user(self):
        """ Validate the data type of a user also validate that type of user is a valid one.
            Args:
                None
            Raises:
                AttributeError: When the user does not have the proper data type.
                ValueError: When the type of user is not valid.
            Return:
                None
        """
        if not isinstance(self._type_of_user,str):
            raise AttributeError("The data type of type of user is not valid.")
        if ((self._type_of_user!="New") & (self._type_of_user!='Existing')):
            raise ValueError("The type of User is not valid.")

    @property
    def type_of_user(self):
        """Get the current type of user."""
        return self._type_of_user
    @property
    def surname(self):
        """Get the current surname."""
        return self._surname
    @property
    def name(self):
        """Get the current user name."""
        return self._name

    def set_calls(self,my_calls):
        """Only for test usage: I put a setter in order to assign some calls to each user, because I already have a calls method that gives me 
        all the calls from one user"""
        self._my_calls=my_calls

    def calls(self):
        """Only for test usage: Method to get all the calls from one user"""
        try:
            return self._my_calls
        except:
            raise ValueError("No calls were loaded for this user.")


    def calculate_billing(self):
        """Sum the cost of every call from one user. The cost of each call is made by a method called calculate and 
        it's defined in the Phone_Call Class.
            Args:
                None
            Raises:
                ValueError: When a call could not be calculated due to some error when calling calculate.
            Return:
                Float (2 decimal places)"""
        accumulator=0
        for call in self.calls():
            try:
                accumulator=accumulator+call.calculate(self)
            except:
                raise ValueError("A Call could not be calculated.")
        return round(accumulator,2)

class Distance_call:
    """ This is a super class made to apply the same init function and validate rate values with national
    and international calls as well.
    Attributes:
        rate_values (Rate_values): Rate values (pences)
    """
    def __init__(self,rate_values):
        """Create Distance_call objects, set values and validate those values.
            Args:
                rate_values (Rate_values): Rate values (pences)
            Returns:
                None
        """
        self._rate_values=rate_values
        self.validate_rate_values()
    def validate_rate_values(self):
        """ Validate that rate_values is Rate_values type
            Args:
                None
            Raises:
                AttributeError: When rate values do not have proper data type.
            Return:
                None
        """
        if (not isinstance(self.rate_values,Rate_values)):
            raise AttributeError("Rate values given not valid in type.")
    @property
    def rate_values(self):
        """Get the current rate values."""
        return self._rate_values
    
class National_call(Distance_call):
    """ A national call will be created and it will be shared by all the calls that are national.
    
    Since all calls share the exact same condition only one instance of this class will be created and all calls
    are going to point to this instance if they are international calls.
    Attributes:
        rate_values (Rate_values): Rate values (pences)
    """
    
    def __init__(self,rate_values):
        """Create a Distance_call object.
            Args:
                rate_values (Rate_values): Rate values (pences)
            Return:
                None
        """
        Distance_call.__init__(self,rate_values)
    def scope_rate(self):
        """Get the National Rate value.
            Args:
                None
            Return:
                None
        """
        return self.rate_values.NATIONAL_RATE

class International_call(Distance_call):
    """ A international call will be created and it will be shared by all the calls that are international.
    
    Since all calls share the exact same condition only one instance of this class will be created and all calls
    are going to point to this instance if they are international calls.
    Attributes:
        rate_values (Rate_values): Rate values (pences)
    """
    def __init__(self,rate_values):
        """Create a Distance_call object.
            Args:
                rate_values (Rate_values): Rate values (pences).
            Return:
                None
        """
        Distance_call.__init__(self,rate_values)
    def scope_rate(self):
        """Get the International Rate value.
            Args:
                None
            Return:
                None"""
        return self.rate_values.INTERNATIONAL_RATE


class Phone_call:
    """A phone call class that contains all the information but the rate.
    
    This is a super class that contains common information and by using polymorphism it calculates the billing of 
    each individual call. 
    Scope call: this attribute has a setter for testing purposes but the excersise says that we can assume that we 
    already have a method to know whether a call is national or international.
    Attributes:
        minutes (int): Amount of minutes that the call lasted.
        date_time (str): Date time when the call has begun. Format: YYYYmmDD HH:MM,
        rate_values (Rate_values):  Weekend rate value per minute (pences)
        scope_call (National_call | International_call): An object to gather the multiplier from that call.

    """
    def __init__(self,minutes,date_time,rate_values):
        """Create Rate_Values objects, set values and validate those values.

            Args:
                minutes (int): Amount of minutes that the call lasted,
                date_time (str): Date time when the call has begun. Format: YYYYmmDD HH:MM,
                rate_values (Rate_values):  Weekend rate value per minute (pences)
            Returns:
                None
        """
        self._minutes=minutes
        self._date_time=date_time
        self._rate_values=rate_values
        self.validate_call_attr()
    
    def set_scope_call(self,scope_call):
        """ ONLY FOR Testing purposes, set scope call """
        self._scope_call=scope_call
    
    def validate_call_attr(self):
        """ Validate that the attributes from call have the correct data type, also validate date format.
            Args:
                None
            Raises:
                AttributeError: When the minutes, rate values or the date time do not have the proper data type.
                ValueError: When the date time is not in the correct format (YYYYMMDD HH:MM).
            Return:
                None
        """
        if not isinstance(self.minutes,int):
            raise AttributeError("The minutes attribute is not loaded or it is not an int.")
        if not isinstance(self.rate_values,Rate_values):
            raise AttributeError("The rates values are not RateValues type.")
        if not isinstance(self.date_time,str):
            raise AttributeError("The date time attribute is not string type.")
        try:
            datetime.strptime(self.date_time, '%Y%m%d %H:%M')
        except ValueError:
            raise ValueError("Incorrect data format, must be YYYYMMDD HH:MM")

    @property
    def minutes(self):
        """Get the minutes of the call."""
        return self._minutes
    @property
    def date_time(self):
        """Get the date and time in which the call has begun."""
        return self._date_time
    @property
    def scope_call(self):
        """Get the information that tells you whether a call was international or national."""
        return self._scope_call
    @property
    def rate_values(self):
        """Get the current rate values."""
        return self._rate_values
    
    def calculate(self,user):
        """ Calculate the amount of pences that a call costs, also validate that the user is valid and that the
        attributes are properly set.
            Args:
                user (User): The user that made the call.
            Raises:
                AttributeError: When the minutes, type of user or the scope do not have the proper data type.
            Return:
                float
        """
        if isinstance(user,User):
            try:
                user.validate_type_of_user()
                return self.minutes*self.rate(user)*self.scope_call.scope_rate()
            except:
                raise AttributeError("The minutes or the Scope rate of the call was not set or does not have valid values.")
        else:
            raise AttributeError("User provided is not User type.")
        

class Regular_call(Phone_call):
    """ A regular call.
    It is a subclass of Phone Call, it has it's own way of calculation the rate. 
    Attributes:
        minutes (int): Amount of minutes that the call lasted,
        date_time (str): Date time when the call has begun. Format: YYYYmmDD HH:MM,
        rate_values (Rate_values):  Weekend rate value per minute (pences)    
    """
    
    def __init__(self,minutes,date_time,rate_values):
        """Create Phone_call objects, set values and validate those values.
            Args:
                minutes (int): Amount of minutes that the call lasted,
                date_time (str): Date time when the call has begun. Format: YYYYmmDD HH:MM,
                rate_values (Rate_values):  Weekend rate value per minute (pences)
            Returns:
                None
        """
        Phone_call.__init__(self,minutes,date_time,rate_values)

    def rate(self,user):
        """Get the rate from a regular call by checking the type of user, also perform validation over the attributes.
            [Business Rule: If the user is new, the regular call rate is the same as late night. Existing users pay 
            the regular rate.]
            Args:
                user (User): User that made the call.
            Raises:
                AttributeError: When the rate is not related to the call.
            Return:
                float
        """
        try:
            if user.type_of_user=='New':
                return self.rate_values.LATE_NIGHT_RATE
            elif user.type_of_user=='Existing':
                return self.rate_values.REGULAR_RATE
        except:
            raise AttributeError("The Rate values were not related to the call or the late night rate or weekend rate was not defined.")

class Late_night_call(Phone_call):
    """ A late night call. 
    
    It is a subclass of Phone Call, it has it's own way of calculation the rate. 
    Attributes:
        minutes (int): Amount of minutes that the call lasted,
        date_time (str): Date time when the call has begun. Format: YYYYmmDD HH:MM,
        rate_values (Rate_values):  Weekend rate value per minute (pences)
    """
    def __init__(self,minutes,date_time,rate_values):
        """Create Phone_call objects, set values and validate those values.
            Args:
                minutes (int): Amount of minutes that the call lasted,
                date_time (str): Date time when the call has begun. Format: YYYYmmDD HH:MM,
                rate_values (Rate_values):  Weekend rate value per minute (pences)
            Returns:
                None
        """
        Phone_call.__init__(self,minutes,date_time,rate_values)
    def rate(self,user):
        """Get the rate from a late night call also perform validation over the attributes.
            Args:
                user (User): User that made the call. (For polymorphism purposes in calculate)
            Raises:
                AttributeError: When the rate is not related to the call.
            Return:
                float
        """
        try:
            return self.rate_values.LATE_NIGHT_RATE
        except:
            raise AttributeError("The Rate values were not related to the call or the late night rate was not defined.")

class Weekend_call(Phone_call):
    """ A weekend call. 
    It is a subclass of Phone Call, it has it's own way of calculation the rate.
    Attributes:
        minutes (int): Amount of minutes that the call lasted,
        date_time (str): Date time when the call has begun. Format: YYYYmmDD HH:MM,
        rate_values (Rate_values):  Weekend rate value per minute (pences) """
    def __init__(self,minutes,date_time,rate_values):
        """Create Phone_call objects, set values and validate those values.
            Args:
                minutes (int): Amount of minutes that the call lasted,
                date_time (str): Date time when the call has begun. Format: YYYYmmDD HH:MM,
                rate_values (Rate_values):  Weekend rate value per minute (pences)
            Returns:
                None
        """
        Phone_call.__init__(self,minutes,date_time,rate_values)
    def rate(self,user):
        """Get the rate from a weekend call also perform validation over the attributes.
            Args:
                user (User): User that made the call. (For polymorphism purposes in calculate)
            Raises:
                AttributeError: When the rate is not related to the call.
            Return:
                float
        """
        try:
            return self.rate_values.WEEKEND_RATE
        except:
            raise AttributeError("The Rate values were not related to the call or the Weekend rate was not defined. ")