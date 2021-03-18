def convert_temp(unit_in, unit_out, temp):
    # YOUR CODE HERE
  if unit_in == 'f' or unit_in == 'c':
    if unit_out == 'f' or unit_out == 'c':
      if unit_in == unit_out:
        print(f'No unit conversion is needed, Temp = {temp} {unit_in}')
      elif unit_in == 'f':
        print(f'Temp = {(temp-32)*.5556} c')
      else:
        print(f'Temp = {(temp*1.8)+32} f')
    else: print('Invlaid unit [UNIT_OUT]')
  else: print('Invlaid unit [UNIT_IN]')
  


print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

