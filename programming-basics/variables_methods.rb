#Convention: Always use lowercase

require 'date'

  age = 28
  #We assign the value 28 to thevariable age

  # ONE YEAR PASSES
  age = age + 1
  # We areassigned the variable
  #the previous value is know overwritten

  puts age


  first_name = "Jess"
  last_name = "Silva Carvalho"

  #Concatenation
  puts first_name + " " + last_name

  #Interpolation
  puts "#{first_name} #{last_name}"

  #Methods
  #IMPORTANT: When using methods in ruby remember  always return the last line of the method even if "return" word is missing
  #define a method
  #A method ending with a "?" return true or false
  #A method ending with a ! is a desructive or dangerous method (save the variable)

  #With no parameters
  def tomorrow
    tomorrow = Date.today + 1
    return tomorrow.strftime("%A, %b %d")
  end

  puts tomorrow

  #With parameters
  def full_name (first, last) #Parameters
    name = "#{first.capitalize} #{last.capitalize}"
    return name
  end

  puts full_name("dIEgo", "reYeS") #Arguments

  #True or false method
  def tall?(height)
    if height >= 180
      return true
    else
      return false
    end
  end

  puts tall?(120)
  puts tall?(200)

  #Destructive method
  city = "london"
  city.upcase
  puts city

  city.upcase! #Save what you modified
  puts city
