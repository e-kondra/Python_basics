def val_checker(call_b=False):
   def _val_checker(func):
      def wrapper(*args):
         if call_b(*args):
            return func(*args)
         else:
            raise ValueError(*args)
      return wrapper
   return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


print(calc_cube(20))
